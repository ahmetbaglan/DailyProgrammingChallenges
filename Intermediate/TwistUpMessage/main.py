import requests
from bs4 import BeautifulSoup
import re



url = 'http://pinyin.info/unicode/diacritics.html'
req = requests.get(url)
req.status_code
soup = BeautifulSoup(req.text,'html.parser')
table = soup.find('table')
lines = table.find_all('tr')

for l in lines:
    a = l.find_all('td')

