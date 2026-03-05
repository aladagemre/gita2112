# Hafta 2 - Örnek 8: Hesap Makinesi
# Kullanılan kavramlar: input(), int/float, if/elif/else, iç içe if, boolean, and

sayi1 = float(input("Birinci sayıyı gir: "))
sayi2 = float(input("İkinci sayıyı gir: "))
islem = input("İşlem seç (+, -, *, /): ")

sonuc_var = True

if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 - sayi2
elif islem == "*":
    sonuc = sayi1 * sayi2
elif islem == "/":
    if sayi2 == 0:
        print("Hata: Sıfıra bölme yapılamaz!")
        sonuc_var = False
    else:
        sonuc = sayi1 / sayi2
else:
    print(f"'{islem}' geçerli bir işlem değil.")
    sonuc_var = False

if sonuc_var:
    print(f"Sonuç: {sayi1} {islem} {sayi2} = {sonuc}")

    pozitif = sonuc > 0
    sifir = sonuc == 0

    if pozitif:
        print("Sonuç pozitif.")
    elif sifir:
        print("Sonuç sıfır.")
    else:
        print("Sonuç negatif.")

    if sayi1 > 0 and sayi2 > 0:
        print("İki sayı da pozitifti.")
