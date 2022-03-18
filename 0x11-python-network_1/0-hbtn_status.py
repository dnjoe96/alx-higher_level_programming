#!/usr/bin/env python3
""" Get response from a given URL"""

import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
response = urllib.request.urlopen(req).read()

print('Body Response:')
print('\t- type: {}'.format(type(response)))
print('\t- content: {}'.format(response))
print('\t- utf-8 content: {}'.format(response.decode()))
