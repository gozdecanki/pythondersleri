import numpy as np


# python list
py_list =[1,2,3,4,5,6,7,8,9]

#numpy array
np_array= np.array([1,2,3,4,5,6,7,8,9])# liste gönderiyoruz

print (type(py_list))#list
print (type(np_array))#numpy.ndarray

py_multi = [[1,2,3],[4,5,6],[7,8,9]]

np_multi = np_array.reshape(3,3)#3*3 matris

print(py_multi)
print(np_multi)

print(np_array.ndim)#1 boyutlu
print(np_multi.ndim)#2 boyutlu

print(np_array.shape)#(9,)
print(np_multi.shape)#(3,3)