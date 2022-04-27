

# URL = "https://www.instagram.com/"
# r = requests.get(URL)

# soup = BeautifulSoup(r.content, "html.parser")

# for row in soup.findAll('div', attrs={'class': '_7UhW9  PIoXz       MMzan    _0PwGv          uL8Hv         '}):
#     print((row.text))

# for row in soup.findAll('p', attrs={'class': 'izU2O '}):
#     print(row)
# table = soup.find('div', attrs={'class':'class="article_consum_wrapper article_page infinite-scroll "'})

# for row in table.findAll('h1', attrs={'class': 'article_title artTitle'}):
#     print(row.text)
# # for img in table.find_all('img'):
# #     print(img)

#Working code
from distutils.log import error
from importlib.resources import path
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import json, os

contents = []
url = "https://www.moneycontrol.com"
# url = "https://replit.org"
# url = "https://www.codewithharry.com"
# url = "https://stackoverflow.com"
# url = "https://www.geeksforgeeks.org"
# url = "https://finance.yahoo.com"

headers = {'Accept': 'text/html'}
r = requests.get(url, headers=headers)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

def scrape(url):
## Get Contents

    title = soup.title

    print('\n\033[1m' + f"Title = {title.text}" '\033[0m')
    contents.append({"Title": title.text})

    try:
        paras = soup.find_all('p')
        if paras:
            print(f"'\033[1m'+ Para = {paras.text} +'\033[0m'"  )
            contents.append({"Paragraph": paras.text})

    except :
        paras = soup.find('p')
        print('\033[1m' + f"Para = {paras.text}" +'\033[0m')
        contents.append({"Paragraph": paras.text})

    try:
        h1s = soup.find_all('h1')
        if h1s:
            print('\033[1m' + f"H1 = {h1s.text}" + '\033[0m', end='\n', sep='\n')
            contents.append({"H1": h1s.text})
    except :
        h1s = soup.find('h1')
        print('\033[1m' + f"H1 = {h1s.text}" + '\033[0m', end='\n', sep='\n')
        contents.append({"H1": h1s.text})

    try:
        
        h2s = soup.find_all('h2')
        if h2s:
            print('\033[1m' + f"H2 = {h2s.text}" + '\033[0m', end='\n', sep='\n')
            contents.append({"H2": h2s.text})
    except :
        h2s = soup.find('h2')
        print('\033[1m' + f"H2 = {h2s.text}" +'\033[0m', end='\n', sep='\n')
        contents.append({"H2": h2s.text})
## Get Tables
    
    scrape_tables(url)

## Get Links

    try:
        anchors = soup.find_all('a')
        # all_links = set()
        # for link in anchors:
        #     if(link.get('href') != '#'): 
        #         linkText = url +link.get('href')
        #         all_links.add(link)
        all_links = []
        print("\n")

        print('\033[1m' + "Links Sucessfully scraped! " +'\033[0m')
        for linkk in anchors:
            
            if linkk['href'].startswith("https://"):
                all_links.append(linkk['href'])
            else:
                all_links.append(url + linkk['href'])
        contents.append({"Links": all_links})

    except:
        print('----------------------------------------------')

## Get Images

    image_tags = soup.find_all('img')
    links = []
    for image_tag in image_tags:
        
        if image_tag['src'].startswith("https://"):
            links.append(image_tag['src'])
        else:
            links.append(url + image_tag['src'])
    
    contents.append({"Images": links})

    print("\n")

    print('\033[1m' + "Images successfully scraped! " + '\033[0m', end='\n')
    
    with open('content.json', 'w') as f:
        json.dump(contents, f, indent=8, ensure_ascii=False)

    print("Created Json File")

    download_images(links=links)


def scrape_tables(url):
    try:
        scraped_table = soup.find_all('table')
        # pprint(scraped_table)
        # for table in scraped_table:
        #     print(table.text)
                
        # html = get_url_content(url)
        table = HTMLTableParser()
        table.feed(str(scraped_table))
        # my_table = pd.DataFrame(table.tables[1])
        # print(my_table, end="\n", sep="\n")
        print("\n\nPANDAS DATAFRAME\n")
        my_table = pd.DataFrame(table.tables)
        my_table.reset_index(drop=True, inplace=True)
        print(my_table)
        file_name = "website_table.xlsx"
        my_table.to_excel(file_name)
        print("\nRecords sucessfully scraped and stored ")
    except:
        print("No tables were found!")

## Not working yet

def download_images(links):
    i = 1

    for link in links:
        image_url = link 
        save_name = f"Images/Test{i}.jpg"
        i+=1
        urllib.request.urlretrieve(image_url, save_name)

def download_pdfs():
    pass

scrape(url)
# scrape_tables(url)





