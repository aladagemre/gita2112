# =============================================================
# ÖDEV 2: Tasarım Hesaplayıcı  [Kolay-Orta]
# =============================================================
# Bu ödevde yapacakların:
#   - return ile değer döndüren fonksiyon yazma
#   - Fonksiyon sonucunu değişkene atama
#   - Fonksiyonu f-string içinde kullanma
#
# Konu: return + parametre + matematik
# Kazanım: return ile print arasındaki farkı kavramak
# =============================================================


print("=== Tasarım Hesaplayıcı ===")
print()


# --- Görev 1: Dikdörtgen Alan ---
# Poster boyutlarını alıp alanını döndüren fonksiyon.
# İpucu: genislik * yukseklik hesapla ve return ile döndür.

def dikdortgen_alan(genislik, yukseklik):
    return ...  # ← genislik * yukseklik


# A3 poster: 29.7 x 42 cm
a3_alan = dikdortgen_alan(29.7, 42)
print(f"A3 poster alanı: {a3_alan:.1f} cm²")

# A4 kağıt: 21 x 29.7 cm
a4_alan = dikdortgen_alan(21, 29.7)
print(f"A4 kağıt alanı: {a4_alan:.1f} cm²")


# --- Görev 2: Daire Alan ---
# Sticker çapını alıp alanını döndüren fonksiyon.
# Daire alanı = 3.14159 * yarıçap ** 2
# İpucu: Çapı yarıçapa çevirmek için 2'ye böl.

print()

def sticker_alani(cap):
    yaricap = cap / 2
    return ...  # ← 3.14159 * yaricap ** 2


# 5 cm çapında sticker
print(f"5 cm sticker alanı: {sticker_alani(5):.1f} cm²")

# 8 cm çapında sticker
print(f"8 cm sticker alanı: {sticker_alani(8):.1f} cm²")


# --- Görev 3: İndirimli Fiyat ---
# Ürün fiyatını ve indirim yüzdesini alıp
# indirimli fiyatı döndüren fonksiyon.

print()

def indirimli_fiyat(fiyat, yuzde):
    indirim = fiyat * yuzde / 100
    return ...  # ← fiyat - indirim


poster_fiyat = indirimli_fiyat(120, 25)
sticker_fiyat = indirimli_fiyat(35, 10)

print(f"Poster (25% indirim): {poster_fiyat:.2f} TL")
print(f"Sticker (10% indirim): {sticker_fiyat:.2f} TL")
print(f"Toplam: {poster_fiyat + sticker_fiyat:.2f} TL")


# --- Görev 4: Sonuçları Karşılaştır ---
# A3 alanı A4'ün kaç katı? Fonksiyon sonuçlarını kullanarak hesapla.

print()
oran = ...  # ← a3_alan / a4_alan
print(f"A3, A4'ün {oran:.1f} katı büyüklüğünde.")


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Tasarım Hesaplayıcı ===
#
# A3 poster alanı: 1247.4 cm²
# A4 kağıt alanı: 623.7 cm²
#
# 5 cm sticker alanı: 19.6 cm²
# 8 cm sticker alanı: 50.3 cm²
#
# Poster (25% indirim): 90.00 TL
# Sticker (10% indirim): 31.50 TL
# Toplam: 121.50 TL
#
# A3, A4'ün 2.0 katı büyüklüğünde.
