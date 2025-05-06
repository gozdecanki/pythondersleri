
list1={34:"istanbul" , 6:"ankara"}

print(list1[34]) # ekranda istanbul yazdığını görürürz. 34 anahtar kelimemizdir
print(list1[6])

#alt satıra devam için \

person = \
{
    1: {
        "name": "ali",
        "surname": "yıldırım",
        "salary": 5000.00
        },
        
     2: {
        "name": "ayşe",
        "surname": "can",
        "salary": 6000.00
        }
   
    }

print(person[1]) # {'name':'ali','srname':'yıldırım','salary':5000.00}
print(person[1]["name"]) #ali
print(person[2]["name"]) #ayşe

# key - value

# 41 => Kocaeli
# 34 => İstanbul

sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])

# print(plakalar[sehirler.index('istanbul')])
# print(plakalar[sehirler.index('kocaeli')])

plakalar = {'kocaeli': 41,'istanbul':34}

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

plakalar['rize'] = 53 # rize indexi yoksa yenisini ekler varsa var olanın değerini değiştirir
# plakalar['izmir'] = 36

# plakalar['izmir'] = 35 # 36 to 35
# print(plakalar)

ogrenciler = {
    100: {
        "ad": "Çınar",
        "soyad": "Turan",
        "yas": 4,
        "notlar": [70,80,70]
    },
    101: {
        "ad": "Ada",
        "soyad": "Bilgi",
        "yas": 10,
        "notlar": [90, 80, 70]
    }
}

sonuc = ogrenciler[101]
print(sonuc)
sonuc = ogrenciler[101]["ad"]
print(sonuc)
sonuc = ogrenciler[101]["soyad"]
print(sonuc)

sonuc = (ogrenciler[100]["notlar"][0] + ogrenciler[100]["notlar"][1] + ogrenciler[100]["notlar"][2]) / 3

print(sonuc)