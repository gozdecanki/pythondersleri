import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://gozde_mongodb:ukobORlCyQfjZBRr@cluster0.f44cpkc.mongodb.net/node-app")
mydb = myclient["node-app"]
mycollection= mydb["products"]


# filter={"name":"Samsung S5"}
# result = mycollection.find(filter)
# for i in result:
#     print(i)

# result = mycollection.find_one(filter)
# print(result)

#_id değerini string olarak gönderirsek eşleşme sağlanamaz. objectId şeklinde göndermemiz gerekiyor
# result = mycollection.find_one({"_id":ObjectId("6a289167030cc4c44e51afcc")})
# print(result)


# result = mycollection.find({
#     "name": {
#         "$in" : ["Samsung S5", "Samsung S6"]
#         }
# })
# for i in result:
#     print(i)


# result = mycollection.find({
#     "price": {
#         "$gt" : 2000  # greater than
#         }
# })
# for i in result:
#     print(i)



# result = mycollection.find({
#     "price": {
#         "$gte" : 2000  # greater than and equal
#         }
    
# })
# for i in result:
#     print(i)

# result = mycollection.find({
#     "price": {
#         "$eq" : 2000  # equal
#         }
    
# })
# for i in result:
#     print(i)

# result = mycollection.find({
#     "price": {
#         "$lt" : 4000  # less than
#         }
    
# })
# for i in result:
#     print(i)

result = mycollection.find({
    "name": {
        "$regex" : "^S"  # name alanı S ile başlayan kayıtları getirir
        }
    
})
for i in result:
    print(i)