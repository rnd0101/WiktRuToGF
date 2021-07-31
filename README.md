# Wiktionary to GrammaticalFramework lexicon utilities

This is a set of scripts, which can be used to convert Russian wiktionary articles into GF lexicon for Russian Resource Grammar (RGL).

Note: `rgl2` corresponds to the renewed Russian RGL og GF while `rgl` - to the older one.

## Get started

In short:

- clone from github
- download Wiktionary XML from ... (ca 2019, if possible)
- activate this code with venv:

```bash
# download XML dump of Ru-wiktionary to ../wikt/ruwiktionary.xml
python3 -n venv venv   # do this once
mkdir ../wiki_page_cache   # this stores
. venv/bin/activate  # do this each time when working with scripts
pip3 install -r requirements
```

Examples:

```bash
python parse_all.py -x ../wikt/ruwiktionary.xml -f rgl2  -p гл -t  "искать"
python parse_all.py -x ../wikt/ruwiktionary.xml -f rgl2  -p сущ -t  "поиск"
python parse_all.py -x ../wikt/ruwiktionary.xml -f rgl2  -p прил -t  "поисковый"
```

The above will (among a lot of debug) something like:

```gf
iskatq_V = mkV imperfective transitive "искать" "ищу" "ищет" "6c" ;
poisk_N = mkN "поиск" Masc Inanimate (ZN 3 No A NoC) ;  -- wikt: сущ ru m ina 3a |основа=по́иск |слоги=
poiskovyj_A = mkA "поисковый" (ZA 1 No A_ NoC) ;
```

Note, that participles and adverbs are not included.

It is also possible to get all verbs (гл), nouns (сущ), adjectives (прил):

```bash
python parse_all.py -x ../wikt/ruwiktionary.xml -f rgl2 -o ruwikt-verbs.txt -p гл
python parse_all.py -x ../wikt/ruwiktionary.xml -f rgl2 -o ruwikt-nouns.txt -p сущ
python parse_all.py -x ../wikt/ruwiktionary.xml -f rgl2 -o ruwikt-adjectives.txt -p прил
```
BUT... the script(s) can break at some entries.

The usual way is to have some dictionary, run against it, fix scripts when needed.

**The result may also require a lot of manual adjustments. There is absolutely no guarantee it will work!**

## Attribution
- Some materials from Russian Wiktionary Lua scripts were used here. Given on the top of source files.

## License

There are some materials, which were licensed under CC BY-SA 3.0 and GFDL. The rest can be Public Domain.
