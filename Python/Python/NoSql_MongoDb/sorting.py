import pymongo


myclient = pymongo.MongoClient("mongodb+srv://gozde_mongodb:ukobORlCyQfjZBRr@cluster0.f44cpkc.mongodb.net/node-app")
mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find().sort("name") # varsayılan artan şekilde sıralar
#result = mycollection.find().sort("name", 1) #artan şekilde sıralar
# result = mycollection.find().sort("name", -1) #azalan şekilde sıralar

# result = mycollection.find().sort("price", -1) #azalan şekilde sıralar

result = mycollection.find().sort([('name',1),('price',-1)])
for i in result:
    print(i)