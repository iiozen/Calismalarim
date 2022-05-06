# Bankamatik Uygulaması

SadikHesap = {
    'ad':'Sadık Turan',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000,
}

AliHesap = {
    'ad':'Ali Turan',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000,
}

def paracek():
    global SadikHesap
    global AliHesap
    print('Hoş geldiniz.\nPara Çekmek için para çekme, çıkış yapmak için çıkış yazınız.')
    while True:
        istenilen = input('Yapmak istediğiniz işlemi giriniz: ')
        if istenilen == 'para çekme':
            pol = 0
            while pol == 0:
                isim, hesapNo = input('Adınızı giriniz: '), input('Hesap Numaranızı giriniz: ')
                if isim == SadikHesap['ad'] and hesapNo == SadikHesap['hesapNo']:
                    print('Hesap bilgileriniz:')
                    for item1,item2 in SadikHesap.items():
                        print("{} : {}".format(item1,item2))
                    para = int(input('Çekmek istediğiniz miktarı giriniz: '))
                    sonuc = SadikHesap['bakiye'] - para
                    topsonuc = (SadikHesap['bakiye']+SadikHesap['ekHesap']) - para
                    if sonuc < 0:
                        if topsonuc < 0 :
                            print('Yetersiz bakiye.')
                            pol+=1
                        else :
                            cevap = input('Bakiyeniz yetersiz.\nEk hesabınızdaki miktarı kullanmak istiyor musunuz?\nevet veya hayır yazınız.\n')
                            if cevap == 'evet' :
                                SadikHesap['bakiye'] = 0
                                SadikHesap['ekHesap'] = topsonuc
                                print(f"Başarıyla {para} tl çektiniz.\nKalan Bakiyeniz 0 tl.\nKalan ek hesap bakiyeniz:{SadikHesap['ekHesap']}\n")
                                pol+=1
                            elif cevap == 'hayır':
                                print('İşlemden çıkılıyor.')
                                pol+=1
                    else:
                        print(f"Başarıyla {para} tl çektiniz.")
                        print(f"Yeni bakiyeniz: {sonuc}")
                        SadikHesap['bakiye'] = sonuc
                        pol+=1
                elif isim ==AliHesap['ad'] and hesapNo == AliHesap['hesapNo']:
                    print('Hesap bilgileriniz:')
                    for item1,item2 in AliHesap.items():
                        print("{} : {}".format(item1,item2))
                    para = int(input('Çekmek istediğiniz miktarı giriniz: '))
                    sonuc = AliHesap['bakiye'] - para
                    topsonuc = (AliHesap['bakiye']+AliHesap['ekHesap']) - para
                    if sonuc < 0:
                        if topsonuc < 0 :
                            print('Yetersiz bakiye.')
                            pol+=1
                        else :
                            cevap = input('Bakiyeniz yetersiz.\nEk hesabınızdaki miktarı kullanmak istiyor musunuz?\nevet veya hayır yazınız.\n')
                            if cevap == 'evet' :
                                AliHesap['bakiye'] = 0
                                AliHesap['ekHesap'] = topsonuc
                                print(f"Başarıyla {para} tl çektiniz.\nKalan Bakiyeniz 0 tl.\nKalan ek hesap bakiyeniz:{AliHesap['ekHesap']}\n")
                                pol+=1
                            elif cevap == 'hayır':
                                print('İşlemden çıkılıyor.')
                                pol+=1
                    else :
                        print(f"Başarıyla {para} tl çektiniz.")
                        print(f"Yeni bakiyeniz: {sonuc}")
                        AliHesap['bakiye'] = sonuc
                        pol+=1
                else:
                    print("İsim veya hesapNo'nuzu hatalı girdiniz.\Tekrar")
            continue
        elif istenilen == 'çıkış':
            print('İyi günler dileriz.')
            break
        else:
            print('Hatalı giriş yaptınız.')
            continue

paracek()

    
