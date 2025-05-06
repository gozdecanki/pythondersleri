# set sıralanamaz ve indexlenemez

meyveler={
    "elma","kiraz","kavun","üzüm"
}

sebzeler ={"bezelye","soğan", "üzüm"}

sonuc=meyveler
print(sonuc)

# sonuc = meyveler[0]#indexlenemez
# print(sonuc)# hata


# for x in meyveler:
#     print(x)
#
#     kiraz
#     üzüm
#     kavun
#     elma

sonuc ="elma" in meyveler
print(sonuc)#True

meyveler.add("Muz")#{'kavun', 'kiraz', 'üzüm', 'elma', 'Muz'}
print(meyveler)

meyveler.update(["vişne","portakal"])
print(meyveler)#{'kiraz', 'vişne', 'kavun', 'portakal', 'üzüm', 'elma', 'Muz'}


meyveler.update(["kavun"])#tekrar kavun eklemeyi deniyoruz. sonuc değişmiyor.2. kavun eklenmemiş oluyor
print(meyveler)#{'kavun', 'vişne', 'portakal', 'Muz', 'üzüm', 'elma', 'kiraz'}

sonuc = len(meyveler)
print(sonuc)#7

meyveler.remove("portakal")# silme işlemi
#meyveler.remove("portakalz")# silme işlemi yaparken olmayan bir key değeri verirsek KeyError hatası alırız
print(meyveler)# {'elma', 'vişne', 'kavun', 'kiraz', 'Muz', 'üzüm'}

meyveler.discard("kiraz")#silme işlemi yapar
#meyveler.discard("kirazz") olmayan bir key ile işlem yaparsa hata vermez
print(meyveler)#{'elma', 'üzüm', 'kavun', 'vişne', 'Muz'}

# sonuc=meyveler.pop()
# print(sonuc)# muz silindi // tekrar run edildiğinde kavun silindi rast gele silme yapıyor

# sonuc= meyveler.clear()
# print(sonuc) #None tümü silindi

#2 setin birleşimi. eğer 2 sette aynı eleman varsa 1 tanesi alınır
sonuc= meyveler.union(sebzeler)
print(sonuc)#{'vişne', 'soğan', 'kavun', 'bezelye', 'üzüm', 'Muz'}
