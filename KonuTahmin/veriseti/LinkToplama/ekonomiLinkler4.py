from bs4 import BeautifulSoup as bs
from donguArama import htmlIcerikdondur
import requests
from textyaz import textYaz
linkler = [
    "https://www.haberturk.com/ekonomi/sigorta"
]

altKategori = [
    "sigorta",
]


for index,url in enumerate(linkler):
    html = requests.get(url).text
    soup = bs(html, "html.parser")
    soup = soup.find_all('div',class_='section')
    textYaz(soup,'1','.')
    # soup = htmlIcerikdondur(soup,soupclass='box column-4',soupic='div')
    soup = soup[4].find_all('div',class_='box column-4')
    # soup = [i.find('div',class_='box column-4') for i in soup[2]]

    soup = htmlIcerikdondur(soup,soupic='a')
    soup = [i.find('a') for i in soup]
    soup = htmlIcerikdondur(soup,soupic='a')
    
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