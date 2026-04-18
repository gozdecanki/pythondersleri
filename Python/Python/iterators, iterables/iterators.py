#iterable ?
#iterator?


sayilar=[1,2,3,4,5 ]
# for i in sayilar:
#     print(i)

# print(dir(sayilar))

iterator= iter(sayilar)
# print(next(iterator)) #1
# print(next(iterator)) #2
# print(next(iterator)) #3
# print(next(iterator)) #4
# print(next(iterator)) #5
# # print(next(iterator)) #6 yok ve hata alır

while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break

    