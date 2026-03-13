gizli_kelime = "python"
tahminler = []
hak = 6

while hak > 0:
    print("Kalan hak:", hak)

    # Kelimenin durumunu göster
    gosterim = ""
    for harf in gizli_kelime:
        if harf in tahminler:
            gosterim += harf + " "
        else:
            gosterim += "_ "

    print(gosterim)

    # Kazanma kontrolü
    if "_" not in gosterim:
        print("Tebrikler, kazandınız!")
        break

    tahmin = input("Bir harf tahmin edin: ").lower()

    if tahmin in tahminler:
        print("Bu harfi zaten tahmin ettiniz!")
    elif tahmin in gizli_kelime:
        tahminler.append(tahmin)
        print("Doğru!")
    else:
        tahminler.append(tahmin)
        hak -= 1
        print("Yanlış!")

if hak == 0:
    print("Haklar bitti! Kelime:", gizli_kelime)
