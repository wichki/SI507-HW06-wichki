# 507/206 Homework 6 Part 2
import requests
from bs4 import BeautifulSoup


#### Part 2 ####
print('\n*********** PART 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Part 2 solution goes here

html = requests.get("http://michigandaily.com").text
soup = BeautifulSoup(html, "html.parser")
# print(html)
# print (soup)

# print(soup.find('div', attrs={"class": "panel-pane pane-mostread"}))

# for i in soup.find('div', attrs={"class": "panel-pane pane-mostread"}):
#     print(i)
chunk = soup.find('div', attrs={"class": "panel-pane pane-mostread"})
# print(chunk)
# print(chunk.find_all("li"))
# print(chunk.find_all("a"))

for i in chunk.find_all("a"):
    print(i.text)
