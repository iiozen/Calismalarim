def textYaz(veri,isim,yer):
    isim = yer+'/'+isim+'.txt'
    veri = str(veri)
    with open(isim,'w',encoding='utf-8')  as f:
        f.write(veri)