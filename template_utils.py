import re
import wikitextparser as wtp

import unicodedata

NOINCLUDE_RE = re.compile(r"<noinclude>.*?</noinclude>|<!--.*?-->", re.MULTILINE|re.DOTALL)
FIELD_RE = re.compile(r"[|]\s*([^=|]+?)\s*=([^=|]*?)(?:<|$)", re.MULTILINE|re.DOTALL)
stem_RE = re.compile(r"[{][{][{](основа\d?)[}][}][}]([\w]+)")
inner_RE = re.compile(r"[|][{][{][{](основа\d?)[}][}][}]")

ACCENT_MAPPING = {
    '́': '',
    '̀': '',
    'а́': 'а',
    'а̀': 'а',
    'е́': 'е',
    'ѐ': 'е',
    'и́': 'и',
    'ѝ': 'и',
    'о́': 'о',
    'о̀': 'о',
    'у́': 'у',
    'у̀': 'у',
    'ы́': 'ы',
    'ы̀': 'ы',
    'э́': 'э',
    'э̀': 'э',
    'ю́': 'ю',
    '̀ю': 'ю',
    'я́́': 'я',
    'я̀': 'я',
}
ACCENT_MAPPING = {unicodedata.normalize('NFKC', i): j for i, j in ACCENT_MAPPING.items()}


def unaccentify(s):
    source = unicodedata.normalize('NFKC', s)
    for old, new in ACCENT_MAPPING.items():
        source = source.replace(old, new)
    return source


def preprocess(s):
    s = unaccentify(s.replace("|{{{1}}}", ""))
    s = s.replace("{{особ.ф.|", "")
    s = NOINCLUDE_RE.sub("", s)
    return s


def stems(value):
    values = [(name, value) for name, value in stem_RE.findall(value)]
    return values


def wtp_parser(s):
    parsed = wtp.parse(unaccentify(s))
    return parsed.pformat().replace("\n        ", " ")


def get_fields(text):
    text = NOINCLUDE_RE.sub("", text)
    text = inner_RE.sub("", text)
    rv = [(name, value) for name, value in FIELD_RE.findall(text)]
    return rv


if __name__ == "__main__":
    # file_path = sys.argv[1]
    # parse(open(sys.argv[1]).read(), sys.argv[2])
    # parse_mw_template(open(file_path).read())

    # f = "фѝтохимика́т"
    # print(unaccentify(f))
    # example = """{{#if:{{{безличный|}}}||{{{основа}}}ал<br >{{{основа}}}ала<br />}}{{{основа}}}ало"""
    # p = wtp.parse(example)
    # funcs = p.parser_functions[0]

    print(get_fields(('{{Гл-блок\n'
 '\n'
 '|Я          ={{{основа1}}}у\n'
 '|Я (прош.) ={{{основа2}}}<br />{{{основа1}}}ла\n'
 '|Мы ={{{основа3|{{{основа}}}}}}ём\n'
 '|Мы (прош.) ={{{основа1}}}ли\n'
 '|Мы (повел.) ={{{основа3|{{{основа}}}}}}ём <br '
 '/>{{{основа3|{{{основа}}}}}}ёмте\n'
 '|Ты ={{{основа3|{{{основа}}}}}}ёшь\n'
 '|Ты (прош.) ={{{основа2}}}<br />{{{основа1}}}ла\n'
 '|Ты (повел.)={{{основа1}}}и\n'
 '|Вы ={{{основа3|{{{основа}}}}}}ёте\n'
 '|Вы (прош.) ={{{основа1}}}ли\n'
 '|Вы (повел.)={{{основа1}}}ите\n'
 '|Он/она/оно ={{{основа3|{{{основа}}}}}}ёт\n'
 '|Он/она/оно (прош.)={{{основа2}}}<br />{{{основа1}}}ла<br />{{{основа1}}}ло\n'
 '|Они ={{{основа1}}}ут\n'
 '|Они (прош.)={{{основа1}}}ли\n'
 '|Прич = {{{основа2}}}ший\n'
 '|Деепр = {{{основа2}}}ши\n'
 '|ПричСтрад = {{{основа3|{{{основа}}}}}}ённый\n'
 '|hide-text={{{hide-text|}}}\n'
 '|слоги={{{слоги|}}}\n'
 '|дореф={{{дореф|}}}\n'
 '|спряжение=8b/b\n'
 '|вид=с\n'
 '|НП={{{НП|}}}\n'
 '|соотв={{{соотв|}}}\n'
 '|соотв-мн={{{соотв-мн|}}}\n'
 '}}')
))