
#step 1 open pip request in chrome   ...copy file 
#step 2 ..go to commond prompt...run it
#step 3 now use vscode
#pip insatll request
#pip install beautifulsoup4
#pip install lxml

#after running step run ..now comment out print(r)and print(soup)


#step run
import requests
from bs4 import BeautifulSoup
url ="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
#print(r)


#using soup to scraping

soup = BeautifulSoup(r.text , "lxml")
#print(soup)

#boxes = soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")
#print(len(boxes))

names = soup.find_all("a",class_="title")
for i in names:
    print(i.text)

prices = soup.find_all("h4","price float-end card-title pull-right")

for i in prices:
    print(i.text)

   