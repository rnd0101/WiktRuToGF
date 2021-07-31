# -*- coding: utf-8 -*-
import json
import re

import cyrtranslit

from common_parser import get_article
from common_parser import parse_article
from fetch_shablon import ns
from template_utils import unaccentify
from template_utils import wtp_parser
from verb_template_parser import get_fields

PRIL_RU_RE = re.compile(r"([{][{](прил\s+ru\s+[^|\s]+).+)", re.DOTALL | re.MULTILINE)
REDIRECT_RE = re.compile(r'#перенаправление\s+\[\[Шаблон:(.+?)\]\]')
PO_SLOGAM_RE = re.compile(r"[|]\s*слоги\s*=\s*[{][^}]+[}][}]")


def stop_on_0_curlies(text):
    new_str = ""
    balance = 0
    for c in text:
        if c == "{":
            balance += 1
        elif c == "}":
            balance -= 1
        new_str += c
        if balance == 0:
            return new_str
    print("!!!!!!!!!!!!!!!!!")
    return new_str


def get_pril(text):
    # text = PO_SLOGAM_RE.sub("", text)
    m = PRIL_RU_RE.search(text)
    if m:
        templ_body, templ_name = m.groups()
        templ_body = stop_on_0_curlies(templ_body)
        return " ".join(templ_body.split()), templ_name


def get_invokation_params(invokation):
    fields = {k.strip(): v.strip() for (k, v) in get_fields(wtp_parser(invokation))}
    return fields


MAP_stemS = {
    "основа": "stem",
    "основа1": "stem1",
    "основа2": "stem2",
    "основа3": "stem3",
}


def slug(s):
    return cyrtranslit.to_latin(s, "ru").replace("'", "q").replace("#", "6").replace("-", "_")


ZALIZNYAK_INDEX_RE = re.compile(r"""прил ru ([0-8](?:(?:[*°]|)(?:[abcdef'"/]{0,4})))?""")

specials = {"srt-sg-m": "sm", "srt-sg-n": "sn", "srt-sg-f": "sf", "srt-pl": "sp"}

ZALIZNYAK_INDEX_PARSE_RE = re.compile(r"""([0-8])(?:([*°]|)([abc]['"]?|[abc]['"]?/[abcdef]['"]?))?$""")


def zal_index(txt):
    m = ZALIZNYAK_INDEX_PARSE_RE.match(txt)
    if m:
        num, ast, stress = m.groups()  # ('2', '*', 'a')
        num = int(num)
        if num == 0:
            return "ZA0"
        ast = {"*": "Ast", "°": "Deg", None: "", "": "No"}[ast]
        stress = (stress or "").upper().replace('"', "''").replace("/", "_")
        if "_" not in stress:
            stress = stress + "_"
        c = ""
        if "(1)" in txt:
            c += "1"
        if "(2)" in txt:
            c += "2"
        if c:
            return "(ZA {} {} {} ZC{})".format(num, ast, stress, c)
        return "(ZA {} {} {} NoC)".format(num, ast, stress)
    return ""

def gf_lexicon(data, orig_tpl):
    m = ZALIZNYAK_INDEX_RE.search(orig_tpl)
    idx = None
    if m:
        idx = zal_index(m.groups()[0])
    print( orig_tpl)
    if set(specials) & set(data) and idx and data.get("comp"):
        render_specials = ";".join('{}="{}"'.format(v, data[k]) for (k, v) in specials.items() if k in data)
        res = """  {}_A = (mkAplus (mkA "{}" "{}" {}) ** {{ {} }}) ;""".format(
            slug(data["nom_masc"]),
            data["nom_masc"],
            data["comp"],
            idx,
            render_specials
        )
    elif not (set(specials) & set(data)) and idx and data.get("comp"):
        render_specials = ";".join('{}="{}"'.format(v, data[k]) for (k, v) in specials.items() if k in data)
        res = """  {}_A = mkA "{}" "{}" {} ;""".format(
            slug(data["nom_masc"]),
            data["nom_masc"],
            data["comp"],
            idx
        )
    elif not (set(specials) & set(data)) and not idx and data.get("comp"):
        render_specials = ";".join('{}="{}"'.format(v, data[k]) for (k, v) in specials.items() if k in data)
        res = """  {}_A = mkA "{}" "{}" ;""".format(
            slug(data["nom_masc"]),
            data["nom_masc"],
            data["comp"]
        )
    elif not (set(specials) & set(data)) and idx and not data.get("comp"):
        render_specials = ";".join('{}="{}"'.format(v, data[k]) for (k, v) in specials.items() if k in data)
        res = """  {}_A = mkA "{}" {} ;""".format(
            slug(data["nom_masc"]),
            data["nom_masc"],
            idx
        )
    else:
        res = """  {}_A = mkA "{}" ; """.format(
            slug(data["nom_masc"]),
            data["nom_masc"]
        )
    return res


gf_lexicon2 = gf_lexicon

SPEC_FORM_RE = re.compile("(srt-sg-[mnf]|srt-pl)\s*=\s*{{особ.ф.\s*[|]\s*(.+?)[}]", re.DOTALL | re.MULTILINE)
COMP_FORM_RE = re.compile("степень\s*=['<;, \[\]\s]*(?:([^ |\[\]'{}<;,]+)|\[\[([^ |\[\]'{}<;,]+)|{{особ.ф.[|]([^ |\[\]'{}<;,]+))", re.DOTALL | re.MULTILINE)


def parse_special_forms(tpl):
    print (tpl)
    data = {}
    for param, word in SPEC_FORM_RE.findall(tpl):
        data[param] = unaccentify(word)
    for w1, w2, w3 in COMP_FORM_RE.findall(tpl.replace(";", " ").replace("'", " ")):
        data["comp"] = unaccentify(w1 or w2 or w3)
        if len(data["comp"]) < 3:
            del data["comp"]

    print(data)
    return data


def transform_article(article_xml, format, nom_masc, xml_dump_path, output_file_path):
    print(f"----------- {nom_masc} ----------")
    article_text = parse_article(article_xml)["text"]
    try:
        pril_invokation, pril_tpl = get_pril(article_text)
    except:
        return

    instantiated = {"nom_masc": nom_masc}
    instantiated.update(parse_special_forms(pril_invokation))
    print(":::::::::::::::", pril_tpl)
    if format == 'json':
        print(json.dumps(instantiated,
                         indent=2,
                         ensure_ascii=False))
    elif format == 'rgl2':
        if output_file_path:
            with open(output_file_path, "at") as out_file:
                print(gf_lexicon2(instantiated, pril_invokation), file=out_file)
        else:
            print(gf_lexicon2(instantiated, pril_invokation))
    elif format == 'rgl':
        if output_file_path:
            with open(output_file_path, "at") as out_file:
                print(gf_lexicon(instantiated, pril_invokation), file=out_file)
        else:
            print(gf_lexicon(instantiated, pril_invokation))
