
# hjsdfhgddhjgh    ctrl + k +c çoklu satır yorum yapma
# vcvc            ctrl + k + u


#Değişken tanımı
# degiskenIdmi= DegiskenDegeri

# Değişken sayı ile başlayamaz
# programa ait ifadeler değişken ismi olamaz 
# özel arakterler kullanılamaz


# DEĞİŞKEN TÜRLERİ
#string : metinsel ifadeleri ve matematisel işlem yapılmayan sayıları tutmamızı sağlar
phoneNumber='5025654220'
phoneNumber="5025654220' nın"
phoneNumber="""5025654220"""
# 3başa 3 sona çift tırnak koymak ; ekranda bu formatta bir metin göstermek istiyorsak bu şekilde yazmamız gerekir

#integer: tam sayıları tutmamızı sağlar.
number1= 5

#değişken tanımlama kullarına örnek
# 1number1=5
# for=5
# number?=5



#float: ondalıklı sayıları tutmamızı sağlar.
#5,5 şeklinde virgülle yazamayız. , python da farklı bir şekilde kullanılıyor
number2= 5.5


#bool: mantıksal ifadeleri tutmamızı sağlar.
bool1= True
bool1= False

print(bool1)


a=5
b=10
a=b

print(a)
print(b)


#int to float
age = 30
result = float(age)
print(result)

#float to int
result=int(result)
print(result)
print(type(result))

#bool to str
isStudent = True
result = str(isStudent)
print(result) #True
print(type(result)) # <class 'str'>

#bool to int
result = int(isStudent)
print(result) # 1
print(type(result)) # <class 'int'>
