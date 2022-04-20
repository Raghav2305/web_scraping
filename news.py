from urllib import response
from bs4 import BeautifulSoup
import pandas as pd
import csv
import requests


URL = "https://www.nytimes.com/international/section/politics"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
news = []

table = soup.find('img', attrs={'class': 'css-13mho3u'})



# for row in table.find_all('a'):
#    news.append(row)
#    print(news, end='\n')

# for row in table.find_all(['h2', 'p'], attrs={'class': 'css-1j9dxys e15t083i0', 'class':'css-1echdzn e15t083i1'}):
#    news.append(row.text)
#    print((news), end='\n')
# for row in table.find_all('a', attrs={'href': '/2022/'}):
   
#    print(row, end='\n')

# for row in table.find_all(['h2', 'p'], attrs={'class':'css-1j9dxys e15t083i0', 'class':'css-1echdzn e15t083i1'}):
#    news.append(row.text)
#    print("".join(news))
#    break 

