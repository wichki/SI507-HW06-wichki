# 507/206 Homework 6 Extra Credit 1
import requests
from bs4 import BeautifulSoup

#### Extra Credit 2 ####
print('\n*********** EXTRA CREDIT 2 ***********')
print('Re-sort Atheletes by State\n')

### Your Extra Credit 2 solution goes here

athletic_html = requests.get("https://www.athletic.net/CrossCountry/Results/Meet.aspx?Meet=135827").text

athletic_soup = BeautifulSoup(athletic_html, "html.parser")
# print(athletic_soup)

table_rows = athletic_soup.find_all(id="D_557666")
# print(table_rows)

for i in table_rows:
    table_cells = i.find_all('td')
    # print(i.text)
print(table_cells)
