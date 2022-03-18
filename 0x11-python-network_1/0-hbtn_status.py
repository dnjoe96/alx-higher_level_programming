#!/usr/bin/python3
""" Get response from a given URL"""

if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        http = response.read()
        print('Body response:')
        print(f'\t- type: {type(http)}')
        print(f'\t- content: {http}')
        print(f'\t- utf8 content: {http.decode("utf-8")}')
