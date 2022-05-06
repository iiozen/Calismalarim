import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://smail:vuH7hErZ0PYGN9i1@cluster0.7axku.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb['products']

# result = mycollection.find_one()             ##### MongoDB operators####
# for i in mycollection.find({},{"_id":0}):         
    # print(i)

filter = {"name":"Samsung S5"}


# result = mycollection.find_one({"_id":ObjectId("5f219cfe22bf223d6c2fa61a")})
# result = mycollection.find({
#     "name":{
#         "$in":["Samsung S5","Samsung S6"]
#     }
# })

# result = mycollection.find({
#     "price":{
#         "$gte": 2000
#     }
# })

# result = mycollection.find({
#     "price":{
#         "$gt": 2000
#     }
# })
# result = mycollection.find({
#     "price":{
#         "$eq": 2000
#     }
# })

# result = mycollection.find({
#     "price":{
#         "$lte": 2000
#     }                                 
# })
# result = mycollection.find(filter)
# result = mycollection.find({
#     "name":{
#         "$regex": "^S"
#     }
# })
# for i in result:
#     print(i)
# # print(result) 
# result = mycollection.find().sort('name',-1)
# result = mycollection.find().sort('price',-1)
# result = mycollection.find().sort([('name',1),('price',-1)])
# for i in result:
#     print(i)