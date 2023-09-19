from NewsApi import NewsApi



news = NewsApi(api=True,webscrape=False)

output = news.fetch_api()

print(output)