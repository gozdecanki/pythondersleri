import pymongo

#local mongodb bağlantısı
# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# mydb = myclient["node-app"]
# print(myclient.list_database_names())

#https://cloud.mongodb.com/ de oluşturduğumuz mongodb bağlantısı
myclient = pymongo.MongoClient("mongodb+srv://gozde_mongodb:ukobORlCyQfjZBRr@cluster0.f44cpkc.mongodb.net/node-app")
mydb = myclient["node-app"]

print(myclient.list_database_names())