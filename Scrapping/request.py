#import requests
from bs4 import BeautifulSoup

with open("practice.html") as html:
    soup = BeautifulSoup(html,'lxml')

#match  = soup.find_all('p',class_="whs2")
print(soup)
