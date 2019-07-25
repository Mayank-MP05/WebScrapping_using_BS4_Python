import requests as req
from bs4 import BeautifulSoup

src = req.get('https://www.w3.org/Style/Examples/011/firstcss.en.html').text

soup = BeautifulSoup(src,'lxml')

match = soup.find_all("div")
lenh = len(match);
for i in range(lenh):
    hed = match[i].h2
#   print(hed)
    if(hed != None):
        print(hed)

ls = match
#print(ls)
