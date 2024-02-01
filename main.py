import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=4c0d1225cfd14c289c4daa2bdd448d11')
#make request

request= requests.get(url)
#get dectionnnary

content = request.json()
#aaccess the article titles
for article in content["articles"]:
       print(article["title"])

