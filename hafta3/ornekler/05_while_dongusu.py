# =============================================================
# DERS 5: while Döngüsü
# =============================================================
# Bu derste öğreneceğiz:
#   - while koşul: ile koşula dayalı tekrarlama
#   - Sayaç kullanımı
#   - break ile döngüden çıkma
#   - while True: + break deseni


# --- Basit while Döngüsü ---
# while, koşul True olduğu sürece çalışır.
# Koşul False olunca durur.

print("=== Geri Sayım ===")
sayac = 5
while sayac > 0:
    print(sayac, end="... ")
    sayac = sayac - 1    # Her seferinde 1 azalt (bu olmazsa sonsuz döngü!)
print("Başla!")


# --- Sayaçla Toplama ---
print()
print("=== 1'den 10'a Toplam ===")
toplam = 0
sayi = 1
while sayi <= 10:
    toplam = toplam + sayi
    sayi = sayi + 1

print("1+2+3+...+10 =", toplam)


# --- break ile Döngüden Çıkma ---
# break komutu döngüyü anında sonlandırır.

print()
print("=== Tahmin Oyunu ===")
gizli_sayi = 7

# input() her zaman metin (str) döndürür. Sayı olarak kullanmak için int() ile çevirmeliyiz.
# Hatırla: Hafta 2'de bu dönüşümü görmüştük.
tahmin = int(input("1-10 arası bir sayı tahmin et: "))

deneme = 1
while tahmin != gizli_sayi:
    if tahmin < gizli_sayi:
        print("Daha büyük!")
    else:
        print("Daha küçük!")
    tahmin = int(input("Tekrar dene: "))
    deneme = deneme + 1

print("Tebrikler!", deneme, "denemede bildin!")


# --- while True + break Deseni ---
# Yukarıdaki "while koşul:" kalıbı: koşul baştan belli olduğunda kullanılır.
# Aşağıdaki "while True + break" kalıbı: koşulun döngü içinde belirlenmesi gerektiğinde kullanılır.
# Kullanıcıdan sürekli veri almak istediğimizde idealdir.
# "bitti" yazana kadar devam eder.

print()
print("=== Malzeme Toplama ===")
print("Malzeme ismi gir (çıkmak için 'bitti' yaz)")

malzemeler = []
while True:
    girdi = input("Malzeme: ")
    if girdi == "bitti":
        break                  # Döngüden çık
    malzemeler.append(girdi)

print()
print("Toplanan malzemeler:", malzemeler)
print("Toplam:", len(malzemeler), "adet")
