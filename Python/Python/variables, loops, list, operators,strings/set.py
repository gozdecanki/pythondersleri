
list1= {1,2,3,4,5}
print(type(list1)) #<class 'set'>

print(list1) # {1,2,3,4,5}

#print(list1[0]) # 'set' object is not subscriptable hatası verir. set yapısında liste oluşturulduğunda istediğimiz indexi yazıp elemanına ulaşamayız

# alt altatüm elemanı yazar
for keep in list1:
    print(keep) # forun içine 1 tab kadar boşluk bırakmak gerekiyor
    

for keep in list1:
    pass  #ya da for için işlevi sonra yazacaksak hata vermemesi adına pass yazıyoruz

print("hello") # forun işi bitmiş oluyor


list1.add(6)
print(list1) # {1,2,3,4,5,6}

#list1.add(7,8,9) ## hata verir tek tek eklemek gerekir yada ;
list1.update([7,8,9,10]) # {1,2,3,4,5,6,7,8,9,10}
print(list1)

list1.remove(10) # silmek istediğim değeri elemanı yazıyoruz index değil
list1.clear() #set() listenin içini boşaltıyor

del list1 # listeyi silmek için
print(list1)# list1 is not defined hatası alırız