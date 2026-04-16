#operatörler : Sayısal, metinsel veya mantıksal işlemleri yapmamızı sağlayan yapılardır.
number1 = 1
number2 = 2
number3 = 3



#Aritmetik operatörler : matematiksel işlemler yapmamızı sağlayan operatörlerdir
result= number1 + number2
print(result)
result= number1 - number2
print(result)
result= number1 * number2
print(result)
result= number1 / number2
print(result)

result= number1 // number2 # tam bölme ifadesi
print(result)

result= number1 % number2 # mod alma
print(result)

result= number1 ** number2 # üs alma ifadesi
print(result)


#Atama operatrleri : veri ataması için kullandığımız operatörlerdir
number1 = 5 # = ifadesi atama operatörüdür
number1 += 1# += ifadesi atama ifadesidir. number1 ifadesine 1 ekle 
print(number1)#6 döner

print("test")

number1 += 1
print(number1)

number1 -= 1
print(number1)

number1 *= 1
print(number1)

number1 /= 1
print(number1)

number1 //= 1
print(number1)

number1 %= 1
print(number1)

number1 **= 1
print(number1)

#Karşılaştırma Operatörleri : birden fazla değişkenin değerlerinin karşılastırıması için kullanıla operatörlerdir.

result= number1 == number2 # number1 number2 ye eşit mi
print(result)

result= number1 != number2 # number1 number2 ye eşit değil mi
print(result)

result= number1 < number2 # number1  number2 den küçük mü
print(result)

result= number1  > number2 # number1  number2 den büyük mü
print(result)

result= number1 <= number2 # number1  number2 den küçük mü veya eşit mi
print(result)

result= number1 >= number2 # number1  number2 den büyük mü veya eşit mi
print(result)

#Mantıksal Operatörler: birden fazla değişkeni aynı anda değerlendirmek için kullanılan operatörlerdir

result= number1 == 5 and number2 == 30 # and her iki tarafında yazdığımız şartların doğru olması gerekir true dönmesi için
print(result)
result= number1 == 5 or number2 == 30 
print(result)