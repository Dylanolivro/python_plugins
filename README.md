[![Licence-MIT](https://img.shields.io/badge/Licence-MIT-blue)](https://github.com/Dylanolivro/Twitter_scrapping/blob/main/LICENSE)

---

[![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-4-563D7C?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)

# Plugins Python

C'est un projet qui permet de récupérer les articles d'un site web via une URL

## Prérequis

-   python 3.11.5
-   pip 23.2.1 (ou une version ultérieure)
-   beautifulsoup4 4.12.2
-   requests 2.31.0

## Installation

Ce projet utilise `BeautifulSoup4`. Vous pouvez l'installer avec le gestionnaire de paquets [pip](https://pip.pypa.io/en/stable/).

Pour installer les dépendances nécessaires, exécutez les commandes suivantes :

```bash
pip install requests
pip install beautifulsoup4
```

Pour plus d'informations sur l'installation et l'utilisation de Beautiful Soup, consultez la [documentation officielle](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## Configuration
Vous devez spécifier l'URL du site à partir duquel vous souhaitez récupérer des articles ou d'autres informations. Modifiez les variables url et start_url en conséquence 

```python
url = "https://www.exemple.com/press_release/"
start_url = "https://www.exemple.com"
```

De plus, ajustez les "chemins" vers les éléments HTML ainsi que leurs éléments enfants pour correspondre à la structure du site :

```python
articles = soup.select('article.news')
title_path = 'h2'  # Chemin vers l'élément du titre
url_path = 'a'  # Chemin vers l'élément de l'URL
date_path = 'time'  # Chemin vers l'élément de la date
abstract_path = '.extrait'  # Chemin vers l'élément de l'abstract
```
Assurez-vous de personnaliser ces chemins en fonction de la structure spécifique du site que vous traitez. Ces variables seront utilisées pour extraire les informations pertinentes à partir de la page web.