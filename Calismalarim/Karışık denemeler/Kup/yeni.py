from tkinter import *
import math

from zekseni import Nokta
import numpy as np
from tkinter import simpledialog,dialog
##y*cos(10)-sin(10)*(x*sin(45)/2+y*sin(45)/2)=y
##sin(10)*y+cos(10)*(x*sin(45)/2+y*sin(45)/2)

class Hareketli:
    def __init__(self):
        self.pencere  = Tk()
        self.pencere.geometry('2000x1300')
        self.alan = Canvas(self.pencere,width=2000,height=1300)
        self.yon = ''
        # butonY = Button(self.pencere,text='Yukarı',command=lambda:self.HareketHali(yon='yukarı'))
        # butonY.pack(side='top')
        # butonA = Button(self.pencere,text='Aşağı',command=lambda:self.HareketHali(yon='aşağı'))
        # butonA.pack(side='top')
        # butonY = Button(self.pencere,text='Sağ',command=lambda:self.HareketHali(yon='sağ'))
        # butonY.pack(side='right')
        # butonA = Button(self.pencere,text='Sol',command=lambda:self.HareketHali(yon='sol'))
        # butonA.pack(side='right')
        # butonY = Button(self.pencere,text='İleri',command=lambda:self.HareketHali(yon='ileri'))
        # butonY.pack(side='left')
        # butonA = Button(self.pencere,text='Geri',command=lambda:self.HareketHali(yon='geri'))
        # butonA.pack(side='left')
        # butonY = Button(self.pencere,text='Saat Yönünde Döndür',command=lambda:self.HareketHali(yon='saatyönü'))
        # butonY.pack(side='top')
        # butonA = Button(self.pencere,text='Saatin Tersine Döndür',command=lambda:self.HareketHali(yon='saattersyönü'))
        # butonA.pack(side='top')
        # butonA = Button(self.pencere,text='X Ekseninde Döndür',command=lambda:self.HareketHali(yon='xeksenidondur'))
        # butonA.pack(side='top')
        # butonA = Button(self.pencere,text='X Ekseninde Ters Döndür',command=lambda:self.HareketHali(yon='xters'))
        # butonA.pack(side='top')
        # butonA = Button(self.pencere,text='X 3D Döndür',command=lambda:self.HareketHali(yon='x3d'))
        # butonA.pack(side='top')

        butonA = Button(self.pencere,text='X Ekseninde Döndür',command=lambda:self.HareketHali(yon='xeksenidondur'))
        butonA.pack(side='top')
        butonA = Button(self.pencere,text='X Ekseninde Ters Döndür',command=lambda:self.HareketHali(yon='xters'))
        butonA.pack(side='top')

        butonA = Button(self.pencere,text='Y Ekseninde Döndür',command=lambda:self.HareketHali(yon='yeksenidondur'))
        butonA.pack(side='right')
        butonA = Button(self.pencere,text='Y Ekseninde Ters Döndür',command=lambda:self.HareketHali(yon='yters'))
        butonA.pack(side='right')

        butonA = Button(self.pencere,text='Z Ekseninde Döndür',command=lambda:self.HareketHali(yon='zeksenidondur'))
        butonA.pack(side='left')
        butonA = Button(self.pencere,text='Z Ekseninde Ters Döndür',command=lambda:self.HareketHali(yon='zters'))
        butonA.pack(side='left')
        butonA=Button(self.pencere,text='Küp Oluştur',command=self.KupOlusturucu)
        butonA.pack(side='top')
        butonA=Button(self.pencere,text='KapaliDevreci',command=self.KupKapaliDevre)
        butonA.pack(side='top')

        butonA=Button(self.pencere,text='Nokta Ayırıcı',command=self.NoktaAyirici)
        butonA.pack(side='top')

        self.birakildi = True
        self.birakildi2 = True
        self.birakildi3 = True
        self.grafikler = {
            'küpler':{},
            'daireler':{},
            'diğer':{}
        }
        

        self.alan.bind('<Button-1>',self.Basildi)
        self.alan.bind('<Motion>',self.HareketHalinde)
        self.alan.bind('<ButtonRelease-1>',self.Birakildi)

        self.alan.bind('<Button-3>',self.Basildi2)
        self.alan.bind('<Motion>',self.HareketHalinde)
        self.alan.bind('<ButtonRelease-3>',self.Birakildi2)


        self.alan.bind('<Button-2>',self.Basildi3)
        self.alan.bind('<Motion>',self.HareketHalinde)

        self.alan.bind('<ButtonRelease-2>',self.Birakildi3)


        self.alan.pack()
        self.ssaci = 0
        self.kupler=[]
        self.kupxyu=[]
        self.kupler2 = []
        self.kupler3d = []
        self.ortanoktalar = []
        self.orta3dortanoktalar=[]
        self.xaci = 0
        self.KupOlustur(600,400,300)

        
        self.pencere.mainloop()

    def KupOlusturucu(self):
        # simpledialog.askfloat('Küpün değerlerini giriniz',prompt= ['x','y','z'],t)
        # self.pencere.wm_attributes('-disabled',True)
        kutucu = Toplevel(self.pencere)
        kutucu.geometry('400x800')
        kutucu.transient(self.pencere)

        # answer = simpledialog.askfloat('title','Nedir bu')
        # B = simpledialog.Dialog(self.alan,'nebu')
        # B.body(self.alan)
        # l = Label(B,text='Text')
        # l.pack(side=LEFT)

        # girdi = simpledialog.SimpleDialog(master=d,title='Title',buttons=['onay','iptal'],text='yazi',default=0,cancel=1)
        # Label(girdi,text='Text yazisi').pack(side=LEFT)

        
        # answer = simpledialog.askstring("Input", "What is your first name?",
        #                                 parent=self.pencere)
        # if answer is not None:
        #     print("Your first name is ", answer)
        # else:
        #     print("You don't have a first name?")




        # kupself.pencere = Canvas(self.alan,background='red',bg='red',width=600,height=400)
        # L1 = Label(kupself.pencere,text='Oluşacağı x noktası')
        # L1.pack(side=LEFT)
        # E1 = Entry(kupself.pencere,bd=5)
        # E1.pack(side = RIGHT)
        # L2 = Label(kupself.pencere,text='Oluşacağı y noktası')
        # L2.pack(side=LEFT)
        # E2 = Entry(kupself.pencere,bd=5)
        # E2.pack(side = RIGHT)
        # L3 = Label(kupself.pencere,text='Oluşacak küpün kenar uzunluğu')
        # L3.pack(side=LEFT,after=L2)
        # E3 = Entry(kupself.pencere,bd=5)
        # E3.pack(side = RIGHT)
        # But = Button(kupself.pencere,text='Oluştur',command=lambda:[self.PenecereSil(kupself.pencere)])
        # # But = Button(kupself.pencere,text='Oluştur',command=lambda:[self.KupOlustur(E1,E2,E3),self.PenecereSil(kupself.pencere)])
        # But.pack(side='bottom')
        # kupself.pencere.pack()


    def PenecereSil(self,pencere):
        self.pencere.destroy()

    def Birakildi(self,event):
        self.birakildi = True
    def Basildi(self,event):
        self.birakildi = False
        self.eskiy = event.y
        self.eskix = event.x
    def Birakildi2(self,event):
        self.birakildi2 = True
    def Basildi2(self,event):
        self.birakildi2 = False
        self.eskix2 = event.x
        self.eskiy2 = event.y
    def Basildi3(self,event):
        self.birakildi3 = False
        self.eskix3 = event.x
        self.eskiy3 = event.y
    def Birakildi3(self,event):
        self.birakildi3 = True
    def HareketHalinde(self,event):
        if not self.birakildi:
            if event.y>self.eskiy:
                self.HareketHali(yon='xters')
                self.eskiy = event.y
            elif event.y<self.eskiy:
                self.HareketHali(yon='xeksenidondur')
                self.eskiy = event.y
            if event.x>self.eskix:
                self.HareketHali(yon='yeksenidondur')
                self.eskix = event.x
            elif event.x<self.eskix:
                self.HareketHali(yon='yters')
                self.eskix = event.x
        # # if not self.birakildi2:
        # #     if event.y>self.eskiy2 or event.x<self.eskix2:
        # #         self.HareketHali(yon='zeksenidondur')
        # #         self.eskix2 = event.y
        # #     elif event.y<self.eskiy2 or event.x>self.eskix2:
        # #         self.HareketHali(yon='zters')
        # #         self.eskix2 = event.y


        # if not self.birakildi2:
        #     if event.y>self.eskiy2:
        #         self.SaatYonu(aci=0.5)
        #         self.eskiy2 = event.y
        #     elif event.y<self.eskiy2:
        #         self.SaatYonu(aci=-0.5)
        #         self.eskiy2 = event.y



        if not self.birakildi2:
            if event.y>self.eskiy2:
                self.HareketHali(yon='zeksenidondur')
                self.eskiy2 = event.y
            elif event.y<self.eskiy2:
                self.HareketHali(yon='zters')
                self.eskiy2 = event.y

        if not self.birakildi3:
            yyon = event.y-self.eskiy3
            xyon = event.x - self.eskix3
            self.Kaydir(yyon=yyon,xyon=xyon)
            self.eskix3=event.x
            self.eskiy3=event.y

            # if event.y>self.eskiy3:
            #     self.Kaydir(yyon=2)
            #     self.eskiy3=event.y
            # elif event.y<self.eskiy3:
            #     self.Kaydir(yyon=-2)
            #     self.eskiy3=event.y
            # if event.x>self.eskix3:
            #     self.Kaydir(xyon=2)
            #     self.eskix3=event.x
            # elif event.x<self.eskix3:
            #     self.Kaydir(xyon=-2)
            #     self.eskix3 = event.x



    def KupOlustur(self,x,y,uzunluk):
        sira = len(self.grafikler['küpler'])
        self.nokta1 = [x,y,0]
        self.nokta3 = [self.nokta1[0],self.nokta1[1]+uzunluk,0]
        self.nokta2 = [self.nokta1[0]+uzunluk,self.nokta1[1],0]
        self.nokta4 = [self.nokta2[0],self.nokta2[1]+uzunluk,0]
        self.nokta5 = [self.nokta3[0],self.nokta3[1],uzunluk]
        self.nokta6 = [self.nokta4[0],self.nokta4[1],uzunluk]
        self.nokta7 = [self.nokta2[0],self.nokta2[1],uzunluk]
        self.nokta8 = [self.nokta1[0],self.nokta1[1],uzunluk]

        v12 = Nokta(self.nokta1,self.nokta2)()
        v13 = Nokta(self.nokta1,self.nokta3)()
        v18 = Nokta(self.nokta1,self.nokta8)()
        v27 = Nokta(self.nokta2,self.nokta7)()
        v24 = Nokta(self.nokta2,self.nokta4)()
        v34 = Nokta(self.nokta3,self.nokta4)()
        v35 = Nokta(self.nokta3,self.nokta5)()
        v46 = Nokta(self.nokta4,self.nokta6)()
        v67 = Nokta(self.nokta6,self.nokta7)()
        v56 = Nokta(self.nokta5,self.nokta6)()
        v78 = Nokta(self.nokta7,self.nokta8)()
        v58 = Nokta(self.nokta5,self.nokta8)()

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
        d12 = [self.nokta1,self.nokta2]
        d13 = [self.nokta1,self.nokta3]
        d18 = [self.nokta1,self.nokta8]
        d27 = [self.nokta2,self.nokta7]
        d24 = [self.nokta2,self.nokta4]
        d34 = [self.nokta3,self.nokta4]
        d35 = [self.nokta3,self.nokta5]
        d46 = [self.nokta4,self.nokta6]
        d67 = [self.nokta6,self.nokta7]
        d56 = [self.nokta5,self.nokta6]
        d78 = [self.nokta7,self.nokta8]
        d58 = [self.nokta5,self.nokta8]
        Kupici3D = [
            d12,
            d13,
            d18,
            d27,
            d24,
            d34,
            d35,
            d46,
            d67,
            d56,
            d78,
            d58
        ]
        self.kupler3d.append(Kupici3D)
        self.kupler2.append(Kupici)

        # ortax = (v12[0][0]+v67[0][0])/2
        # ortay = (v12[0][1]+v67[0][1])/2

        ortax = (d12[0][0]+d67[0][0])/2
        ortay = (d12[0][1]+d67[0][1])/2
        ortaz = (d12[0][2]+d67[0][2])/2

        self.ortax = ortax
        self.ortay = ortay
        self.ortaz = ortaz
        self.orta3dortanoktalar.append([ortax,ortay,ortaz])
        # ortaci =[ [0,0,0] , [ortax,ortay,ortaz] ]
        # ortalarim = Nokta(ortaci[0],ortaci[1])()
        # self.ortanoktalar.append([ortalarim[1][0],ortalarim[1][1]])
        # self.ortanoktalar.append([ortalarim[1][0],ortalarim[1][1]])

        # ilerisi = [ortalarim[1][0]+30,ortalarim[1][1]+30]
        # self.alan.create_oval(ortalarim[1],ilerisi)
        sira = 'küp%i' % (sira+1)
        self.grafikler['küpler'][sira] = {
            '3dnoktalar':Kupici3D,
            '2dnoktalar':Kupici,
            'ortanoktalar':[ortax,ortay,ortaz],
            'kapaliDevreler':{}
        }
        self.KupCizer2()



    def KupKapaliDevre(self):
        kupsayisi = len(self.grafikler['küpler'])
        for i in range(kupsayisi):
            kup = 'küp%i'%(i+1)
            self.grafikler
        # for kup in self.grafikler['küpler']:
        #     if len(kup['kapaliDevreler'])==0:
        #         ## İLKKEZ KAPALI DEVRELER OLUŞTURULACAK
        #         pass
            # else:
            for ucdbasnokta,ucdsonnokta in kup['3dnoktalar']:
                vektorsayi = 1
                for ucddevambasnokta,ucddevamsonnokta in kup['3dnoktalar']:
                    if vektorsayi==1 and ucdbasnokta==ucddevambasnokta:
                        pass
                    else:

                        vektorsayi+=1





    def NoktaAyirici(self):
        for kup in range(len(self.grafikler['küpler'])):
            ci = 'küp%i'%(kup+1)
            ucdnoktalar = self.grafikler['küpler'][ci]['3dnoktalar']
            noktalar = {}
            # print(ucdnoktalar)
            nk = 1
            for cizgi in ucdnoktalar:
                n0 = cizgi[0]
                n1 = cizgi[1]
                # self.grafikler['küpler'][ci]['']
                for i in noktalar.values():
                    print(list(noktalar.values()).index([900,400,0]))
                    # list.
                noktaci = 'nokta%i'%(nk)
                noktalar[noktaci] = n0
                nk+=1
                # if noktalar.values.index(n0)==-1:
                #     noktaci = 'nokta%i'%(nk)
                #     noktalar[noktaci] = n0
                #     nk+=1
                # if noktalar.index(n1)==-1:
                #     noktaci = 'nokta%i'%(nk)
                #     noktalar[noktaci] = n0
                #     nk+=1
        print(noktalar)

    def KupCizer2(self):
        araliklar = []
        for kup in self.kupler3d:
            for ic in kup:
                xmin = min([ic[0][0],ic[1][0]])
                xmax = max([ic[0][0],ic[1][0]])
                ymin = min([ic[0][1],ic[1][1]])
                ymax = max([ic[0][1],ic[1][1]])
                zmin = min([ic[0][2],ic[1][0]])
                zmax = max([ic[0][2],ic[1][2]])
                araliklar.append([[xmin,xmax],[ymin,ymax],[zmin,zmax]])

        for kup in self.kupler2:
            for ic in kup:
                # print(ic)
                pass
        for kup in self.kupler2:
            for ic in kup:
                self.alan.create_line(ic,width=0.01)


    # def SaatYonu(self,aci):
    #     self.alan.delete(ALL)
    #     donmematrisi = np.mat(np.array([
    #         [math.cos(math.radians(aci)),-math.sin(math.radians(aci))],
    #         [math.sin(math.radians(aci)),math.cos(math.radians(aci))]
    #         # [0,0,1]
    #     ]))

    #     hebele = 0

    #     for kup in self.kupler2:
    #         kup2 = self.kupler3d[hebele]
    #         yenikup = []
    #         yeni3dkup = []
    #         zehir = 0
    #         ortax,ortay,ortaz = self.orta3dortanoktalar[hebele]
    #         for ic in kup:
    #             ic2 = kup2[zehir]
    #             xb = ic2[0][0]
    #             yb = ic2[0][1]
    #             zb = ic2[0][2]
    #             xs = ic2[1][0]
    #             ys = ic2[1][1]
    #             zs = ic2[1][2]

    #             # xyzb = np.array([
    #             #     [xb],
    #             #     [yb],
    #             #     [zb]
    #             # ])

    #             # xyzs = np.array([
    #             #     [xs],
    #             #     [ys],
    #             #     [zs]
    #             # ])




    #             xyzb = np.array([
    #                 [ortax-xb],
    #                 [ortay-yb]
    #                 # [ortaz-zb]
    #             ])

    #             xyzs = np.array([
    #                 [ortax-xs],
    #                 [ortay-ys]
    #                 # [ortaz-zs]
    #             ])


    #             sonucmatrisib = donmematrisi * xyzb
    #             sonucmatrisis = donmematrisi * xyzs

    #             yxb,yyb = sonucmatrisib
    #             yxs,yys = sonucmatrisis

    #             yxb,yyb,yzb = float(yxb)+ortax,float(yyb)+ortay,float(zb)
    #             yxs,yys,yzs = float(yxs)+ortax,float(yys)+ortay,float(zs)
    #             # yxb= xb*math.cos(math.radians(xaci))-yb*math.sin(math.radians(xaci))
    #             # yyb= xb*math.sin(math.radians(xaci))+yb*math.cos(math.radians(xaci))
    #             # yzb = zb
    #             # yxs= xs*math.cos(math.radians(xaci))-ys*math.sin(math.radians(xaci))
    #             # yys= xs*math.sin(math.radians(xaci))+ys*math.cos(math.radians(xaci))
    #             # yzs = zs


    #             yeni3dkup.append([[yxb,yyb,yzb],[yxs,yys,yzs]])
    #             nk1,nk2 = yeni3dkup[zehir]
    #             yenikupe = Nokta(nk1,nk2)()
    #             yenikup.append(yenikupe[0]+yenikupe[1])
    #             # if zehir == 0:
    #             #     nokta1 = [ic2[0][0],ic2[0][1],ic2[0][2]]
    #             # if zehir == 8:
    #             #     nokta6 = [ic2[0][0],ic2[0][1],ic2[0][2]]
    #             zehir+=1
    #         # self.ortanoktalar[hebele] = [yeniortax,yeniortay]
    #         nokta1 = yeni3dkup[0][0]
    #         nokta6 = yeni3dkup[8][0]
    #         yeniortax, yeniortay,yeniortaz = (nokta1[0]+nokta6[0])/2,(nokta1[1]+nokta6[1])/2,(nokta1[2]+nokta6[2])/2

    #         self.kupler2[hebele] = yenikup
    #         self.kupler3d[hebele] = yeni3dkup
    #         self.orta3dortanoktalar[hebele] = [yeniortax,yeniortay,yeniortaz]
    #         hebele+=1
    #     self.KupCizer2()

    def Dondurme(self,xaci=0,yaci=0,zaci=0):
        matrisx =np.mat(np.array([
            [1,0,0],
            [0,math.cos(math.radians(xaci)),-math.sin(math.radians(xaci))],
            [0,math.sin(math.radians(xaci)),math.cos(math.radians(xaci))]
        ]))

        matrisy = np.mat(np.array([
            [math.cos(math.radians(yaci)),0,math.sin(math.radians(yaci))],
            [0,1,0],
            [-math.sin(math.radians(yaci)),0,math.cos(math.radians(yaci))]
        ]))

        matrisz = np.mat(np.array([
            [math.cos(math.radians(zaci)),-math.sin(math.radians(zaci)),0],
            [math.sin(math.radians(zaci)),math.cos(math.radians(zaci)),0],
            [0,0,1]
        ]))
        donmematrisi = matrisz * matrisy * matrisx
        # xyz = [
        #     [xdgr],
        #     [ydgr],
        #     [zdgr]
        # ]


        # sonucmatrisi = donmematrisi * xyz

        # yenix,yeniy,yeniz = sonucmatrisi
        hebele =0
        for kup in self.kupler2:
            kup2 = self.kupler3d[hebele]
            yenikup = []
            yeni3dkup = []
            zehir = 0
            ortax,ortay,ortaz = self.orta3dortanoktalar[hebele]
            for ic in kup:
                ic2 = kup2[zehir]
                xb = ic2[0][0]
                yb = ic2[0][1]
                zb = ic2[0][2]
                xs = ic2[1][0]
                ys = ic2[1][1]
                zs = ic2[1][2]

                # xyzb = np.array([
                #     [xb],
                #     [yb],
                #     [zb]
                # ])

                # xyzs = np.array([
                #     [xs],
                #     [ys],
                #     [zs]
                # ])




                xyzb = np.array([
                    [ortax-xb],
                    [ortay-yb],
                    [ortaz-zb]
                ])

                xyzs = np.array([
                    [ortax-xs],
                    [ortay-ys],
                    [ortaz-zs]
                ])


                sonucmatrisib = donmematrisi * xyzb
                sonucmatrisis = donmematrisi * xyzs

                yxb,yyb,yzb = sonucmatrisib
                yxs,yys,yzs = sonucmatrisis

                yxb,yyb,yzb = float(yxb)+ortax,float(yyb)+ortay,float(yzb)+ortaz
                yxs,yys,yzs = float(yxs)+ortax,float(yys)+ortay,float(yzs)+ortaz
                # yxb= xb*math.cos(math.radians(xaci))-yb*math.sin(math.radians(xaci))
                # yyb= xb*math.sin(math.radians(xaci))+yb*math.cos(math.radians(xaci))
                # yzb = zb
                # yxs= xs*math.cos(math.radians(xaci))-ys*math.sin(math.radians(xaci))
                # yys= xs*math.sin(math.radians(xaci))+ys*math.cos(math.radians(xaci))
                # yzs = zs


                yeni3dkup.append([[yxb,yyb,yzb],[yxs,yys,yzs]])
                nk1,nk2 = yeni3dkup[zehir]
                yenikupe = Nokta(nk1,nk2)()
                yenikup.append(yenikupe[0]+yenikupe[1])
                # if zehir == 0:
                #     nokta1 = [ic2[0][0],ic2[0][1],ic2[0][2]]
                # if zehir == 8:
                #     nokta6 = [ic2[0][0],ic2[0][1],ic2[0][2]]
                zehir+=1
            # self.ortanoktalar[hebele] = [yeniortax,yeniortay]
            nokta1 = yeni3dkup[0][0]
            nokta6 = yeni3dkup[8][0]
            yeniortax, yeniortay,yeniortaz = (nokta1[0]+nokta6[0])/2,(nokta1[1]+nokta6[1])/2,(nokta1[2]+nokta6[2])/2

            self.kupler2[hebele] = yenikup
            self.kupler3d[hebele] = yeni3dkup
            self.orta3dortanoktalar[hebele] = [yeniortax,yeniortay,yeniortaz]
            hebele+=1
        self.KupCizer2()



    def Kaydir(self,xyon:float=0,yyon:float=0):
        self.alan.delete(ALL)
        hebele =0
        for kup in self.kupler3d:
            yeni3dkup = []
            zehir =0
            yenikup = []
            for ic in kup:
                [xb,yb,zb],[xs,ys,zs] = ic

                yxb = xb + xyon
                yxs = xs + xyon
                yyb = yb + yyon
                yys = ys + yyon


                yeni3dkup.append([[yxb,yyb,zb],[yxs,yys,zs]])
                n1,n2 = yeni3dkup[zehir]
                yenikupe = Nokta(n1,n2)()
                yenikup.append(yenikupe[0]+yenikupe[1])
                zehir+=1
            # if zehir ==0:
            #     nokta1 = [ic[0][0],ic[0][1],ic[0][2]]
            # elif zehir == 6:
            #     nokta6 = [ic[1][0],ic[1][1],ic[1][2]]
            nokta1 = yeni3dkup[0][0]
            nokta6 = yeni3dkup[8][0]
            yeniortax, yeniortay,yeniortaz = (nokta1[0]+nokta6[0])/2,(nokta1[1]+nokta6[1])/2,(nokta1[2]+nokta6[2])/2
            self.kupler2[hebele] = yenikup
            self.kupler3d[hebele] = yeni3dkup
            self.orta3dortanoktalar[hebele] = [yeniortax,yeniortay,yeniortaz]
            hebele+=1
        self.KupCizer2()


    # def XeksenDondurur(self,xaci):
    #     hebele = 0
    #     print("İşlem öncesi = ",self.ortanoktalar)
    #     # print("KUP ESKİ VERSİYON : ",self.kupler2,len(self.kupler2[0]))
    #     for kup in self.kupler2:
    #         kup2 = self.kupler3d[hebele]
    #         yenikup = []
    #         yeni3dkup = []
    #         zehir = 0
    #         for ic in kup:
    #             ic2 = kup2[zehir]
    #             # print("ic2 : ",ic2)
    #             # ortax,ortay,ortaz = self.ortanoktalar[hebele]
    #             ortax,ortay = self.ortanoktalar[hebele]
    #             xb = ic2[0][0]
    #             yb = ic2[0][1]
    #             zb = ic2[0][2]
    #             xs = ic2[1][0]
    #             ys = ic2[1][1]
    #             zs = ic2[1][2]

    #             # yyb= (ortax-xb)*math.cos(math.radians(xaci))-(ortay-yb)*math.sin(math.radians(xaci))
    #             # yxb= (ortax-xb)*math.sin(math.radians(xaci))+(ortay-yb)*math.cos(math.radians(xaci))
    #             # yzb = zb
    #             # yxs= (ortax-xs)*math.cos(math.radians(xaci))-(ortay-ys)*math.sin(math.radians(xaci))
    #             # yys= (ortax-xs)*math.sin(math.radians(xaci))+(ortay-ys)*math.cos(math.radians(xaci))
    #             # yzs = zs

    #             yxb= xb*math.cos(math.radians(xaci))-yb*math.sin(math.radians(xaci))
    #             yyb= xb*math.sin(math.radians(xaci))+yb*math.cos(math.radians(xaci))
    #             yzb = zb
    #             yxs= xs*math.cos(math.radians(xaci))-ys*math.sin(math.radians(xaci))
    #             yys= xs*math.sin(math.radians(xaci))+ys*math.cos(math.radians(xaci))
    #             yzs = zs

    #             # yxb+=ortax
    #             # yyb+=ortay

    #             # yzb+=ortaz

    #             # yxs+=ortax
    #             # yys+=ortay

    #             # yzs+=ortaz
    #             # yenikup.append([ic[0],ic[1],ic[2],ic[3]])
    #             yeni3dkup.append([[yxb,yyb,yzb],[yxs,yys,yzs]])
    #             # print('Yeni ic2 xyz: ', yeni3dkup[zehir])
    #             nk1,nk2 = yeni3dkup[zehir]
    #             yenikupe = Nokta(nk1,nk2)()
    #             yenikup.append(yenikupe[0]+yenikupe[1])
    #             if zehir == 0:
    #                 nokta1 = [ic[0],ic[1]]
    #             if zehir == 7:
    #                 nokta6 = [ic[2],ic[3]]
    #             zehir+=1
    #         yeniortax, yeniortay = (nokta1[0]+nokta6[0])/2,(nokta1[1]+nokta6[1])/2
    #         self.ortanoktalar[hebele] = [yeniortax,yeniortay]
    #         self.kupler2[hebele] = yenikup
    #         self.kupler3d[hebele] = yeni3dkup
    #         hebele+=1
    #     # print("KUP YENİ VERSİYON : ",self.kupler2,len(self.kupler2[0]))
    #     # print('EKSEN DÖNDÜRME BİTTTİİİİ!!!!!')
    #     print("İşlem sonrası = ",self.ortanoktalar)
    #     self.KupCizer2()



    def HareketHali(self,yon:str):
        self.alan.delete(ALL)
        if yon =='xeksenidondur':
            # self.XeksenDondurur(xaci = 5)
            self.Dondurme(xaci = .5)
        elif yon =='xters':
            # self.XeksenDondurur(xaci=-5)
            self.Dondurme(xaci=-0.5)
        elif yon =='yeksenidondur':
            # self.XeksenDondurur(xaci=-5)
            self.Dondurme(yaci=0.5)
        elif yon =='yters':
            # self.XeksenDondurur(xaci=-5)
            self.Dondurme(yaci=-0.5)
        elif yon =='zeksenidondur':
            # self.XeksenDondurur(xaci=-5)
            self.Dondurme(zaci=1)
        elif yon =='zters':
            # self.XeksenDondurur(xaci=-5)
            self.Dondurme(zaci=-1)
        if yon=='sağ':
            kupcu = []
            for i in self.kupler:
                i[0]=i[0]+10
                self.KupCizer(i[0],i[1],i[2])
                kupcu.append(i)
            self.kupler=kupcu
        elif yon=='sol':
            kupcu = []
            for i in self.kupler:
                i[0]=i[0]-10
                self.KupCizer(i[0],i[1],i[2])
                kupcu.append(i)
            self.kupler=kupcu
        elif yon =='yukarı':
            kupcu = []
            for i in self.kupler:
                i[1]=i[1]-10
                self.KupCizer(i[0],i[1],i[2])
                kupcu.append(i)
            self.kupler=kupcu
        elif yon =='aşağı':
            kupcu = []
            for i in self.kupler:
                i[1]=i[1]+10
                self.KupCizer(i[0],i[1],i[2])
                kupcu.append(i)
            self.kupler=kupcu
        elif yon =='ileri':
            kupcu = []
            for i in self.kupler:
                i[2]=i[2]-3
                self.KupCizer(i[0],i[1],i[2])
                kupcu.append(i)
            self.kupler=kupcu
        elif yon =='geri':
            kupcu = []
            for i in self.kupler:
                i[2]=i[2]+3
                self.KupCizer(i[0],i[1],i[2])
                kupcu.append(i)
            self.kupler=kupcu
        elif yon =='çsy':
            pass
        elif yon =='çsa':
            pass
        elif yon =='çsoly':
            pass
        elif yon =='çsola':
            pass
        elif yon =='saatyönü':
            self.ssaci+=5
            if self.ssaci>=360:
                while self.ssaci>=360:
                    self.ssaci -=360
            for i in self.kupler:
                self.KupCizer(i[0],i[1],i[2])
        elif yon =='saattersyönü':
            self.ssaci-=5
            if self.ssaci<0:
                while self.ssaci<0:
                    self.ssaci = self.ssaci + 360
            for i in self.kupler:
                self.KupCizer(i[0],i[1],i[2])


Hareketli()