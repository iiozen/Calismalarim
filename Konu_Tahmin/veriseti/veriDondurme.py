import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
import requests
class VeriIslemleri():
    def veriDondur(self,veri):
        """
        Döndürülen listenin ilk elemanı txtlerin konumları
        diğeri ise konu başlıklarıdır. \nTablo için 3. eleman kullanılır.
        """
        birlikteHepsi= []
        konumlar = []
        tumkonular = []
        for x in veri:
            konular = []
            genelkonular = x
            konular.append(genelkonular)
            for i in veri[x]:

                ustkonular = i
                konular.append(ustkonular)
                try:
                    for j in veri[x][i]:
                        birlikte=[]
                        konum = 'LinkToplama/veri/'+x+'/'+i+'/'+j+'.txt'
                        konumlar.append(konum)
                        altkonular = j
                        konular.append(altkonular)
                        birlikte.append(genelkonular)
                        birlikte.append(ustkonular)
                        birlikte.append(altkonular)
                        birlikte.append(konum)


                except:
                    birlikte=[]
                    konum = 'LinkToplama/veri/'+x+'/'+i+'.txt'
                    konumlar.append(konum)
                    altkonular = i
                    konular.append(altkonular)
                    birlikte.append(genelkonular)
                    birlikte.append(ustkonular)
                    birlikte.append(altkonular)
                    birlikte.append(konum)
                birlikteHepsi.append(birlikte)
            tumkonular.append(konular)

        return [konumlar,tumkonular,birlikteHepsi]


    def Tablola(self,veri,baslik):
        x = self.TabloDondur(veri,baslik)
        print(x)
    def TabloDondur(self,veri,baslik):
        df = pd.DataFrame(data=veri,columns=baslik)
        return df



    def txtOkuDondur(self,konum):
        with open(konum,'r',encoding='utf-8') as f:
            x = f.read()
            return x

    def veriKaz(self,link,genel_konu,ust_konu,alt_konu):
        html = requests.get(link)
        html.encoding = 'utf-8'
        html = html.text
        soup = bs(html,'lxml')
        title = soup.find('h1',class_='title').get_text(strip=True)
        spottitle = soup.find('h2',class_='spot-title')
        article = soup.find('article')
        icerikler = article.findChildren('p')
        icerikler.append(spottitle)
        icerikdeneme = []
        for icerik in icerikler:
            hazirlist = []

            icerik = icerik.get_text(strip=True)
            if icerik!='':
                hazirlist.append(icerik)
                hazirlist.append(title)
                hazirlist.append(genel_konu)
                hazirlist.append(ust_konu)
                hazirlist.append(alt_konu)
                icerikdeneme.append(hazirlist)
        return icerikdeneme


    def linkKontrol(self,link):
        link = link.strip()
        link = link.strip("'")
        if '/video/' in link:
            link = ''
        else:
            if link.startswith('/'):
                link = 'https://www.haberturk.com'+link
        return link

    def veriMain(self,tablo):
        konum = tablo['Konum']
        genel_konu = tablo['Genel Konu']
        ust_konu = tablo['Üst Konu']
        alt_konu = tablo['Alt Konu']
        tabloicerik = []
        linklerim = []
        for index,i in enumerate(konum):
            x = self.txtOkuDondur(i)
            x = x.lstrip('[').rstrip(']').split(',')
            for link in x:
                linkim = self.linkKontrol(link)
                if linkim !='':
                    linklerim.append(linkim)

                    icerik = self.veriKaz(linkim,genel_konu=genel_konu[index],ust_konu=ust_konu[index],alt_konu=alt_konu[index])
                    for tabloic in icerik:
                        tabloicerik.append(tabloic)

        return tabloicerik