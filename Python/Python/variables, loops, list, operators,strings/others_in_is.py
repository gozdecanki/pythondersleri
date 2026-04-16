# Identity Operator: is

# x=y=[1,2,3]
# z=[1,2,3]

# print(x==y) # true
# print(x==z) # true
# print(x is y)# true 
# print(x is z)# false burada referans olarak eşit olmadıkları için false dönüyor

x=[1,2,3]
y=[2,4]
print(x is y)# false

#y yi x e benzetelim
del x[2]
y[1]=1
y.reverse()

print(x==y) #true
print(x is y)#false
print(x is not y)#true

#özetle == içerik kontrolü, is ise referans kontrolü

#Membership operator:in

x=['apple','banana']
print('banana' in x)

name='Çınar'
print('a' in name)
print('a' not in name)