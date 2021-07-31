# -*- coding: utf-8 -*-
import re

import adjective_parser
from common_parser import from_cache
from common_parser import get_article
from common_parser import to_cache
import verb_parser
import noun_parser

OUTSIDE = 0
INSIDE = 1

PAGE_RE = re.compile("<title>(.+?)</title>")
TEMPLATE_TITLE_RE = re.compile(r"Шаблон:(прил|сущ|гл)[ -]?ru")
TEMPLATE_PRESENT_RE = re.compile(r"Шаблон:(прил|сущ|гл)[ -]ru\b|[{][{](прил|сущ|гл)[ -]?ru")


def articles_iter(xml_dump_path, pos, pattern):
    """ Iterate all articles, where pos is 'гл', 'сущ' "
    """
    with open(xml_dump_path, "rt") as infile:
        state = OUTSIDE
        current_article = ""
        for line in infile:
            if state == OUTSIDE:
                if line.strip() == "<page>":
                    current_article = line
                    state = INSIDE
            else:
                current_article += line
                if line.strip() == "</page>":
                    state = OUTSIDE
                    if TEMPLATE_PRESENT_RE.search(current_article):
                        yield current_article


def single_article(pos, title, page, xml_dump_path, output_path, output_format):
    cached_page = from_cache(title)
    if cached_page and cached_page != page:
        print(f"page {title} changed")
    to_cache(title, page)
    if "{{{{{} ru".format(pos) in page or "{{{{{}-ru".format(pos) in page:
        if pos == "гл":
            try:
                verb_parser.transform_article(page, output_format, title, xml_dump_path, output_path)
            except KeyError:
                print("-- failed --")
                raise
        elif pos == "сущ":
            try:
                noun_parser.transform_article(page, output_format, title, xml_dump_path, output_path)
            except KeyError:
                raise
                print("-- failed --")
        elif pos == "прил":
            try:
                adjective_parser.transform_article(page, output_format, title, xml_dump_path, output_path)
            except KeyError:
                print("-- failed --")
                raise


def main(xml_dump_path, output_format, output_path, pos, title):
    if title:
        print(" {} ".format(adjective_parser.slug(title)))
        page = get_article(title, xml_dump_path)
        single_article(pos, title, page, xml_dump_path, output_path, output_format)
    else:
        for page in articles_iter(xml_dump_path, pos, ''):
            m = PAGE_RE.search(page)
            if m:
                title = m.group(1)
                if ":" in title and not TEMPLATE_TITLE_RE.search(title):
                    continue

                single_article(pos, title, page, xml_dump_path, output_path, output_format)


def load(xml_dump_path, output_format, pos):
    for page in articles_iter(xml_dump_path, pos, ''):
        m = PAGE_RE.search(page)
        if m:
            title = m.group(1)
            if ":" in title and not TEMPLATE_TITLE_RE.search(title):
                continue

            cached_page = from_cache(title)
            if cached_page and cached_page != page:
                print(f"page {title} changed")
            to_cache(title, page)
            print(f"{title}")
