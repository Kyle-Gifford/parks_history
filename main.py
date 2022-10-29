import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Globe_Life_Field'
# url = 'https://en.wikipedia.org/wiki/Yankee_Stadium'
result = requests.get(url)
html_doc = result.text

# with open("glf.txt") as file:
#     html_doc = file.read()


loc = html_doc.find('<h2><span class="mw-headline" id="History">')
loc2 = html_doc.find('<h2>', loc+1)
html_doc = html_doc[loc:loc2]

soup = BeautifulSoup(html_doc, 'html.parser')

all_p = soup.find_all('p')

output = ""
for para in all_p:
    output += para.get_text()
print(output)