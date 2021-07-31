"""
Reorganize

"""

from wikt_decl_table import get_rus_adjective_table
from wikt_stress_table import get_rus_adj_stress_table

STRESSED = "Stressed"
UNSTRESSED = "Unstressed"

GENDER_MAP = {
    "f": "Fem",
    "m": "Masc",
    "n": "Neut",
}

STEM_MAP = {
    "1-hard": 1,
    "2-soft": 2,
    "3-velar": 3,
    "4-sibilant": 4,
    "5-letter-ц": 5,
    "6-vowel": 6,
    "7-letter-и": 7,
    "8-third": 8
}

CASE_MAP = {
    "m": {
        "nom-sg": "msnom",
        "gen-sg": "msgen",
        "dat-sg": "ms",
        "acc-sg": "ms",
        "ins-sg": "ms",
        "prp-sg": "ms",
        "srt-sg": "sm",
    },
    "f": {
        "nom-sg": "fsnom",
        "gen-sg": "fsgen",
        "dat-sg": "fsdat",
        "acc-sg": "fsacc",
        "ins-sg": "fsins",
        "prp-sg": "fsprep",
        "srt-sg": "sf",
    },
    "n": {
        "nom-sg": "nsnom",
        "gen-sg": "nsgen",
        "dat-sg": "nsdat",
        "acc-sg": "nsacc",
        "ins-sg": "nsins",
        "prp-sg": "nsprep",
        "srt-sg": "sn",
    },
    "pl": {
        "nom-pl": "pnom",
        "gen-pl": "pgen",
        "dat-pl": "pdat",
        "acc-pl": "pacc",
        "ins-pl": "pins",
        "prp-pl": "pprep",
        "srt-pl": "sp"
    }
}

NUMCASE_MAP = {
    "nom-sg": "?snom",
    "gen-sg": "?sgen",
    "dat-sg": "?sdat",
    "acc-sg": "?sacc",
    "ins-sg": "?sins",
    "prp-sg": "?sprep",
    "nom-pl": "pnom",
    "gen-pl": "pgen",
    "dat-pl": "pdat",
    "acc-pl": "pacc",
    "ins-pl": "pins",
    "prp-pl": "pprep",
    "srt-sg-m": "sm",
    "srt-sg-f": "sf",
    "srt-sg-n": "sn",
    "srt-pl": "sp"
}

to_save = {
    "msnom",
    "fsnom",
    "nsnom",
    "pnom",
    "msgen",
    "fsgen",
    "pgen",
    "msdat",
    "fsacc",
    "msins",
    "fsins",
    "pins",
    "msprep",
    "sm",
    "sf",
    "sn",
    "sp",
}


def stress_map(s):
    return s.upper()


def format_record(d):
    return "{" + ";".join(f'{k}={v}' for k, v in d.items()) + "}"


def get_numcase(case, g):
    if case.startswith("srt") and not case.endswith("pl"):
        case = case + "-" + g
    mcase = NUMCASE_MAP[case]
    if "?" in mcase:
        mmcase = mcase.replace("?", g)
    else:
        mmcase = mcase
    if mmcase in to_save:
        return mmcase


def stressed_items(value):
    for case, stressed in value["ending"].items():
        if stressed:
            mcase = NUMCASE_MAP[case]
            if "?" in mcase:
                for g in "mfn":
                    mmcase = mcase.replace("?", g)
                    if mmcase in to_save:
                        yield mmcase
            else:
                if mcase in to_save:
                    yield mcase


def produce_stress_table(orig, indent=" " * 6):
    lines = []
    for stress_type, value in orig.items():
        mstress_type = stress_map(stress_type).replace("/", "_")
        mcases = '"|"'.join(list(stressed_items(value)))
        if mcases:
            lines.append(f'{indent}<{mstress_type}, "{mcases}"> => {STRESSED}')
    lines.append(f'{indent}<_, _> => {UNSTRESSED}')
    return " ;\n".join(lines)


PROCEDURE = r"""
  stressSelectionAdj : EndingSpec -> StressSchema -> Str -> Str
    = \es, ss, c ->
    selStress es (stressTable ss c) ;

  stressTableAdj : StressSchema -> Str -> Stressedness
    = \ss, c ->
    case <ss, c> of {
%(stresses)s
    } ;

  gDtBasedSelectionAdj : Gender -> DeclType -> AdjectiveEndFormsS1
    = \g, dt -> case dt of {
      0 => immutableCasesS1 ;
%(endings)s
    } ;
}
"""


def produce_endings_table(orig, indent=" " * 6):
    lines = []
    case_rec = {}
    for g, gv in orig.items():
        mg = GENDER_MAP.get(g)
        for stem, sv in gv.items():
            mstem = STEM_MAP[stem]
            case_rec.setdefault(mstem, {})
            for case in CASE_MAP[g]:
                mcase = sv[case]
                if type(mcase) != list:
                    mcase = [mcase, mcase]

                mmcase = get_numcase(case, g)
                if mmcase is not None:
                    case_rec[mstem][mmcase] = '<{}>'.format(",".join('"{}"'.format(m) for m in mcase))
            # del case_rec["sacc"], case_rec["pacc"]
    for mstem in case_rec:
        fcase_rec = format_record(case_rec[mstem])
        if mg is None:
            lines.append(f"{indent}{mstem} => {fcase_rec}")
        else:
            lines.append(f"{indent}{mstem} => {fcase_rec}")
    return " ;\n".join(lines)


def main():
    endings = produce_endings_table(get_rus_adjective_table())
    stresses = produce_stress_table(get_rus_adj_stress_table())
    print(PROCEDURE % {"endings": endings, "stresses": stresses})


if __name__ == "__main__":
    main()
