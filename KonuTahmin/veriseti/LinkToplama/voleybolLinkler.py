from re import T
from typing import Text
from bs4 import BeautifulSoup as bs
from donguArama import htmlIcerikdondur
import requests
from textyaz import textYaz
linkler = [
    "https://www.haberturk.com/spor/voleybol"
           ]

altKategori = [
    "voleybol"
]

for index,url in enumerate(linkler):
    html = requests.get(url).text
    soup = bs(html, "html.parser")
    soup = soup.find('div',class_='master')
    soup = soup.find('div',class_='container-layer')
    soup = soup.find('div',class_='container')
    soup = soup.find('div',class_='left-layer')
    soup = soup.find('div',class_='list')
    soup = soup.find_all('div',class_='item')
    
    soup = [i.find('div',class_='widget-news') for i in soup]

    soup = htmlIcerikdondur(soup,soupic='a')
    soup = [i.find('a') for i in soup]

    links = []
    for link in soup:
        links.append(link.get('href'))
    print(altKategori[index]+' : ',str(len(links))+' adet link var.')
    textYaz(links,altKategori[index],'veri/spor/voleybol')