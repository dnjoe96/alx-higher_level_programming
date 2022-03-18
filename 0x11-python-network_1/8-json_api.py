#!/usr/bin/python3
""" Sends a post request  """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        info = {"q": sys.argv[1]}
    else:
        info = {"q": ""}
    r = requests.post("http://0.0.0.0:5000/search_user", data=info)
    try:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] ".format(r.json().get("id")), end="")
            print(r.json().get("name"))
    except Exception as e:
        print("Not a valid JSON")
