try:
    sayi1 = int(input("1. sayıyı giriniz: "))
    sayi2 = int(input("2. sayıyı giriniz: "))
    sayi3 = int(input("3. sayıyı giriniz: "))

    if sayi1 == sayi2 == sayi3:
        print("Bütün sayılar eşit!")
    else:
        if sayi1 >= sayi2 and sayi1 >= sayi3:
            print(f"En büyük sayı: {sayi1}")
        elif sayi2 >= sayi1 and sayi2 >= sayi3:
            print(f"En büyük sayı: {sayi2}")
        else:
            print(f"En büyük sayı: {sayi3}")

except ValueError:
    print("Lütfen geçerli bir sayı giriniz!")
