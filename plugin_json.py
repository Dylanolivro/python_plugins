import requests
import json
from _itemclass import DateController

url_test = ("https://aabbsearch301.aws.mtxgp.net//searchblox/servlet/SearchServlet?query=*&default=AND&xsl=json&facet"
            "=on&filter=module%3A(%22News%22)&pagesize=10&f.categories.filter=AABB%20Community%5EAssociation%20News"
            "%5EAnnual%20Meeting&page=1&sort=lastmodified&sortdir=desc&facet.field=categories&f.categories.size=1000")
items = []


def scrape_articles_json(url, items_array):
    response = requests.get(url)
    # Analyze the JSON content of the response
    data = json.loads(response.text)
    # Find all items in results
    articles = data['results']['result']

    print(len(articles))
    for article in articles:
        # Create a dictionary to store article information
        item = {}
        title = article['title'].strip()
        item['title'] = title

        url = article['location']
        start_url = "https://www.aabb.org"
        if start_url in url:
            item['url'] = url
        else:
            item['url'] = start_url + url

        date = article['indexdate'].strip()
        item['date'] = DateController.date_conversion(date)

        item['content'] = article['description'].strip()

        # Add dictionary to list
        items_array.append(item)

    return items_array


items = scrape_articles_json(url_test, items)

json_str = json.dumps(items)
# Write JSON string to file
with open('json/items.json', 'w') as json_file:
    json_file.write(json_str)
