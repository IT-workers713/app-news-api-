import streamlit as st
import requests

api_key="8skWaUcfZPbTwy8mURQVcbEaZNLgyejQU5yTOQsG"
#generate api key from from nasa
st.title("astronot image of the day from nasa")
#set title of api
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
#define the url and the apikey in url variable
request = requests.get(url)
response = request.json()
#get information from website title,image,explanation
titre = response["title"]
image = response["url"]
description = response["explanation"]
#download the image jpg format
image_filepath ="img.jpg"
req = requests.get(image)
with open(image_filepath,"wb") as file:
    file.write(req.content)
# send the information and represent it into  streamlit web app
st.title(titre)
st.image(image_filepath)
st.write(description)



