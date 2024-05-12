
#list
list1=[1,2,3]

#tuple
list2=(1,2,3) 

# aşağıdaki işlem tuple da yapılamaz : does not support item assignment hatası verir
#list2[0]=2
#print(list2)
# tuple ın listeden en önemli farkı; oluşturulurken verilen elemanlar sonrasında değiştirilemez


print(list2.count(2)) # verilen değer tuple da kaç tane : 1

print(list2.index(1)) # liste içinde kaçıncı indexte : 0

print(list2.index(1,0)) # liste içinde kaçıncı indexte : 0

print(list2.index(1,0,-1)) # liste içinde kaçıncı indexte : 0

#print(list2.index(1,1,-1)) #1. index ile sonuncu index arasında ara, liste içinde kaçıncı indexte : exception oluşur, verdiğin değer tupleda yok



#tuple dan list e dönüştürme

list2= list(list2)
print(type(list2)) # tipini : <class 'list'> bu şekilde döndürür

list2[0]=2 # değer değiştiriyoruz
print(list2) #[2,2,3]

#list den tuple a dönüştürme

list1=tuple(list1)
print(type(list1)) # tipini : <class 'tuple'> bu şekilde döndürür
list1[0]=5 # hata verir. list1 artık tuple olduğuiçin değerini değiştiremeyiz. does not support item assignment