#farklı bir uygulama çalıştırmak için kullanılır
import subprocess as sp

app = input("lütfen çalıştırmak istediğiniz uygulamayı giriniz :")

sp.call(app) # notepad.exe yazdığımızda uygulama açılır