# Licenced CC BY-SA 3.0 and GFDL
# From: https://ru.wiktionary.org/wiki/%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C:inflection/ru/declension/data/endings/noun

def get_rus_noun_table():
  return {
    "m": {
        "1-hard": {
            "nom-sg": "",
            "gen-sg": "а",
            "dat-sg": "у",
            "acc-sg": "?",
            "ins-sg": ["ом", "ом"],
            "prp-sg": ["е", "е"],
            "nom-pl": "ы",
            "gen-pl": ["ов", "ов"],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "2-soft": {
            "nom-sg": "ь",
            "gen-sg": "я",
            "dat-sg": "ю",
            "acc-sg": "?",
            "ins-sg": ["ем", "ём"],
            "prp-sg": ["е", "е"],
            "nom-pl": "и",
            "gen-pl": ["ей", "ей"],
            "dat-pl": "ям",
            "acc-pl": "?",
            "ins-pl": "ями",
            "prp-pl": "ях"
        },
        "3-velar": {
            "nom-sg": "",
            "gen-sg": "а",
            "dat-sg": "у",
            "acc-sg": "?",
            "ins-sg": ["ом", "ом"],
            "prp-sg": ["е", "е"],
            "nom-pl": "и",
            "gen-pl": ["ов", "ов"],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "4-sibilant": {
            "nom-sg": "",
            "gen-sg": "а",
            "dat-sg": "у",
            "acc-sg": "?",
            "ins-sg": ["ем", "ом"],
            "prp-sg": ["е", "е"],
            "nom-pl": "и",
            "gen-pl": ["ей", "ей"],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "5-letter-ц": {
            "nom-sg": "",
            "gen-sg": "а",
            "dat-sg": "у",
            "acc-sg": "?",
            "ins-sg": ["ем", "ом"],
            "prp-sg": ["е", "е"],
            "nom-pl": "ы",
            "gen-pl": ["ев", "ов"],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "6-vowel": {
            "nom-sg": "й",
            "gen-sg": "я",
            "dat-sg": "ю",
            "acc-sg": "?",
            "ins-sg": ["ем", "ём"],
            "prp-sg": ["е", "е"],
            "nom-pl": "и",
            "gen-pl": ["ев", "ёв"],
            "dat-pl": "ям",
            "acc-pl": "?",
            "ins-pl": "ями",
            "prp-pl": "ях"
        },
        "7-letter-и": {
            "nom-sg": "й",
            "gen-sg": "я",
            "dat-sg": "ю",
            "acc-sg": "?",
            "ins-sg": ["ем", "ём"],
            "prp-sg": ["и", "е"],
            "nom-pl": "и",
            "gen-pl": ["ев", "ёв"],
            "dat-pl": "ям",
            "acc-pl": "?",
            "ins-pl": "ями",
            "prp-pl": "ях"
        },
        "8-third": {
            "nom-sg": "ь",
            "gen-sg": "и",
            "dat-sg": "и",
            "acc-sg": "?",
            "ins-sg": ["ем", "ём"],
            "prp-sg": ["и", "и"],
            "nom-pl": "и",
            "gen-pl": ["ей", "ей"],
            "dat-pl": "ям",
            "acc-pl": "?",
            "ins-pl": "ями",
            "prp-pl": "ях"
        }
    },
    "f": {
        "1-hard": {
            "nom-sg": "а",
            "gen-sg": "ы",
            "dat-sg": "е",
            "acc-sg": "у",
            "ins-sg": ["ой", "ой"],
            "prp-sg": ["е", "е"],
            "nom-pl": "ы",
            "gen-pl": ["", ""],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "2-soft": {
            "nom-sg": "я",
            "gen-sg": "и",
            "dat-sg": ["е", "е"],
            "acc-sg": "ю",
            "ins-sg": ["ей", "ёй"],
            "prp-sg": ["е", "е"],
            "nom-pl": "и",
            "gen-pl": ["ь", "ей"],
            "dat-pl": "ям",
            "acc-pl": "?",
            "ins-pl": "ями",
            "prp-pl": "ях"
        },
        "3-velar": {
            "nom-sg": "а",
            "gen-sg": "и",
            "dat-sg": "е",
            "acc-sg": "у",
            "ins-sg": ["ой", "ой"],
            "prp-sg": ["е", "е"],
            "nom-pl": "и",
            "gen-pl": ["", ""],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "4-sibilant": {
            "nom-sg": "а",
            "gen-sg": "и",
            "dat-sg": "е",
            "acc-sg": "у",
            "ins-sg": ["ей", "ой"],
            "prp-sg": ["е", "е"],
            "nom-pl": "и",
            "gen-pl": ["", "ей"],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "5-letter-ц": {
            "nom-sg": "а",
            "gen-sg": "ы",
            "dat-sg": "е",
            "acc-sg": "у",
            "ins-sg": ["ей", "ой"],
            "prp-sg": ["е", "е"],
            "nom-pl": "ы",
            "gen-pl": ["", ""],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "6-vowel": {
            "nom-sg": "я",
            "gen-sg": "и",
            "dat-sg": ["е", "е"],
            "acc-sg": "ю",
            "ins-sg": ["ей", "ёй"],
            "prp-sg": ["е", "е"],
            "nom-pl": "и",
            "gen-pl": ["й", "й"],
            "dat-pl": "ям",
            "acc-pl": "?",
            "ins-pl": "ями",
            "prp-pl": "ях"
        },
        "7-letter-и": {
            "nom-sg": "я",
            "gen-sg": "и",
            "dat-sg": ["и", "е"],
            "acc-sg": "ю",
            "ins-sg": ["ей", "ёй"],
            "prp-sg": ["и", "е"],
            "nom-pl": "и",
            "gen-pl": ["й", "й"],
            "dat-pl": "ям",
            "acc-pl": "?",
            "ins-pl": "ями",
            "prp-pl": "ях"
        },
        "8-third": {
            "nom-sg": "ь",
            "gen-sg": "и",
            "dat-sg": ["и", "и"],
            "acc-sg": "ь",
            "ins-sg": ["ью", "ью"],
            "prp-sg": ["и", "и"],
            "nom-pl": "и",
            "gen-pl": ["ей", "ей"],
            "dat-pl": "ям",
            "acc-pl": "?",
            "ins-pl": "ями",
            "prp-pl": "ях"
        }
    },
    "n": {
        "1-hard": {
            "nom-sg": ["о", "о"],
            "gen-sg": "а",
            "dat-sg": "у",
            "acc-sg": "?",
            "ins-sg": ["ом", "ом"],
            "prp-sg": ["е", "е"],
            "nom-pl": "а",
            "gen-pl": ["", ""],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "2-soft": {
            "nom-sg": "е",
            "gen-sg": "я",
            "dat-sg": "ю",
            "acc-sg": "?",
            "ins-sg": ["ем", "ём"],
            "prp-sg": ["е", "е"],
            "nom-pl": "я",
            "gen-pl": ["ь", "ей"],
            "dat-pl": "ям",
            "acc-pl": "?",
            "ins-pl": "ями",
            "prp-pl": "ях"
        },
        "3-velar": {
            "nom-sg": ["о", "о"],
            "gen-sg": "а",
            "dat-sg": "у",
            "acc-sg": "?",
            "ins-sg": ["ом", "ом"],
            "prp-sg": ["е", "е"],
            "nom-pl": "а",
            "gen-pl": ["", ""],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "4-sibilant": {
            "nom-sg": ["е", "о"],
            "gen-sg": "а",
            "dat-sg": "у",
            "acc-sg": "?",
            "ins-sg": ["ем", "ом"],
            "prp-sg": ["е", "е"],
            "nom-pl": "а",
            "gen-pl": ["", "ей"],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "5-letter-ц": {
            "nom-sg": ["е", "о"],
            "gen-sg": "а",
            "dat-sg": "у",
            "acc-sg": "?",
            "ins-sg": ["ем", "ом"],
            "prp-sg": ["е", "е"],
            "nom-pl": "а",
            "gen-pl": ["", ""],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        },
        "6-vowel": {
            "nom-sg": "е",
            "gen-sg": "я",
            "dat-sg": "ю",
            "acc-sg": "?",
            "ins-sg": ["ем", "ём"],
            "prp-sg": ["е", "е"],
            "nom-pl": "я",
            "gen-pl": ["й", "й"],
            "dat-pl": "ям",
            "acc-pl": "?",
            "ins-pl": "ями",
            "prp-pl": "ях"
        },
        "7-letter-и": {
            "nom-sg": "е",
            "gen-sg": "я",
            "dat-sg": "ю",
            "acc-sg": "?",
            "ins-sg": ["ем", "ём"],
            "prp-sg": ["и", "е"],
            "nom-pl": "я",
            "gen-pl": ["й", "й"],
            "dat-pl": "ям",
            "acc-pl": "?",
            "ins-pl": "ями",
            "prp-pl": "ях"
        },
        "8-third": {
            "nom-sg": ["о", "о"],
            "gen-sg": "а",
            "dat-sg": "у",
            "acc-sg": "?",
            "ins-sg": ["ом", "ом"],
            "prp-sg": ["и", "и"],
            "nom-pl": "а",
            "gen-pl": ["", ""],
            "dat-pl": "ам",
            "acc-pl": "?",
            "ins-pl": "ами",
            "prp-pl": "ах"
        }
    }
}


def get_rus_adjective_table():
  return {
    "m": {
        "1-hard": {
            "nom-sg": ["ый", "ой"],
            "gen-sg": ["ого", "ого"],
            "dat-sg": ["ому", "ому"],
            "acc-sg": "?",
            "ins-sg": "ым",
            "prp-sg": ["ом", "ом"],
            "srt-sg": ""
        },
        "2-soft": {
            "nom-sg": "ий",
            "gen-sg": "его",
            "dat-sg": "ему",
            "acc-sg": "?",
            "ins-sg": "им",
            "prp-sg": "ем",
            "srt-sg": "ь"
        },
        "3-velar": {
            "nom-sg": ["ий", "ой"],
            "gen-sg": ["ого", "ого"],
            "dat-sg": ["ому", "ому"],
            "acc-sg": "?",
            "ins-sg": "им",
            "prp-sg": ["ом", "ом"],
            "srt-sg": ""
        },
        "4-sibilant": {
            "nom-sg": ["ий", "ой"],
            "gen-sg": ["его", "ого"],
            "dat-sg": ["ему", "ому"],
            "acc-sg": "?",
            "ins-sg": "им",
            "prp-sg": ["ем", "ом"],
            "srt-sg": ""
        },
        "5-letter-ц": {
            "nom-sg": ["ый", "ой"],
            "gen-sg": ["его", "ого"],
            "dat-sg": ["ему", "ому"],
            "acc-sg": "?",
            "ins-sg": "ым",
            "prp-sg": ["ем", "ом"],
            "srt-sg": ""
        },
        "6-vowel": {
            "nom-sg": "ий",
            "gen-sg": "его",
            "dat-sg": "ему",
            "acc-sg": "?",
            "ins-sg": "им",
            "prp-sg": "ем",
            "srt-sg": "й"
        },
        "7-letter-и": {
            "nom-sg": "ий",
            "gen-sg": "его",
            "dat-sg": "ему",
            "acc-sg": "?",
            "ins-sg": "им",
            "prp-sg": "ем",
            "srt-sg": "ь"
        }
    },
    "f": {
        "1-hard": {
            "nom-sg": "ая",
            "gen-sg": ["ой", "ой"],
            "dat-sg": ["ой", "ой"],
            "acc-sg": "ую",
            "ins-sg": ["ой", "ой"],
            "prp-sg": ["ой", "ой"],
            "srt-sg": "а"
        },
        "2-soft": {
            "nom-sg": "яя",
            "gen-sg": "ей",
            "dat-sg": "ей",
            "acc-sg": "юю",
            "ins-sg": "ей",
            "prp-sg": "ей",
            "srt-sg": "я"
        },
        "3-velar": {
            "nom-sg": "ая",
            "gen-sg": ["ой", "ой"],
            "dat-sg": ["ой", "ой"],
            "acc-sg": "ую",
            "ins-sg": ["ой", "ой"],
            "prp-sg": ["ой", "ой"],
            "srt-sg": "а"
        },
        "4-sibilant": {
            "nom-sg": "ая",
            "gen-sg": ["ей", "ой"],
            "dat-sg": ["ей", "ой"],
            "acc-sg": "ую",
            "ins-sg": ["ей", "ой"],
            "prp-sg": ["ей", "ой"],
            "srt-sg": "а"
        },
        "5-letter-ц": {
            "nom-sg": "ая",
            "gen-sg": ["ей", "ой"],
            "dat-sg": ["ей", "ой"],
            "acc-sg": "ую",
            "ins-sg": ["ей", "ой"],
            "prp-sg": ["ей", "ой"],
            "srt-sg": "а"
        },
        "6-vowel": {
            "nom-sg": "яя",
            "gen-sg": "ей",
            "dat-sg": "ей",
            "acc-sg": "юю",
            "ins-sg": "ей",
            "prp-sg": "ей",
            "srt-sg": "я"
        },
        "7-letter-и": {
            "nom-sg": "яя",
            "gen-sg": "ей",
            "dat-sg": "ей",
            "acc-sg": "юю",
            "ins-sg": "ей",
            "prp-sg": "ей",
            "srt-sg": "я"
        }
    },
    "n": {
        "1-hard": {
            "nom-sg": ["ое", "ое"],
            "gen-sg": ["ого", "ого"],
            "dat-sg": ["ому", "ому"],
            "acc-sg": "?",
            "ins-sg": "ым",
            "prp-sg": ["ом", "ом"],
            "srt-sg": ["о", "о"]
        },
        "2-soft": {
            "nom-sg": "ее",
            "gen-sg": "его",
            "dat-sg": "ему",
            "acc-sg": "?",
            "ins-sg": "им",
            "prp-sg": "ем",
            "srt-sg": ["е", "ё"]
        },
        "3-velar": {
            "nom-sg": ["ое", "ое"],
            "gen-sg": ["ого", "ого"],
            "dat-sg": ["ому", "ому"],
            "acc-sg": "?",
            "ins-sg": "им",
            "prp-sg": ["ом", "ом"],
            "srt-sg": ["о", "о"]
        },
        "4-sibilant": {
            "nom-sg": ["ее", "ое"],
            "gen-sg": ["его", "ого"],
            "dat-sg": ["ему", "ому"],
            "acc-sg": "?",
            "ins-sg": "им",
            "prp-sg": ["ем", "ом"],
            "srt-sg": ["е", "о"]
        },
        "5-letter-ц": {
            "nom-sg": ["ее", "ое"],
            "gen-sg": ["его", "ого"],
            "dat-sg": ["ему", "ому"],
            "acc-sg": "?",
            "ins-sg": "ым",
            "prp-sg": ["ем", "ом"],
            "srt-sg": ["е", "о"]
        },
        "6-vowel": {
            "nom-sg": "ее",
            "gen-sg": "его",
            "dat-sg": "ему",
            "acc-sg": "?",
            "ins-sg": "им",
            "prp-sg": "ем",
            "srt-sg": ["е", "ё"]
        },
        "7-letter-и": {
            "nom-sg": "ее",
            "gen-sg": "его",
            "dat-sg": "ему",
            "acc-sg": "?",
            "ins-sg": "им",
            "prp-sg": "ем",
            "srt-sg": ["е", "ё"]
        }
    },
    "pl": {
        "1-hard": {
            "nom-pl": "ые",
            "gen-pl": "ых",
            "dat-pl": "ым",
            "acc-pl": "?",
            "ins-pl": "ыми",
            "prp-pl": "ых",
            "srt-pl": "ы"
        },
        "2-soft": {
            "nom-pl": "ие",
            "gen-pl": "их",
            "dat-pl": "им",
            "acc-pl": "?",
            "ins-pl": "ими",
            "prp-pl": "их",
            "srt-pl": "и"
        },
        "3-velar": {
            "nom-pl": "ие",
            "gen-pl": "их",
            "dat-pl": "им",
            "acc-pl": "?",
            "ins-pl": "ими",
            "prp-pl": "их",
            "srt-pl": "и"
        },
        "4-sibilant": {
            "nom-pl": "ие",
            "gen-pl": "их",
            "dat-pl": "им",
            "acc-pl": "?",
            "ins-pl": "ими",
            "prp-pl": "их",
            "srt-pl": "и"
        },
        "5-letter-ц": {
            "nom-pl": "ые",
            "gen-pl": "ых",
            "dat-pl": "ым",
            "acc-pl": "?",
            "ins-pl": "ыми",
            "prp-pl": "ых",
            "srt-pl": "ы"
        },
        "6-vowel": {
            "nom-pl": "ие",
            "gen-pl": "их",
            "dat-pl": "им",
            "acc-pl": "?",
            "ins-pl": "ими",
            "prp-pl": "их",
            "srt-pl": "и"
        },
        "7-letter-и": {
            "nom-pl": "ие",
            "gen-pl": "их",
            "dat-pl": "им",
            "acc-pl": "?",
            "ins-pl": "ими",
            "prp-pl": "их",
            "srt-pl": "и"
        }
    }
}


def get_rus_pronoun_table():
  return {
    "m": {
        "1-hard": {
            "nom-sg": "",
            "gen-sg": "а",
            "dat-sg": "у",
            "ins-sg": "ым",
            "prp-sg": "е",
            "nom-pl": "ы",
            "gen-pl": "ых",
            "dat-pl": "ым",
            "ins-pl": "ыми",
            "prp-pl": "ых"
        },
        "2-soft": {
            "nom-sg": "ь",
            "gen-sg": "я",
            "dat-sg": "ю",
            "ins-sg": "им",
            "prp-sg": ["ем", "ём"],
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        },
        "3-velar": {
            "nom-sg": "",
            "gen-sg": "а",
            "dat-sg": "у",
            "ins-sg": "ым",
            "prp-sg": "е",
            "nom-pl": "ы",
            "gen-pl": "ых",
            "dat-pl": "ым",
            "ins-pl": "ыми",
            "prp-pl": "ых"
        },
        "4-sibilant": {
            "nom-sg": "",
            "gen-sg": ["его", "ого"],
            "dat-sg": ["ему", "ому"],
            "ins-sg": "им",
            "prp-sg": ["ем", "ом"],
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        },
        "5-letter-ц": {
            "nom-sg": "",
            "gen-sg": "а",
            "dat-sg": "у",
            "ins-sg": "ым",
            "prp-sg": "е",
            "nom-pl": "ы",
            "gen-pl": "ых",
            "dat-pl": "ым",
            "ins-pl": "ыми",
            "prp-pl": "ых"
        },
        "6-vowel": {
            "nom-sg": "ь",
            "gen-sg": "его",
            "dat-sg": "ему",
            "ins-sg": "им",
            "prp-sg": ["ем", "ём"],
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        },
        "7-letter-и": {
            "nom-sg": "ь",
            "gen-sg": "я",
            "dat-sg": "ю",
            "ins-sg": "им",
            "prp-sg": ["ем", "ём"],
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        }
    },
    "f": {
        "1-hard": {
            "nom-sg": "а",
            "gen-sg": "а",
            "dat-sg": "ой",
            "acc-sg": "у",
            "ins-sg": "ой",
            "prp-sg": "ой",
            "nom-pl": "ы",
            "gen-pl": "ых",
            "dat-pl": "ым",
            "ins-pl": "ыми",
            "prp-pl": "ых"
        },
        "2-soft": {
            "nom-sg": "я",
            "gen-sg": "ей",
            "dat-sg": "ей",
            "acc-sg": "ю",
            "ins-sg": "ей",
            "prp-sg": "ей",
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        },
        "3-velar": {
            "nom-sg": "а",
            "gen-sg": "а",
            "dat-sg": "ой",
            "acc-sg": "у",
            "ins-sg": "ой",
            "prp-sg": "ой",
            "nom-pl": "ы",
            "gen-pl": "ых",
            "dat-pl": "ым",
            "ins-pl": "ыми",
            "prp-pl": "ых"
        },
        "4-sibilant": {
            "nom-sg": "а",
            "gen-sg": ["ей", "ой"],
            "dat-sg": ["ей", "ой"],
            "acc-sg": "у",
            "ins-sg": ["ей", "ой"],
            "prp-sg": ["ей", "ой"],
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        },
        "5-letter-ц": {
            "nom-sg": "а",
            "gen-sg": "а",
            "dat-sg": "ой",
            "acc-sg": "у",
            "ins-sg": "ой",
            "prp-sg": "ой",
            "nom-pl": "ы",
            "gen-pl": "ых",
            "dat-pl": "ым",
            "ins-pl": "ыми",
            "prp-pl": "ых"
        },
        "6-vowel": {
            "nom-sg": "я",
            "gen-sg": "ей",
            "dat-sg": "ей",
            "acc-sg": "ю",
            "ins-sg": "ей",
            "prp-sg": "ей",
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        },
        "7-letter-и": {
            "nom-sg": "я",
            "gen-sg": "ей",
            "dat-sg": "ей",
            "acc-sg": "ю",
            "ins-sg": "ей",
            "prp-sg": "ей",
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        }
    },
    "n": {
        "1-hard": {
            "nom-sg": "о",
            "gen-sg": "а",
            "dat-sg": "у",
            "ins-sg": "ым",
            "prp-sg": "е",
            "nom-pl": "ы",
            "gen-pl": "ых",
            "dat-pl": "ым",
            "ins-pl": "ыми",
            "prp-pl": "ых"
        },
        "2-soft": {
            "nom-sg": ["е", "ё"],
            "gen-sg": "я",
            "dat-sg": "ю",
            "ins-sg": "им",
            "prp-sg": ["ем", "ём"],
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        },
        "3-velar": {
            "nom-sg": "о",
            "gen-sg": "а",
            "dat-sg": "у",
            "ins-sg": "ым",
            "prp-sg": "е",
            "nom-pl": "ы",
            "gen-pl": "ых",
            "dat-pl": "ым",
            "ins-pl": "ыми",
            "prp-pl": "ых"
        },
        "4-sibilant": {
            "nom-sg": ["е", "о"],
            "gen-sg": ["его", "ого"],
            "dat-sg": ["ему", "ому"],
            "ins-sg": "им",
            "prp-sg": ["ем", "ом"],
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        },
        "5-letter-ц": {
            "nom-sg": "о",
            "gen-sg": "а",
            "dat-sg": "у",
            "ins-sg": "ым",
            "prp-sg": "е",
            "nom-pl": "ы",
            "gen-pl": "ых",
            "dat-pl": "ым",
            "ins-pl": "ыми",
            "prp-pl": "ых"
        },
        "6-vowel": {
            "nom-sg": ["е", "ё"],
            "gen-sg": "его",
            "dat-sg": "ему",
            "ins-sg": "им",
            "prp-sg": ["ем", "ём"],
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        },
        "7-letter-и": {
            "nom-sg": ["е", "ё"],
            "gen-sg": "я",
            "dat-sg": "ю",
            "ins-sg": "им",
            "prp-sg": ["ем", "ём"],
            "nom-pl": "и",
            "gen-pl": "их",
            "dat-pl": "им",
            "ins-pl": "ими",
            "prp-pl": "их"
        }
    }
}