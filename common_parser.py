# -*- coding: utf-8 -*-
import os
import re
import subprocess
from hashlib import sha1

from bs4 import BeautifulSoup

PAGE_RE = re.compile(r"<page>.+?</page>", re.DOTALL)
ARTICLE_CACHE = os.path.join(os.path.dirname(__file__), "../wiki_page_cache")


def parse_article(xml):
    if not xml:
        return {"text": ""}
    soup = BeautifulSoup(xml, 'lxml')
    try:
        return {
            "text": soup.find("text").get_text()
        }
    except:
        pass


def take_page(text):
    m = PAGE_RE.search(text)
    if m:
        return m.group(0)


def slugify_article(name):
    return sha1(name.encode("utf-8")).hexdigest()


def from_cache(title):
    title = title.replace("&quot;", '"')
    cache_location = os.path.join(ARTICLE_CACHE, slugify_article(title))
    if os.path.exists(cache_location):
        return open(cache_location, "rt").read()


def to_cache(title, page):
    title = title.replace("&quot;", '"')
    cache_location = os.path.join(ARTICLE_CACHE, slugify_article(title))
    with open(cache_location, "wt") as outfile:
        outfile.write(page)


def get_article(name, file_path):
    page = from_cache(name)
    if page is None:
        cmd = (
            '/usr/bin/grep', "'<title>{}</title>'".format(name.replace('"', "&quot;")), '-A', '10000', '-B', '3',
            file_path)
        print("CMD: {}".format(" ".join(cmd)))
        s = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE)
        output = s.communicate()[0].decode("utf-8")
        if output:
            page = take_page(output)
            to_cache(name, page)

    return page
