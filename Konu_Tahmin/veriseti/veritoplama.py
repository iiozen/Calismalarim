from verisetiDict import linkler
from veriDondurme import VeriIslemleri
import pandas as pd
import numpy as np

vi = VeriIslemleri()
baslik = ['Genel Konu','Üst Konu','Alt Konu','Konum']
df = vi.veriDondur(linkler)
df = vi.TabloDondur(df[2],baslik)


baslik2 = ['icerik','başlık','genel_konu','ust_konu','alt_konu']
veri = vi.veriMain(df)

veri = vi.TabloDondur(veri,baslik2)
print(veri)

veri.to_csv('spottitlesiz.csv',index=False)



