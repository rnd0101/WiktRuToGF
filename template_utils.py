import re

import unicodedata

NOINCLUDE_RE = re.compile(r"<noinclude>.*?</noinclude>|<!--.*?-->", re.MULTILINE | re.DOTALL)
FIELD_RE = re.compile(r"[|]\s*([^=|]+?)\s*=([^=|]*?)(?:<|$)", re.MULTILINE | re.DOTALL)
stem_RE = re.compile(r"[{][{][{](основа\d?(?:/основа\d?)?)[}][}][}]([\w]*)\s*$")
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
    import wikitextparser as wtp
    parsed = wtp.parse(unaccentify(s))
    return parsed.pformat().replace("\n        ", " ")


def _repl_default(m):
    return "/" + m.group(1)


def get_fields(text):
    text = NOINCLUDE_RE.sub("", text)
    text = inner_RE.sub(_repl_default, text)
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

    print(get_fields((
        """{{Гл-блок

|Я          ={{{основа1}}}у
|Я (прош.) ={{{основа2}}}<br />{{{основа1}}}ла
|Мы ={{{основа3|{{{основа}}}}}}ём
|Мы (прош.) ={{{основа1}}}ли
|Мы (повел.) ={{{основа3|{{{основа}}}}}}ём <br />{{{основа3|{{{основа}}}}}}ёмте
|Ты ={{{основа3|{{{основа}}}}}}ёшь
|Ты (прош.) ={{{основа2}}}<br />{{{основа1}}}ла
|Ты (повел.)={{{основа1}}}и
|Вы ={{{основа3|{{{основа}}}}}}ёте
|Вы (прош.) ={{{основа1}}}ли
|Вы (повел.)={{{основа1}}}ите
|Он/она/оно ={{{основа3|{{{основа}}}}}}ёт
|Он/она/оно (прош.)={{{основа2}}}<br />{{{основа1}}}ла<br />{{{основа1}}}ло
|Они ={{{основа1}}}ут
|Они (прош.)={{{основа1}}}ли
|Прич = {{{основа2}}}ший
|Деепр = {{{основа2}}}ши
|ПричСтрад = {{{основа3|{{{основа}}}}}}ённый
|hide-text={{{hide-text|}}}
|слоги={{{слоги|}}}
|дореф={{{дореф|}}}
|спряжение=8b/b
|вид=с
|НП={{{НП|}}}
|соотв={{{соотв|}}}
|соотв-мн={{{соотв-мн|}}}
}}"""
    )
    ))
