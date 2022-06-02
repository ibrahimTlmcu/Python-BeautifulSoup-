from bs4 import BeautifulSoup
import requests
import time 




url = "https://www.imdb.com/chart/top/"
request = requests.get(url)

soup = BeautifulSoup(request.content,"lxml")

top_250 = soup.find("tbody",attrs={"class":"lister-list"}).find_all("tr")

film_sira = 1


for film in top_250:

    adi =film.find("td",attrs ={"class":"titleColumn"}).a.text
    yili =film.find("td",attrs={"class":"titleColumn"}).span.txt
    puan = film.find("td",attrs={"class":"ratingColumn"}).strong.get("title")


    print("film sıra",film_sira)
    print("film adi",adi)
    print("film yili",yili)
    print("Film puan",puan)

    print("\n\n")
    film_sira +=1
    film = ""
    



#top = soup.find("td",attrs ={"class":"titleColumn"}).a.text

