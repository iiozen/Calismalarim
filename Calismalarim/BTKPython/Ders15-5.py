# Json Demo
import json
import re
class Menu:
    def __init__(self):
        try:
            file = open('kayit.txt','x')
        except:
            pass
        print('Anamenü'.center(100,'*'))
        self.anaMenu()
    def anaMenu(self):
        print(' 1- İşlem Menüsü\n', '2- Çıkış')
        secim = input('Seçim yapınız: ')
        if secim == '1':
            print('\n')
            self.islemMenu()
        elif secim == '2':
            cikis()
        else:
            print('Hatalı seçim yaptınız. Tekrar seçim yapınız.')
            self.anaMenu()
    def islemMenu(self):
        print('İşlem Menüsü'.center(100,'-'))
        print(' 1- Kayıt Ol.\n', '2- Giriş Yap.\n', '3- Anamenüye Dön ')
        secim = input('Yapmak istediğiniz işlemi seçiniz: ')
        if secim == '1':
            Kayit()
        elif secim == '2':
            Giris()
        elif secim == '3':
            self.__init__()
        else:
            print('Hatalı giriş yaptınız.')
            self.islemMenu()

class Giris:
    def __init__(self):
        print('Giriş Menüsü'.center(100,'.'))
        print('Giriş yapmak için:') 
        with open("kayit.txt","r",encoding="utf-8") as f:
            okudum = f.read()
            okudum = json.loads(okudum)
            self.okudum = okudum
            self.kontrol_kullaniciAd = okudum['kullanıcı adı']
            self.kontrol_sifre = okudum['şifre']
        self.girisDeneme()
    def girisDeneme(self):
        self.tmm=0
        k_ad = input('Kullanıcı adınızı giriniz: ')
        if k_ad == 'çıkış':
            Menu()
        else:
            for i in self.kontrol_kullaniciAd:
                if i == k_ad:
                    self.tmm=1
                    self.kullaniciad=k_ad
                    self.index = self.kontrol_kullaniciAd.index(i)
                    k_sifre = input('Şifrenizi giriniz: ')
                    if self.kontrol_sifre[self.index] == k_sifre:
                        self.sifre = k_sifre
                        print('Giriş Başarılı. Giriş Menüsüne Yönlendiriliyorsunuz.')
                        self.ad = self.okudum["ad"][self.index]
                        self.soyad = self.okudum["soyad"][self.index]
                        self.girisBasarili()
                    else:
                        print('Şifre hatalı.')
                        self.girisDeneme()
            if self.tmm !=1:
                print('Kullanıcı adı hatalı. İşlem Menüsüne çıkmak için çıkış yazınız.')
                self.girisDeneme()
    def girisBasarili(self):
        print(f'Hoş Geldiniz {self.ad} {self.soyad}.'.center(60,' '))
        self.girisMenu()
    def girisMenu(self):
        print('1- Kimlik Bilgilerini Göster\n2- Hesaptan Çıkış Yap')
        islem = input('Yapmak istediğiniz işlemi seçiniz: ')
        if islem == '1':
            self.kimlikGoster()
        elif islem == '2':
            print('Anamenüye çıkılıyor.')
            Menu()
        else:
            print('Hatalı giriş yaptınız.')
            self.girisMenu()
    def kimlikGoster(self):
        k= self.okudum
        print(f"Ad Soyad: {self.ad} {self.soyad}\nKullanıcı adı: {self.kullaniciad}\nŞifre: {self.sifre}\nemail adresi: {k['email adresi'][self.index]}\nYaş: {k['yaş'][self.index]}\nMeslek: {k['meslek'][self.index]}")
        self.girisBasarili()
class Kayit:
    def __init__(self):
        print('Kayıt işlemlerine hoş geldiniz.')
        self.isim()
    def isim(self):
        liste = []
        x= input('Adınızı ve soyadınızı aralarında bir boşluk bırakarak giriniz: ')
        if re.search("[0-9]",x):
            print('İsminizde sayı olamaz.')
            self.isim()
        elif re.search("\W\s",x):
            print('İsminizde özel karakter olamaz.')
            self.isim()
        x = x.split()
        soyad = x[len(x)-1]
        x.remove(x[len(x)-1])
        ad = ''
        for i in x:
            ad = ad +' '+ i
        print(f'Sayın {ad} {soyad}')
        self.ad = ad
        self.soyad = soyad
        self.kullaniciAd()
    def kullaniciAd(self):
        kullanici_Ad = input('Kullanıcı adınızı giriniz: ')
        k_Uzunluk = len(kullanici_Ad)
        if k_Uzunluk<8:
            print('Kullanıcı adı 8 karakterden az olamaz.')
            self.kullaniciAd()
        elif re.search('\s',kullanici_Ad):
            print('Kullanıcı adda boşluk kullanılamaz.')
            self.kullaniciAd()
        elif re.search('\W|[_]',kullanici_Ad):
            print('Kullanıcı adı yalnızca harf ve sayılardan oluşabilir.')
            self.kullaniciAd()
        else:
            with open("kayit.txt",'r',encoding='utf-8') as f:
                k_Uzunluk = len(kullanici_Ad)
                read = f.read()
                read = json.loads(read)
                kontrol_k_Ad = read["kullanıcı adı"]
                for kontrol in kontrol_k_Ad:
                    if kullanici_Ad == kontrol:
                        print('Bu kullanıcı adı zaten alınmış. Yenisini giriniz: ')
                        self.kullaniciAd()
        self.kullanici_Ad = kullanici_Ad
        self.sifre()
    def sifre(self):
        pasw = input('Şifre belirleyiniz: ')
        sifre_Uzunluk = len(pasw)
        if sifre_Uzunluk<7:
            print('Şifre en az 8 karakter olabilir.')
            self.sifre()
        elif not re.search("[0-9]",pasw):
            print('Şifre en az 1 tane sayı içermelidir.')
            self.sifre()
        elif not re.search("[.,?*!-/\=+#&%]|[_]",pasw):
            print('Şifre en az 1 tane özel karakter (.,?*!-_/\=+#&%) içermelidir.')
            self.sifre()
        else:
            self.sifrem=pasw
            self.email()
    def email(self):
        e_mail = input('emai adresinizi giriniz: ')
        if not re.search("\w|[@]",e_mail):
            print('emailde özel karakter olamaz.')
            self.email()
        elif not re.findall("...[@]...+\.com",e_mail):
            print('Doğru email adresi giriniz.')
            self.email()
        else:
            with open("kayit.txt",'r',encoding="utf-8") as f:
                a = f.read()
                a = json.loads(a)
                k_email = a["email adresi"]
                for i in k_email:
                    if i==e_mail:
                        print('Bu mail adresi kayıtlı. Başka mail adresi giriniz.')
                        self.email()
            self.e_mail = e_mail
            self.Yas()
    def Yas(self):
        yas= input('Yaşınızı giriniz: ') 
        try:
            yas = int(yas)
            if yas<=5:
                print("Yaşınız pozitif ve 5'den büyük olmalıdır.")
                self.Yas()  
            else:
                self.yas = str(yas)
                self.Meslek()
        except:
            print('Yaşınızı sayısal olarak giriniz.')
            self.yas()
    def Meslek(self):
        meslek = input('Mesleğinizi giriniz: ')
        self.meslek = meslek
        self.kayitSon()
    def kayitSon(self):
        with open("kayit.txt","r+",encoding="utf-8") as f:
            oku = f.read()
            oku = json.loads(oku)
            liste_Ad, liste_Soyad,liste_kullaniciAd,liste_sifre,liste_mail,liste_yas,liste_meslek=[],[],[],[],[],[],[]
            for i in oku["ad"]:
                liste_Ad.append(i)
            for i in oku["soyad"]:
                liste_Soyad.append(i)
            for i in oku["kullanıcı adı"]:
                liste_kullaniciAd.append(i)
            for i in oku["şifre"]:
                liste_sifre.append(i)
            for i in oku["email adresi"]:
                liste_mail.append(i)
            for i in oku["yaş"]:
                liste_yas.append(i)
            for i in oku["meslek"]:
                liste_meslek.append(i)
            liste_Ad.append(self.ad)
            liste_Soyad.append(self.soyad)
            liste_kullaniciAd.append(self.kullanici_Ad)
            liste_sifre.append(self.sifrem)
            liste_mail.append(self.e_mail)
            liste_yas.append(self.yas)
            liste_meslek.append(self.meslek)
            eklenilecek = {
            "ad" : liste_Ad,
            "soyad" : liste_Soyad,
            "kullanıcı adı" : liste_kullaniciAd,
            "şifre" : liste_sifre,
            "email adresi" : liste_mail,
            "yaş" : liste_yas,
            "meslek" : liste_meslek
            }
            f.seek(0)
            eklenilecek = json.dumps(eklenilecek)
            f.write(eklenilecek)
        print('Kayıt Başarılı. Menüye yönlendiriliyorsunuz.')
        Menu()
class cikis:
    def __init__(self):
        print("Uygulamadan Çıkıldı.")

Menu()