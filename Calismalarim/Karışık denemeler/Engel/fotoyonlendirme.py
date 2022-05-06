from datetime import  datetime
from tkinter import *
import math
import time
import numpy as np
from PIL import ImageTk, Image

class Cizim:
    def __init__(self):
        self.pencere = Tk()
        # self.pencere.geometry('1600x1200')
        self.pencere.attributes('-fullscreen',True)
        self.alan = Canvas(self.pencere,highlightthickness=0,bg='gray')
        self.label1=Label(self.alan)
        self.konum=[0,0]  
        self.adim = 10
        self.imaga1 = Image.open("blt.png")
        self.image1boyut=[50,50]
        self.image1 = self.imaga1.resize((self.image1boyut[0],self.image1boyut[1]), Image.ANTIALIAS)                
        self.test = ImageTk.PhotoImage(self.image1)
        self.duvar1boyut=[]
        self.duvar1koordinat=[]
        self.label1 = Label(master=self.alan,image=self.test)
        self.label1.image = self.test

        # self.duvar1r = Image.open('dvr.png')
        # self.duvar1boyut= [150,300]
        # self.duvar1 = self.duvar1r.resize((self.duvar1boyut[0],self.duvar1boyut[1]),Image.ANTIALIAS)
        # self.dtest1 = ImageTk.PhotoImage(self.duvar1)
        # self.duvar1l = Label(master = self.alan, image=self.dtest1)
        # self.duvar1l.image=self.dtest1
        # self.duvar1koordinat = [1500,720]
        # self.duvar1l.place(x=self.duvar1koordinat[0],y=self.duvar1koordinat[1])

        self.Duvarci([1500,720],[150,300])
        # self.Duvarci([350,720],[25,50])
        # self.Duvarci([750,1200],[75,30])
        # self.Duvarci([2000,50],[43,99])

        self.sag = True
        self.sol = True
        self.yukari = True
        self.asagi = True

        self.basladi=0
        self.yukariasagi=True
        self.sonislem ='bos'


        self.Updater()

        self.alan.focus_set()
        self.alan.bind('<KeyPress>',self.Basilan)
        self.alan.bind('<KeyRelease>',self.Basilan)
        self.alan.bind('<Button-1>',self.Mouseagit)
        self.alan.pack(fill=BOTH, expand=True)
        self.flscren = Button(self.alan,text='Fullscreen',command=self.Flscrn)
        self.flscren.pack()

      


        self.geni = self.alan.winfo_width()
        self.yuks = self.alan.winfo_height()
    
        

        self.pencere.mainloop()



    def Duvarci(self,koordinat,boyut):
        self.duvar1r = Image.open('dvr.png')
        # self.duvar1boyut= boyut
        self.duvar1boyut.append(boyut)
        # self.duvar1 = self.duvar1r.resize((self.duvar1boyut[0],self.duvar1boyut[1]),Image.ANTIALIAS)
        self.duvar1 = self.duvar1r.resize((boyut[0],boyut[1]),Image.ANTIALIAS)
        self.dtest1 = ImageTk.PhotoImage(self.duvar1)
        self.duvar1l = Label(master = self.alan, image=self.dtest1)
        self.duvar1l.image=self.dtest1
        # self.duvar1koordinat = koordinat
        self.duvar1koordinat.append(koordinat)
        # self.duvar1l.place(x=self.duvar1koordinat[0],y=self.duvar1koordinat[1])
        self.duvar1l.place(x=koordinat[0],y=koordinat[1])

    def Basilan(self,event):
        if event.char=='w' or event.char=='W':
            self.Yukari()
        elif event.char=='s' or event.char=='S':
            self.Asagi()
        elif event.char=='d' or event.char=='D':
            self.Sag()
        elif event.char=='a' or event.char=='A':
            self.Sol()                        



    def Mouseagit(self,event):
        self.gidilecekyer = [event.x,event.y]
        self.baslangickonum = self.konum
        self.Gidis()



    def Duvar1KonumBakma(self):
        for sss,duvar in enumerate(self.duvar1koordinat):
            xmax, xmin = duvar[0]+self.duvar1boyut[sss][0],duvar[0]
            ymax, ymin = duvar[1]+self.duvar1boyut[sss][1],duvar[1]
            x,y =self.konum
            if abs(xmax-x)<abs(xmin-x):
                konumumx = 'sag'
            else:
                konumumx = 'sol'

            if abs(ymax-y)<abs(ymin-y):
                konumumy = 'asagi'
            else:
                konumumy = 'yukari'

            if konumumx =='sag':
                if abs(x-xmax)>=self.adim:
                    self.sol=True
                else:
                    if y-ymax>0 or ymin-y-self.image1boyut[1]>0:
                        self.sol = True
                    else:
                        self.sol = False
            elif konumumx =='sol':
                if abs(x+self.image1boyut[0]-xmin)>=self.adim:
                    self.sag = True
                else:
                    if y-ymax>0 or ymin-y-self.image1boyut[1]>0:
                        self.sag = True
                    else:
                        self.sag = False

            if konumumy =='asagi':
                if abs(y-ymax)>=self.adim:
                    self.yukari=True
                else:
                    if x-xmax>0 or xmin-x-self.image1boyut[0]>0:
                        self.yukari=True
                    else:
                        self.yukari = False
            elif konumumy == 'yukari':
                if abs(y+self.image1boyut[1]-ymin)>=self.adim:
                    self.asagi = True
                else:
                    if x-xmax>0 or xmin-x-self.image1boyut[0]>0:
                        self.asagi = True
                    else:
                        self.asagi = False




    def ImgAlanKoord(self):
        x,y = self.konum
        x1,y1 = x,y
        x2,y2 = x+self.image1boyut[0],y
        x3,y3 = x,y+self.image1boyut[1]
        x4,y4 = x+self.image1boyut[0],y+self.image1boyut[1]
        
        xvaris,yvaris = self.gidilecekyer
        # print(x1,x2,y1,y3)
        if xvaris>=x1 and xvaris<=x2 and yvaris>=y1 and yvaris<=y3:
            return True
        
        # elif yvaris>=y1 and yvaris<=y2:
        #     return 1
        else:
            return False


    def Gidis(self):

        mesafex = self.gidilecekyer[0]-self.konum[0]
        mesafey = self.gidilecekyer[1]-self.konum[1]
        self.Duvar1KonumBakma()
        imgdonen = self.ImgAlanKoord()
        sagsol = False
        
        if abs(mesafex)<=10 or abs(mesafey)<=10:
            aki =True
        else:
            aki=False
            # if imgdonen:
        if imgdonen and aki:
            pass


        # if abs(mesafex)>10 or abs(mesafey)>10:
        else:
            if abs(mesafex)>= 10 and self.yukariasagi:
                    
                if mesafex<0 and self.sol:
                    self.Sol()
                    self.sonislem='bos'
                elif mesafex>0 and self.sag:
                    self.Sag()
                    self.sonislem='bos'
                else:
                    if self.sonislem !='bos':
                        if self.sonislem=='yukari':
                            self.Yukari()
                        elif self.sonislem=='asagi':
                            self.Asagi()
                    else:
                        if mesafey<0:
                            self.Yukari()
                            self.sonislem='yukari'
                        elif mesafey>0:
                            self.sonislem='asagi'
                            self.Asagi()
                    # if abs(mesafey)>=10 and sagsol == False:
                    #     if mesafey<0:
                    #         self.Yukari()
                    #     elif mesafey>0:
                    #         self.Asagi()
            elif abs(mesafey)>=10:
                
                if mesafey<0 and self.yukari:
                    self.yukariasagi=True
                    self.sonislem='bos'
                    self.Yukari()
                elif mesafey>0 and self.asagi:
                    self.yukariasagi=True
                    self.Asagi()
                    self.sonislem='bos'
                else:
                    self.yukariasagi=False
                    if self.sonislem !='bos':
                        if self.sonislem=='sol':
                            self.Sol()
                        elif self.sonislem=='sag':
                            self.Sag()
                    else:
                        if mesafex<0:
                            self.Sol()
                            self.sonislem='sol'
                        elif mesafex>0:
                            self.sonislem='sag'
                            self.Sag()



            self.alan.after(20,self.Gidis)
        # else:
        #     pass
        #     # print("Hedefe Ulaşıldı")






    # def Gidis(self):

    #     mesafex = self.gidilecekyer[0]-self.konum[0]
    #     mesafey = self.gidilecekyer[1]-self.konum[1]
    #     self.Duvar1KonumBakma()
    #     sagsol = False
    #     if abs(mesafex)>10 or abs(mesafey)>10:
    #         print(self.yukari,self.asagi,self.yukariasagi)
    #         if abs(mesafex)>=abs(mesafey):
    #             if abs(mesafex)>= 10 and self.yukariasagi:
                        
    #                 if mesafex<0 and self.sol:
    #                     self.Sol()
    #                 elif mesafex>0 and self.sag:
    #                     self.Sag()
    #                 else:
    #                     self.Yukari()
    #                     # if abs(mesafey)>=10 and sagsol == False:
    #                     #     if mesafey<0:
    #                     #         self.Yukari()
    #                     #     elif mesafey>0:
    #                     #         self.Asagi()
    #             elif abs(mesafey)>=10:
                    
    #                 if mesafey<0 and self.yukari:
    #                     print("yukaricalisir")
    #                     self.yukariasagi=True
    #                     self.Yukari()
    #                 elif mesafey>0 and self.asagi:
    #                     print("asagicalisir")
    #                     self.yukariasagi=True
    #                     self.Asagi()
    #                 else:
    #                     print("asagi yukari calismaz")
    #                     self.yukariasagi=False
    #                     self.Sag()
    #         else:
    #             if abs(mesafey)>=10:
                   
    #                 if mesafey<0 and self.yukari:
    #                     print("yukaricalisir")
    #                     self.yukariasagi=True
    #                     self.Yukari()
    #                 elif mesafey>0 and self.asagi:
    #                     print("asagicalisir")
    #                     self.yukariasagi=True
    #                     self.Asagi()
    #                 else:
    #                     print("asagi yukari calismaz")
    #                     self.yukariasagi=False
    #                     self.Sag()
    #             elif abs(mesafex)>= 10 and self.yukariasagi:
                    
    #                 if mesafex<0 and self.sol:
    #                     self.Sol()
    #                 elif mesafex>0 and self.sag:
    #                     self.Sag()
    #                 else:
    #                     self.Yukari()

    #         self.alan.after(20,self.Gidis)
    #     else:
    #         print("Hedefe Ulaşıldı")




    def Yukari(self):
        self.Baslat()
        self.ImgYonlendir(90)
        self.KoorImgYukle([0,-self.adim])



    def Asagi(self):
        self.Baslat()
        self.ImgYonlendir(270)
        self.KoorImgYukle([0,self.adim])


    def Sag(self):
        self.Baslat()
        self.ImgYonlendir(0)
        self.KoorImgYukle([self.adim,0])


    def Sol(self):
        self.Baslat()
        self.ImgYonlendir(180)
        self.KoorImgYukle([-self.adim,0])    


















        
    def Baslat(self):
        self.basladi=1

    def Updater(self):
        geni = self.alan.winfo_width()
        yuks = self.alan.winfo_height()
        if self.basladi!=1:
            self.konum=[geni/2,yuks/2]
            self.KoorImgYukle()
        else:
            self.KoorImgYukle([self.konum])

        self.alan.after(20,self.Updater)

    def ImgYonlendir(self,yonlendirme=0):
 
        img1 = self.imaga1.resize((50,50),Image.ANTIALIAS)
        img1 = img1.rotate(yonlendirme)
        self.test = ImageTk.PhotoImage(img1)

        # self.label1 = Label(master=self.alan,image=self.test)
        self.label1.configure(image=self.test)
        self.label1.image = self.test
        # self.test = ImageTk.PhotoImage(self.image1)

        # self.label1 = Label(master=self.alan,image=self.test)
        # self.label1.image = self.test


    def KoorImgYukle(self,islem=[0,0]):
        # try:
        #     self.label1.destroy()
        # except:
        #     pass
        # self.label1.destroy()
        
        if islem !=[0,0]:
            self.konum = [self.konum[0]+islem[0],self.konum[1]+islem[1]]
        
        x,y = self.konum
        
        self.label1.place_configure(x=x,y=y)








    def Flscrn(self):
        self.pencere.attributes('-fullscreen',True)
        self.flscren.destroy()
        self.flscren = Button(self.alan,text='Windowed',command=self.Wndwd)
        self.flscren.pack()

    def Wndwd(self):
        self.pencere.attributes('-fullscreen',False)
        self.flscren.destroy()
        self.flscren = Button(self.alan,text='Fullscreen',command=self.Flscrn)
        self.flscren.pack()


Cizim()