# import requests
# from bs4 import BeautifulSoup

# def process(path):
#     url = path
#     reqs = requests.get(url)
#     soup = BeautifulSoup(reqs.text, 'html.parser')

#     for link in soup.find_all('a'):
#         print(link.get('href'))

# process("https://www.quera.org/")

import re

def process(path):
    with open(path) as f:
        urls = f.read()
        links = re.findall('"((http)s?://.*?)"', urls)
        result = []
    for url in links:
        result.append(url[0])
    
    return result

print(process("htmlsampletest2.html"))

