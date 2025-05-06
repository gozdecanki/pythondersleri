import re # regular expressions kütüphanesi

# number = int (input("Sayı giriniz: "))
#
# if(number==0):
#     raise Exception("0 Kabul edilen bir değer değildir")


password = input("Şifre oluşturunuz: ")
#1. en az 6 karakter
if(len(password)<6):
    raise Exception("En az 6 karakter olmalıdır")

#2. en az 1 büyük
elif not re.search("[A-Z]", password): # password ün içinde büyük harf yoksa
    raise Exception("En az 1 büyük harf olmalı")

#3. en az 1 küçük
elif not re.search("[a-z]", password):
    raise Exception("En az 1 küçük harf olmalı")

#4. en az 1 rakam
elif not re.search("[0-9]", password):
    raise Exception("En az 1 rakam olmalı")
else:
    print("şifre oluşturulmuştur : " , password)