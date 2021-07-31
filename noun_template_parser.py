# -*- coding: utf-8 -*-

import re

from template_utils import get_fields
from template_utils import preprocess
from template_utils import stems

IMPERSONAL_IF_RE = re.compile(r"[#]if:[{][{][{]безличный|[}][}][}][|].{0,2}[|]")

EXAMPLE = """
|form={{{form|}}}
|case={{{case|}}}
|nom-sg={{{основа}}}я
|nom-pl={{{основа}}}и
|gen-sg={{{основа}}}и
|gen-pl={{{основа1|{{{основа}}}й}}}
|dat-sg={{{основа}}}е 
|dat-pl={{{основа}}}ям
|acc-sg={{{основа}}}ю 
|acc-pl={{{основа1|{{{основа}}}и}}}
|ins-sg={{{основа}}}ей
|ins-sg2={{{основа}}}ею
|ins-pl={{{основа}}}ями
|prp-sg={{{основа}}}е 
|prp-pl={{{основа}}}ях
|loc-sg={{{М|}}} 
|voc-sg={{{З|}}} 
|prt-sg={{{Р|}}}
|hide-text={{{hide-text|}}}
|слоги={{{слоги|}}}
|дореф={{{дореф|}}}
|Сч={{{Сч|}}}
|st={{{st|}}}
|pt={{{pt|}}}
|затрудн={{{затрудн|}}}
|коммент={{{коммент|}}}
|зачин={{{зачин|}}}
|клитика={{{клитика|}}}
|кат=неодуш
|род={{{род|жен}}}
|скл=1
|зализняк=6a
"""

FORM_MAPPING = {
    "nom-sg": "nom-sg",
    "nom-pl": "nom-pl",
    "gen-sg": "gen-sg",
    "gen-pl": "gen-pl",
    "dat-sg": "dat-sg",
    "dat-pl": "dat-pl",
    "acc-sg": "acc-sg",
    "acc-pl": "acc-pl",
    "ins-sg": "ins-sg",
    "ins-sg2": "ins-sg2",
    "ins-pl": "ins-pl",
    "prp-sg": "prp-sg",
    "prp-pl": "prp-pl",
    "loc-sg": "loc-sg",
    "voc-sg": "voc-sg",
    "prt-sg": "prt-sg",
}


def parse_mw_template(s):
    s = preprocess(s)
    forms = {}
    print(s)
    for name, value in get_fields(s):
        form_id = FORM_MAPPING.get(name)
        if form_id:
            forms[form_id] = [x for x in stems(value)]

    return forms
