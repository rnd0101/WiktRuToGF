# -*- coding: utf-8 -*-
from parse_common import load
from parse_common import main

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--xml-dump-path", help="Path of XML dump")
    parser.add_argument("-o", "--output-path", help="Path of output file")
    parser.add_argument("-f", "--format", help="Format for output")
    parser.add_argument("-l", "--load", action="store_true", help="load")
    parser.add_argument("-p", "--pos", help="Part of speech")
    parser.add_argument("-t", "--title", help="Single title")
    args = parser.parse_args()
    if args.load:
        load(args.xml_dump_path, args.format, args.pos)
    else:
        main(args.xml_dump_path, args.format, args.output_path, args.pos, args.title)
