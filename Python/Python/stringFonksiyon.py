
#string Fonksiyon

companyName="Bilgo Soft"
age=10

text=len(companyName)
text=companyName.capitalize() # sadece ilk kelime büyük harf diğeri küçük Bilgo soft
text=companyName.casefold()# hepsini kücük harf bilgo soft
text=companyName.center(50,'*')# ***********************Bilgo Soft********************  tolam 50 karakter olacak sekilde bilgo softun karakter syısını cıkarıp geri kalnı * yapar ve merkeze yerleştirir
text=companyName.rjust(50,'*')#*******************************Bilgo Soft başına 40 tane yıldız bilgo soft 10 karakter toplam 50
text=companyName.ljust(50,'*')#Bilgo Soft***************************
text=companyName.count("o")# değişkende kaç tane o varsa onu döner, yoksa 0 döner
text=companyName.find(" ") # boluk karakterinin indexini döner = 5
text=companyName.startswith("B")# değişken B ile başlıyor mu başlasa True başlamıyorsa False değer döner
text=companyName.startswith("Bilgo")# değişken Bilgo ile m i başlıyor True döner
text=companyName.endswith("t")# son harfi t ile mi bitiryo  True
text=companyName.upper()#BILGO SOFT
text=companyName.lower()#bilgo soft
text=companyName.title()# tüm kelimelerin 1. harflerini büyük harf çevirir

companyName2="   Bilgo soft    "
text=companyName2.strip()#baştaki ve sondaki başlığı silmek istersek
print(text)
text=companyName2.lstrip()#baştaki  başlığı silmek istersek
print(text)
text=companyName2.rstrip()#sondaki başlığı silmek istersek
print(text)

text=companyName2.split(" ")# ['','','','Bilgo','','soft','','',''] şeklinde parçalar ve listeye atar
print(text)

text="-".join(companyName2)# her karakter arasına - ekler. - - - B-i-l-g-o- -s-o-f-t- - - -
print(text)

text=companyName2.replace("s","S")
print(text)

text=companyName2.replace("s","S").replace("i","İ")
print(text)

text=companyName.swapcase()# büyük harfleri küçük küçükleri büyük yapmayı sağlar
print(text)

print(type(text))# <class 'str'>
print(type(age))# <class 'int'>