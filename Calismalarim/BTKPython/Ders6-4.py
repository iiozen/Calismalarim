sayilar = [1,3,5,7,9,12,19,21]
# 1. Sorunun cevabı
t=0
while t < len(sayilar):
    print(sayilar[t])
    t+=1
# 2. Sorunun cevabı
sayib , sayis = int(input('baslangic sayisi: ')), int(input('bitis sayisi: '))
while sayib <= sayis:
    if sayib%2==1:
        print(sayib)
    sayib+=1
# 3. Sorunun cevabı
t = 100
while t >=1:
    print(t)
    t-=1
# 4. Sorunun cevabı
numbers = []
t = 0
while t<5:
    a = input('sayi: ')
    numbers.append(a)
    t+=1
numbers.sort()
print(numbers)
# 5. Sorunun cevabı
name = []
price = []
adet = int(input('Urun sayısını giriniz: '))
geri = adet
while geri>0:
    nme, prc = input('Urun adını giriniz: '), input('Fiyatı: ')
    name.append(nme)
    price.append(prc)
    geri-=1
urunler = {'name':name,'price':price}
sayar = 0
while adet > 0:
    print(f"{urunler['name'][sayar]}, {urunler['price'][sayar]}")
    adet-=1
    sayar+=1