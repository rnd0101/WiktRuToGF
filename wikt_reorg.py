"""
Reorganize into:

StemType Gender Stress => {
      snom  = "" ;
      pnom  = "ы" ;
      sgen  = "а" ;
      pgen  = "ов" ;
      sdat  = "у" ;
      pdat  = "ам" ;
      sacc  = "" ;
      pacc  = "ы" ;
      sins  = "ом" ;
      pins  = "ами" ;
      sprep = "е" ;
      pprep = "ах" ;
  }


"""

from wikt_decl_table import get_rus_noun_table
from wikt_stress_table import get_rus_noun_stress_table

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
    "nom-sg": "snom",
    "nom-pl": "pnom",
    "gen-sg": "sgen",
    "gen-pl": "pgen",
    "dat-sg": "sdat",
    "dat-pl": "pdat",
    "acc-sg": "sacc",
    "acc-pl": "pacc",
    "ins-sg": "sins",
    "ins-pl": "pins",
    "prp-sg": "sprep",
    "prp-pl": "pprep",
}


def stress_map(s):
    return s.upper()


def format_record(d):
    return "{" + ";".join(f'{k}={v}' for k, v in d.items()) + "}"


def produce_stress_table(orig, indent=" " * 6):
    lines = []
    for stress_type, value in orig.items():
        mstress_type = stress_map(stress_type)
        mcases = '"|"'.join(CASE_MAP[case] for case, stressed in value["ending"].items() if stressed)
        if mcases:
            lines.append(f'{indent}<{mstress_type}, "{mcases}"> => {STRESSED}')
    lines.append(f'{indent}<_, _> => {UNSTRESSED}')
    return " ;\n".join(lines)


PROCEDURE = r"""
  stressSelection : EndingSpec -> StressSchema -> Str -> Str
    = \es, ss, c ->
    selStress es (stressTable ss c) ;

  stressTable : StressSchema -> Str -> Stressedness
    = \ss, c ->
    case <ss, c> of {
%(stresses)s
    } ;

  gDtBasedSelection : Gender -> DeclType -> NounEndFormsS1
    = \g, dt -> case <g, dt> of {
      <_, 0> => immutableCasesS1 ;
%(endings)s
    } ;
}
"""


def produce_endings_table(orig, indent=" " * 6):
    lines = []
    for g, gv in orig.items():
        mg = GENDER_MAP[g]
        for stem, sv in gv.items():
            mstem = STEM_MAP[stem]
            case_rec = {}
            for case in CASE_MAP:
                mcase = sv[case]
                if type(mcase) != list:
                    mcase = [mcase, mcase]
                case_rec[CASE_MAP[case]] = '<{}>'.format(",".join('"{}"'.format(m) for m in mcase))
            # del case_rec["sacc"], case_rec["pacc"]
            fcase_rec = format_record(case_rec)
            lines.append(f"{indent}<{mg}, {mstem}> => {fcase_rec}")
    return " ;\n".join(lines)


def main():
    # print({v: k + 1 for (k, v) in enumerate(list(get_rus_noun_table().values())[0].keys())})
    endings = produce_endings_table(get_rus_noun_table())
    stresses = produce_stress_table(get_rus_noun_stress_table())
    print(PROCEDURE % {"endings": endings, "stresses": stresses})


# print(get_rus_noun_stress_table())


if __name__ == "__main__":
    main()
