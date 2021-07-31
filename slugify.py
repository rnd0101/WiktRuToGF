# -*- coding: utf-8 -*-
from adjective_parser import slug

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-path", help="Path of input file")
    parser.add_argument("-o", "--output-path", help="Path of output file")
    parser.add_argument("-f", "--format", help="""Format for output like '  {slug}_Adv = "{word}" ;'  """)
    args = parser.parse_args()

    with open(args.input_path) as inp:
        with open(args.output_path, "a") as out:
            for line in inp.readlines():
                out.write(args.format.format(slug=slug(line.strip()), word=line.strip()))
                out.write("\n")
