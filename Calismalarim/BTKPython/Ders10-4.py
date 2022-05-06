import re
import math
liste =["1","2","5a","10b","abc","10","50"]

# # 1. Sorunun cevabı
# def sayiBul(liste):
#     yeniListe= []
#     for sayi in liste:
#         try:
#             sayi = int(sayi)
#             yeniListe.append(sayi)
#         except:
#             pass
#     return yeniListe
# liste = sayiBul(liste)
# print(liste)
# 2. Sorunun cevabı
# class Devamci:
#     def __init__(self):
#         print("Sayı girişi kontrolcü uygulaması.\nUygulamayı sonlandırmak için 'q' yazınız.")
#         self.baslikSayi = 0
#         self.Baslik()
#     def Baslik(self):
#         print(f"Kontrol edilecek {self.baslikSayi+1}. bilgi.".center(100,'-'))
#         self.baslikSayi+=1
#         self.Giris()
#     def Giris(self):
#         girilen = input('Kontrol edilecek bilgiyi giriniz: ')
#         self.girilen = girilen
#         self.cikisKontrol()
#     def cikisKontrol(self):
#         if self.girilen == 'q':
#             print(f"{self.baslikSayi-1} adet bilgi kontrol edildi.")
#             return True
#         else:
#             self.hataKontrol()
#     def hataKontrol(self):
#         if not re.search("[a-z,ı,ğ,ü,ş,ö,ç,A-Z,Ğ,Ü,Ş,İ,Ö,Ç]",self.girilen) :
#             if re.search("\s",self.girilen):
#                 raise Exception("Boşluk kullanamazsınız.")
#             elif re.search("[0-9]",self.girilen):
#                 print(f"Girilen bilgi sayısaldır: {int(self.girilen)}")
#             else:
#                 raise Exception("Özel karakter kullanamazsınız.")
#         else :
#             raise Exception ("Harf kullanamazsınız.")
#         self.Baslik()
# while True:
#     try:
#         a = Devamci()
#         if a:
#             break
#     except Exception as ex:
#         print(ex)
# 3. Sorunun cevabı
# class Parola:
#     def __init__(self,sifre):
#         if re.search("[ŞğüÜıİĞşÖöÇç]",sifre):
#             raise Exception("Türkçe karakter kullanılamaz.")            
#         else:
#             print(f"Girilen şifre kullanılabilir.")            


# try:
#     Parola('Komenaç')
# except Exception as ex: 
#     print(ex)
# 4. Sorunun cevabı
class Faktoriyel:
    def __init__(self,sayi):
        self.girilen = sayi
        self.hataKontrol()
    def hataKontrol(self):
        if not re.search("[a-z,ı,ğ,ü,ş,ö,ç,A-Z,Ğ,Ü,Ş,İ,Ö,Ç]",self.girilen) :
            if re.search("\s",self.girilen):
                raise Exception("Boşluk kullanamazsınız.")
            elif re.search("[-,+,*,/]",self.girilen):
                raise Exception("Matematiksel işlemlere izin verilmedi.")
            elif re.search("[0-9]",self.girilen):
                print(f"Girilen bilgi sayısaldır: {int(self.girilen)}")
                self.girilen = int(self.girilen)
                self.islemiYap()
            else:
                raise Exception("Özel karakter kullanamazsınız.")
        else :
            raise Exception ("Harf kullanamazsınız.")
    def islemiYap(self):
        sonuc = 1
        if self.girilen == (0,1):
            pass
        else:
            for x in range(self.girilen):
                sonuc = sonuc*(x+1)
        print(f"Faktoriyel alma sonucu: {sonuc},Gerçek sonuç: {math.factorial(self.girilen)}")
print("Faktoriyel alma uygulaması başlatılıyor.\nÇıkış için 'q' girişi yapınız.")
while True:
    try:
        x = input('Giriş yapınız: ')
        if x=='q' :
            print('Uygulamadan çıkıldı.')
            break
        Faktoriyel(x)
    except Exception as ex:
        print(ex)













