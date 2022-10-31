# parks_history
This is a web scraper api that retreives history from wikipedia pages

## How to request data:
The calling process will make an http request using the url of the process followed by the name of a ballpark
for example if the api was running on http://localhost:64123, the desired program or individual would perform an http GET request to:
http://localhost:64123/stadium name
e.g. http://localhost:64123/Coors_Field

## How to receive data:
Data is sent as an HTTP response with JSON data. The only attribute of the data is "history" which contains a string of the history for a given page. This json data may be parsed to be of further use.
Python parse example:<br>
history will be saved in the "history" variable.
```
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
```
## UML
![UML](/images/uml.png)