import requests
import json
import time
from tqdm.auto import tqdm

API = "https://api.jikan.moe/v3"
path = "/top/manga"
pages = 269

# Need to get mal_id, rank, title, type, score
# Iterate through each page
for i in tqdm(range(1, pages)):
    response = requests.get(f"{API}{path}/{i}")
    # Iterates through each item on the page and 'indexes' the items (i.e [0], [1], [2], etc)
    time.sleep(1.5)
    for item in response.json()['top']:
        # Here, you can add the specific info you want
        print(item["mal_id"], item['rank'], item['title'], item['score'], item['type'])


'''response = requests.get(API+path)
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())'''