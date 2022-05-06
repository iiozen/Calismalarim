import math
class Nokta:
    # def __init__(self,nokta1:dict={'x':'X eksenindeki noktası','y':'Y Eksenindeki Noktası', 'z': 'Z eksenindeki Noktası'},nokta2:dict={'x':'X eksenindeki noktası','y':'Y Eksenindeki Noktası', 'z': 'Z eksenindeki Noktası'}):
    #     print("Nokta1 'in\nX : ", nokta1['x'],"\nY : ",nokta1['y'],'\nZ : ',nokta1['z'])
    #     print("Nokta2 'in\nX : ", nokta2['x'],"\nY : ",nokta2['y'],'\nZ : ',nokta2['z'])
    def __init__(self,nokta1:list=['x1','y1','z1'],nokta2:list=['x2','y2','z2']):
        self.nokta1 = nokta1
        self.nokta2 = nokta2
        self.HataBakar()
        self.VektorelIslemler()
        self.EksenDusur()
        # self.__repr__()
        
    def VektorelIslemler(self):
        self.x1,self.y1,self.z1 = self.nokta1
        self.x2,self.y2,self.z2 = self.nokta2

        self.x = self.x2 - self.x1
        self.y = self.y2 - self.y1
        self.z = self.z2 - self.z1
        self.sinus = math.sin(math.radians(45))
        self.vektor = math.sqrt(self.x**2+self.y**2+self.z**2)
        # self.Zyuzde = self.z/(self.x+self.y+self.z)
        try:
            self.Z2yuzde = self.z2/(self.x2+self.z2+self.y2)
        except:
            self.Z2yuzde=0
        try:
            self.Z1yuzde = self.z1/(self.x1+self.y1+self.z1)
        except:
            self.Z1yuzde=0
    def EksenDusur(self):
        # zetki2 = self.z * self.sinus * self.Zyuzde / 2
        # zetki1 = self.z1 * self.sinus * self.Z1yuzde / 2
        # zetki2 = self.z2 * self.sinus * self.Z2yuzde / 2
        zetki1 = self.z1  * self.sinus /2
        zetki2 = self.z2 * self.sinus /2
        # self.x2Yeni = self.x + zetki2
        # # self.y2Yeni = self.y + zetki2
        # # self.x1Yeni = self.x1 + zetki2
        self.x2Yeni = self.x2 + zetki2
        self.y2Yeni = self.y2 + zetki2
        self.x1Yeni = self.x1 + zetki1
        self.y1Yeni = self.y1 + zetki1
    # def __repr__(self):
    #     return repr([[self.x1,self.x2],[self.x2Yeni,self.y2Yeni],[self.vektor]])
    def __call__(self):
        # return [[self.x1,self.x2],[self.x2Yeni,self.y2Yeni],[self.vektor]]
        return [[self.x1Yeni,self.y1Yeni],[self.x2Yeni,self.y2Yeni],[self.vektor]]


    def HataBakar(self):
        try:
            if len(self.nokta1) !=3 or len(self.nokta2)!=3:
                print('Girilen noktalar x,y,z olmak üzere 3 değer içermelidir.')
                exit()
            for i in self.nokta1:
                if type(i)== float or type(i)== int:
                    continue
                else:
                    print('Girilen ilk noktanın x,y,z değerleri int veya float olmalıdır.')
                    exit()
            for i in self.nokta2:
                if type(i)== float or type(i)== int:
                    continue
                else:
                    print('Girilen ikinci noktanın x,y,z değerleri int veya float olmalıdır.')
                    exit()
        except:
            exit()
    