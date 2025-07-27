
#install pip reques
#install beautifulsoup
#install pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.iplt20.com/auction/2022"
r=requests.get(url)
#print(r)

soup = BeautifulSoup(r.text , "lxml")
#print(soup)

table = soup.find("table",class_="ih-td-tab w-100 auction-tbl")
title=table.find_all("th")
print(title)
#print(table)


header =[]
for i in title:
    name=i.text
    header.append(name)

df = pd.DataFrame(columns=header)
#print(df)   


rows = table.find_all("tr")
#print(rows)

for i in rows[1:]:
    tds = i.find_all("td")
    if tds and tds[0].find("div", class_="ih-pt-ic") is not None:
        first_td = tds[0].find("div", class_="ih-pt-ic").text.strip()
    else:
        first_td = ""

    data = tds[1:]  # Skip first <td> since it's already used
    row = [tr.text.strip() for tr in data]
    row.insert(0, first_td)
    l = len(df)
    df.loc[l] = row
print(df)    

df.to_csv("IPL Auction Stats.csv")

 #do not use this..as it is not complete query

#for i in rows[1:]:
#    first_td = i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
#    data = i.find_all("td")[1:]
#    row = [tr.text for tr in data]
#    #print(row)
#    row.insert(0,first_td) # type: ignore
#    l=len(df)
#    df.loc[l]=row
#print(df)   