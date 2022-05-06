# 1. sorunun cevabı
sayi = int(input('Kontrol Edilecek Sayıyı Giriniz: '))
sonuc = ' değildir.', 'dır.'
result = 0<=sayi and sayi<=100
print(f"1. sorunun cevabı: Sayı 0 ile 100 arasında{sonuc[result]}")
# 2. sorunun cevabı
sayi = int(input("Kontrol edilecek sayıyı giriniz: "))
sonuc = ' değildir.', 'dır.'
result = 0<=sayi and sayi%2==0
print(f"2. sorunun cevabı: Sayı pozitif çift sayı{sonuc[result]}")
3. sorunun cevabı
email, parola = input("Email adresi giriniz: "), input("Parolayı giriniz:")
kemail, kparola = 'dogru@gmail.com', '147S147ss'
sonuc = 'Mail veya parola hatalı.', 'Başarıyla giriş yaptınız.'
result = email == kemail and parola == kparola
print(f"3. sorunun cevabı: {sonuc[result]}")
# 4. sorunun cevabı
sayi1, sayi2, sayi3 = int(input('1. sayı: ')), int(input('2. sayı: ')), int(input('3. sayı: '))
sonuc = 'küçüktür veya eşittir.', 'büyüktür.'
result1 = sayi1 > sayi2
result2 = sayi1 > sayi3
result3 = sayi2 > sayi3
print(f"4. sorunun cevabı: 1. sayı 2. sayıdan {sonuc[result1]}\n1. sayı 3. sayıdan {sonuc[result2]}\n2. sayı 3. sayıdan {sonuc[result3]}")
# 5. sorunun cevabı
vize1, vize2, final = int(input('Vize1 notu: ')), int(input('Vize2 notu: ')), int(input('Final notu: '))
ort = (vize1+vize2)/2*0.6 + final*0.4
sonuc = 'kaldı.', 'geçti.'
result = ( ort >= 50 and final >= 50) or final >=70
print(f"5. sorunun cevabı: Ortalamanız: {ort} Geçme Durumunuz: {sonuc[result]}")
# 6. sorunun cevabı
ad, kilo, boy = input('Adınız: '), int(input('Kilonuz: ')), int(input('Boyunuz (cm): '))
boy = boy/100
result = kilo/boy**2
sonuc = 'İndeks kriterleri dışındadır.', 'Şişman (Obez).', 'Fazla Kilolu.', 'Normal.', 'Zayıf.'
test1 = 0 < result < 18.4
test2 = 0 < result < 24.9
test3 = 0 < result < 29.9
test4 = 0 < result < 34.9
result2 = 0
result2 = test1 + test2 + test3 + test4
print(f"6. sorunun cevabı: {ad} kilo indeksiniz : {result}, {sonuc[result2]}")






