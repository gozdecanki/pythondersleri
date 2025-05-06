ad ='Çınar'
soyad='Turan'
yas= 4

print('My name is {} {}'.format(ad, soyad))

print('My name is {1} {0}'.format(ad, soyad)) # yer değiştirdik index numarası ile

print('My name is {s} {n}'.format(n=ad, s=soyad))

# tek tırnak string ifadenin bir parçası olsun istiyorsak string ifadeyi çift tırnak ile yazammaız gerekir
print("My name is {} {}.I'm {} years old.".format(ad, soyad, yas))

# aynı değeri birden fazla yerde kullanmak için dex numarsı verip kullanabiliriz. ya da değişken ismi verip yaabiliriz
print("My name is {0} {1}.I'm {2} years old.{2}".format(ad, soyad, yas))

#noktadan sonra 3 rakam   n:1.3
number = 200/700
print('the result is {n:1.3}'.format(n=number)) # the result is 0.286

#10 sayısı yer tutucu olarak görev yapıyor. sayının kendisi ve nokta işareti dahil boşluklar 10 adettir
print('the result is {n:10.3}'.format(n=number)) # the result is      0.286

#f string
print(f"My name is {ad} {soyad} and I'm {yas} years old.")# My name is Çınar Turan and I'm 4 years old.