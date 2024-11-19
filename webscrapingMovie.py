import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"

page = requests.get(url)

# print(page.status_code)

df = pd.DataFrame(columns=["Avarage Rating", "Title", "Year"])
data = BeautifulSoup(page.content, 'html.parser')
# print(data)
tables = data.find_all("tbody")
rows = tables[0].find_all("tr")

count = 0

for row in rows:
    if count < 50:
        col = row.find_all("td")
        if len(col) != 0:
            data_dict = {"Avarage Rating": int(col[0].text), "Title": str(
                col[1].text), "Year": int(col[2].text)}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count += 1
    else:
        break

# print(df)
df.to_csv('top_50_movies.csv')


db_name = 'movies.db'
table_name = 'movies'
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
