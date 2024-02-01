import requests
from send_email import send_email
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=4c0d1225cfd14c289c4daa2bdd448d11')
#make request

request= requests.get(url)
#get dectionnnary

content = request.json()

#access the article titles
body = ""
for article in content["articles"]:
       #if there is an error check if article title is none
       if article["title"] is not None:
              body = body + article["title"] + "\n" + article["description"] + 2 * "\n"


body=body.encode("utf-8")
send_email(message=body)
