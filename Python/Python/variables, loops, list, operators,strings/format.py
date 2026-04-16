
# string Format

#1.YÖNTEM
print("Hello"+"World")# iki kelimeyi birleştirir HelloWorld
print("Hello"+" "+"World")# iki kelimeyi birleştirir araya boşluk koyar Hello World

company ="Bilgo Soft"

print(company, "bir yazılım kuruluşudur")# Bilgo Soft bir yazılım kuruluşudur
print(company+" "+"bir yazılım kuruluşudur")# Bilgo Soft bir yazılım kuruluşudur
print( "{0} bir yazılım kuruluşudur".format(company))# Bilgo Soft bir yazılım kuruluşudur

company1="Bilgo"
company2="Soft"
#0 ve 1 index numarasıdır format metodundaki değişkenlerin
print( "{0} {1} bir yazılım kuruluşudur".format(company1,company2))# Bilgo Soft bir yazılım kuruluşudur

print( "{C1} {C2} bir yazılım kuruluşudur".format(C1=company1,C2=company2))# Bilgo Soft bir yazılım kuruluşudur

print(f"{company} {company1} bir yazılım kuruluşudur")



name="Gözde"
surname="Cankı"
age=30
job="Mühendis"
city="Ankara"
salary="5000.68"

print(f"Merhaba,\n\tBenim adım {name}, soyadım {surname}. Ben {age} yaşındayım. Ben {job}im. Ben {city}'de yaşıyorum. Ben {salary} TL kazanıyorum.")

number1=5
number2=10
print(f"Toplam: {number1 + number2 }\nÇıkarma: {number1-number2}\nÇarpma: {number1*number2}\nBölme: {number1/number2}")