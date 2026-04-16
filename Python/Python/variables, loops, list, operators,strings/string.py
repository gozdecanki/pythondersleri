ad ="Gözde"
soyad="Cankı"
yas="32"

msg="Benim adım " + ad + " ve soyadım "+ soyad + ".Yaşım ise "+ yas + "."

karakterSayisi= len(msg)
print(karakterSayisi)
print(msg) # Benim adım Gözde ve soyadım Cankı.Yaşım ise 32.
print(msg[0]) # B
print(msg[1]) # e
print(msg[-1]) # .  '-' ile başlayınca tersten bakıyoruz
print(msg[karakterSayisi-1]) # .


print(msg[0:5]) # Benim 0-4 dahil 5 dahil değil

print(msg[6:16]) # adım Gözde 16. index dahil değil
print(msg[:10]) # Benim adım en baştan 10. indexe kadar yazar 10 dahil değil
print(msg[10:]) #  Gözde ve soyadım Cankı.Yaşım ise 32. 10. indexten  başlar en sona kadar yazar

# Benim adım Gözde ve soyadım Cankı.Yaş/ım ise 32/.
print(msg[-10:-1]) # ım ise 32 şeklinde sonuç döner. -1 indexi dahil değil

#Benim adım Gözde ve soyadım Cankı.Yaşım ise 32.
print(msg[0:40:2]) # 0 dan 40 a kadar 2 şer 2 şer -> Bnmaı öd esydmCnıYşm

print(msg[::1])# baştan sona 1 er 1 er -> Benim adım Gözde ve soyadım Cankı.Yaşım ise 32.
print(msg[::-1])# en sondan başa doğru yazar-> .23 esi mışaY.ıknaC mıdayos ev edzöG mıda mineB

