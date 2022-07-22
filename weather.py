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

# don't paste the stuff below yet, wait until I tell you to

from ast import literal_eval

data = literal_eval(data)
print(str(data["weather"][0]["main"]) + "\n" + str(data["main"]["temp"]) + "\n" + data["name"] + " ," + data["sys"]["country"])
  
# and then at the end just import scratchattach and stuff and do cloud variable stuff :)
