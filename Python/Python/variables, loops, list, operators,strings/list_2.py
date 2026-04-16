msg="Python Kursumuza Hoş Geldiniz. Ben Gözde Cankı Erdoğan".split()
print(msg) # ['Python', 'Kursumuza', 'Hoş', 'Geldiniz.', 'Ben', 'Gözde', 'Cankı', 'Erdoğan']
print(msg[0]) # Python
print(msg[0][0]) #Python 'ın P si

sayilar=[1,3,5,7,9]

sonuc=sayilar
print(sonuc)

sonuc=sayilar[0]
print(sonuc)

sonuc=sayilar[4]
print(sonuc)

isimler = ['ahmet', 'ali','can','ada']

sonuc=isimler[0]
print(type(isimler[0]))

print(type(sayilar[0]))


listeAli=['Ali',20]
listeAhmet=['Ahmet',22]

sonuc=listeAli[0]
print(sonuc) # Ali
sonuc=listeAli[1]
print(sonuc)# 20


#ogrenciler=[['Ali',20],['Ahmet',22]]
ogrenciler=[listeAli,listeAhmet]

sonuc=ogrenciler[0][0]
print(sonuc)#Ali

sonuc=ogrenciler[1][0]
print(sonuc)#Ahmet



