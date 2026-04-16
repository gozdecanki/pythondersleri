# sayilar =[2,5,7,9]

# i=1
# while i<=10:
#     print(f"{i} Merhaba")
#     i+=1


# while i<=100:
#     if(i%2==1):
#       print("tek sayi",i)
#     else:
#        print("çift sayi", i)
#     i+=1

# username=''
# print(bool(username))# false

# username='a'
# print(bool(username))# true

username=''
while not username: # username bilgisine değer girilmediği müddetçe dön. username set edilirse false olacak ve döngü duracak
    username= input('kullanıcı adınız:')

print('girdiğiniz kullanıcı adı:', username)