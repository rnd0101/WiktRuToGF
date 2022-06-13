# -*- coding: utf-8 -*-

import re
from pprint import pprint

from template_utils import get_fields
from template_utils import preprocess
from template_utils import stems

IMPERSONAL_IF_RE = re.compile(r"[#]if:[{][{][{]безличный|[}][}][}][|].{0,2}[|]")

EXAMPLE = """
|Я          ={{{основа2}}}у́
|Я (прош.)  ={{{основа}}}а́л<br />{{{основа}}}а́ла
|Мы         ={{{основа1}}}ем
|Мы (прош.) ={{{основа}}}а́ли
|Ты         ={{{основа1}}}ешь
|Ты (прош.) ={{{основа}}}а́л<br />{{{основа}}}а́ла
|Ты (повел.)={{{основа2}}}и́
|Вы         ={{{основа1}}}ете
|Вы (прош.) ={{{основа}}}а́ли
|Вы (повел.)={{{основа2}}}и́те
|Он/она/оно ={{{основа1}}}ет
|Он/она/оно (прош.)={{{основа}}}а́л<br />{{{основа}}}а́ла<br />{{{основа}}}а́ло
|Они        ={{{основа1}}}ут
|Они (прош.)={{{основа}}}а́ли
|ПричНаст   = {{{основа1}}}ущий
|ПричПрош   = {{{основа}}}а́вший
|ПричСтрад={{{основа1}}}емый
|ПричСтрадПрош={{{основа3}}}анный
|ДеепрНаст  = {{{основа2}}}а́
|ДеепрПрош  = {{{основа}}}а́в, {{{основа}}}а́вши
|Будущее    = буду/будешь... {{{основа}}}а́ть
|Инфинитив = {{{основа}}}а́ть
"""

FORM_MAPPING = {
    "Я": "PresSgP1",
    "Я (прош.)": "PastSgP1",
    "Мы": "PresPlP1",
    "Мы (прош.)": "PastPlP1",
    "Ты": "PresSgP2",
    "Ты (прош.)": "PastSgP2",
    "Ты (повел.)": "ImpSgP2",
    "Вы": "PresPlP2",
    "Вы (прош.)": "PastPlP2",
    "Вы (повел.)": "ImpPlP2",
    "Он/она/оно": "PresP3_all",
    "Он/она/оно (прош.)": "PastP3",
    "Они": "PresPlP3",
    "Они (прош.)": "PastPlP3",
    "Будущее": "Future",
    "Инфинитив": "Inf",
    "вид": "Aspect",
    "НП": "Transitivity",
    "спряжение": "Conjugation",
    "возвратный": "Reflexivity",
    "безличный": "Personality",
    "ПричНаст": "PresActPart",
    "ПричПрош": "PastActPart",
    "ПричСтрад": "PresPassPart",
    "ПричСтрадПрош": "PastPassPart",
    "Деепр": "Transgressive",
    "ДеепрНаст": "PresTransgressive",
    "ДеепрПрош": "PastTransgressive",
}


def map_aspect(v):
    if v == "с":
        return "Perfective"
    if v == "н":
        return "Imperfective"
    return "Imperfective?"


def map_reflexivity(v):
    if v == "1":
        return "Reflexive"
    return ""


def map_transitivity(v):
    if v == "1":
        return "Intransitive"
    return "Transitive"


def map_personality(v):
    if v == "1":
        return "Impersonal"
    return ""


def parse_mw_template(s):
    s = preprocess(s)
    forms = {}
    print(s)
    for name, value in get_fields(s):
        form_id = FORM_MAPPING.get(name)
        if form_id:
            if name == "вид":
                forms[form_id] = map_aspect(value)
            elif name == "спряжение":
                forms[form_id] = value
            elif name == "возвратный":
                forms[form_id] = map_reflexivity(value)
            elif name == "НП":
                forms[form_id] = map_transitivity(value)
            elif name == "безличный":
                forms[form_id] = map_personality(value)
            else:
                forms[form_id] = [x for x in stems(value)]

    pres_pl_p3_form = forms.get("PresPlP3")
    if pres_pl_p3_form:
        post = pres_pl_p3_form[0][1]
        forms["ConjHeuristic"] = guess_gf_conj(post)
    return forms


def guess_gf_conj(post):
    return "first" if post.endswith("ут") or post.endswith("ют") else "secondA"
