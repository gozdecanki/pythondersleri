liste =[10,4,7,9,70]

sayilar= []

for i in range(10):
    sayilar.append(i)


#comprehension
#sayilar = [i for i in range(10)]    
#sayilar = [i*i for i in range(10)]    #karesini alabiliz

#sayilar =[i*2 for i in liste]
#print(sayilar)

# isim = "Ahmet"

# sonuc =[c.upper() for c in isim]
# print(sonuc)


# sonuc =[str(sayi) for sayi in liste]
# print(sonuc)

isimler =["Ahmet","ali","Çınar","DeNiz"]
sonuc=[i.lower() for i in isimler]
print(sonuc)