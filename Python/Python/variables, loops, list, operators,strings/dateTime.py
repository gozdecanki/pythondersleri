import datetime as dt

print(dt.datetime.now()) # 2025-05-06 19:07:12.333559

print(dt.datetime.now().time()) #19:07:32.659881
print(dt.datetime.now().hour) #19
print(dt.datetime.now().minute) #8
print(dt.datetime.now().second) #29
print(dt.datetime.now().day) #6
print(dt.datetime.now().month) #5
print(dt.datetime.now().year) #2025

print(f"Sistem tarihi : {dt.datetime.now().day}/{dt.datetime.now().month}/{dt.datetime.now().year}")#Sistem tarihi : 6/5/2025