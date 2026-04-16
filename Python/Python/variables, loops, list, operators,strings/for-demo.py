sayilar = [1,5,15,35,57,72,75,10]
toplam=0
# for sayi in sayilar:
#     print(sayi)


# for sayi in sayilar:
#     if(sayi % 5==0):
#         print(sayi)


# for sayi in sayilar:
#     toplam+=sayi

# print(f"{toplam}")
        

# for sayi in sayilar:
#     if(sayi % 2==0):
#         print(sayi , sayi*sayi)

urunler =['iphone 8','iphone X','iphone XR', 'samsung S10']

# for urun in urunler:
#     print(urun[1]) #2. karakterleri yazdırdık

count=0
for urun in urunler:
    #print(urun.find('iphone'))
    index=urun.find('iphone')#içinde iphone olanları bul
    if(index>-1):
        count+=1
print(count)

# for urun in urunler:
#     print(urun.index('iphone'))