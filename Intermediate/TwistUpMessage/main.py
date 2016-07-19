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
my_dict = {" ": " "}
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
        b = b + d[i][random.randint(0, len(d[i])-1)]
    return  b

def findTheKey(d,v):#NOT VERY SURE IF THIS WILL ALWAYS WORK
    a = list(d.keys())
    b = list(d.values())
    for l in b:
        if v in l:
            return a[b.index(l)]
    return None

def deTwistIt(d, text):## CHANGE
    b = ""
    for  t in text:
        r = findTheKey(d,t)
        if(r != None):
            b+=r
    return b

a = raw_input("lol")

print deTwistIt(my_dict,twistIt(my_dict, a))

