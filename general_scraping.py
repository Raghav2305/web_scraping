

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
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import json

headers = {'Accept': 'text/html'}

def get_soup(url):
    r = requests.get(url, headers=headers)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    return soup

def scrape(soup):
    
    title = soup.title

    print('\n\033[1m' + f"Title = {title.text}" '\033[0m')

    try:
        paras = soup.find_all('p')
        if paras:
            print(f"'\033[1m'+ Para = {paras.text} +'\033[0m'"  )

    except :
        paras = soup.find('p')
        print('\033[1m' + f"Para = {paras.text}" +'\033[0m')

    try:
        h1s = soup.find_all('h1')
        if h1s:
            print('\033[1m' + f"H1 = {h1s.text}" + '\033[0m', end='\n', sep='\n')

    except :
        h1s = soup.find('h1')
        print('\033[1m' + f"H1 = {h1s.text}" + '\033[0m', end='\n', sep='\n')


    try:
        
        h2s = soup.find_all('h2')
        if h2s:
            print('\033[1m' + f"H2 = {h2s.text}" + '\033[0m', end='\n', sep='\n')

    except :
        h2s = soup.find('h2')
        print('\033[1m' + f"H2 = {h2s.text}" +'\033[0m', end='\n', sep='\n')

def get_url_content(url):
    req = urllib.request.Request(url=url)
    open_ = urllib.request.urlopen(req)
    return open_.read()



def scrape_tables(url):
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
    my_table = pd.DataFrame(table.tables[4])
    print(my_table)
    file_name = "website_table.xlsx"
    my_table.to_excel(file_name)
    print("\nRecords sucessfully scraped and stored ")

    
def scrape_links(soup, url):
    try:
        anchors = soup.find_all('a')
        # all_links = set()
        # for link in anchors:
        #     if(link.get('href') != '#'): 
        #         linkText = url +link.get('href')
        #         all_links.add(link)
        all_links = []
        print("\n")

        print('\033[1m' + "Links: " +'\033[0m')
        for linkk in anchors:
            
            if linkk['href'].startswith("https://") :
                all_links.append(linkk['href'])
            else:
                all_links.append(url + linkk['href'])

        for a_links in all_links:
            print(a_links, end="\n")
    except:
        print('----------------------------------------------')

def scrape_images(soup, url):
    image_tags = soup.find_all('img')
    links = []
    for image_tag in image_tags:
        
        if image_tag['src'].startswith("https://"):
            links.append(image_tag['src'])
        else:
            links.append(url + image_tag['src'])

    print("\n")

    print('\033[1m' + "Images: " + '\033[0m', end='\n')

    for link in links:
        print(link, end='\n')

url = "https://www.moneycontrol.com/"
# url = "https://reactjs.org"


soup = get_soup(url)

scrape(soup)
scrape_tables(url)
scrape_links(soup, url)
scrape_images(soup, url)
# import urllib.request
# urllib.request.urlretrieve(links[0], "Images/innovators.jpg")




