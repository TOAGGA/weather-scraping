import requests 
from bs4 import BeautifulSoup # don't forget to install requests and bs4

lat, lon = 35, 139

url = "https://fcc-weather-api.glitch.me/api/current?lat=" + str(lat) + "&lon=" + str(lon)
reponse = requests.get(url)

if reponse.ok:
    soup = BeautifulSoup(reponse.text, "lxml")
    data = str(soup.find("p"))

    data = data.replace("<p>", "")
    data = data.replace("</p>", "")
    print(data)
  
