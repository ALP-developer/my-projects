print("""
****************
KULLANICI GİRİŞİ 
****************
""")



sys_kul_adı = "alp"

sys_parola  = "1234"

giriş_hakkı = 3
while True:
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")

    if (kullanıcı_adı != sys_kul_adı and parola == sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giriş_hakkı -= 1
        print("Giriş Hakkı: ", giriş_hakkı)
    elif (kullanıcı_adı == sys_kul_adı and parola != sys_parola):
        print("Parola Hatalı...")
        giriş_hakkı -= 1

        print("Giriş Hakkı: ", giriş_hakkı)
    elif (kullanıcı_adı != sys_kul_adı and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı...")
        giriş_hakkı -= 1
        print("Giriş Hakkı: ", giriş_hakkı)

    else:
        print("Başarıyla Giriş Yaptınız...")
        break
    if (giriş_hakkı == 0 ):

        print("Giriş Hakkınız Bitti...")
        break