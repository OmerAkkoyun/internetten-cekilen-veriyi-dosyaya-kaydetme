import requests
from bs4 import BeautifulSoup

url="http://www.mettjob.com/about.html"
r=requests.get(url)
icerik=BeautifulSoup(r.content,"html.parser")
sadelestir=icerik.find_all("div",{"class":"col-lg-6"})

for i in sadelestir:
    k=((i.text).strip())
    dosya =open("C:/Users/Omer/Desktop/Kayit.txt","a",encoding="utf-8")
    yazdir=dosya.write(k)