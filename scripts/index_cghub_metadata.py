#! /usr/bin/env python3
import argparse
import json
import logging
import sys

from lxml import etree
import requests

FLUSH_FREQUENCY = 100
UPDATE_URL = 'http://localhost:8983/solr/cgsearch/update?commit=true'
UPDATE_HEADERS =  {'content-type': 'application/json'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--metadata-file', dest='metadata_file', required=True)
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    if args.verbose: logging.basicConfig(level=logging.DEBUG)

    context = etree.iterparse(open(args.metadata_file, "rb"), events=("start",), tag="Result")
    to_post = []
    for i, event in enumerate(context):
        elem = event[1]
        id = elem.attrib.get('id')
        disease_abbr = elem.xpath('disease_abbr/text()')
        to_post.append({'id': id, 'disease_abbr': disease_abbr})
        if not i % FLUSH_FREQUENCY:
            requests.post(UPDATE_URL, headers=UPDATE_HEADERS, data=json.dumps(to_post))
            logging.debug("Indexed % results" % i)
            to_post = []
