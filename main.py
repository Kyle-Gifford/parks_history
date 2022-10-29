import requests
from bs4 import BeautifulSoup

park_name = "Yankee_Stadium"
park_name = "Globe_Life_Field"


# TODO uncomment dev mode
# url = 'https://en.wikipedia.org/wiki/' + park_name
# result = requests.get(url)
# html_doc = result.text

# TODO remove dev mode from file
park_file = park_name + ".txt"
with open(park_file) as file:
    html_doc = file.read()


loc = html_doc.find('<h2><span class="mw-headline" id="History">')
loc2 = html_doc.find('<h2>', loc+1)
html_doc = html_doc[loc:loc2]

soup = BeautifulSoup(html_doc, 'html.parser')

all_p = soup.find_all('p')

output = ""
for para in all_p:
    output += para.get_text()
print(output)