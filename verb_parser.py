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
from verb_template_parser import parse_mw_template

GLAGOL_RU_RE = re.compile(r"([{][{](гл\s+ru\s+[^|\s]+|гл\s+ru).+?\s*[}][}])\s*$", re.DOTALL | re.MULTILINE)
REDIRECT_RE = re.compile(r'#перенаправление\s+\[\[Шаблон:(.+?)]]')
PO_SLOGAM_RE = re.compile(r"[{][{][^}]по-слогам+?[}][}]")
PO_SLOGAM2_RE = re.compile(r"[|]\s*слоги\s*=[^\n]*")


def get_glagol(text):
    text = PO_SLOGAM_RE.sub("", text)
    text = PO_SLOGAM2_RE.sub("", text)
    m = GLAGOL_RU_RE.search(text)
    if m:
        templ_name, templ_body = m.groups()
        return " ".join(templ_name.split()), templ_body


def get_invokation_params(invokation):
    fields = {k.strip(): v.strip() for (k, v) in get_fields(wtp_parser(invokation))}
    return fields


MAP_stemS = {
    "основа": "stem",
    "основа1": "stem1",
    "основа2": "stem2",
    "основа3": "stem3",
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
                r = None
                for key in varname.split("/"):
                    r = template_params.get(key)
                    if r:
                        break
                if r is not None:
                    t = unaccentify(r + postfix)
                    computed.append(t)
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
    return cyrtranslit.to_latin(s, "ru").replace("'", "q").replace("#", "6").replace("-", "_").replace(" ", "_")


def gf_lexicon(data, orig_tpl):
    aspect = data.get("Aspect", "Imperfective")
    if "PresSgP1" in data and data["PresSgP1"].startswith(data["stem"]):
        postfix = data["PresSgP1"][len(data["stem"]):]
        res = """  {}_V = regV {} {} "{}" "{}" "{}" "{}" "{}" ;  -- wikt: {}""".format(
            slug(data["Inf"]),
            aspect.lower(),
            data["ConjHeuristic"], data["stem"], postfix,
            data.get("PastSgP1Masc", ""), data.get("ImpSgP2", ""), data["Inf"],
            orig_tpl.replace("\n", " ").replace("{{", "").replace("}}", "")
        )
    else:
        # mkV perfective          "свяжу" "свяжешь" "свяжет" "свяжем" "связали" "свяжут" "связал" "свяжи" "связать" ;
        res = """   {}_V = mkV {} "{}" "{}" "{}" "{}" "{}" "{}" "{}" "{}" "{}" ;  -- wikt: {}""".format(
            slug(data["Inf"]).strip(),
            aspect.lower(),
            data.get("PresSgP1", ""),
            data.get("PresSgP2", ""),
            data.get("PresSgP3", data.get("PresP3_all", "!!!")),
            data.get("PresPlP1"),
            data.get("PresPlP2"),
            data.get("PresPlP3"),
            data.get("PastSgP1Masc"),
            data.get("ImpSgP2"),
            data["Inf"],
            orig_tpl.replace("\n", " ").replace("{{", "").replace("}}", "")
        )
    return res


ZALIZNYAK_INDEX_RE = re.compile(r"""([0-9]|1[0-6])(?:([*°]|)([abcdef'"/]{0,4}))?$""")


def zal_index(txt):
    m = ZALIZNYAK_INDEX_RE.match(txt)
    if m:
        num, ast, stress = m.groups()  # ('2', '*', 'a')
        num = int(num)
        ast = {"*": "Ast", "°": "Deg", None: "", "": "No"}[ast]
        stress = (stress or "").upper().replace('"', "''")
        c = ""
        if "(1)" in txt:
            c += "1"
        if "(2)" in txt:
            c += "2"
        if c:
            return "(ZV {} {} {} ZC{})".format(num, ast, stress, c)
        return "(ZV {} {} {} NoC)".format(num, ast, stress)
    return ""


def gf_lexicon2(data, orig_tpl):
    aspect = data.get("Aspect", "Imperfective")
    transitivity = data.get("Transitivity", "Transitive")
    if data["Inf"].endswith("йти") or data["Inf"].endswith("дать") \
            or data["Inf"].endswith("йтись") or data["Inf"].endswith("даться"):
        res = """  -- {}_V = mkV {} {} "{}" ;  ---- {}""".format(
            slug(data["Inf"]),
            aspect.lower(),
            transitivity.lower(),
            data["Inf"],
            orig_tpl.replace("\n", " ").replace("{{", "").replace("}}", "")
        )  # 'PresP3_all'
    elif "PresSgP1" in data:
        if data.get("Conjugation") and zal_index(data["Conjugation"]):
            idx = ' "{}"'.format(data["Conjugation"])
        else:
            idx = ''
        res = """  {}_V = mkV {} {} "{}" "{}" "{}"{} ; """.format(
            slug(data["Inf"]),
            aspect.lower(),
            transitivity.lower(),
            data["Inf"],
            data["PresSgP1"],
            data.get("PresSgP3", data["PresP3_all"]),
            idx
            # orig_tpl.replace("\n", " ").replace("{{", "").replace("}}", "")
        )  # ''
    else:
        res = """  -- {}_V = mkV {} {} "{}" ;  ---- {}""".format(
            slug(data["Inf"]),
            aspect.lower(),
            transitivity.lower(),
            data["Inf"],
            orig_tpl.replace("\n", " ").replace("{{", "").replace("}}", "")
        )  # 'PresP3_all'

    return res


def transform_article(article_xml, format, infinitive, xml_dump_path, output_file_path):
    print(f"----------- {infinitive} ----------")
    aspect = None
    article_text = parse_article(article_xml)["text"]
    try:
        glagol_invokation, glagol_tpl = get_glagol(article_text)
    except:
        return
    print(":::::::::::::::", glagol_tpl)
    if glagol_tpl.endswith("СВ") and not glagol_tpl.endswith("НСВ"):
        aspect = "Perfective"
    elif glagol_tpl.endswith("НСВ"):
        aspect = "Imperfective"
    template_xml = get_article(ns.format(glagol_tpl), xml_dump_path)
    template_text = parse_article(template_xml)["text"]
    match_redir = REDIRECT_RE.search(template_text)
    if match_redir:
        glagol_tpl1 = match_redir.group(1)

        if not aspect and glagol_tpl.endswith("СВ") and not glagol_tpl.endswith("НСВ"):
            aspect = "Perfective"
        elif not aspect and glagol_tpl.endswith("НСВ"):
            aspect = "Imperfective"

        print("REDIR: {} -> {}".format(glagol_tpl, glagol_tpl1))
        template_xml = get_article(ns.format(glagol_tpl1), xml_dump_path)
        template_text = parse_article(template_xml)["text"]

    template_params = get_invokation_params(glagol_invokation)
    parsed_template = parse_mw_template(template_text)
    # print("-----------------")
    # print(parsed_template)
    # print("-----------------")
    # print(template_params)
    # print("-----------------")
    instantiated = call_template(parsed_template, template_params)
    if instantiated.get("Aspect"):
        if aspect:
            instantiated["Aspect"] = aspect
        else:
            instantiated["Aspect"] = instantiated["Aspect"].replace("?", "")
    elif aspect:
        instantiated["Aspect"] = aspect
    if "Inf" not in instantiated:
        instantiated["Inf"] = unaccentify(infinitive)
    if format == 'json':
        print(json.dumps(instantiated,
                         indent=2,
                         ensure_ascii=False))
    elif format == 'rgl2':
        if output_file_path:
            with open(output_file_path, "at") as out_file:
                print(gf_lexicon2(instantiated, glagol_invokation), file=out_file)
        else:
            print(gf_lexicon2(instantiated, glagol_invokation))
    elif format == 'rgl':
        if output_file_path:
            with open(output_file_path, "at") as out_file:
                print(gf_lexicon(instantiated, glagol_invokation), file=out_file)
        else:
            print(gf_lexicon(instantiated, glagol_invokation))
