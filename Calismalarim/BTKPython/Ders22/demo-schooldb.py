import mysql.connector
from datetime import datetime
from Ders22.connection import connection


class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            Student.connection.close()
            print('Bağlantı sonlandırıldı.')
    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students 
        Student.mycursor.executemany(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            Student.connection.close()
            print('Bağlantı sonlandırıldı.')

    @staticmethod
    def StudentInfo():
        # sql = "select * from student"
        # sql = "select * from student LIMIT 5"
        # sql = "select studentnumber,name,surname from student"
        # sql = "select studentnumber,name,surname from student where gender='K'"
        # sql='select * from student where YEAR(birthdate) = 2003'
        # sql='select * from student where YEAR(birthdate) = 2005 and name = "Ali"'
        # sql = "select * from student where name like '%an%' or surname like '%an%'"        
        # sql = 'select count(id) from student where gender="E"'
        sql = 'select name,surname from student where gender ="K" order by name,surname '

        Student.mycursor.execute(sql)
        try:
            results = Student.mycursor.fetchall()
            for result in results:
                print(result)
        except mysql.connector.Error as err:
            print('hata',err)
        finally:
            Student.connection.close()

    @staticmethod
    def getStudentById(id):
        sql = 'select * from student where id = %s'
        value = (id,)
        Student.mycursor.execute(sql,value)
        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5] )
        except mysql.connector.Error as err:
            print('hata',err)
        
    def updateStudent(self):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)        
        Student.mycursor.execute(sql,values)        
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print('hata',err)
    @staticmethod
    def getStudentsGender(gender):
        sql = 'select * from student where gender = %s'
        value = (gender,)
        Student.mycursor.execute(sql,value)
        try:
            return Student.mycursor.fetchall()
            
        except mysql.connector.Error as err:
            print('hata',err)
    @staticmethod
    def updateStudents(liste):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = []
        order = [1,2,3,4,5,0]
        for item in liste:
            item = [item[i] for i in order]
            values.append(item)
        Student.mycursor.executemany(sql,values)        
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print('hata',err)


# students = Student.getStudentsGender('E')
# print(students)
# liste = []
# for std in students:
#     std = list(std)
#     # std[2] = 'Ms '+ std[2]
#     std[2] = std[2].strip('Mr ')
#     liste.append(std)
# Student.updateStudents(liste)



# students = Student.getStudentsGender('E')
# for student in students:
#     print(student)






# student = Student.getStudentById(10)
# student.name = 'Çınar'
# student.surname = 'Turan'
# student.updateStudent()

# Student.StudentInfo()




# ahmet = Student("403","Mehmet","yılmaz",datetime(2003,7,13),"E")
# ahmet.saveStudent()



# ogrenciler = [
#     ("301","Ahmet","Yılmaz",datetime(2005,5,17),"E"),
#     ("302","Ali","Can",datetime(2005,6,17),"E"),
#     ("303","Canan","Tan",datetime(2005,7,7),"K"),
#     ("304","Ayşe","Taner",datetime(2005,9,23),"K"),
#     ("305","Bahadır","Toksöz",datetime(2005,7,27),"E"),
#     ("306","Ali","Cenk",datetime(2005,8,25),"E")
# ]

# Student.saveStudents(ogrenciler)