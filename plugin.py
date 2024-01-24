import requests,json
from bs4 import BeautifulSoup
from _itemclass import MYNEWS
from html import unescape, escape

isJson = False
printItems = True

# JSON URL
# url = "https://aabbsearch301.aws.mtxgp.net//searchblox/servlet/SearchServlet?query=*&default=AND&xsl=json&facet=on&filter=module%3A(%22News%22)&pagesize=10&f.categories.filter=AABB%20Community%5EAssociation%20News%5EAnnual%20Meeting&page=1&sort=lastmodified&sortdir=desc&facet.field=categories&f.categories.size=1000"
url = "https://www.guadeloupe.franceantilles.fr/"
start_url = "https://www.guadeloupe.franceantilles.fr"

def scrape_articles(url, data):
    data["items"] = items

    response = requests.get(url)
    # Analyser le contenu HTML de la page avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Trouver tous les articles sur la page
    articles = soup.select('.content-main article.article')
    title_path = 'a'
    url_path = 'a'
    date_path = 'time'
    abstract_path = '.extrait'

    print(len(articles))
    for article in articles:
        # Créer un dictionnaire pour stocker les informations de l'article
        item = {}

        item['title'] = escape(unescape(article.select(title_path)[1].get_text(strip=True)))

        # url = article.select(url_path)[1].get('href')
        url = escape(unescape(article.select_one(url_path).get('href')))
        if start_url in url:
            item['url'] = url
        else:
            item['url'] = start_url + url

        date = escape(unescape(article.select_one(date_path).get_text(strip=True)))
        item['date'] = MYNEWS.DATE_Conversion(date, isFrench=None, dbg=None)

        item['content'] = escape(unescape(article.select_one(abstract_path).get_text(strip=True)))
        # Ajouter le dictionnaire à la liste
        items.append(item)

    return items

def scrape_articles_json(url, data):
    data["items"] = items
    response = requests.get(url)
    # Analyser le contenu JSON de la réponse
    data = json.loads(response.text)
    # Trouver tous les articles dans les résultats
    articles = data['results']['result']
    
    # print(len(articles))
    for article in articles:
        # Créer un dictionnaire pour stocker les informations de l'article
        item = {}

        item['title'] = article['title']

        url = article['location']
        if start_url in url:
            item['url'] = url
        else:
            item['url'] = start_url + url

        date = article['indexdate']
        item['date'] = MYNEWS.DATE_Conversion(date,isFrench=None, dbg=None)

        item['content'] = article['description']

        # Ajouter le dictionnaire à la liste
        items.append(item)

    return items

data = {
    "Site" : url,
    "items": []

}
if isJson:
    items = scrape_articles_json(url, data)
else:
    items = scrape_articles(url, data)

if printItems:
    print(items)

json_str = json.dumps(items)
# Écrire la chaîne JSON dans un fichier
with open('json/items.json', 'w') as json_file:
    json_file.write(json_str)


# ! ---------------------------------------------------------
# Pour récupérer le premier lien
    # url = article.select_one(url_path).get('href')
# Si on a besoin du deuxième lien
    # url = article.select(url_path)[1].get('href')

# ! ---------------------------------------------------------
# Scraping d'un fichier JSON
    # def scrape_articles_json(url, data):
    #     response = requests.get(url)
    #     # Analyser le contenu JSON de la réponse
    #     json_data = json.loads(response.text)
    #     # Trouver tous les articles dans les résultats
    #     articles = json_data['results']['result']

    #     for article in articles:
    #         # Créer un dictionnaire pour stocker les informations de l'article
    #         item = {}

    #         item['title'] = article['title']

    #         url = article['location']
    #         if start_url in url:
    #             item['url'] = url
    #         else:
    #             item['url'] = start_url + url

    #         date = article['indexdate']
    #         item['date'] = MYNEWS.DATE_Conversion(date,isFrench=None, dbg=None)

    #         item['content'] = article['description']

    #         # Ajouter le dictionnaire à la liste
    #         data["items"].append(item)

    #     return data

    # data = {
    #     "Site" : url,
    #     "items": []
    # }

    # if isJson:
    #     data = scrape_articles_json(url, data)
    # else:
    #     items = scrape_articles(url, data)
