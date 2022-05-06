import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://smail:vuH7hErZ0PYGN9i1@cluster0.7axku.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]
#delete_one()
#delete_many()

for i in mycollection.find():
    print(i)

print('*'*50)

# mycollection.delete_one({'name':'Samsung S6'})
# mycollection.delete_many({'name':{'$regex':"^S"}})
result = mycollection.delete_many({})
print(f"{result.deleted_count} adet kayıt silindi.")




for i in mycollection.find():
    print(i)

