import requests
import json
from bs4 import BeautifulSoup
from _itemclass import DateController
from html import unescape, escape

url_test = "https://www.guadeloupe.franceantilles.fr/"
items = []


def scrape_articles(url, items_array):
    response = requests.get(url)
    # Analyze HTML page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all articles on the page
    articles = soup.select('.content-main article.article')
    title_path = 'a'
    url_path = 'a'
    date_path = 'time'
    abstract_path = '.extrait'

    print(len(articles))
    for article in articles:
        # Create a dictionary to store article information
        item = {}
        title = escape(unescape(article.select(title_path)[1].get_text(strip=True)))
        item["title"] = title
        # url = article.select(url_path)[1].get('href')
        url = escape(unescape(article.select_one(url_path).get('href')))
        start_url = "https://www.guadeloupe.franceantilles.fr"
        if start_url in url:
            item['url'] = url
        else:
            item['url'] = start_url + url

        date = escape(unescape(article.select_one(date_path).get_text(strip=True)))
        item['date'] = DateController.date_conversion(date, is_french=True)

        item['content'] = escape(unescape(article.select_one(abstract_path).get_text(strip=True)))
        # Add dictionary to list
        items_array.append(item)
    return items_array


items = scrape_articles(url_test, items)

json_str = json.dumps(items)
# Write JSON string to file
with open('json/items.json', 'w') as json_file:
    json_file.write(json_str)
# print(items)
