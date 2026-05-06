import numpy as np

#result= np.array([1,3,5,7,9])
# OR
#result= np.arange(1,10)#1 dahil 2. dahil değil: 1 den 9 a kadar 9 dahil
#result= np.arange(1,100,3)
#result= np.zeros(10)#[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#result= np.ones(10)#[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]


#result = np.linspace(0,100,5)#[  0.  25.  50.  75. 100.] 5 eşit parcaya böler verilen aralığı
#result = np.linspace(0,5,5) #[0.   1.25 2.5  3.75 5.  ]

#result = np.random.randint(0,10)#0-9 dahil sayı üretir
#result = np.random.randint(20)#0 dan 20 ye kadar rastgele sayı üretir

#result = np.random.randint(1,10,3)#1 ile 10 arasında 3 sayı üret. liste şeklinde döner
#result = np.random.rand(5)# 0 ile 1 arasında 5 sayı üretir. [0.53887606 0.27694611 0.19155203 0.4056201  0.10863612]
#result = np.random.randn(5)# eksi değerler de üretilir.[ 1.73764241  0.50025834 -1.0771176   1.27654876 -2.64649681]

# np_array = np.arange(50)
# np_multi= np_array.reshape(5,10)
# print(np_multi)

# print(np_multi.sum(axis=1))# satır toplamı
# print(np_multi.sum(axis=0))#sütun toplamı

rnd_numbers = np.random.randint(1,100,10)#1-100 arasında 10 sayı üret

# result= rnd_numbers.max()
# result= rnd_numbers.min()
# result= rnd_numbers.mean()
#result= rnd_numbers.argmax()#en büyük sayının indexini getirir
result= rnd_numbers.argmin()#en küçük sayının indexini getirir
print(result)