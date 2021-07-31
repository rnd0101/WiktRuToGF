# -*- coding: utf-8 -*-
import json
import re

import cyrtranslit

from common_parser import get_article
from common_parser import parse_article
from fetch_shablon import ns
from noun_template_parser import get_fields
from noun_template_parser import parse_mw_template
from template_utils import unaccentify
from template_utils import wtp_parser

NOUN_TPL_RU_RE = re.compile(r"сущ ru ([fmn]) (ina|a) (\S+?)$")
NOUN_TPL_RU2_RE = re.compile(r"сущ ru ([fmn]) (ina|a) [(]п ([1-8][ab])[)]$")
NOUN_RU_RE = re.compile(r"([{][{](сущ\s+ru\s+[^|$\n]*).+?\s*[}][}])\s*$", re.DOTALL | re.MULTILINE)
NOUN_RU_NEW_RE = re.compile(r"([{][{]сущ-ru\s*[|]\s*([^ |}]+)\s*[|]\s*([^}]+?)[}][}])", re.DOTALL | re.MULTILINE)
REDIRECT_RE = re.compile(r'#перенаправление\s+\[\[Шаблон:(.+?)\]\]')
PO_SLOGAM_RE = re.compile(r"[{][{]по-слогам[^}]+[}][}]")
PO_SLOGAM2_RE = re.compile(r"[|]\s*слоги\s*=\s*[{][^}]+[}][}]")


def get_noun(text):
    text = PO_SLOGAM_RE.sub("", text)
    text = PO_SLOGAM2_RE.sub("", text)
    m = NOUN_RU_RE.search(text)
    if m:
        templ_name, templ_body = m.groups()
        return " ".join(templ_name.split()), templ_body
    m = NOUN_RU_NEW_RE.search(text)
    if m:
        return None, m.groups()


def get_invokation_params(invokation):
    fields = {k.strip(): v.strip() for (k, v) in get_fields(wtp_parser(invokation))}
    return fields


MAP_stemS = {
    "основа": "stem",
    "основа1": "stem1",
    "основа2": "stem2",
    "основа3": "stem3",
}

MAP_GENDER = {
    "f": "Fem",
    "m": "Masc",
    "n": "Neut",
    "ж": "Fem",
    "м": "Masc",
    "с": "Neut",
}

MAP_ANIMACY = {
    "a": "Animate",
    "о": "Animate",
    "ina": "Inanimate",
    None: "Inanimate",
}


def parse_template_name(tpl_name):
    # сущ ru n ina 0
    m = NOUN_TPL_RU_RE.match(tpl_name)
    if m:
        g, a, form = m.groups()
        return {
            "gender": MAP_GENDER[g],
            "animacy": MAP_ANIMACY[a],
            "form": form,
        }


def parse_template_name_adj(tpl_name):
    # сущ ru n ina 0
    m = NOUN_TPL_RU2_RE.match(tpl_name)
    if m:
        g, a, form = m.groups()
        return {
            "gender": MAP_GENDER[g],
            "animacy": MAP_ANIMACY[a],
            "form": form,
            "adj": True,
        }


# Р₂ , П₂
ZALIZNYAK_INDEX2_RE = re.compile(
    r"""([жмс])([о])?,?\s+([0-9])(?:([*°]|)([a-f]['"]{0,2}))?(?:.*?\[?((?:②|①|\([12]\))+))?""", re.I)

ZALIZNYAK_ADJ_INDEX2_RE = re.compile(
    r"""([жмс])([о])?\s*<п ([1-8][*]?[ab])>""", re.I)


def parse_template_new(param):
    (_tpl_name, word, z_index) = param
    z_index = z_index.split("|")[0].strip()
    m = ZALIZNYAK_INDEX2_RE.match(z_index)
    if m:
        # ('с', None, '0', None, None, None, None)
        gender, animacy, num, ast, stress, circled = m.groups()
        if num == "0":
            form = "0"
        else:
            form = "{}{}{}".format(num, ast or "", stress or "")
            if circled:
                form += circled.replace("①", "(1)").replace("②", "(2)")
        return {
            "gender": MAP_GENDER[gender],
            "animacy": MAP_ANIMACY[animacy],
            "form": form,
        }
    m = ZALIZNYAK_ADJ_INDEX2_RE.match(z_index)
    if m:
        gender, animacy, form = m.groups()
        return {
            "gender": MAP_GENDER[gender],
            "animacy": MAP_ANIMACY[animacy],
            "adj": True,
            "form": form,
        }


def call_template(parsed_template, template_params):
    # print(template_params)
    called = {}
    for stem_key, stem in MAP_stemS.items():
        r = template_params.get(stem_key)
        if r:
            called[stem] = r
    for k, values in parsed_template.items():
        if isinstance(values, (list, set, tuple)):
            computed = []
            for varname, postfix in values:
                try:
                    t = unaccentify(template_params[varname] + postfix)
                    computed.append(t)
                except KeyError:
                    pass
            called[k] = computed
        else:
            called[k] = values

    if 'PastP3' in called:
        if 'PastSgP1' in called:
            if called['PastSgP1'] == called['PastP3'][:2]:
                called['PastSgP1'] = called['PastP3']
        if 'PastSgP2' in called:
            if called['PastSgP2'] == called['PastP3'][:2]:
                called['PastSgP2'] = called['PastP3']
    for multiple in 'PastP3', 'PastSgP1', 'PastSgP2':
        if multiple in called and len(called[multiple]) == 3:
            called[multiple + "Masc"], called[multiple + "Fem"], called[multiple + "Neut"] = called[multiple]

    processed = {}
    for k, values in called.items():
        if isinstance(values, (list, set, tuple)):
            if len(values) == 1:
                processed[k] = values[0]
        else:
            processed[k] = values

    return processed


def slug(s):
    return cyrtranslit.to_latin(s, "ru").replace("'", "q").replace("#", "6").replace("-", "_")


def gf_lexicon(data, orig_tpl):
    # lin malqchik_N = mkN "мальчик" "мальчика" "мальчику" "мальчика" "мальчиком" "мальчике" "мальчиками"
    #                      "мальчики" "мальчиков" "мальчикам" "мальчиков" "мальчиками" "мальчиках" Masc Animate ;
    res = """   {}_N = mkN "{}" "{}" "{}" "{}" "{}" "{}" "{}" "{}" "{}" "{}" "{}" "{}" "{}" {} {} ;  -- wikt: {}""".format(
        slug(data["word"]).strip(),
        data.get("nom-sg", ""),
        data.get("gen-sg", ""),
        data.get("dat-sg", ""),
        data.get("acc-sg", ""),
        data.get("ins-sg", ""),
        data.get("prp-sg", ""),
        data.get("prp-sg", ""),  # loc-sg !!!
        data.get("nom-pl", ""),
        data.get("gen-pl", ""),
        data.get("dat-pl", ""),
        data.get("acc-pl", ""),
        data.get("ins-pl", ""),
        data.get("prp-pl", ""),
        data.get("Gender", ""),
        data.get("Animacy", ""),
        orig_tpl.replace("\n", " ").replace("{{", "").replace("}}", "")
    )
    return res


ZALIZNYAK_INDEX_RE = re.compile(r"""([0-9])(?:([*°]|)([abcdef]['"]{0,2}))?""")


def zal_index(features):
    m = ZALIZNYAK_INDEX_RE.match(features["form"])
    if m:
        num, ast, stress = m.groups()  # ('2', '*', 'a')
        num = int(num)
        ast = {"*": "Ast", "°": "Deg", None: "", "": "No"}[ast]
        stress = (stress or "").upper().replace('"', "''")
        if num == 0:
            return "Z0"
        c = ""
        if "(1)" in features["form"]:
            c += "1"
        if "(2)" in features["form"]:
            c += "2"
        if c:
            return "(ZN {} {} {} ZC{})".format(num, ast, stress, c)
        return "(ZN {} {} {} NoC)".format(num, ast, stress)
    return ""


def gf_lexicon2(data, orig_tpl, features):
    pluralia_tantum = "pt=1" in orig_tpl
    if data["Adjective"]:
        # zhivotnoe_N = mkN (mkA "животный") Neut Animate ;  -- wikt: сущ ru n a (п 1a)
        if data["word"].endswith("щая") or data["word"].endswith("щее") \
                or data["word"].endswith("шая") or data["word"].endswith("шее") \
                or data["word"].endswith("жая") or data["word"].endswith("жее") \
                or data["word"].endswith("чая") or data["word"].endswith("чее"):
            data["nom-sg"] = data["word"][:-2] + "ий"
        elif data["word"].endswith("ое") or data["word"].endswith("ая") or data["word"].endswith("ые"):
            data["nom-sg"] = data["word"][:-2] + "ый"
        elif data["word"].endswith("ие"):
            data["nom-sg"] = data["word"][:-2] + "ий"
        else:
            data["nom-sg"] = data["word"]
        word_slug = slug(data["word"]).strip()
        res = """  {}_N = mkN (mkA "{}") {} {}{} ;  -- wikt: {}""".format(
            word_slug,
            data["nom-sg"],
            data.get("Gender", ""),
            data.get("Animacy", ""),
            " only_plural" if pluralia_tantum else "",
            orig_tpl.replace("\n", " ").replace("{{", "").replace("}}", "")
        )
        return res

    # lin malqchik_N = mkN "мальчик" "мальчика" "мальчику" "мальчика" "мальчиком" "мальчике" "мальчиками"
    #                      "мальчики" "мальчиков" "мальчикам" "мальчиков" "мальчиками" "мальчиках" Masc Animate ;
    z = zal_index(features)
    data["nom-sg"] = data.get("nom-sg", "") or data["word"]
    word_slug = slug(data["word"]).strip()
    res = """  {}_N = mkN "{}" {} {} {}{} ;  -- wikt: {}""".format(
        word_slug,
        data["nom-sg"],
        data.get("Gender", ""),
        data.get("Animacy", ""),
        z,
        " only_plural" if pluralia_tantum else "",
        orig_tpl.replace("\n", " ").replace("{{", "").replace("}}", "")
    )
    # try:
    #     res += """\n--{word_slug}_N {nom-sg} {gen-sg} {dat-sg} {acc-sg} {ins-sg} {prp-sg} """.format(word_slug=word_slug, **data)
    #     res += """{nom-pl} {gen-pl} {dat-pl} {acc-pl} {ins-pl} {prp-pl}""".format(**data)
    # except KeyError:
    #     pass
    return res


def transform_article(article_xml, format, nominative, xml_dump_path, output_file_path):
    print(f"----------- {nominative} ----------")
    article_text = parse_article(article_xml)["text"]
    try:
        noun_invokation, noun_tpl = get_noun(article_text)
    except:
        return

    print(":::", repr(noun_tpl))
    instantiated = {}
    if noun_invokation is not None:
        noun_features = parse_template_name(noun_tpl)
        if noun_features is None:
            noun_features = parse_template_name_adj(noun_tpl)
    else:
        noun_features = parse_template_new(noun_tpl)

    if noun_features is None:
        return
    if noun_invokation is not None:
        template_xml = get_article(ns.format(noun_tpl), xml_dump_path)
        template_text = parse_article(template_xml)["text"]
        match_redir = REDIRECT_RE.search(template_text)
        if match_redir:
            noun_tpl1 = match_redir.group(1)
            print(repr(noun_tpl1))
            print("REDIR: {} -> {}".format(noun_tpl, noun_tpl1))
            template_xml = get_article(ns.format(noun_tpl1), xml_dump_path)
            template_text = parse_article(template_xml)["text"]

        template_params = get_invokation_params(noun_invokation)
        parsed_template = parse_mw_template(template_text)

        print("-----------------")
        print(parsed_template)
        print("-----------------")
        print(template_params)
        print("-----------------")

        instantiated = call_template(parsed_template, template_params)
    else:
        noun_invokation = "|".join(noun_tpl)
    instantiated["word"] = nominative  # ???
    instantiated["Gender"] = noun_features["gender"]
    instantiated["Animacy"] = noun_features["animacy"]
    instantiated["Form"] = noun_features["form"]
    instantiated["Adjective"] = noun_features.get("adj", False)
    if format == 'json':
        print(json.dumps(instantiated,
                         indent=2,
                         ensure_ascii=False))
    elif format == 'rgl':
        if output_file_path:
            with open(output_file_path, "at") as out_file:
                print(gf_lexicon(instantiated, noun_invokation), file=out_file)
        else:
            print(gf_lexicon(instantiated, noun_invokation))
    elif format == 'rgl2':
        if output_file_path:
            with open(output_file_path, "at") as out_file:
                print(gf_lexicon2(instantiated, noun_invokation, noun_features), file=out_file)
        else:
            print(gf_lexicon2(instantiated, noun_invokation, noun_features))
