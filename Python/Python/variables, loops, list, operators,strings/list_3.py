diller=["Python","C#","Java","Javascript", "React"]

sonuc =diller
print(sonuc)

sonuc=type(diller)
print(sonuc)

sonuc=diller[0:2]#2.index dahil değil ['Python', 'C#']
print(sonuc)

sonuc=diller[2:]#2. indexten sona kadar. ['Java', 'Javascript', 'React']
print(sonuc)

sonuc=diller[:3]# baştan başla 3. index dahil değil
print(sonuc)

sonuc=diller[-1]# React
print(sonuc)

sonuc=diller[-4 :-1]# ['Python', 'C#', 'Java'] -1. index dahil değil
print(sonuc)

diller[0]="Html" #0. indexin değerini değiştirmiş olduk
#diller[-1]="Html" #-1. indexin değerini değiştirmiş olduk
sonuc=diller
print(sonuc)

sonuc=len(diller)
print(sonuc)#5

sonuc= diller+["Angular","Vuejs"]
print(sonuc)# ['Html', 'C#', 'Java', 'Javascript', 'React', 'Angular', 'Vuejs']

if"Java" in diller:
    print("evet değer listenin bir elemanı")


for x in diller:
    print(x)#diller alt alta yazar

 #   Html
 #  C  #
 #  Java
 #  Javascript
 #  React


del diller[0]# 0. indexteki elemanı siler
print(diller)# ['C#', 'Java', 'Javascript', 'React']