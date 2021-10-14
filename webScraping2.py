import requests
from bs4 import BeautifulSoup
import pandas as pd

start_url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page=requests.get(start_url)
soup=BeautifulSoup(page.text,"html.parser")
star_table=soup.find("table")

temp_list=[]
table_rows=star_table.find_all("tr")

for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip()for i in td]
    temp_list.append(row)

star_name=[]
mass=[]
radius=[]
distance=[]

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    mass.append(temp_list[i][8])
    radius.append(temp_list[i][9])
    distance.append(temp_list[i][5])

df=pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=["star_name","distance","mass","radius"])
df.to_csv("brown_dwarf_stars.csv")