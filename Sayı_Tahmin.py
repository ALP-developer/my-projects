import time
import random

print("""*****************


    Sayı Tahmin Etme Oyunu

    1 ile 40 arasında sayıyı tahmin edin.

     *****************""")

rastkele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True:

    tahmin = int(input("Tahmininiz:"))

    if (tahmin < rastkele_sayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(2)

        print("Daha yüksek bir sayı söyleyin")
        tahmin_hakkı -= 1

    elif (tahmin > rastkele_sayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(2)

        print("Daha küçük bir sayı söyleyin")
        tahmin_hakkı -= 1

    else:
        print("Bilgiler sorgulanıyor....")
        time.sleep(2)

        print("Sayınız Doğru!!",rastkele_sayı)
        break

    if (tahmin_hakkı == 0):
        print("Tahmin hakkınız bitti")
        print("Sayınız:",rastkele_sayı)

        break








