
print("""
********************
Hesap Makinesi Programı

İşlemler;
1. toplama işlemi
2. çıkarma işlemi
3. çarpma işlemi
4. bölme işlemi

*********************

""")

a = int(input("birinci sayı:"))
b = int(input("ikinci sayı:"))

islem = input("İşlemi giriniz:")

if islem == "1":
    print("{} ile {} ün toplamı {} dir.".format(a,b,a+b))
elif islem == "2":
    print("{} ile {} nin farkı {} dir.".format(a,b,a-b))
elif islem == "3":
    print("{} ile {} nin çarpımı {} dir.".format(a,b,a*b))
elif islem == "4":
    print("{} ile {} nin bölümü {} dir.".format(a,b,a/b))
else:
    print("Geçersiz işlem")

#######################################KULLANICI GİRİŞİ PROGRAMI####################

print("""
***************
KULLANICI GİRİŞİ
***************
""")

sys_kullaniciadi = "gizem"
sys_parola = "12345"

kullaniciadi = input("Kullanıcı adı:")
parola = input("Parola:")

if (kullaniciadi == sys_kullaniciadi and parola != sys_parola):
    print("Parola hatalı.")
elif (kullaniciadi != sys_kullaniciadi and parola == sys_parola):
    print("Kullanıcı adı hatalı.")
elif (kullaniciadi != sys_kullaniciadi and parola != sys_parola):
    print("Kullanıcı adı ve parola hatalı.")
else:
    print("Sisteme giriş yapıldı.") 