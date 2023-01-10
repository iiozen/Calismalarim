import numpy as np
import joblib
from onisleme import Onisleme
from bs4 import BeautifulSoup as bs
import requests
from googlesearch import search
import sqlite3 as sql

class Robot():
    def __init__(self):
        # Countvector fit halleri
        self.cv_baslik = joblib.load('vectorizerBaslik300.joblib')
        self.cv_icerik = joblib.load('vectorizerIcerik.joblib')

        # Labelencoder fit hali genel üst ve alt konular için
        self.legenel_konu = joblib.load('labelEncodergenel_konu.joblib')
        self.leust_konu = joblib.load('labelEncoderust_konu.joblib')
        self.lealt_konu = joblib.load('labelEncoderalt_konu.joblib')


        # Tahmin edecek modellerin eğitilmiş halleri
        self.model_baslik = joblib.load('baslikModel300.joblib')
        self.model_genel_konu = joblib.load('modelgenel_konu.joblib')
        self.model_ust_konu = joblib.load('modelust_konu.joblib')
        self.model_alt_konu = joblib.load('modelalt_konu.joblib')
    
    def KonuBul(self,paragraf):
        
        paragraf = Onisleme([paragraf])[0]
        if paragraf !='':
            paragraf = np.array([paragraf]).astype('U')
            paragraf = self.cv_icerik.transform(paragraf).toarray()
            
            genel_konu = self.model_genel_konu.predict(paragraf)
            ust_konu = self.model_ust_konu.predict(paragraf)
            alt_konu = self.model_alt_konu.predict(paragraf)
            
            genel_konu = self.legenel_konu.inverse_transform(genel_konu)[0].replace('_',' ')
            ust_konu = self.leust_konu.inverse_transform(ust_konu)[0].replace('_',' ')
            alt_konu = self.lealt_konu.inverse_transform(alt_konu)[0].replace('_',' ')
            konutahmin = [genel_konu,ust_konu,alt_konu]
            
            
            konular = []
            gkonular = []
            for konu in konutahmin:
                if konu not in konular:
                    konular.append(konu)
                    gkonular.append(konu)

            konular.pop(0)
            print('Genel konu : ',genel_konu,' / alt konu:',', '.join(konular))
            
            basliktahmin = self.model_baslik.predict(paragraf)
            
            basliktahmin = self.cv_baslik.inverse_transform(basliktahmin)
            
            basliktahminler = []
            for baslik in basliktahmin:
                for i in baslik:
                    basliktahminler.append(str(i))
                
            if basliktahminler!=[]:
                print('tahmini arama kelimeleri: ',', '.join(basliktahminler))
                basliktahminler = ', '.join(basliktahminler)
            else:
                basliktahminler = 'baslik tahmin yok.'
            
            cevap = self.GoogleArama(konular=gkonular,basliklar=basliktahminler)
            
            print('\n\n Yazılım cevabı : ',cevap)
            self.SqleGir(tahminkonular=konutahmin,tahminbasliklar=basliktahminler,cevap=cevap)
            
    
    def SqleGir(self,tahminkonular,tahminbasliklar,cevap):
        vt = sql.connect('robot.db')
        im = vt.cursor()
        im.execute("CREATE TABLE IF NOT EXISTS islemler (genel_konu, ust_konu, alt_konu,basliktahminler,cevap)")
        genel_konu = tahminkonular[0]
        ust_konu = tahminkonular[1]
        alt_konu = tahminkonular[2]
        im.execute("""INSERT INTO islemler VALUES (?,?,?,?,?)""",(genel_konu,ust_konu,alt_konu,tahminbasliklar,cevap))
        vt.commit()
        vt.close()
    
    def GoogleArama(self,konular,basliklar):
        try:
            konular = ' '.join(konular)
            if basliklar != []:
                basliklar = ' '.join(basliklar)
                konular = konular+' '+basliklar

            
            links = []
            for j in search(query=konular, tld="co.in", num=40, stop=40, pause=0.2):
                links.append(j)
            
            cevap = 'Cevap bulunamadı.'
            for link in links:
                html = requests.get(link)
                html.encoding = 'utf-8'
                html = html.text
                soup = bs(html,'html.parser')
                try:
                    cevap = soup.find('h2')
                    if cevap.find('a')==None:
                        cevap = cevap.get_text(strip=True)
                        if len(cevap)<25:
                            continue
                    else:
                        continue
                    break
                except:
                    continue
                
        except:
            cevap = 'Cevap ararken hata ile karşılaştım.'
        return cevap
            
            