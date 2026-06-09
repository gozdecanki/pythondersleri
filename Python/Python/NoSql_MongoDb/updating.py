import pymongo


myclient = pymongo.MongoClient("mongodb+srv://gozde_mongodb:ukobORlCyQfjZBRr@cluster0.f44cpkc.mongodb.net/node-app")
mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

# mycollection.update_one( #ilk bulduğunu günceller
#     {'name':'Samsung S6'},
#     {'$set':{
#         'name':'IPhone 6',
#         'price': 5000
#     }}
# )

# mycollection.update_many( #birden fazla kayıt bulursa hepsini günceller
#     {'name':'Samsung S5'},
#     {'$set':{
#         'name':'IPhone 8',
#         'price': 5000
#     }}
# )

# parametre haline getirebiliriz
query = {'name':'Samsung S9'}
newvalues =  {'$set':{
        'name':'IPhone 11',
        'price': 10000
    }}
result = mycollection.update_many(query, newvalues)
print(f'{result.modified_count} adet kayıt güncellendi')

for i in mycollection.find():
    print(i)









productList =[
    # {"_id":1, "name":"Samsung S5", "price":3000}, otomatik object id zaten oluşturuluyor fakat _id şeklinde değer vererek ezebiliriz
    {"name":"Samsung S5", "price":3000, "description":"iyi telefon"},
    {"name":"Samsung S6", "price":4000, "categories":['telefon','elektronik']},
    {"name":"Samsung S7", "price":5000},
    {"name":"Samsung S8", "price":6000},
    {"name":"Samsung S9", "price":7000},
    {"name":"Samsung S10", "price":8000}
]