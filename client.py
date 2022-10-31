import requests
import json

search_term = "petco park"

search_url = 'http://host:port/{}'.format(search_term)

try:
    response = requests.get(search_url)
    response_dny = json.loads(response.text)
    history = response_dny['history']
    print(history)
except:
    print('unable to retreive stadium history')