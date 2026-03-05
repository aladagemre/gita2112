# =============================================================
# DERS 3: for Döngüsü ve range()
# =============================================================
# Bu derste öğreneceğiz:
#   - for i in range(n) ile tekrarlama
#   - range(başlangıç, bitiş) kullanımı
#   - range(başlangıç, bitiş, adım) kullanımı
#   - Döngü içinde print()


# --- Basit Tekrar: range(n) ---
# range(5) → 0, 1, 2, 3, 4 sayılarını üretir (5 dahil değil!)
# for döngüsü bu sayıları sırayla i değişkenine atar.

print("=== Basit Sayma ===")
for i in range(5):
    print("Sayı:", i)


# --- Katman Numaralama ---
# Tasarım yazılımlarında katmanlar numaralanır.
# range(1, 11) → 1'den 10'a kadar (11 dahil değil)

print()
print("=== Katman Listesi ===")
for katman in range(1, 11):
    print("Katman", katman)


# --- Adımlı Sayma: range(başlangıç, bitiş, adım) ---
# Üçüncü parametre adım büyüklüğünü belirler.

print()
print("=== İkişer İkişer ===")
for sayi in range(0, 11, 2):
    # end=" " → print sonunda satır atlamak yerine boşluk koyar (yan yana yazdırır)
    print(sayi, end=" ")
print()  # Satır sonu


print()
print("=== Beşer Beşer ===")
for sayi in range(0, 51, 5):
    print(sayi, end=" ")
print()


# --- Geri Sayım ---
# Adımı negatif yaparsak geri sayarız.

print()
print("=== Geri Sayım ===")
for sayi in range(10, 0, -1):
    print(sayi, end="... ")
print("Başla!")


# --- Döngü İçinde Hesaplama ---
# Döngü değişkenini işlemlerde kullanabiliriz.

print()
print("=== Kare Sayılar ===")
for n in range(1, 6):
    kare = n * n
    print(n, "×", n, "=", kare)
