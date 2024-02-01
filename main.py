import requests
from send_email import send_email
topic = "tesla"
url = ('https://newsapi.org/v2/top-headlines?'
       f"q={topic}&"
       'apiKey=4c0d1225cfd14c289c4daa2bdd448d11'
       '&language=en')
#make request

request= requests.get(url)
#get dectionnnary

content = request.json()

#access the article titles
body = ""
for article in content["articles"][:20]:
       #if there is an error check if article title is none
       if article["title"] is not None:
              body = "Subject : Today's news "+"\n"+body + article["title"] + "\n" + article["description"] +"\n"+article["url"]+ 2 * "\n"


body=body.encode("utf-8")
send_email(message=body)
