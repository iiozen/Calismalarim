from zekseni import Nokta
from tkinter import *
import time

def cizer(yn1,yn2):
    alan.create_line(yn1,yn2,arrow='last')


pencere  = Tk()
pencere.geometry('2000x1300')
alan = Canvas(pencere,width=2000,height=1300)
alan.pack()





nokta1 = [600,600,0]

nokta2 = [800,600,0]

nokta3 = [600,400,0]

nokta4 = [800,400,0]

nokta5 = [600,400,200]

nokta6 = [800,400,200]

nokta7 = [800,600,200]

nokta8 = [600,600,200]

# v12 = nokta1+nokta2
# v13 = nokta1+nokta3
# v18 = nokta1+nokta8
# v27 = nokta2+nokta7
# v24 = nokta2+nokta4
# v34 = nokta3+nokta4
# v35 = nokta3+nokta5
# v46 = nokta4+nokta6
# v67 = nokta6+nokta7
# v56 = nokta5+nokta6
# v78 = nokta7+nokta8
# v58 = nokta5+nokta8



v12 = Nokta(nokta1,nokta2)()
v13 = Nokta(nokta1,nokta3)()
v18 = Nokta(nokta1,nokta8)()
v27 = Nokta(nokta2,nokta7)()
v24 = Nokta(nokta2,nokta4)()
v34 = Nokta(nokta3,nokta4)()
v35 = Nokta(nokta3,nokta5)()
v46 = Nokta(nokta4,nokta6)()
v67 = Nokta(nokta6,nokta7)()
v56 = Nokta(nokta5,nokta6)()
v78 = Nokta(nokta7,nokta8)()
v58 = Nokta(nokta5,nokta8)()


Kupici = [
    v12[0]+v12[1],
    v13[0]+v13[1],
    v18[0]+v18[1],
    v27[0]+v27[1],
    v24[0]+v24[1],
    v34[0]+v34[1],
    v35[0]+v35[1],
    v46[0]+v46[1],
    v67[0]+v67[1],
    v56[0]+v56[1],
    v78[0]+v78[1],
    v58[0]+v58[1]
]
kupler=[]
kupler.append(Kupici)
for kup in kupler:
    for ic in kup:
        alan.create_line(ic,width=2)
    

# nokta3 = [600,400,0]
# nokta3 = [600,400,0]
# nokta3 = [600,400,0]

# for i in range(8):
#     z=0
#     if i ==0:
#         x=600
#         y=400
#     elif i == 1:
#         x=600
#         y=600
#     elif i<6:
#         y=400
#         x=400
#     elif x<8:
#         y=600
#         x=400
#     for j in range(200):

#         alan.delete(ALL)
#         nokta2 = [x,y,z]
#         yn1,yn2,vektor=Nokta(nokta1,nokta2)()
#         cizer(yn1,yn2)
#         pencere.update()
#         # if i%2==0:
#         #     z+=1
#         # else:
#         #     z-=1
#         z+=1
        # time.sleep(0.003)



pencere.mainloop()
