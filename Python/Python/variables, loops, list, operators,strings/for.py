
from cgi import print_exception


for keep in range(5): # range kaç defa döneceğini belirtmek için kullanılıyor. : 'yi kullanmak şart
    #print("hello")
    pass

for keep in range(1,10):# 1 den 10 a kadar yaz dedik ama 10 u dahil etmiyor. 9 a kadar yazıyor
    #print(keep)
 pass
    
for keep in range(10+1):# 0'dan 10 a kadar yazdı. başlangıç değeri vermezsek 0 ı baz alır
    #print(keep)
     pass
    
for keep in range(1,10,2):# 1 den 10 a kadar 2şer olarak yazacak. 1i yazdı 2yi atladı 3ü yazacak şeklinde
    #print(keep) # 1 3 5 7  9
     pass
    
    
for keep in range(2,10,2):# 1 den 10 arasındaki çift sayıları yazdırma. 
    #print(keep) # 2 4 6 8
     pass
    
    
for keep in range(1,10,2):# 1 den 10 a kadar 2şer olarak yazacak. 1i yazdı 2yi atladı 3ü yazacak şeklinde
    #print(keep) # 1,3,5,7,9
     pass

    
list1=[1,2,3,4,5,6,7,8,9,10]
for keep in list1:
    #print(keep) # tüm elemanları alt alta yazdı
    pass

for keep in "TÜRKİYE":
    #print(keep) # tüm elemanları alt alta yazdı. T Ü R K İ Y E
    pass
    
dic1={"name":"ali", "surname":"yıldırım"}

for keep in dic1.items():
   print(keep)   #  ('name','ali') ('surname','yıldırım')
   
#list2=[]
#for keep in range(1,1001): # ekrana 1 den 1000 e kadar yaz
    #list2.append(keep)
    
#print(list2) # liste biçiminde yazar

#for keep in list2:
    #print(keep) # alt alta yazar


#list2=[keep for keep in range(1,1001)] #liste şeklne yazar. append kullanmadan
#print(list2)

#yıldızlarla ekranda for kullanma

number= int(input("satır sayısı giriniz: "))

for keep in range(1,number+1):
    print("*"*keep) # keep değerim kadar yıldız bas
    
for keep in range(10,1-1,-1):  # baslangıc değeri bitiş degerinen büyükse 3. değişkene - yazmak zorundayız. 1-1 yazma sebebimiz de bitiş noktası dahil edilmediği içn 0 da yazabiliriz
        print(keep) # 10 dan 1 e kadar 1 dahil olarak ekrana teker teker yazdırmış olduk
        
for keep in range(10,0,-2):  
        print(keep) # 10 dan 1 e kadar çift sayıları yazdırdı 10 8 6 4 2