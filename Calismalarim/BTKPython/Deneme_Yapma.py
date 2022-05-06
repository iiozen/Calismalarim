# # a = [1,2,3,4,5]
# # b = ['bir','iki','üç','dört','beş']
# # result = list(zip(a,b))
# # print(result)
# a = [1,2,3,4,5]
# result = list(map(lambda num: num%2==0, a))
# print(result)

# import random

# result = format(random.uniform(0,100),".3f")
# result = float(result)
# if result <= 25:
#     print(f"Gelen sayı: {result}\nBaşarılı.")
# else :
#     print(f"Gelen sayı: {result}\nBaşarısız.")




# while True:
#     try:
#         x= int(input('x: '))
#         y= int(input('y: '))
#         print(x/y)
#     except Exception as ex:
#         print('Hatalı giriş', ex)
#     else:
#         break
#     finally:
#         print('try except sonlandı.')

# file = open("newfile.txt","w",encoding='utf-8')

# file.close()
# def kareAlir(sayi=5):
#     sonuc = sayi**2
#     print(sonuc)
# kareAlir(5)

# import re
# str = "10 90 10 -10 +10 +85 -83 85 82 82"
# result = re.findall('[0-9]+[+-]',str)
# result = len(result)
# print(result)
# import re
# stri = ["10+", "+90+", "10", "-10", "+10" ,"+85-", "-83"," 85-" ,"82+" ,"82-"]
# list = []
# for str in stri:

#     result = re.findall(".[+|-]$",str)
    
#     print(result)
#     if len(result)>0:
#         list.append(result)
# print(len(list))
# import json
# name,yas = "Ali","18"
# with open("deneme.txt","r+",encoding="utf-8") as metin:
#     yazi = "{"+'"name":"{0}","yas":"{1}"'.format(name,yas)+"}"
#     metin.write(yazi)
#     metin.seek(0)
#     x = metin.readline()
#     print(x)
#     print(type(x))
#     metin.seek(0)
#     x = json.loads(x)
#     print(type(x))
#     print(x['name'],x['yas'])

# # import json
# # print(json.__file__)
# dene = [1,5,6,7,1,5,2,1,5]
# # dene = set(dene)
# # dene = list(dene)
# # print(dene,type(dene))

# output = set()
# for x in dene:
#     output.add(x)
# print(output)
# def student(sayi1,sayi2):
#     if sayi1 is 15:
#         sayi1 = 0
#     else:
#         sayi1 = sayi1
#     print(sayi1,sayi2)

# student(15,15)
# class dene:
#     def __init__(self,a,b,c,d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#     def don(self):
#         print(self.a,self.b,self.c,self.d)
#     def dener(self):

#         print(self.a,self.b,self.c,self.d)

# a = 1
# b = 2
# c = 3
# d = 4
# obj = dene(a,b,c,d)
# obj.a = 5
# obj.b = 6
# obj.c = 7
# obj.d = 8
# obj.don()
# # obj.a = 5
# # obj.b = 6
# # obj.c = 7
# # obj.d = 8
# obj.dener()

