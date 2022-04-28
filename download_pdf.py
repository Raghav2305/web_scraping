# from requests.compat import urljoin
# from urllib.request import urlopen
# import requests
# import os
# from bs4 import BeautifulSoup

# def download_pdf(url):
#     folder_location = r'C:/Users/ASUS/Desktop/Cloudstrats/Web Scraping/web_scraping/PDFs'
#     if not os.path.exists(folder_location):
#         os.mkdir(folder_location)
#     response = urlopen(url).read().decode("utf-8")
#     soup= BeautifulSoup(response, "html.parser")     
#     for link in soup.select("a[href$='.pdf']"):
#         #Name the pdf files using the last portion of each link which are unique in this case
#         filename = os.path.join(folder_location,link['href'].split('/')[-1])
#         with open(filename, 'wb') as f:
#             f.write(requests.get(urljoin(url,link['href'])).content)

