opelObj={
    "marka": "Opel",
    "model":"Corsa",
    "yil":"2025"
}

sonuc =opelObj["marka"]
print(sonuc)
sonuc=opelObj.get("marka")
print(sonuc)


for x in opelObj:
    print(x)

print("****************")
for x in opelObj:
    print(opelObj[x])
print("****************")
for x in opelObj.values():
    print(x)
print("****************")

for x,y in opelObj.items():
    print(x,y)
   # print(x + ':', y)

sonuc="marka" in opelObj
print(sonuc)

sonuc=len(opelObj)
print(sonuc)#3

opelObj["renk"]= "kırmızı" #ekleme
print(opelObj)# {'marka': 'Opel', 'model': 'Corsa', 'yil': '2025', 'renk': 'kırmızı'}

opelObj.pop("renk") # silme
print(opelObj)#{'marka': 'Opel', 'model': 'Corsa', 'yil': '2025'}

opelObj.popitem()#sondan silme yapar
print(opelObj)#{'marka': 'Opel', 'model': 'Corsa'}

del opelObj["marka"]
print(opelObj)#{'model': 'Corsa'}