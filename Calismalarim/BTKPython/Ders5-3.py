# 1. Sorunun cevabı
isim, yas, egitim = input('Adınız: '), input('Yaşınız: '), input('Eğitim durumunuz: ')
yas = int(yas)
egitim = egitim.lower()
if ((egitim == 'üniversite' or egitim =='lise') and yas >=18):
    print(f"Sayın {isim} ehliyet alabilirsiniz.")
else : 
    print(f"Sayın {isim} ehliyet alamazsınız.")
# 2. Sorunun cevabı
yazili1, yazili2, sozlu = int(input('1. yazılı: ')), int(input('2. Yazılı: ')), int(input('Sozlu: '))
ort = (yazili1 + yazili2 + sozlu)/2
print(f"Ortalamanız: {ort}")
if 0<=ort<=24:
    print(f"Notunuz : 0")
elif 25<=ort<=44:
    print(f"Notunuz : 1")
elif 45<=ort<=54:
    print(f"Notunuz : 2")
elif 55<=ort<=69:
    print(f"Notunuz : 3")
elif 70<=ort<=84:
    print(f"Notunuz : 4")
elif 85<=ort<=100:
    print(f"Notunuz : 5")
# 3. Sorunun cevabı
import datetime
zaman = input('Sırasıyla yıl ay günü aralarında boşluk olacak şekilde giriniz: ')
zaman = zaman.split()
zaman[0], zaman[1], zaman[2] = int(zaman[0]), int(zaman[1]), int(zaman[2])
zaman = datetime.date(zaman[0], zaman[1], zaman[2])
suan = datetime.date.today()
fark = suan - zaman
fark = fark.days
yil = fark//365
if yil >=1:
    print(f"1. Bakım yılı.")
    if yil >=2:
        print(f"2. Bakım yılı.")
        if yil >=3:
            print(f"3. Bakım yılı.")
            if yil >=4:
                print(f"4. Bakım yılı.")
                if yil >=5:
                    print(f"5. Bakım yılı.")
                    if yil >=6:
                        print(f"6. Bakım yılı.")
                        if yil >=7:
                            print(f"7. Bakım yılı.")
                            if yil >=8:
                                print(f"8. Bakım yılı.")
                                if yil >=9:
                                    print(f"9. Bakım yılı.")
                                    if yil >=10:
                                        print(f"10. Bakım yılı.")
                                        if yil >=11:
                                            print(f"11. Bakım yılı.")
                                            if yil >=12:
                                                print(f"12. Bakım yılı.")









    

