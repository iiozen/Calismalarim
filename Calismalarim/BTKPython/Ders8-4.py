class Person():
    def __init__(self):
        print('Person created')

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        print('Student Created')
s1 = Student()