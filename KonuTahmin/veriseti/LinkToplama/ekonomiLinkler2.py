from re import T
from typing import Text
from bs4 import BeautifulSoup as bs
from donguArama import htmlIcerikdondur
import requests
from textyaz import textYaz
linkler = [
    "https://www.haberturk.com/ekonomi/doviz",
    "https://www.haberturk.com/ekonomi/kripto-para",
    "https://www.haberturk.com/ekonomi/is-yasam",
    "https://www.haberturk.com/ekonomi/turizm",
    "https://www.haberturk.com/ekonomi/enerji",
    "https://www.haberturk.com/ekonomi/emlak",
           ]

altKategori = [
    "döviz",
    "kripto_para",
    "iş_yaşam",
    "turizm",
    "enerji",
    "emlak",
]


for index,url in enumerate(linkler):
    html = requests.get(url).text
    soup = bs(html, "html.parser")
    soup = soup.find('section',id='MainSixNews')
    soup = soup.find_all('div',class_='box-xs-6')
    
    # soup = [i.find('div',class_='middleBigNewsContent') for i in soup]

    # soup = htmlIcerikdondur(soup,soupic='a')
    soup = [i.find('a') for i in soup]
    
    

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
    textYaz(links,altKategori[index],'veri/ekonomi')