from re import T
from typing import Text
from bs4 import BeautifulSoup as bs
from donguArama import htmlIcerikdondur
import requests
from textyaz import textYaz
linkler = ['https://www.haberturk.com/spor/futbol/super_lig',
           'https://www.haberturk.com/spor/futbol/sampiyonlar_ligi',
           "https://www.haberturk.com/spor/futbol/turkiye_kupasi",
           "https://www.haberturk.com/spor/futbol/avrupa_ligi",
           "https://www.haberturk.com/spor/futbol/ispanya",
           "https://www.haberturk.com/spor/futbol/ingiltere",
           "https://www.haberturk.com/spor/futbol/almanya",
           "https://www.haberturk.com/spor/futbol/italya",
           "https://www.haberturk.com/spor/futbol/fransa",
           "https://www.haberturk.com/spor/futbol/1_lig",
           "https://www.haberturk.com/spor/futbol/tff_2_lig",
           "https://www.haberturk.com/spor/futbol/tff_3_lig",
           ]

altKategori = [
    "süper_lig",
    "şampiyonlar_ligi",
    "türkiye_kupası",
    "avrupa_ligi",
    "ispanya_ligi",
    "ingiltere_ligi",
    "almanya_ligi",
    "italya_ligi",
    "fransa_ligi",
    "birinci_lig",
    "ikinci_lig",
    "üçüncü_lig",
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
    textYaz(links,altKategori[index],'veri/spor/futbol')