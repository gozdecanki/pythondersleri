name = "Gözde Cankı"


# for harf in name:
#     if(harf=="d"):
#         continue #d yi gördüğünde işlem yapma atla demiş olduk
#     print(harf)

# for harf in name:
#     if(harf=="d"):
#         break #d yi gördüğünde işlem yapma döngüyü bitir
#     print(harf)


# i=0
# while(i<5):
#     if(i==3):
#         break
#     print(i)
#     i+=1
# print('döngü bitti')#012 3 ve sonrası yazmaz


#1-100 arası çift sayı toplamı
toplam=0
i=0
while i<=100:
    i+=1
    if(i%2==1):
        continue #tekleri atla
    toplam +=i

print("toplam:", toplam)

