# def topla(*degerler):
#     print(degerler)
#     return sum(degerler)

# print(topla(9,51,5,6,1,4,8,41,31,19,1,3))
def displayUser(**sozluk):
    for key, value in sozluk.items():
        print('{} is {}'.format(key,value))



displayUser (name = 'Çınar', age = 2, city = 'istanbul')
displayUser (name = 'Ada', age = 12, city = 'kocaeli',phone = '123123')
displayUser (name = 'Yiğit', age = 14, city = 'ankara', phone = '21321', email = 'a2p3oa2@hotmail.com')


