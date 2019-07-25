import requests as req
import bs4 as bs

res = req.get("https://www.amazon.in/gp/site-directory?ref_=nav_shopall_btn").text

soup = bs.BeautifulSoup(res,"lxml")
divs = soup.find_all('div',class_="popover-grouping")
divlen = len(divs)

for j in range(divlen):
    print()
    print()
    heading = divs[j].h2.text
    print(heading)
    print()
    liList = divs[j].ul.find_all('li')
    lenLi = len(liList)
    for i in range(lenLi):
        print(liList[i].text)
    print(heading)
#print(divs)