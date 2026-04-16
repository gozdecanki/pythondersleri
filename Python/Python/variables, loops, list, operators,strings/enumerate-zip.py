# markalar=["opel","bmw","mercedes"]

# index =0
# for marka in markalar:
#     index +=1
#     print(f"{index}-{marka}")

# index =0
# for marka in markalar:
#     print(f"{index+1}-{markalar[index]}")
#     index+=1

#enumarate

# obj1= enumerate(markalar)
# print(type(obj1)) #<class 'enumerate'>
# print(list(obj1)) #[(0, 'opel'), (1, 'bmw'), (2, 'mercedes')]

# for i in enumerate(markalar):
#     print(i)
#  sonuç  : 
# (0, 'opel')
# (1, 'bmw')
# (2, 'mercedes')

# for index,value in enumerate(markalar):
#     print(f"{index} - {value}")

# for index,value in enumerate(markalar):
#     print(f"{index+1} -{value}")

# for index,value in enumerate(markalar,10):#listeye 10 dan başla
#     print(f"{index} - {value}") #10 - opel 11 - bmw 12 - mercedes


#zip

liste1= [1,2,3,4,5]
liste2 =['a','b','c','d','e']
liste4 =[100,200,300,400,500]
# #liste3 =['a','b','c','d','e','f']
# print(list(zip(liste1,liste2))) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
# #print(list(zip(liste1,liste3))) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')] #eşleşmeyenler yazılmaz f ile eşleşecek sayı yok o 
# print(list(zip(liste1,liste2,liste4))) #[(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]

for item in zip(liste1,liste2):
    print(item)

for a,b,c in zip(liste1,liste2,liste4):
    print(a,b,c) #1 a 100 2 b 200 .....