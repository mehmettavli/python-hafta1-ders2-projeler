try:
    notu = int(input("0 ile 100 arasında not giriniz: "))

    if 90 <= notu <= 100:
        print("AA")
    elif 80 <= notu <= 89:
        print("BA")
    elif 70 <= notu <= 79:
        print("BB")
    elif 60 <= notu <= 69:
        print("CB")
    elif 50 <= notu <= 59:
        print("CC")
    elif 0 <= notu <= 49:
        print("FF")
    else:
        print("Lütfen 0 ile 100 arasında bir değer giriniz!")

except ValueError:
    print("Lütfen sayı giriniz!")
