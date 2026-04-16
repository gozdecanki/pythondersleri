
#Liste nedir? : Liste birden fazla veriyi bellek üzerinde tutmamızı sağlayan yapılardır.index numarası 0 dan başlıyor

list1= []

list2=[1,2,3,4,5]

print(list2[0])
print(list2[3-1]) # 3. elemanı bulmak için n-1=3-1
print(list2[3])

print(list2[-1]) # son elemanı bu şekilde yazdırılablir
print(list2[-2]) # sondan 1 önceki elemanı yazdırır

print(list2[0:3]) # 1. elemandan yani 0. indexten, 4. elemana kadar yani 3. indexe kadar yazdırma : sonuc:[1,2,3] 3 ile belirtilen dahil edilmez 
print(list2[0:3+1]) # dahil edilsin istersek sonuc: [1,2,3,4]

print(list2[0:]) # sonuc:[1,2,3,4,5] 
print(list2[:3]) # sonuc:[1,2,3]
print(list2[0::2]) # sonuc : [1,3,5] bu :: ifadeyi kullanırsak elemanları 0. indexten itibaren bir yaz bir yazma demiş oluruz
print(list2[0::3]) # sonuc [1,4] 1 yaz iki atla 3.yaz

list2[0]=0 # değer değiştirme
print(list2) #sonuc : [0,2,3,4,5]


#list fonksiyonları
 
print(len(list2)) # kac eleman oldugu : 5
list2.append(6)
print(list2) #sonuc:[0,2,3,4,5,6] 

list1= list2.copy()
print(list1) # list2 deki değerler list1 e kopyalanmış oldu

print(min(list2)) # listedeki en küçük değeri 0
print(max(list2)) # listedeki en büyük değeri 6

list2.insert(1,1) # listeye eleman ekleme [0,1,2,3,4,5,6] :> 1,1  1. indexte 2 vardı. 1. indexin önüne 1 i eleman olarak ekle demiş olduk
print(list2)

list2.pop()
print(list2) # listenin son elemanı olmadan getirir [0,1,2,3,4,5] siler

list2.pop(0) # 0. indexi siler
print(list2) #[1,2,3,4,5] 

list2.remove(5) # direkt olarak silmek isteiğimiz veriyi verip sildiriyoruz
print(list2) #[1,2,3,4] 

list2.reverse() # listeyi ters cevir 
print(list2) #[4,3,2,1]

list2.sort()# küçükten büyüge sırala
print(list2) #[1,2,3,4] 
 # büyükten küçüge sıralmak için listeye önce sort işlemi snra reverse işlemi yapılır

print(list2.count(2)) # listede 2 kaç tane var : 1
print(list2.count(55)) # listede 55 olmadığı için 0 döner

list2.clear() # listenin elemanlarını siler
print(list2) # []

del list2 # listeyi siler
print(list2) # çalıştırırsak list2 tanımlı değilhatası alırız