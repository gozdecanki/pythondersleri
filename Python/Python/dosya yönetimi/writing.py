# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Eğer konumda aynı dosya varsa dosyayı siler ve yeni oluşturur. 
with open("D:/myworkspace/pythondersleri/Python/Python/newfile.txt","w",encoding="UTF-8") as file:
    file.write("Çınar Turan\n")
    file.write("Sadık Turan\n")
    file.write("Sena Turan") 
    print(file)

with open("D:/myworkspace/pythondersleri/Python/Python/newfile.txt") as file:
    print(file.read())