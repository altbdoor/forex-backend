#!/usr/bin/env python

import json
import ssl
import sys
import urllib.request

api_key = sys.argv[1]
api_url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}'

# https://stackoverflow.com/a/33770290/6616962
ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

with urllib.request.urlopen(api_url, context=ctx) as r, open('data.json', 'w') as f:
    content = r.read()
    content = json.loads(content)
    f.write(json.dumps(content['rates']))

# crontab hourly "0 0 * * *"
