from bs4 import BeautifulSoup
import time 
import csv
import requests
from requests_html import HTML,HTMLSession
import pandas as pd



START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(START_URL)
time.sleep(10)

soup = BeautifulSoup(page.text,"html.parser")

star_table = soup.find("table")

star_data = star_table.find_all("tr")

star_list = []

for tr in star_data:
    td = tr.find_all("td")
    row = [i.text.rstrip()for i in td]
    star_list.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1,len(star_list)):
    name.append(star_list[i][1])
    distance.append(star_list[i][3])
    mass.append(star_list[i][5])
    radius.append(star_list[i][6])

df = pd.DataFrame(list(zip(name,distance,mass,radius)),columns=["name","distance","mass","radius"])
df.to_csv("Output.csv")





