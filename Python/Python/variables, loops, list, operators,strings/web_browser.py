import webbrowser as wb

url= "https://www.bilgosoft.com/"

new=0 # 0- 1 -2 , hangi sayfada nasıl açılacağını belirtiyoruz. default olarak 0.
# 0 ise aynı, 1 ise farklı pencerede, 2 ise aynı pencerede farklı sekmede açılır

autoraise= True

#3 ü de birbirinin yerine geçebilir
#wb.open(url,new,autoraise)
#wb.open_new(url) # aynı pencere farklı sekme
wb.open_new_tab(url) # aynı pencere farklı sekme
