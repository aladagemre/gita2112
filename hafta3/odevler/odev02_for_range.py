# =============================================================
# ÖDEV 2: for + range() — Katman Oluşturucu  [Kolay]
# =============================================================
# Bu ödevde yapacakların:
#   - range() ile sayı dizisi oluştur
#   - for döngüsüyle tekrarlı işlemler yap
#   - Farklı range() kullanımlarını dene
#
# Konu: for + range()
# Kazanım: range() parametrelerini anlayıp kullanabilmek
# =============================================================


print("=== Katman Oluşturucu ===")
print()


# --- Görev 1: Katman Listesi ---
# 1'den 8'e kadar katman numarası yazdır.
# İpucu: range(1, 9)

print("--- Katmanlar ---")
for katman in range(...):  # ← range içine doğru sayıları yaz
    print("Katman", katman)


# --- Görev 2: Çift Numaralı Katmanlar ---
# 2, 4, 6, 8, 10 yazdır (ikişer ikişer)
# İpucu: range(2, 11, 2)

print()
print("--- Çift Katmanlar ---")
for katman in range(...):  # ← başlangıç, bitiş, adım
    print("Katman", katman)


# --- Görev 3: Geri Sayım ---
# 5'ten 1'e geri say, sonra "Render başladı!" yazdır.
# İpucu: range(5, 0, -1)

print()
print("--- Render Geri Sayım ---")
for sayi in range(...):  # ← geri sayım için doğru değerler
    print(sayi, end="... ")
print("Render başladı!")


# --- Görev 4: Katman Boyutu Hesaplama ---
# Her katman için genişlik hesapla.
# Katman 1 → 100px, Katman 2 → 200px, ..., Katman 5 → 500px
# İpucu: genislik = katman * 100

print()
print("--- Katman Boyutları ---")
for katman in range(1, 6):
    genislik = ...  # ← katman * 100 hesapla
    print("Katman", katman, "→", genislik, "px")


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Katman Oluşturucu ===
#
# --- Katmanlar ---
# Katman 1
# Katman 2
# Katman 3
# Katman 4
# Katman 5
# Katman 6
# Katman 7
# Katman 8
#
# --- Çift Katmanlar ---
# Katman 2
# Katman 4
# Katman 6
# Katman 8
# Katman 10
#
# --- Render Geri Sayım ---
# 5... 4... 3... 2... 1... Render başladı!
#
# --- Katman Boyutları ---
# Katman 1 → 100 px
# Katman 2 → 200 px
# Katman 3 → 300 px
# Katman 4 → 400 px
# Katman 5 → 500 px
