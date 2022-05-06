# Quiz Uygulaması
class Soru:
    def __init__(self,soru,siklar,cevap):
        self.soru = soru
        self.siklar = siklar
        self.cevap = cevap
    def Kontrol(self,cevap):
        return self.cevap == cevap
class Sinav:
    def __init__(self,sorular):
        self.sorular = sorular
        self.sayar = 0
        self.puan = 0
        self.baslikAtar()
    def soruGoster(self):
        print(f"Soru {self.sayar+1}: {self.sorular[self.sayar].soru}")
        for abc in self.sorular[self.sayar].siklar:
            print('->  '+abc)
        cevap = input('Cevabınız: ')
        self.cevapKontrol(cevap)
    def cevapKontrol(self,cevap):
        self.cevap = cevap
        if self.sorular[self.sayar].Kontrol(self.cevap):
            self.puan+=1
        self.sayar+=1
        self.sinavBitir()
    def sinavBitir(self):
        if len(self.sorular) == self.sayar:
            print("Sinav bitti.")
            self.puanHesaplar()
        else :
            self.baslikAtar()
    def puanHesaplar(self):
        print(f"Doğru cevap sayınız: {self.puan}")
    def baslikAtar(self):
        print(f"Toplam {len(self.sorular)} sorudan {self.sayar+1}. soru".center(110,'-'))
        self.soruGoster()
s1 = Soru('Aralarından hangisi en küçüktür?',['5','10','20','30'],'5')
s2 = Soru('Aralarından hangisi en büyüktür?',['30','10','5','20'],'30')
s3 = Soru('Aralarından hangisi en tam sayıdır?',['5.65','10.32','20','-%30'],'20')
s4 = Soru('Deli yazınız.',['Hadi','Deli','Yazar','mısın?'],'Deli')
s5 = Soru('Farklı olanı yazınız.',['Farklı','Garip','Different','İlginç'],'İlginç')
sorular = [s1,s2,s3,s4,s5]
Sinav(sorular)