import pandas as pd
from onisleme import Onisleme
veri = pd.read_csv('spottitlesiz.csv')
degistir = [['saglik','gundem','dunya'],['sağlık','gündem','dünya']]


h = pd.DataFrame(veri)
h['genel_konu']=h['genel_konu'].replace(degistir[0],degistir[1])



yeniicerik = []
for cmle in h['icerik']:
    cumle = Onisleme([cmle])
    cumle = cumle[0]
    yeniicerik.append(cumle)



yenibaslik = []
for cmle in h['başlık']:
    cumle = Onisleme([cmle])
    cumle = cumle[0]
    yenibaslik.append(cumle)



h['icerik'] = yeniicerik
h['başlık'] = yenibaslik
print(h)

h.to_csv('egitimehazir.csv',index=False)