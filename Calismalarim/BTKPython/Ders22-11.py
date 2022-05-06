import mysql.connector
# def insertProduct(name,price,imageUrl,description):
#     connection = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = 'MySql1594',
#         database = 'node-app'
#     )
#     cursor = connection.cursor()
#     sql = 'INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)'
#     values = (name, price, imageUrl,description)
#     cursor.execute(sql,values)
#     try:
#         connection.commit()
#         print(f"{cursor.rowcount} tane kayıt eklendi.")        
#         print(f"son eklenen kaydın id: {cursor.lastrowid}")        
#     except mysql.connector.Error as err:
#         print('hata:', err)
#     finally:
#         connection.close()
#         print('database bağlantısı kapandı.')

def insertProducts(liste):
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'MySql1594',
        database = 'node-app'
    )
    cursor = connection.cursor()
    sql = 'INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)'
    values = liste
    cursor.executemany(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")        
        print(f"son eklenen kaydın id: {cursor.lastrowid}")        
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

liste = []

# name = input('ürün adı: ')
# price = input('ürün fiyatı: ')
# imageUrl = input('ürün resim adı: ')
# description = input('ürün açıklaması: ')
# insertProduct(name,price,imageUrl,description)

while True:
    name = input('ürün adı: ')
    price = input('ürün fiyatı: ')
    imageUrl = input('ürün resim adı: ')
    description = input('ürün açıklaması: ')

    liste.append((name,price,imageUrl,description))

    result = input('devam etmek istiyor musunuz? (e/h)')
    if result =='h':
        print('Kayıtlarınız veritabanına aktarılıyor...')
        print(liste)
        insertProducts(liste)
        break