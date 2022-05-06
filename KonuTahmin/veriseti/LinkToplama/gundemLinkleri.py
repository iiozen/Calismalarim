from re import T
from typing import Text
from bs4 import BeautifulSoup as bs
from donguArama import htmlIcerikdondur
import requests
from textyaz import textYaz
linkler = [
    
        "https://www.haberturk.com/gundem/egitim",
        "https://www.haberturk.com/gundem/guvenlik",
        "https://www.haberturk.com/gundem/inanc",
        "https://www.haberturk.com/gundem/politika"
        
           ]

altKategori = [
    "eğitim",
    "güvenlik",
    "inanç",
    "politika"
]


for index,url in enumerate(linkler):
    html = requests.get(url).text
    soup = bs(html, "html.parser")
    soup = soup.find('div',class_='detail-container')
    soup = soup.find('div',class_='detail-content')
    soup = soup.find_all('div',class_='CategoryFourNews')
    
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
    textYaz(links,altKategori[index],'veri/gundem')