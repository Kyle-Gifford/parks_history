PORT = 8080 # use port of your choice

import requests
from bs4 import BeautifulSoup
from flask import Flask, Response
import json


app = Flask(__name__)

@app.route('/<string:park_name>')
def get_history(park_name):
    url = 'https://en.wikipedia.org/wiki/' + park_name
    response = requests.get(url)
    
    # return 404 if not found
    if response.status_code != 200:
        return Response(status=response.status_code)
    html_doc = response.text

    beginning = html_doc.find('<h2><span class="mw-headline" id="History">')
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
   app.run(host="0.0.0.0", port = PORT)