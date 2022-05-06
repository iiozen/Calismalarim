from re import T
from typing import Text
from bs4 import BeautifulSoup as bs
from donguArama import htmlIcerikdondur
import requests
from textyaz import textYaz
linkler = [
        "https://www.haberturk.com/saglik/genel-saglik",
        "https://www.haberturk.com/saglik/anne-ve-cocuk",
        "https://www.haberturk.com/saglik/kalp-sagligi",
        "https://www.haberturk.com/saglik/saglikli-beslenme",
        "https://www.haberturk.com/saglik/kanser",
        "https://www.haberturk.com/saglik/cinsel-saglik",
        "https://www.haberturk.com/saglik/estetik-cerrahi"
           ]

altKategori = [
    "genel_sağlık",
    "hamilelik_ve_çocuk_hastalıkları",
    "kalp_sağlığı",
    "sağlıklı_beslenme",
    "kanser",
    "cinsel_sağlık",
    "estetik_cerrahi"
]


for index,url in enumerate(linkler):
    html = requests.get(url).text
    soup = bs(html, "html.parser")
    soup = soup.find('div',id='categorySlider')
    soup = soup.findChildren('a')
    # soup = soup.find_all('div',class_='owl-item')
    
    # soup = [i.find('div',class_='middleBigNewsContent') for i in soup]

    # soup = htmlIcerikdondur(soup,soupic='a')
    # soup = [i.find('a') for i in soup]
    
    

    links = []
    for link in soup:
        # link.select('a')
        # try:
        #     print(link.findChild("a")['href'])
        # except:
        #     pass
        links.append(link.get('href'))
        # print(link.get('href'))
    print(altKategori[index]+' : ',str(len(links))+' adet link var.')
    textYaz(links,altKategori[index],'veri/saglik')