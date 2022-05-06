ogrenci = input('Öğrenci numaranızı giriniz: ')
ogrenciAd = input('Adınızı giriniz: ')
ogrenciSoyad = input('Soyadınızı giriniz: ')
ogrenciTel = input('Telefon numaranızı giriniz: ')
ogrenciler= {
    ogrenci:{
        'ad': ogrenciAd,
        'soyad': ogrenciSoyad,
        'telefon': ogrenciTel
}
}

ogrenci = input('Öğrenci numaranızı giriniz: ')
ogrenciAd = input('Adınızı giriniz: ')
ogrenciSoyad = input('Soyadınızı giriniz: ')
ogrenciTel = input('Telefon numaranızı giriniz: ')
ogrenciler[ogrenci]= {
    'ad': ogrenciAd,
    'soyad': ogrenciSoyad,
    'telefon': ogrenciTel
}

ogrenci = input('Öğrenci numaranızı giriniz: ')
ogrenciAd = input('Adınızı giriniz: ')
ogrenciSoyad = input('Soyadınızı giriniz: ')
ogrenciTel = input('Telefon numaranızı giriniz: ')
ogrenciler[ogrenci]= {
    'ad': ogrenciAd,
    'soyad': ogrenciSoyad,
    'telefon': ogrenciTel
}

numara = input('Bilgilerini öğrenmek istediğiniz öğrenci numarasını giriniz: ')
print(f"Öğrenci Numarası: {numara}\nAdı: {ogrenciler[numara]['ad']}\nSoyadı: {ogrenciler[numara]['soyad']}\nTelefon Numarası: {ogrenciler[numara]['telefon']}")