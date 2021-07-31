def get_rus_acc_table():
    return {
        "m": {
            "1-hard": (["snom", "pnom"], ["sgen", "pgen"]),
            "2-soft": (["snom", "pnom"], ["sgen", "pgen"]),
            "3-velar": (["snom", "pnom"], ["sgen", "pgen"]),
            "4-sibilant": (["snom", "pnom"], ["sgen", "pgen"]),
            "5-letter-ц": (["snom", "pnom"], ["sgen", "pgen"]),
            "6-vowel": (["snom", "pnom"], ["sgen", "pgen"]),
            "7-letter-и": (["snom", "pnom"], ["sgen", "pgen"]),
            "8-third": (["snom", "pnom"], ["sgen", "pgen"]),  # путь
        },
        "f": {
            "1-hard": (["у", "pnom"], ["у", "pgen"], "ins-sg", "ою"),  # корова, лопата
            "2-soft": (["ю", "pnom"], ["ю", "pgen"], "ins-sg", "ею"),
            "3-velar": (["у", "pnom"], ["у", "pgen"], "ins-sg", "ою"),  # дорогой-дорогою, собака-собакою
            "4-sibilant": (["у", "pnom"], ["у", "pgen"], "ins-sg", "ою-ею"),  # кляча, саранча
            "5-letter-ц": (["у", "pnom"], ["у", "pgen"], "ins-sg", "ею"),
            "6-vowel": (["ю", "pnom"], ["ю", "pgen"], "ins-sg", "ею-ёю"),
            "7-letter-и": (["ю", "pnom"], ["ю", "pgen"], "ins-sg", "ею-ёю"),
            "8-third": (["ь", "pnom"], ["ь", "pgen"], "ins-sg", "ию-ью"),
        },
        "n": {
            "1-hard": (["snom", "pnom"], ["sgen", "pgen"]),
            "2-soft": (["snom", "pnom"], ["sgen", "pgen"]),
            "3-velar": (["snom", "pnom"], ["?", "pgen"]),
            "4-sibilant": (["snom", "pnom"], ["snom", "pgen"]),
            "5-letter-ц": (["snom", "pnom"], ["snom", "pnom"]),
            "6-vowel": (["snom", "-"], ["snom", "-"]),  # -no-pl
            "7-letter-и": (["snom", "pnom"], ["snom", "pnom"]),
            "8-third": (["snom", "pnom"], ["?", "?"]),
        }
    }
