# sayilar=[4,6,9,10,35,57,89,125,244]

# i=0
# while (i<len(sayilar)):
#     print(sayilar[i])
#     i+=1

# while sayilar:
#     print(sayilar.pop()) #sondan başlayarak yazdırır

# while sayilar:
#     print(sayilar.pop(0)) #baştan başlayarak yazdırır

# baslangic = int(input('baslangic:'))
# bitis = int(input('bitis:'))
# i=baslangic

# while i< bitis:
#     i+=1
#     if(i%2==1):
#         print(i)


# i=100
# while i>0:
#     print(i)
#     i-=1

sayilar=[]
i=0
while (i<5):
    sayi = int(input('sayi: '))
    sayilar.append(sayi)
    i+=1

sayilar.sort()
print(sayilar)