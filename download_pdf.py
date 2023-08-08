from urllib.parse import urljoin
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import os
import general_scraping as gs
# import urllib
# from urllib.parse import urljoin

# pdf_content= []


def download_pdfs(url):
    folder_location = r"C:\Users\ASUS\PycharmProjects\Scraping Engine\web_scraping\PDFs"
    if not os.path.exists(folder_location):
        os.mkdir(folder_location)
    response = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(response, "html.parser")
    for link in soup.select("a[href$='.pdf']"):
        filename = os.path.join(folder_location, link['href'].split('/')[-1])
        # pdf_content.append(urljoin(url,link['href']).content)
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url, link['href'])).content)
