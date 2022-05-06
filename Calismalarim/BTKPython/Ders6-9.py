# Asal Sayı Uygulaması
print("Asal olup olmadığını öğrenmek istediğiniz sayıları giriniz.\nUygulamadan çıkış yapmak için 'bitir' yazınız ")
giris = None
while True:
    giris = input('Giris yapınız: ')
    deneme = 0
    degerler = []
    if giris == 'bitir':
        print("Uygulama sonlandırıldı.")
        break
    else:
        giris = int(giris)
        if giris == 1:
            print(f"{giris} asal sayı değildir.")
        if giris == 2:
            print(f"{giris} asal sayıdır.")
        for x in range(2,giris):
            sonuc = giris%x
            if sonuc == 0:
                degerler.append(x)
                deneme+=1
        if deneme==0 and giris !=2 and giris!=1:
            print(f"{giris} asal sayıdır.")
        elif deneme>0 :
            print(f"{giris} asal sayı değildir.{degerler}'e bölünebilir.")


    
    
