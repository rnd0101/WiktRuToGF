import os
import sys
from urllib.parse import urlencode
import cyrtranslit

import requests
from bs4 import BeautifulSoup

URL = "https://ru.wiktionary.org/w/index.php"

ns = "Шаблон:{}"
SHABLON_EXAMPLE = "Шаблон:гл ru 4b-тСВ"


def convert_name(name):
    name = name.replace("гл ru ", "")
    name = "v_" + name \
        .replace(".", "_dot_") \
        .replace("ь", "6") \
        .replace("Ь", "6") \
        .replace("НСВ", "_imperf_") \
        .replace("СВ", "_perf_") \
        .replace("^", "_hat_") \
        .replace("°", "_deg_") \
        .replace("&quot;", "_quot_") \
        .replace("^/", "_sl_")
    name = cyrtranslit.to_latin(name, "ru")
    return name


def save_to_file(name, text):
    file_name = convert_name(name)
    file_path = os.path.join("../wiki_page_cache", file_name)
    with open(file_path, "wt") as fh:
        fh.write(text)


def make_url(name):
    """
    "https://ru.wiktionary.org/w/index.php?title=%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD:%D0%B3%D0%BB_ru_4b-%D1%82%D0%A1%D0%92&action=edit"
    """
    name = name.replace(" ", "_")
    return URL + "?" + urlencode({"title": name, "action": "edit"})


def get_shablon_text(name):
    url = make_url(ns.format(name))
    print(url)
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find("textarea", {"id": "wpTextbox1"}).get_text()


if __name__ == "__main__":
    name = sys.argv[1]
    text = get_shablon_text(name)
    # text ="111"
    save_to_file(name, text)
    # egrep ':гл ru 6a<' ../wikt/ruwiktionary.xml -A 100 -B 1
    # egrep 'гл ru 7b/bСВ' ../wikt/ruwiktionary.xml  -B 50 | egrep '<title>[^<]+</title>'
