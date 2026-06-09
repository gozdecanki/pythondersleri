import pymongo


myclient = pymongo.MongoClient("mongodb+srv://gozde_mongodb:ukobORlCyQfjZBRr@cluster0.f44cpkc.mongodb.net/node-app")
mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

print('*'*50)

# mycollection.delete_one({"name": "IPhone 6"})
# for i in mycollection.find():
#     print(i)


# mycollection.delete_many({"name":{"$regex":"^S"} })
# for i in mycollection.find():
#     print(i)


result = mycollection.delete_many({})
print(f'{result.deleted_count}  adet eleman silindi')
for i in mycollection.find():
    print(i)
