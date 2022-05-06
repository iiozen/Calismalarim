from tkinter import *

class Cizim:
    def __init__(self):
        self.pencere = Tk()
        self.pencere.geometry('1600x1200')
        self.alan = Canvas(self.pencere,width=1600,height=1200,bg='black')
        self.alan.bind('<Button-1>',self.Ilk)
        self.alan.bind('<Motion>',self.Cizim)
        self.alan.bind('<ButtonRelease-1>',self.CizDur)
        self.alan.focus_set()
        self.alan.bind('<Control-z>',self.GeriAl)
        self.alan.bind('<Control-Z>',self.GeriAl)
        self.ilknokta=[]
        self.alan.pack()
        self.ciz=False
        self.pencere.mainloop()
    def Ilk(self,event):
        self.ilknokta = [event.x,event.y]
        self.ciz = True
    def Cizim(self,event):
        if self.ciz:
            self.alan.create_line(self.ilknokta,event.x,event.y,width=2,fill='red')
            self.ilknokta = [event.x,event.y]
    def CizDur(self,event):
        self.ciz = False
    def Pencereci(self):
        print('PENCERECİ')
        frm = Frame(self.alan,background='white')
        kt = self.alan.create_window(200,200,anchor='nw',height=200,width=200,window=frm)
    def GeriAl(self,event):
        gerial = list(self.alan.find_all())[-5:]
        [self.alan.delete(sonbes) for sonbes in gerial]
Cizim()