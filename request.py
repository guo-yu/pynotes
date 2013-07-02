#!/usr/bin/python
# Filename : request.py

import requests

r = requests.get('http://google.com')

if r.status_code == 200:
  print 'your network access is cool'
else:
  print 'you are behind the GFW'