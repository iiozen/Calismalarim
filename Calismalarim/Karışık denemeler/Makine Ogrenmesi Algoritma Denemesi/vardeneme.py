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
        
kuraliste = []

EkleCek(kuraliste,sutun,None)


    
toplamodul = 0
    

for i in range(int(satir/2)):
    csutun = kuraliste[rnd.randrange(len(kuraliste))]
    odul = veriler[i,csutun]
    odulsutun = csutun
    if odul==1:
        # odulsutun = csutun
        toplamodul+=1
    # else:
    #     odulsutun = None
    BasariliBasarisiz(kuraliste,sutun,odul,odulsutun)
enyuksekAdet = 0
enyuksekEleman = 0
for i in range(sutun):
    kere = kuraliste.count(i)
    if kere > enyuksekAdet:
        enyuksekAdet = kere
        enyuksekEleman = i
print(enyuksekEleman,enyuksekAdet)
print('Toplam Ödül : ', toplamodul)
plt.hist(kuraliste)
plt.show()
# %%
d = 10
ddd = [1] *2




# %%
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ileri = [i for i in range(0,10001)]
    
# loglu = [math.sqrt((3/2)*math.log(i)/i) for i in ileri]
# loglu = [math.sqrt(1/math.log(i)) for i in ileri]
loglu = [1.001**i for i in ileri ]

plt.plot(ileri,loglu,c='red')
plt.show()


    
    
# %%
dl = [[]]*10
# %%
import random

rasbeta = random.betavariate(1,5)*100

# %%
