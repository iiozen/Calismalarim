# 1. Sorunun cevabı
def goster(kelime,kere):
    for i in range(kere):
        print(kelime)
kelime = input('Kelimeyi giriniz: ')
kere = int(input('Kaç defa gösterilecek giriniz: '))
goster(kelime,kere)
#############################2. Soru pek iyi değildi. Bu yüzden tam yapmadım.
# 2. Sorunun cevabı
# def listyapar(*eleman):
#     eleman = list(eleman)
#     print(eleman)
#     print(type(eleman))
# liste = []
# print('Listeye çevirmek istediğiniz elemanları gönderiniz. Eleman girişini sonlandırmak için bitti yazınız.')
# while True:
#     a = input('Elemanı giriniz: ')
#     if a == 'bitti':
#         break
#     else:
#         liste = (x for )
# listyapar(liste)
# girilen = (x for x in range(len(a)) )
# listyapar(girilen)
######################################################
3. Sorunun cevabı
def asal(a1,a2):
    
    asallar = []
    while True:
        sonuc = a1-a2
        if sonuc == 0:
            print('2 tane aynı değer girdiniz ')
            a1 = int(input("Baslangıcı giriniz: "))
            a2 = int(input("Bitişi giriniz: "))
        elif sonuc > 0:
            while a1 >= a2:
                bolum = 0
                for i in range(2,a2):
                    if a2%i == 0 :
                        bolum +=1
                if bolum == 0 and a2 !=1 and a2>0 :
                    asallar.append(a2)
                a2+=1
            return asallar
            break
        elif sonuc < 0 :
            while a2 >= a1:
                bolum = 0
                for i in range (2,a1):
                    if a1%i == 0 :
                        bolum+=1
                if bolum ==0 and a1 != 1 and a1>0:
                    asallar.append(a1)
                a1+=1
            return asallar
            break
baslangic, bitis = int(input("Baslangıcı giriniz: ")), int(input("Bitişi giriniz: "))
result = asal(baslangic,bitis)
print('Belirlenen başlangıç ve bitiş sayıları ve arasındaki asal sayılar:')
for sayi in result:
     print(sayi)
# 4. Sorunun cevabı
def bolenler(sayi):
    liste = []
    for i in range(2,sayi):
        if sayi%i==0:
            liste.append(i)
    return liste
sayi = int(input('Tam bölenlerini bulmak istediğiniz sayıyı giriniz: '))
sonuc = bolenler(sayi)
print(sonuc)





    


    