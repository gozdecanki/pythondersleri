#
# #sayı girilen kısma string girildiğinde hata yönetimi
# try:
#     number = int(input("Sayı giriniz : "))
#     print(number)
#
# except:
#     print("Sayı giriniz")#hata varsa bu kısım çalışır
#
# else:
#     print("Hatasız çalıştı")# hata yoksa bu kısım çalışır
#
# finally:
#     print("Bilgo soft")# hata varsa da yoksa da çalışır
#

# try:
#     number1= float(input("1. sayısı giriniz:"))
#     number2= float(input("2. sayısı giriniz:"))
#     print(f"{number1}/{number2}= {number1/number2}")
# except Exception as error:
#     print("hatalı giriş yapıldı")
#     print(error)
# except ValueError as vError:
#     print("değer hatası")
# except ZeroDivisionError as zeroError:
#     print("bolen 0 olamaz.")
#     print(zeroError)
# except:
#     print("hatalı giriş")
# else:
#     pass
# finally:
#     print("bilgo soft")

try:
    number1= float(input("1. sayısı giriniz:"))
    number2= float(input("2. sayısı giriniz:"))
    options = input("""Toplama:+
    Çıkarma: -
    Çarpma : *
    Bölme : /
    seçim: """)

    if(options=="+"):
        print(f"{number1}{options}{number2} = {number1 +number2}")
    elif (options == "-"):
        print(f"{number1}{options}{number2} = {number1 - number2}")
    elif(options=="*"):
        print(f"{number1}{options}{number2} = {number1 * number2}")
    elif (options == "/"):
        print(f"{number1}{options}{number2} = {number1 / number2}")
    else:
        print("hatalı giriş")
except Exception as error:
    print("hatalı giriş",  error)
else:
    print("program hatasız")
finally:
    print("bilgo soft")