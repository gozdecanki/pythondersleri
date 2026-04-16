import re

cp="Bilgo Soft"

print(re.findall("o",cp)) # ['o', 'o']
print(re.findall("x",cp)) # []


print(re.split(" ",cp)) #['Bilgo', 'Soft']
print(len(re.split(" ",cp))) #2

print(re.search("Bilgo", cp))#<re.Match object; span=(0, 5), match='Bilgo'>
print(re.search("Bilgo", cp).span())#(0,5)
print(re.search("Bilgo", cp).start())#0 , başlangıç index numarası
print(re.search("Bilgo", cp).end())#5 , bitiş index numarası
print(re.search("o", cp).group())# o, 2 adet var ama 1 tanesini yazar.


