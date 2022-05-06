from robot import Robot

robot = Robot()
print('Konuşmadan çıkmak için 0 giriniz.')
paragraf=''
while paragraf!='0':
    if paragraf!='':
        robot.KonuBul(paragraf)
    paragraf = input('Metin giriniz: ')
