from re import T
from typing import Text
from bs4 import BeautifulSoup as bs
from donguArama import htmlIcerikdondur
import requests
from textyaz import textYaz
linkler = [
    "https://www.haberturk.com/spor/basketbol/stbl",
           "https://www.haberturk.com/spor/basketbol/euroleague",
           "https://www.haberturk.com/spor/basketbol/eurocup",
           "https://www.haberturk.com/spor/basketbol/dunya_sampiyonasi",
           "https://www.haberturk.com/spor/basketbol/sampiyonlar_lig",
           "https://www.haberturk.com/spor/basketbol/kadinlar_euroleague",
           "https://www.haberturk.com/spor/basketbol/milli_takim",
           "https://www.haberturk.com/spor/basketbol/diger",
           "https://www.haberturk.com/spor/basketbol/nba"
           ]

altKategori = [
    "spor_toto_basketbol_ligi",
    "euro_league",
    "eurocup",
    "dünya_şampiyonası",
    "şampiyonlar_ligi",
    "kadınlar_euroleague",
    "milli_takım",
    "basketbol",
    "nba"
]
for index,url in enumerate(linkler):
    html = requests.get(url).text
    soup = bs(html, "html.parser")
    soup = soup.find('div',class_='master')
    soup = soup.find('div',class_='container-layer')
    soup = soup.find('div',class_='container')
    soup = soup.find('div',class_='left-layer')
    soup = soup.find('div',class_='list')
    # soup = htmlIcerikdondur(soup,soupic='div',soupclass='item')
    soup = soup.find_all('div',class_='item')
    # soup = [i.find('div',class_='widget-news') for i in soup]
    
    # soup = htmlIcerikdondur(soup,soupic='div',soupclass='widget-news')
    soup = [i.find('div',class_='widget-news') for i in soup]

    soup = htmlIcerikdondur(soup,soupic='a')
    soup = [i.find('a') for i in soup]
    # soup = htmlIcerikdondur(soup,soupic='a')
    
    
    # # soup = soup.find('div',class_='widget-news')
    # # for link in soup.find_all('a'):
    
    # for link in soup.find_all('a'):
        
    #     print(link.get('href'))
    #     # print(link.get('href'))   
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
    textYaz(links,altKategori[index],'veri/spor/basketbol')