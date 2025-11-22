sifre = input("Şifre giriniz (en az 6 karakter): ")

if len(sifre) < 6:
    print("Şifre çok kısa!")

elif sifre == "16bursa16":
    print("Giriş başarılı!")

else:
    print("Yanlış şifre!")
