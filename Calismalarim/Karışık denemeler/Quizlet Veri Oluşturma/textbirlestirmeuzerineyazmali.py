import os
class DosyaBirlestir:
    '''
    kelimeler: ingilizce kelimelerin bulunduğu txt dosyasının konumu
    words: türkçe kelimelerin bulunduğu txt dosyasının konumu
    yazdirma: kelimelerin birleştirilip yazdırılacak yeni txt dosyasının konumu ve ismi= [konum,isim]
    ayirac: ingilizce ve türkçe kelimeler arasında kelimeleri ayırmak için kullanılacak sembol
    ayirac2 : ingilizce ve türkçe olarak birleştirilen kelimeleri ayıracak sembol orjinal olarak satır atlanmasıdır : /n
    kelimelimit : Sayı girilirse o sayıdan fazla olan kelimeler için yeni dosya açar ve böyle devam eder.
    '''
    def __init__(self,kelimeler:str,words:str,yazdirma:list,ayirac:str,kelimelimit:int,ayirac2='/n'):
        self.ayirac = ayirac
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
            raise ValueError('Dosyalar eşit boyutta kelime içermiyor:\ningilizce kelime sayısı:',self.kelimelerliste,'\nTürkçe kelimeler sayısı:',self.wordsliste) 
        
    def Yazdir(self):
        
        yazdirilacakliste = []
        for i in range(len(self.kelimelerliste)):
            satir = self.kelimelerliste[i]+self.ayirac+self.wordsliste[i]+self.ayirac2
            yazdirilacakliste.append(satir)
            
        yazdirmastr = self.konum + '/'+self.isim+'.txt'
        devammi='Evet'
        if os.path.exists(yazdirmastr):
            devammi = input(self.isim+'.txt dosyası zaten var üzerine yazmak istiyor musunuz? Evet/hayır')
            devammi = self.UzerineYazma(devammi=devammi)
        # if devammi=='Evet':
            with open(yazdirmastr,'w',encoding='utf-8') as f:
                f.writelines(yazdirilacakliste)
            print('Dosya Oluşturma Başarılı.')
                
        if devammi=='hayır':
            print('Dosya Oluşturulmadı.')
        
    # def UzerineYazma(self,devammi):
    #     if devammi!='Evet' and devammi!='hayır':
    #         self.HataliGiris()
    #     else:
    #         return devammi
    # def HataliGiris(self):
    #     devammi = input('Hatalı giriş yaptınız. Dosyayı üzerine yazmak için Evet yazmamak için hayır yazınız.')
    #     self.UzerineYazma(devammi)
        
        
    def DosyaOlustur(self,yazdirilacakliste,yazdirmastr):
        with open(yazdirmastr,'w',encoding='utf-8') as f:
            f.writelines(yazdirilacakliste)
        print('Dosya Oluşturma Başarılı.')