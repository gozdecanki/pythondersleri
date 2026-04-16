
# result = input("basvuru sonucunu giriniz: ")

# if(result=="olumlu"):
#     print("işe alındınız")
    
# else:
#     print("işe alınmadınız")


# number= int (input("sayı giriniz: "))
# if(number==50):
#     print("sayı 50")
    
# elif(number<0):
#     print("negatif")
    
# elif(number<50):
#     print("50 den küçük")
    
# elif(number>50):
#     print("pozitif")
    
# else:
#     print("50 den büyük")


# gender = input("cinsiyet bilgisi giriniz(E/K): ")

# if gender=="E":
#     BirtOfDate = int(input("doğum yılınızı giriniz: "))
    
#     if 2020-BirtOfDate ==20 or  2020-BirtOfDate >20 :
#         print("yasıız askere gitmeye elverişlidir.")
        
#     elif(2020-BirtOfDate !=20):
#         print("yasınız askere gitmeye elverişli değildir.")
    
#     else:
#         print("yasınız hesaplanamadı")
        
# elif gender=="K":
#      print("kadınlar askere alınamıyor")

# else:
#     print("hatalı giriş")


for keep in range(1,11):
    if(keep==6):
        break # keep 6 ise dögüyü kır çık . sonuc 1 den 5 e kadar alt alta yazacak
    print(keep)
    
    print("*****************")
for keep in range(1,11):
    if(keep==6):
        continue # keep 6 ise 1 den 10 a kadar yaz ama 6 yı yazmadan devam etmiş olacak. continue kendinden sonraki işlemi yapmaz döngüye devam eder. 
    print(keep)