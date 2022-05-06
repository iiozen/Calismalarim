website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

c1= len(course)
print(f"course karakter dizisinde {c1} tane karakter bulunmaktadır. ")

c2 = website[7:10]
print(c2)

c3 = website[len(website)-3:len(website)]
print(c3)

c41=course[:15]
c42=course[-15:]
print("4. sorunun cevabı = ",c41,c42)

c5 = course[::-1]
print(f"5. sorunun cevabı = {c5}")

name, surname, age, job = 'Bora', 'Yılmaz' , 32, 'mühendis'

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

print("7. soruyu yapamadım")

c8="abc"
c8 = c8*3
print(c8)

