import mysql.connector

def veriAl():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'MySql1594',
        database = 'schooldb'
    )
    cursor = connection.cursor()
    # yapilacak = input('Yapılacak işlemi seçin:\n1-  ')
    # cursor.execute(f'Select {a} From Student')
    # cursor.execute(f'Select {a} From Student Where {aranan}{islem}')
    cursor.execute('Select * From Student')
    a = cursor.fetchall()
    for i in a:
        print(i)
veriAl()