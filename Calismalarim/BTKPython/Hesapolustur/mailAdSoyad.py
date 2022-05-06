import random
import string

lower_letters = string.ascii_lowercase

upper_letters = string.ascii_uppercase

name_num = random.randint(1,2)


lower_num1 = random.randint(4,8)
lower_num2 = random.randint(4,8)


li1,li2 = [],[]
for i in range(lower_num2):
    lower_letter2 = random.choice(lower_letters)
    li2.append(lower_letter2)
for i in range(lower_num1):
    lower_letter1 = random.choice(lower_letters)
    li1.append(lower_letter1)



ad = random.choice(upper_letters)
soyad = random.choice(upper_letters)
for letter in li1:
    ad = ad + letter
for letter in li2:
    soyad = soyad + letter
  
if name_num ==2:
    li3 = []
    lower_num3 = random.randint(4,8)
    for i in range(lower_num3):
        lower_letter3 = random.choice(lower_letters)
        li3.append(lower_letter3)
    ad2 = random.choice(upper_letters)
    for letter in li3:
        ad2 = ad2 + letter
    ad = ad + ' ' + ad2
    soyad = soyad
else:
    ad = ad
    soyad = soyad

