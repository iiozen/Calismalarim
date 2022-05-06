while True:
    islem = input("Yetkili girisi icin 'yetkili' ogrenci girisi icin 'ogrenci' çıkış için 'çıkış' yazınız.")
    if islem == 'yetkili':
        while True:
            print("Yetkili girişi başarılı.Geri dönek için 'geri' yazınız Kaydetmek istediğiniz öğrencinin:")
            with open("deneme.txt","r+",encoding="utf-8") as file:
                name = str("Ad Soyad: "+input('Ad soyad: ')+"\n")
                if name == 'Ad Soyad: geri\n':
                    print('İşlem menüsüne çıkılıyor.')
                    break
                puan,harf= str("Puanı: "+input('Puanı: ')+"\n"),str("Harf Notu: "+input('Harf Notu: ')+"\n\n")                           
                liste = file.readlines()
                file.seek(0)
                liste2= [harf,puan,name]
                for item in liste2:
                    liste.insert(0,item)
                file.writelines(liste)
                file.seek(0)
                print(file.read())
    elif islem == 'ogrenci':
        print('Başarıyla öğrenci girişi yapıldı.\n')
        with open("deneme.txt","r",encoding="utf-8") as file:
            print(file.read())
    elif islem == 'çıkış':
        break
    else:
        print('Hatalı giriş yaptınız.')    