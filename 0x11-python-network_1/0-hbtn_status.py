#!/usr/bin/python3
""" Get response from a given URL"""

if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    response = urllib.request.urlopen(req).read()

    print('Body Response:')
    print(f'\t- type: {type(response)}')
    print(f'\t- content: {response}')
    print(f'\t- utf8 content: {response.decode("utf-8")}')
