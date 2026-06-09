import pymongo

myclient = pymongo.MongoClient("mongodb+srv://gozde_mongodb:ukobORlCyQfjZBRr@cluster0.f44cpkc.mongodb.net/node-app")
mydb = myclient["node-app"]
mycollection= mydb["products"]

#result = mycollection.find_one()

#for i in mycollection.find(): tüm kolonları ile birlikte tüm veriyi getirir
#for i in mycollection.find({},{"_id":0, "name":1, "price":1}): # sorgu sonucunda hangi kolonlar gelsin istiyorsak karşısına 1 istemiyorsak da 0 yazıyoruz
for i in mycollection.find({},{"_id":0, "name":1, "price":1}):
    print(i)

#print(result)