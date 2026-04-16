# for keep in range(1,6,1):# 1-5 e kadar yazar 6 dahil değil
#     print(keep)
#     pass

# keep =1
# while(keep<=5):
#     print(keep)
#     keep +=1


# start=10
# while start >=1:
#     print(start)
#     start -=1


# #tek sayıları yazdır
# number= 1
# while(number<=10):
#     if(number %2 != 0):
#         print(number)
#     number +=1

#
# while(True):
#     print("Bilgo Soft")

# start =1
# while( start<=10):
#     if(start==6):
#         break #6 dan sonrası yazmaz
#     print(start)
#     start +=1

start =1
while( start<=10):
    if(start==6):
        start +=1
        continue #6 dan sonrası yazmaz ve çalışması da durmaz. program kitlenir kilitlenmemesi için üstte start +=1 yazıyoruz
    print(start)# sonuc olarak 1-10 a kadar 6 hariç yazar
    start +=1