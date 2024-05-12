
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