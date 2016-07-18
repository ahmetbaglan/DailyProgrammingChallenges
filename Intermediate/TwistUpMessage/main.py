import requests
from bs4 import BeautifulSoup
import re
import random



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


def twistIt(d, text):
    b = ""
    for i in a:
        b = b + d[i][random.randint(0, len(d[i]))]
    return  b

def deTwistIt(d, text):## CHANGE
    # for i in d.values():
    #     for t in text:
    #         if t in i:
    pass

a = raw_input("lol")

print twistIt(my_dict, a)

