# def sayi_say(max):
#     sayi=1
#     sayilar=[]
#     while sayi<=max:
#         sayilar.append(sayi)
#         sayi +=1
#     return sayilar


# sonuc=sayi_say(10)
# print(sonuc)


def sayi_say(max):
    sayi=1
    # sayilar=[]
    while sayi<=max:
        # sayilar.append(sayi)
        yield sayi
        sayi +=1


# sonuc=sayi_say(10)
# print(next(sonuc))
# print(next(sonuc))
# print(next(sonuc))
# print(next(sonuc))....

# generator =sayi_say(10)
# print(help(generator))
# iterator = iter(generator)
# print(next(iterator))

# iterator = sayi_say(10) # generator tipinde oldğ. için zaten sınıfra özel olarak iter func tanımlı
# print(next(iterator))
# print(next(iterator))

# for i in iterator: # 3. indexten devam eder yazmaya
#     print(i)

# iterator = sayi_say(10) 
# sonuc = list(iterator)
# print(sonuc)


generator = (i for i in range(1,11))
print(generator)
print(next(generator))