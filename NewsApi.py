import constants

class NewsApi:
    api_urls = [
        f"https://newsapi.org/v2/top-headlines?country=us&apiKey={constnats.news_api}&category=business"
    ]

    webscrape_urls = []

    api_articles = []
    webscrape_articles = []


    def __init__(self, api=True, webscrape=True):
        self.api_urls = NewsApi.api_urls
        self.webscrape_urls = NewsApi.webscrape_urls
        self.api = api
        self.websrape = webscrape


    def fetch_api(self):
        if self.api == False:
            return

        import requests
        articles = []
        for url in self.api_urls:
            top_news = requests.get(url).json()
            for x in top_news.get("articles"):
                # 'source','author','title','description','url','urlToImage','publishedAt','content'
                articles.append(x.get("title"))
        return articles








    def fetch_webscrape(self):
        if self.webscrape == False:
            return
        
        ...
