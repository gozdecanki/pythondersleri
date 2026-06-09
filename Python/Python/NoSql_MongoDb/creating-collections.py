import pymongo

#local mongodb bağlantısı
# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# mydb = myclient["node-app"]
# print(myclient.list_database_names())

#https://cloud.mongodb.com/ de oluşturduğumuz mongodb bağlantısı
myclient = pymongo.MongoClient("mongodb+srv://gozde_mongodb:ukobORlCyQfjZBRr@cluster0.f44cpkc.mongodb.net/node-app")
mydb = myclient["node-app"]
mycollection= mydb["products"]

# product ={"name":"Samsung S5", "price":3000}
# result=mycollection.insert_one(product)

# print(result)
# print(type(result))
# print(result.inserted_id)

productList =[
    # {"_id":1, "name":"Samsung S5", "price":3000}, otomatik object id zaten oluşturuluyor fakat _id şeklinde değer vererek ezebiliriz
    {"name":"Samsung S5", "price":3000, "description":"iyi telefon"},
    {"name":"Samsung S6", "price":4000, "categories":['telefon','elektronik']},
    {"name":"Samsung S7", "price":5000},
    {"name":"Samsung S8", "price":6000},
    {"name":"Samsung S9", "price":7000},
    {"name":"Samsung S10", "price":8000}
]

result=mycollection.insert_many(productList)
print(result.inserted_ids)