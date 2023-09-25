import constants
import requests

class NewsApi:
    api_urls = [
        f"https://newsapi.org/v2/top-headlines?country=us&apiKey={constants.news_api}&category=business"
    ]

    webscrape_urls = []


    def __init__(self, api=True, webscrape=True):
        self.api_urls = NewsApi.api_urls
        self.webscrape_urls = NewsApi.webscrape_urls
        
        self.api = api
        self.websrape = webscrape
        
        self.api_articles = []
        self.webscrape_articles = []


    def fetch_api(self):
        if self.api == False:
            return
        articles = []
        for url in self.api_urls:
            top_news = requests.get(url).json()
            for a in top_news.get("articles"):
                # 'source','author','title','description','url','urlToImage','publishedAt','content'
                articles.append(a)
                self.api_articles.append(a)
        return articles








    def fetch_webscrape(self):
        if self.webscrape == False:
            return
        from bs4 import BeautifulSoup
        from urllib.parse import urljoin

        for x in self.webscrape_urls:
            # Check if the content is HTML
            content_type = data.headers.get('Content-Type')
            if 'text/html' not in content_type:
                print(f"Skipping {x}, not an HTML page.")
                continue

            # INIT SOUP
            html = data.text
            soup = BeautifulSoup(html, 'html.parser')

            # Extract and store text from the HTML page
            text_data = """"""
            for string in soup.stripped_strings:
                text_data.append(string)

            self.webscrape_articles.append(text_data)

            # # collect links from webpage
            # for link in soup.find_all('a', href=True):
            #     url = link['href']
            #     full_url = urljoin(self.base_url, url)
            #     self.links.add(full_url)






















if __name__ == "__main__":
    news = NewsApi()
    news_articles = news.fetch_api()
    for article in news_articles:
        print( article )