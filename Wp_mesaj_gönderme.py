# pywhatkit modulumuz

import pywhatkit as kit


# ilk aralığa gönderilecek numara 2.aralığa text 3.aralığa gönderilecek saat

try:
    kit.sendwhatmsg("+90549*********","Beni Takip Et :) ",11,50)
    print("Mesaj Gönderildi")

except:

    print("Beklenmeyen bir hata oluştu.")
