# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# PATH = "C:\Program Files (x86)\chromedriver.exe"

# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # driver.get("https://www.google.com")

# # driver = webdriver.Chrome(ChromeDriverManager().install())
# # driver.maximize_window()

# # driver.get("https://finance.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAGA2m577cmhEieQcr_0HkSvFKRiGzIjUFTmLKSfEXJJuSilYOJp-2Sbp2AwqbZbF0uB9YpuRXpoPxrXaPkV7IPB57fXhf21_gunoJKmyeFAyZ61-IWPUefxYurUtF-kIg9kcAcIhA5C7QCQPmgHZF-cglQhfJOwqo4VdlkMlZGaA")
# # driver.implicit_wait(10)

# # driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# # driver = webdriver.Chrome(executable_path=PATH)
# # driver.implicitly_wait(10)
# # driver.get("https://www.youtube.com/")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

# driver.get("https://www.google.com")
# driver.maximize_window()

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())
   
quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':'all_quotes'}) 
   
for row in table.findAll('div',
                         attrs = {'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
   
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
    
def create_df(filename):
    with open(filename, 'r') as f:
        df = pd.read_csv(f)
        print(df['lines'])
        f.close()

create_df(filename=filename)