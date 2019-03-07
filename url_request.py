#!/home/roadrunner/venvs/exp/bin/python

import sys
import os
import requests
import json

from argparse import ArgumentParser

parser = ArgumentParser(description='Writes the URL content to the destination file')
parser.add_argument('url', help='URL to read content')
parser.add_argument('file', help='destination file for URL content')
parser.add_argument('--type', default='html', help='responce type JSON or HTML')

args = parser.parse_args()
r = requests.get(args.url)

with open (f'./{args.file}', 'w') as f:
    if args.type == 'json':
        content = r.json()
        try:
            json.dump(content, f)
        except ValueError:
            print(f'Error: {args.url} not in JSON format!')

    else:
        f.write(r.text)


