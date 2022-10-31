# github URL:
# https://github.com/Kyle-Gifford/parks_history


# public facing URL:
# https://parkshistory.chichone.repl.co/ParkNameHere


PORT = 8080 # use port of your choice
HOST = 'localhost'

try:
    from credentials import *
    PORT = chosen_port
    HOST = chosen_host
except:
    PORT = 8080
    HOST = 'localhost'

import requests
from bs4 import BeautifulSoup
from flask import Flask, Response
import json


app = Flask(__name__)

@app.route('/<string:search_term>')
def get_history(search_term):
    # search for wikipedia article
    search_url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search={}&limit=1&namespace=0&format=json'.format(search_term)
    response = requests.get(search_url)
    url = json.loads(response.text)
    # 404 if no search result found
    try:
        url = url[3][0]
    except:
        return Response(status=404)

    # get article
    response = requests.get(url)
    
    # return 404 if article not found
    if response.status_code != 200:
        return Response(status=response.status_code)
    html_doc = response.text

    beginning = html_doc.find('<h2><span class="mw-headline" id="History">')
    # if article has no history return 404
    if beginning < 0:
        return Response(status=404)

    end = html_doc.find('<h2>', beginning+1)
    html_doc = html_doc[beginning:end]
    
    parsed_html = BeautifulSoup(html_doc, 'html.parser')
    
    all_paragraphs = parsed_html.find_all('p')
    
    history = ""
    for para in all_paragraphs:
        history += '\n'
        history += para.get_text()

    dny = {"history": history[1:]} # remove initial newline

    return json.dumps(dny)


if __name__ == '__main__':
   app.run(host=HOST, port=PORT, debug=True)