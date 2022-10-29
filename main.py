import requests
# import json
from bs4 import BeautifulSoup

# url = 'https://en.wikipedia.org/wiki/Globe_Life_Field'
# x = requests.get(url)
# html_doc = x.text

with open("glf.txt") as file:
    html_doc = file.read()

print(html_doc)

loc = html_doc.find('<h2><span class="mw-headline" id="History">')
print('***')
print(loc)
print('^^^')

# soup = BeautifulSoup(html_doc, 'html.parser')
# print('hi from main')
# all_p = soup.find_all('p')
# para_count = 0
# for para in all_p:
#     if para_count > 3:
#         break
#     para_count += 1
#     print(para.get_text())
# for para_num in range(4):
#     print(all_p[para_num].get_text())
print('done')