#-*- coding:utf-8 -*-
import json
from pprint import pprint
import sys
from xml.etree import ElementTree
import os

def extract_from_opml(filename):
    results = []
    with open(filename, 'rt', encoding='utf-8') as f:
        text = f.read()
        tree = ElementTree.fromstring(text)
    for node in tree.findall('.//outline'):
        url = node.attrib.get('xmlUrl')
        title = node.attrib.get('title')
        if url:
            results.append({"url":url,
                            "title":title})

    # ensure_ascii=False 옵션이 한글 깨짐 원인
    return json.dumps({"sources-rss": results}, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print("No file supplied, exiting")
        exit()

    sources = extract_from_opml(sys.argv[1])
    with open( os.path.splitext(sys.argv[1])[0] + ".json", 'wt', encoding='utf-8') as f:
        f.write(sources);