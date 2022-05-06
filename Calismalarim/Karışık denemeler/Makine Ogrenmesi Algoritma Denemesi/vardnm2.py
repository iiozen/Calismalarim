#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

veriler = pd.read_csv('Ads.csv').values

import random as rnd

satir,sutun = veriler.shape


def EkleCek(liste,bazsutun,odulsutun,adet=1):
    for i in range(bazsutun):
        # for j in range(bazsutun):
        liste.append(i)
    if odulsutun!=None:
        for i in range(adet):
            liste.append(odulsutun)


def BasariliBasarisiz(liste,bazsutun,odul,odulsutun,adet=2):
    if odul==1:
        for i in range(adet):
            liste.append(odulsutun)

    # else:
    #     liste.remove(odulsutun)
    #     for i in range(bazsutun):
    #         liste.append(i)

# kuraliste = []

# EkleCek(kuraliste,sutun,None)
kuraliste2 = [1]*sutun


toplamodul = 0


for i in range(int(satir)):
    # csutun = kuraliste[rnd.randrange(len(kuraliste))]
    csutun = rnd.sample(range(sutun),counts=kuraliste2,k=1)
    for x in range(sutun):
        bir = veriler[i,x]
        if bir==1:
            # kuraliste.append(x)
            kuraliste2[x]+=1000
        else:
            # kuraliste2=[dd+1 for dd in kuraliste2]
            kuraliste2[x]-=277
            if kuraliste2[x]<1:
                kuraliste2[x]=1

    odul = veriler[i,csutun]
    odulsutun = csutun
    if odul==1:
        # odulsutun = csutun
        toplamodul+=1
    # else:
    #     odulsutun = None
    # BasariliBasarisiz(kuraliste,sutun,odul,odulsutun)
# enyuksekAdet = 0
# enyuksekEleman = 0
# for i in range(sutun):
#     kere = kuraliste.count(i)
#     if kere > enyuksekAdet:
#         enyuksekAdet = kere
#         enyuksekEleman = i
# print(enyuksekEleman,enyuksekAdet)
print('Toplam Ödül : ', toplamodul)
plt.hist(range(sutun),weights=kuraliste2)
plt.show()
# %%



# %%
d =4
bes = [5, 5, 5, 5]
bes = [x+1 for x in bes]

# %%
