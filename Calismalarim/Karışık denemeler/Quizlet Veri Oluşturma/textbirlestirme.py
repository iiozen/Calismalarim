import os
class DosyaBirlestir:
    '''
    kelimeler: ingilizce kelimelerin bulunduğu txt dosyasının konumu
    words: türkçe kelimelerin bulunduğu txt dosyasının konumu
    yazdirma: kelimelerin birleştirilip yazdırılacak yeni txt dosyasının konumu ve ismi= [konum,isim]
    ayirac: ingilizce ve türkçe kelimeler arasında kelimeleri ayırmak için kullanılacak sembol
    ayirac2 : ingilizce ve türkçe olarak birleştirilen kelimeleri ayıracak sembol orjinal olarak satır atlanmasıdır : /n
    kelimelimit : Sayı girilirse o sayıdan fazla olan kelimeler için yeni dosya açar ve böyle devam eder.
    kelimeminlimit : Kalan kelime sayısı bu limitin altındaysa kelimeler son listeye eklenir.
    '''
    def __init__(self,kelimeler:str,words:str,yazdirma:list,ayirac:str,kelimelimit:int,kelimeminlimit:int,ayirac2='/n'):
        self.ayirac = ayirac
        self.kelimelimit = kelimelimit
        self.kelimeminlimit = kelimeminlimit
        self.ayirac2 = ayirac2
        self.konum,self.isim = yazdirma
        if kelimelimit<=0:
            raise ValueError("Kelime limit sayısı 0 veya 0'dan küçük olamaz.")
        with open(kelimeler,'r',encoding='utf-8') as f:
            kelimelerlist = f.readlines()
            self.kelimelerliste = []
            for i in kelimelerlist:
                i=i.strip()
                if i.find('\n')!=-1:
                    i = i.replace('\n','')
                if len(i)>0:
                    self.kelimelerliste.append(i)
            

                        
        with open(words,'r',encoding='utf-8') as f:
            wordslist = f.readlines()
            self.wordsliste = []
            for i in wordslist:
                i=i.strip()
                if i.find('\n')!=-1:
                    i = i.replace('\n','')
                if len(i)>0:
                    self.wordsliste.append(i)
        
        if len(self.kelimelerliste)==len(self.wordsliste):
            self.Yazdir()
        else:
            yazi = '\nDosyalar eşit sayıda kelime içermiyor:\nİngilizce kelime sayısı:'+str(len(self.kelimelerliste))+'\nTürkçe kelime sayısı:'+str(len(self.wordsliste))
            raise ValueError(yazi)
            
        
    def Yazdir(self):
        
        yazdirilacakliste = []
        for i in range(len(self.kelimelerliste)):
            satir = self.kelimelerliste[i]+self.ayirac+self.wordsliste[i]+self.ayirac2
            yazdirilacakliste.append(satir)
        yazdirilacakliste2 = []
        tt = []
        for i,kelime in enumerate(yazdirilacakliste):
            tt.append(kelime)
            if i+1==len(yazdirilacakliste):
                yazdirilacakliste2.append(tt)
                
            elif (i+1)%self.kelimelimit==0:
                limit = len(self.kelimelerliste)-(i+1)
                if limit>=self.kelimeminlimit:
                    yazdirilacakliste2.append(tt)
                    tt=[]

                
        
        self.isimBulma(yazdirilacakliste=yazdirilacakliste2)
        
        
    def isimBulma(self,yazdirilacakliste):
        yazdirmastr = self.konum + '/'+self.isim+'-'
        numara = 1
        for i in yazdirilacakliste:
            devam = True
            while devam:
                dosya = yazdirmastr + str(numara) + '.txt'
                if not os.path.exists(dosya):
                    dosyaismi = self.isim + '-' + str(numara) + '.txt'
                    self.DosyaOlustur(yazdirmastr = dosya,yazdirilacak=i,dosyaismi=dosyaismi)
                    devam=False
                numara+=1
       
        
                

        
        
    def DosyaOlustur(self,yazdirilacak,yazdirmastr,dosyaismi):
        with open(yazdirmastr,'w',encoding='utf-8') as f:
            f.writelines(yazdirilacak)
        print(len(yazdirilacak),' kelimeden oluşan ',dosyaismi,' dosyası oluşturuldu.')