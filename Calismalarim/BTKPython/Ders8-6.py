# Quiz Uygulaması
class Question:
    def __init__(self,metin,siklar,cevap,sayar):
        self.metin = metin
        self.sayar = sayar
        self.siklar = siklar
        self.cevap = cevap
    def Kontrol (self,cevaplarim):
        self.cevaplarim = cevaplarim
        print(f"Soru{self.sayar+1}. {self.metin}\n{self.siklar[0]}{self.siklar[1]}{self.siklar[2]}{self.siklar[3]}{self.siklar[4]}")
        verilen_Cevap = input('Cevabınızı şık olarak giriniz: ')
        verilen_Cevap = verilen_Cevap.upper()
        cevaplarim.append(verilen_Cevap)
        return [self.cevap == verilen_Cevap,self.cevaplarim]
class Quiz(Question):
    def __init__(self,metin,siklar,cevap,sayar):
        Question.__init__(self,metin,siklar,cevap,sayar)
        self.derece = 0
        self.bilinen = 0
        self.dogrucevaplar = 0
        self.bilinenler = []
    def sonhal(self,puan,bilinen,por,hangisorular,i,yanlislar,dogruluk):
        self.i = i
        self.dogruluk = dogruluk
        self.yanlislar=yanlislar
        self.puan = puan
        self.bildik = bilinen
        self.incisoru = por+1
        self.hangisorular = hangisorular
        if self.dogruluk == True:
            self.hangisorular.append(self.incisoru)
            self.i+=1
            self.puan +=20
            self.bildik +=1
            return [self.puan,self.bildik,self.hangisorular,self.i,self.yanlislar]
            # ,self.bilinenler,self.i]
        else:
            self.yanlislar.append(self.incisoru)
            return[self.puan,self.bildik,self.hangisorular,self.i,self.yanlislar]

            

bilinenler = []         
metin = ["Türkiye'nin başkenti neresidir?","Hangisi Ege bölgesindedir?","Türkiye'nin en kalabalık şehri hangisidir?","Hangisi Akdeniz bölgesindedir?","Osmangazinin mezarı nerededir?"]
siklar = "A.İstanbul\n","B.Ankara\n","C.Adana\n","D.İzmir\n","E.Bursa\n"
cevap = ["B","D","A","C","E"]
por=0
i=0
bilinen = 0
puan = 0
cevaplarim = []
hangisorular = []
yanlislar = []
while por<5:
    soru = Quiz(metin[por],siklar,cevap[por],por)
    dogruluk,cevaplarim = soru.Kontrol(cevaplarim)
    puan, bilinen, hangisorular, i,yanlislar= soru.sonhal(puan,bilinen,por,hangisorular,i,yanlislar,dogruluk)
    por+=1
print(f"Doğru bildiğiniz sorular:")
for x in hangisorular:
    print(f"{x}.")
print(f"Toplamda {bilinen} adet soruyu doğru bildiniz.\nPuanınız: {puan}\n")
print(f"Yanlis cevap veriler sorular:")
for x in yanlislar:
    print(f"{x}.")
print(f"Toplamda {len(yanlislar)} adet soru(sorular)'a yanlis cevap(lar) verildi.")
for x in yanlislar:
    soru = x-1
    print(f"\n{soru+1}.soru\n{metin[soru]} sorusuna yanlış cevap verdiniz.\n{siklar}\nCevabınız: {cevaplarim[soru]}\nDoğru cevap: {cevap[soru]} ")
print(f"cevaplariniz: {cevaplarim}")
if puan<50:
    soyle = 'Kaldınız.'
else:
    soyle = 'Geçtiniz.'

print(f"{len(hangisorular)} adet doğru cevap\n{len(yanlislar)} adet yanlış cevap ile\n100 üzerinden {puan} alarak {soyle}")