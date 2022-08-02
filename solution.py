import requests
from bs4 import BeautifulSoup

def process(path):
    url = path
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    for link in soup.find_all('a'):
        print(link.get('href'))

process("https://www.quera.org/")