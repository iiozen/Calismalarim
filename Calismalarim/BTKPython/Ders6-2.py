sayilar = [1,3,5,7,9,12,19,21]
# 1. Soru cevabı
for sayi in sayilar:
    if sayi%3==0:
        print(f"{sayi}")
# 2. Soru cevabı
a=0
for sayi in sayilar:
    a +=sayi
print(f"sayilar listesinin toplamı: {a}")
# 3. Soru cevabı
for sayi in sayilar:
    if sayi%2==1:
        print(f"tek sayımız: {sayi}, karesi: {sayi**2}")
#####
sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']
# 4. Soru cevabı
a = 0
for sehir in sehirler:
    if len(sehir)<=5:
        print(f"en fazla 5 karakterli sehir: {sehir}")
########
urunler = [
    {'name': 'samsung S6', 'price':'3000'},
    {'name': 'samsung S7', 'price':'4000'},
    {'name': 'samsung S8', 'price':'5000'},
    {'name': 'samsung S9', 'price':'6000'},
    {'name': 'samsung S10', 'price':'7000'}
]
a=0
# 5. Soru cevabı
for fiyat in urunler:
    a+=float(fiyat['price'])
print(f"Ürünlerin toplam fiyatı: {a}")
# 6. Soru cevabı
for fiyat in urunler:
    if float(fiyat['price'])<=5000:
        print(f"Urun: {fiyat['name']}, fiyatı: {fiyat['price']}")

