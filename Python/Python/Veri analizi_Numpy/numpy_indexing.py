import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
result = numbers[-1]
result = numbers[0:3]#0,5,10
result = numbers[:3]#0,5,10
result = numbers[3:]
result = numbers[::]
result = numbers[::-1]#listeyi ters çevirir

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numbers2[0]
result = numbers2[2]
result = numbers2[0,2]#1. satırdaki elamanın 2. indexindeki değer
result = numbers2[2,1]
result = numbers2[:,2]#tüm satırları seçip her bir satırdaki 2. indexteki veriyileri getirir
result = numbers2[:,0]
result = numbers2[:,0:2]#tüm satırları seç ve 0 ile 2. index arasındaki değerleri getirir. 2 dahil değil
result = numbers2[-1,:]#son satırı al ve tüm kolon elemanlarını al: [50,75,85]
result = numbers2[:2,:2]#2 satır 2. sütünları alarak 

# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1 # referans
arr2 = arr1.copy()#değerleri kopyalıyor sadece. adresleri farklı

arr2[0] = 20

print(arr1)
print(arr2)


# [0 1 2 3 4 5 6 7 8 9]
# [20  1  2  3  4  5  6  7  8  9]