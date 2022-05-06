# 1. sorunun cevabı
sayi1, sayi2 = int(input('1. sayıyı giriniz: ')),int(input('2. sayıyı giriniz: '))
sonuc = '2. sayı','1. sayı'
result = sayi1>sayi2
result = result
print(f"1. sorunun cevabı: {sonuc[result]} büyüktür.")
# 2. sorunun cevabı
vize, final = int(input('Vize puanını giriniz: ')), int(input('Final puanını giriniz: '))
sonuc= 'kaldı','geçti'
ort= vize*0.6 + final*0.4
result = ort>50
result = result
print(f"2. sorunun cevabı: {sonuc[result]}")
# 3. sorunun cevabı
sonuc = 'çifttir.', 'tektir.'
sayi = int(input('Sayı giriniz: '))
result = sayi%2
print(f"3. sorunun cevabı: Girilen sayı {sonuc[result]}")
# 4. sorunun cevabı
sonuc = 'negatiftir', 'pozitiftir.'
sayi = int(input('Sayi giriniz: '))
result = sayi>=0
print(f"4. sorunun cevabı: Girilen sayı {sonuc[result]}")
# 5. sorunun cevabı
email, parola = 'email@sadikturan.com', 'abc123'
kemail, kparola = input('Kontrol edilecek email adresini giriniz: '), input('Parolayı giriniz: ')
sonuc = 'Kullanıcı adı veya parola yanlış.','Kullanıcı adı veya parola yanlış.' ,'Kullanıcı adı ve parola doğru.'
result1 = email==kemail
result2 = parola == kparola
result = result1 + result2
print(f"5. sorunun cevabı: {sonuc[result]}")

