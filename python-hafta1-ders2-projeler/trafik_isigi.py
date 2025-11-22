renk = input("Lütfen YEŞİL, SARI veya KIRMIZI giriniz: ").upper()

if renk == "KIRMIZI":
    print("DUR!")
elif renk == "SARI":
    print("Hazırlan.")
elif renk == "YEŞİL":
    print("Geç.")
else:
    print("Geçersiz renk seçimi!")
