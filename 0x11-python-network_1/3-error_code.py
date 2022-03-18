#!/usr/bin/python3
""" Get response from a given URL"""

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.error

    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as response:
            http = response.read()
        print(http.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
