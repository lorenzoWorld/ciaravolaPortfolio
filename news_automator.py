import requests
from sys import argv

API_KEY = '178645d6321c4d32908f257d837e8038'

URL = 'https://newsapi.org/v2/top-headlines?'

def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "it",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "it",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json().get('articles', [])  

    if not articles:
        print("No articles found.")
        return

    for article in articles:
        print(article['title'])
        print(article['url'])
        print('')

def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "en",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=query_parameters)

    sources = response.json().get('sources', [])  

    if not sources:
        print("No sources found.")
        return

    for source in sources:
        print(source['name'])
        print(source['url'])

if __name__ == "__main__":
    if len(argv) < 2:
        print("Please provide a category as an argument.")
    else:
        category = argv[1]
        print(f"Getting news for {category}...\n")
        get_articles_by_category(category)
        print(f"Successfully retrieved top {category} headlines")

#python news_automator.py technology 
