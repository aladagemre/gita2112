# =============================================================
# DERS 3: return — Fonksiyondan Değer Döndürme
# =============================================================
# Bu derste öğreneceğiz:
#   - return anahtar kelimesi
#   - print vs return farkı (ÇOK ÖNEMLİ!)
#   - Döndürülen değeri değişkene atama
#   - Fonksiyonu ifade içinde kullanma
#   - return ile fonksiyonun bitmesi
# =============================================================


# --- Sorun: print ile Sonucu Kullanamıyoruz ---

def ortalama_yanlis(puanlar):
    toplam = 0
    for p in puanlar:
        toplam += p
    print(toplam / len(puanlar))    # Ekrana yazar ama...


sonuc = ortalama_yanlis([85, 90, 78])
print("Sonuç:", sonuc)
# Çıktı:
#   84.33333333333333    ← print yazdırdı
#   Sonuç: None          ← ama sonuc değişkeni boş!

# Neden? print() ekrana yazar, fonksiyondan değer ÇIKARMAZ.
# Fonksiyon None (hiçbir şey) döndürür.


# --- Çözüm: return ---

print()
print("--- return ile ---")


def ortalama_hesapla(puanlar):
    toplam = 0
    for p in puanlar:
        toplam += p
    return toplam / len(puanlar)    # Değeri DÖNDÜR


sonuc = ortalama_hesapla([85, 90, 78])
print(f"Ortalama: {sonuc:.1f}")     # Ortalama: 84.3

# Artık sonuc değişkeni gerçek bir değer tutuyor.
# İstediğimiz yerde kullanabiliriz.


# --- print vs return Karşılaştırma ---
print()
print("--- print vs return ---")


def topla_print(a, b):
    print(a + b)        # Ekrana yazar


def topla_return(a, b):
    return a + b        # Değeri döndürür


# print versiyonu:
x = topla_print(3, 5)     # 8 yazdırır
print("x =", x)            # x = None

# return versiyonu:
y = topla_return(3, 5)    # Hiçbir şey yazdırmaz
print("y =", y)            # y = 8

# FARK: print sadece gösterir, return veriyi verir.


# --- Fonksiyonu İfade İçinde Kullanma ---
print()
print("--- Poster Alanı Hesaplama ---")


def poster_alani(genislik, yukseklik):
    return genislik * yukseklik


# Değişkene atayarak:
alan = poster_alani(50, 70)
print(f"Poster alanı: {alan} cm²")

# Doğrudan f-string içinde:
print(f"A3 alanı: {poster_alani(29.7, 42.0):.1f} cm²")

# Başka bir hesapta:
toplam_alan = poster_alani(50, 70) + poster_alani(30, 40)
print(f"Toplam alan: {toplam_alan} cm²")


# --- return ile Fonksiyon Biter ---
print()
print("--- return sonrası ---")


def bolme(a, b):
    if b == 0:
        return "Sıfıra bölünemez!"     # Fonksiyon burada biter
    return a / b                         # b sıfır değilse buraya gelir


print(bolme(10, 3))     # 3.333...
print(bolme(10, 0))     # Sıfıra bölünemez!


# --- İndirim Hesaplama ---
print()
print("--- İndirim Hesaplama ---")


def indirimli_fiyat(fiyat, yuzde):
    indirim = fiyat * yuzde / 100
    return fiyat - indirim


# Farklı ürünler için kullanalım:
poster = indirimli_fiyat(120, 25)
print(f"Poster (25% indirim): {poster:.2f} TL")

sticker = indirimli_fiyat(35, 10)
print(f"Sticker (10% indirim): {sticker:.2f} TL")

# İki sonucu karşılaştıralım:
if poster > sticker:
    print("Poster daha pahalı.")
