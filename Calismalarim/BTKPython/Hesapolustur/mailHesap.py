import random
import string
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase




lower_num = random.randint(7,15)
upper_num = random.randint(1,5)

li1,li2 = [],[]

for i in range(lower_num):
    lower_letter = random.choice(lower_letters)
    li1.append(lower_letter)
for i in range(upper_num):
    upper_letter = random.choice(upper_letters)
    li2.append(upper_letter)
lisum = li1+li2
mail_letters = []
for i in range(upper_num+lower_num):
    l = random.choice(lisum)
    lisum.remove(l)
    mail_letters.append(l)
mail = ''
for letter in mail_letters:
    mail = mail + letter


