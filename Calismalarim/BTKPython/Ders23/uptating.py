import pymongo
from bson.objectid import ObjectId
from mongohesap import hesap
myclient = pymongo.MongoClient(hesap)

mydb = myclient["node-app"]
mycollection = mydb['products']
# for i in mycollection.find():
#     print(i)

# mycollection.update_one(
#     {'name':'Samsung S6'},
#     {'$set':{
#         'name':'IPhone 7',
#         'price': 5000
#     }}
# )
query = {'name':'Samsung S7'}
newvalues = {'$set':{
    'name':'IPhone 8',
    'price': 5000
}}
result = mycollection.update_many(query,newvalues)
print(f'{result.modified_count} adet kayıt güncellendi.')
for i in mycollection.find():
    print(i)
#update_one
#update_many