# Sayı Tahmin Uygulaması
import random
sayi = random.randint(1,100)
hak = int(input('Hak sayısını giriniz: '))
can = 100
eksi = 100/hak
girilen = int(input('Tahmin ettiğiniz sayıyı giriniz: '))
can -=eksi
while girilen != sayi and can>0:
    if sayi>girilen:
        girilen = int(input('Yukarı: '))
    elif sayi<girilen:
        girilen = int(input('Aşağı: '))
    if sayi == girilen:
        can = int(can)
        print(f"Tahmininiz doğru. Sayı: {sayi}, kalan can: {can}")
        break    
    can -=eksi
if can <=0:
    print(f"Canınız 0'ın altına düştü kaybettiniz. Sayı: {sayi} idi.")


        

