#!/usr/bin/python3
""" Get response from a given URL"""

if __name__ == '__main__':
    import sys
    import urllib.request

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        header = response.info()

    print(header.get('X-Request-Id'))
