names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1. cevap
names.append('Cenk')
print(f"1. sorunun cevabı = {names}")
# 2. cevap
names.insert(0,"Sena")
print(f"2. sorunun cevabı = {names}")
# 3. cevap
names.remove("Deniz")
print(f"3. sorunun cevabı = {names}")
# 4. cevap
names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
indexi = names.index("Deniz")
print(f"4. sorunun cevabı = {indexi}")
# 5. cevap
indexi = names.index("Ali")
print(f"5. sorunun cevabı = {indexi}")
result = 'Ali' in names
print(f"5. sorunun 2. cevabı = {result}")

# 6. cevap
names.reverse()
print(f"6. sorunun cevabı = {names}")
# 7. cevap
names.sort()
print(f"7. sorunun cevabı = {names}")
# 8. cevap
years.sort()
print(f"8. sorunun cevabı = {years}")
# 9. cevap
str = "Chevrolet,Dacia"
result = str.split(',')
print(f"9. sorunun cevabı = {result}")
# 10. cevap
enb=max(years)
enk= min(years)
print(f"10. sorunun cevabı = en küçük: {enk}, en büyük: {enb}")
# 11. cevap
result = years.count(1998)
print(f"11. sorunun cevabı = {result}")
# 12. cevap
years.clear()
print(f"9. sorunun cevabı = {years}")
# 13. cevap
result = [input('1. markayı giriniz:'),input('2. markayı giriniz:'),input('3. markayı giriniz:')]
print(f"10. sorunun cevabı = {result}")











