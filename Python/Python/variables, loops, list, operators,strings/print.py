
print("Hello world")
print('Hello world')
print("""Hello world""")


print("""Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
""") # buraya yazarsak 3 tırnagı bir alt satı boş bırakıyor. hello worldün devamına yazarsak boşluk bırakmaz
print(5)


print("""Hello world
Hello world
Hello world
Hello world
Hello world
Hello world""") # bu seilde yazdığımız için boşluk bırakmaz aşağı satırda
print() # ekranda bos satır oluşturur
print(5)


print("""Hello world
Hello world
Hello world
Hello world
Hello world
Hello world""", "\n") # \n kaçış dizisi alt satırda boşluk  bırakır
print(5)


print("Hello", end="\n")# hello yazdıktan sonra bir alt satıra geç. end bu ifade bitince ne olacağını belirler
print("World")
# çıktısı    Hello   şeklinde alt alta yazacak
# alt satrda World

print("Hello", end="")# hello yazdıktan sonra world yazacak çıktısı HelloWorld şeklindedir
print("World")


print("Hello", end="\t")# hello yazdıktan sonra bir tab kadar boşluk bırakıp world yazacak çıktısı Hello    World şeklindedir
print("World")


print("Hello", end=".")# hello yazdıktan sonra . bırakıp world yazacak çıktısı Hello.World şeklindedir
print("World")


print(5.5)
print(True)
# print(true) name 'true' is not defined

print("Merhaba", 5, False) # Merhaba 5 False çıktısı

number1=5
print(number1)

company="bilgosoft"

number2=10
print(number1, number2, company)


#sep keywordu her ifadenin arasına eklenecek ifadeyi söyler
print("Hello", "World", "Python", sep="-")# Hello-World-Python çıktısı
print("Hello", "World", "Python", sep="\t")# Hell    World      Python çıktısı


print(5-5)#matematiksel işlem sonuc 0

number=10
print(number-5) #matematiksel işlem sonuc 5
print(number-number) #matematiksel işlem sonuc 0

print("Hello"*5)#HelloHelloHelloHelloHello ekrana 5 tane Hello yazdı
#print("Hello" + 5) işlemi sonuç vermez hata alırız