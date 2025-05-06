import random

number= random.random() #0.0 - 1.1 aralığında

number= random.uniform(1,100) #1 ile 100 arasında ondalık sayı üretir

number = random.randint(1,100) #1 ile 100 arasında tam sayı üretir. 1 ve 100 dahil

number = random.randrange(1,100)

number= random.randrange(1,100,3)#1 ile 100 arasında 3 e bölümünden kalan 1 olan

print(number)

numbers =[1,2,3,4,5,6]
print(random.choice(numbers))# listeden rastgele seçim yapar

print(random.sample(numbers,4))# listeden rastgele 4 tane seçim yapar -> [4, 6, 1, 3]

number= random.randint(1,3)
guess= int(input("tahmininizi girin : "))
if(number==guess):
    print("tahmininiz doğru. Tebrikler")
else:
    print("hatalı tahmin")
