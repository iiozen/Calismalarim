website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1. cevap
s = ' Hello World '
result = s.strip()
print(f"1. sorunun cevabı = {result}")

# 2. cevap
a= 'sadikturan'
result = website.find(a)
result= website[result:len(a)+result]
print(f"2. sorunun cevabı = {result}")

# 3. cevap
result = course.lower()
print(f"3. sorunun cevabı = {result}")

# 4. cevap
result = website.count('a')
print(f"4. sorunun cevabı = {result}")

# 5. cevap
result = website.startswith('www')
result2 = website.endswith('com')
print(f"5. sorunun cevabı = {result} , {result2}")

# 6. cevap
result = website.find('.com')
print(f"6. sorunun cevabı = {result}")

# 7. cevap
result = course.isalpha()
print(f"7. sorunun cevabı = {result}")

# 8. cevap
s = 'Contents'
result = s.center(50,'*')
print(f"8. sorunun cevabı = {result}")

# 9. cevap
result = course.replace(' ','-')
print(f"9. sorunun cevabı = {result}")

# 10. cevap
s = 'Hello World'
result = s.replace('World','There')
print(f"10. sorunun cevabı = {result}")

# 11.cevap
result = course.split()
print(f"11-1. sorunun cevabı = {result}")
result = course.replace(' ','')
print(f"11-2. sorunun cevabı = {result}")








