# 507/206 Homework 6 Extra Credit 1
import requests
from bs4 import BeautifulSoup

#### Extra Credit 1 ####
print('\n*********** EXTRA CREDIT 1 ***********')
print('Top 10 Headlines: News\n')

### Your Extra Credit 1 solution goes here
news = "https://www.michigandaily.com/section/news"
sports = "https://www.michigandaily.com/section/sports"
arts = "https://www.michigandaily.com/section/arts"

news_html = requests.get(news).text
sports_html = requests.get(sports).text
arts_html = requests.get(arts).text

news_soup = BeautifulSoup(news_html, "html.parser")
sports_soup = BeautifulSoup(sports_html, "html.parser")
arts_soup = BeautifulSoup(arts_html, "html.parser")

news_list_items = news_soup.find_all("div", class_="views-field views-field-field-short-headline")

sports_list_items = sports_soup.find_all("div", class_="views-field views-field-field-short-headline")

arts_list_items = arts_soup.find_all("div", class_="views-field views-field-field-short-headline")

# print(len(list_items[:10]))
for i in news_list_items[:10]:
    print(i.text)

print('\nTop 10 Headlines: Sports\n')
for i in sports_list_items[:10]:
    print(i.text)

print('\nTop 10 Headlines: Arts\n')
for i in arts_list_items[:10]:
    print(i.text)
