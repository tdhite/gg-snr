#!/usr/bin/env python3

import os

SERVER_GG_DIR = '/var/www/_gg'
os.environ['GG_RUNNER'] = '1'
os.environ['GG_DIR'] = SERVER_GG_DIR

import cgi
import sys
import time
import json
import base64

import function as lambdafunc
from ggpaths import GGPaths, GG_DIR, make_gg_dirs

with open("config") as fin:
    for line in fin:
        line = line.strip()
        line = line.split('=')
        os.environ[line[0]] = line[1]

request_data = sys.stdin.read()
event = json.loads(request_data)

try:
    output = lambdafunc.handler(event, {})
except Exception as ex:
    output = {
        'errorType': ex.__class__.__name__,
        'message': str(ex)
    }

output_data = json.dumps(output)
sys.stdout.write('Content-Length: {}\r\n'.format(len(output_data)))
sys.stdout.write('\r\n')

sys.stdout.write(output_data)