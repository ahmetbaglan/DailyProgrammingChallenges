import requests
from bs4 import BeautifulSoup
import re



url = 'http://pinyin.info/unicode/diacritics.html'
req = requests.get(url)
req.status_code
soup = BeautifulSoup(req.text,'html.parser')
table = soup.find('table')
lines = table.find_all('tr')
my_dict = {}
a = []
nowLetter = ''
for l in lines:
    if(l.get("class") == ["letter_separator"]):
        a = l.find_all('td')
        nowLetter = a[1].text
        my_dict[nowLetter] = []
    else:
        if(len(my_dict)!= 0):
            a = l.find_all('td')
        if(len(a) == 4):
            my_dict[nowLetter].append(a[1].text)

a = raw_input("lol")
b = ""
for i in a:
    b = b + my_dict[i][0]

print b

