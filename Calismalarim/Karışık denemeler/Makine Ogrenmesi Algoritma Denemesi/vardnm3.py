#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

veriler = pd.read_csv('Ads.csv').values

import random as rnd



#%%
def DegeriBul(veriler,toplama=1000,baslangic=1,durdurmasira=5,orttekrar=5,min_limit_orani=0.95):
    yapilanislem=0
    satir,sutun = veriler.shape
    toplamodullistesi = [0]*toplama
    odullersozde2=[]
    max_odulort=0
    max_baslangic=1
    durdurma = 0
    while baslangic<=toplama:
        kuraliste2 = [1]*sutun
        
        odulort = [0]*orttekrar
        odullersozde=[]
        for ortodul in range(orttekrar):
            toplamodul = 0
            for i in range(int(satir)):
                csutun = rnd.sample(range(sutun),counts=kuraliste2,k=1)
                for x in range(sutun):
                    bir = veriler[i,x]
                    if bir==1:
                        # kuraliste.append(x)
                        kuraliste2[x]+=toplama
                    else:
                        # kuraliste2=[dd+1 for dd in kuraliste2]
                        kuraliste2[x]-=baslangic
                        if kuraliste2[x]<1:
                            kuraliste2[x]=1

                odul = veriler[i,csutun]
                # odulsutun = csutun
                if odul==1:
                    toplamodul+=1
            odulort[ortodul]=toplamodul
        odullersozde2.append(odulort)
        # odullersozde2.append(odullersozde)
        odultopl = 0
        for j in odulort:
            odultopl+=j
        odulort = odultopl/orttekrar
        toplamodullistesi[baslangic-1]=odulort
        if odulort>max_odulort:
            max_odulort=odulort
            max_baslangic=baslangic
            durdurma = 0
        elif odulort<max_odulort*min_limit_orani:
            durdurma+=1
        if durdurma==durdurmasira:
            break
        baslangic+=1
    return toplamodullistesi,max_baslangic,max_odulort

#%%
toplamodul_listesi,azaltmadegeri,degeri = DegeriBul(veriler=veriler,toplama=1000,baslangic=1,orttekrar=5,durdurmasira=5)

# %%
