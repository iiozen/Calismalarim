x, y, z = 2, 5, 107

numbers = 1, 5, 7, 10, 6
# 1. sorunun cevabı
sayi1,sayi2 = input('1. sayıyı giriniz: '), input('2. sayıyı giriniz: ')
result = int(sayi1)*int(sayi2) - (x+y+z)
print(f"1. sorunun cevabı: {result}")
# 2. sorunun cevabı
result = y//x
print(f"2. sorunun cevabı: {result}")
# 3. sorunun cevabı
result = (x+y+z)%3
print(f"3. sorunun cevabı: {result}")
# 4. sorunun cevabı
result = y**x
print(f"4. sorunun cevabı: {result}")
# 5. sorunun cevabı
x, *y, z = numbers
result = z**3
print(f"5. sorunun cevabı: {result}")
# 6. sorunun cevabı
result = y[0]+y[1]+y[2]
print(f"6. sorunun cevabı: {result}")

print(y)


