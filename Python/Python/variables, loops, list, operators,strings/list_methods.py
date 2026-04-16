sayilar = [1,5,8,9,3,45,77,5]
harfler = ['a','b','e','s','a','y']

sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = max(harfler)

# ekleme
sayilar.append(10)
sayilar.insert(3,5)
sayilar.insert(-1,50)
sayilar.insert(len(sayilar),150)

# silme
sayilar.pop()#sondaki elemanı siler
sayilar.pop(0)#baştaki elemanı siler
sayilar.remove(45)# 45 e eşit olan değerleri siler
harfler.remove('y')

# sıralama
sayilar.sort()# küçükten büyüğe doğru sıralar
harfler.sort()
sayilar.reverse()# büyükten küçüğe doğru sıralar

# print(sayilar.count(5))#listede kaç tane 5 varsa onu sayar
# print(harfler.count('a'))

print(sayilar.index(3)) # 3 değeri hangi indexte ise onu döner
sayilar.clear() # liste elemanlarının hepsi silinir

sonuc = sayilar
# sonuc = harfler

print(sonuc)