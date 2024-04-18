import requests
import json

query = input("What topic related news do you want?")
url= "https://newsapi.org/v2/everything?q={query}&from=2024-03-13&sortBy=publishedAt&apiKey=6e5e087e2e174007979688b8f93bf3e6"
r= requests.get(url)
# print(r.text)
news=json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------------------------")