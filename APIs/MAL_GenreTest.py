import requests
import json

API = "https://api.jikan.moe/v3"
path = "/manga/1/"
response = requests.get(API+path)


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=3)
    print(text)


jprint(response.json()['genres'])