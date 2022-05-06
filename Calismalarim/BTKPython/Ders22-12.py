import mysql.connector
import datetime
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'MySql1594',
    database = 'schooldb'
)
cursor = connection.cursor()

class liste_Olustur:
    def __init__(self):
        self.liste = []
        self.liste_Islemi()
    def liste_Islemi(self):
        self.StudentNumber = input('Öğrenci numarasını giriniz: ')
        self.Name = input('Öğrencinin adını giriniz: ')
        self.Surname = input('Öğrencinin soyadını giriniz:')
        self.Birthday = input('Doğum Tarihini giriniz: ')
        a = self.Birthday.split()
        self.Birthday = datetime.date(int(a[0]),int(a[1]),int(a[2]))
        self.Gender = input('Öğrencinin cinsiyetini Erkek/Kız (E/K) olarak giriniz: ')
        self.liste_Yazar()
    def liste_Yazar(self):
        self.liste.append((self.StudentNumber,self.Name,self.Surname,self.Birthday,self.Gender))
        self.kontrolor()
    def kontrolor(self):
        a = input('Veri girişine devam etmek için hiçbir şey yazmadan entere basınız.\nDurdurmak için herhangi bir yazı gönderiniz.')
        if a !='':
            kayit_Islem(self.liste)
        else:
            self.liste_Islemi()

class kayit_Islem:
    def __init__(self,liste):
        self.liste = liste
        print('Girilen veriler veritabanına kaydediliyor.')
        
        self.kaydeder()
        # else:
        #     self.tekli_Kaydeder()
    def kaydeder(self):
        connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'MySql1594',
        database = 'schooldb'
        )
        cursor = connection.cursor()
        sql = 'INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)'
        values = self.liste
        cursor.executemany(sql,values)
        try:
            connection.commit()
            print(f"{cursor.rowcount} tane kayıt eklendi.")        
            print(f"İlk eklenen kaydın id: {cursor.lastrowid}\nSon eklenen kaydın id: {cursor.lastrowid+cursor.rowcount-1}")        
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            connection.close()
            print('database bağlantısı kapandı.')

liste_Olustur()
