# =============================================================
# ÖDEV 1: Stüdyo Selamlama  [Kolay]
# =============================================================
# Bu ödevde yapacakların:
#   - def ile fonksiyon tanımlama
#   - Parametre kullanma
#   - Fonksiyonu farklı argümanlarla çağırma
#
# Konu: def + parametre + çağırma + f-string
# Kazanım: Fonksiyon tanımlayıp çağırabilmek
# =============================================================


print("=== Stüdyo Selamlama Sistemi ===")
print()


# --- Görev 1: Tek Parametreli Fonksiyon ---
# "Merhaba, Defne! Stüdyoya hoş geldin." formatında yazdırsın.
# İpucu: f-string kullan.

def selamla(...):  # ← parametre adını yaz (isim)
    print(f"Merhaba, {...}! Stüdyoya hoş geldin.")  # ← aynı parametre adını yaz


# Fonksiyonu 3 farklı isimle çağır:
selamla("Defne")
selamla("Cem")
selamla("Ayşe")


# --- Görev 2: İki Parametreli Fonksiyon ---
# "Merhaba, Defne! Grafik Tasarım bölümüne hoş geldin." formatında yazdırsın.

print()

def detayli_selamla(..., ...):  # ← iki parametre: isim, bolum
    print(f"Merhaba, {...}! {...} bölümüne hoş geldin.")  # ← parametreleri yaz


detayli_selamla("Defne", "Grafik Tasarım")
detayli_selamla("Cem", "İç Mimarlık")
detayli_selamla("Ayşe", "Endüstriyel Tasarım")


# --- Görev 3: Çizgi Fonksiyonu ---
# Verilen uzunlukta "-" karakteri yazdırsın.

print()

def cizgi(...):  # ← parametre: uzunluk
    print(...  * uzunluk)  # ← "-" karakterini uzunluk kadar tekrarla


cizgi(20)
print("Proje Listesi")
cizgi(20)
print("1. Logo Tasarımı")
print("2. Poster")
cizgi(20)


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Stüdyo Selamlama Sistemi ===
#
# Merhaba, Defne! Stüdyoya hoş geldin.
# Merhaba, Cem! Stüdyoya hoş geldin.
# Merhaba, Ayşe! Stüdyoya hoş geldin.
#
# Merhaba, Defne! Grafik Tasarım bölümüne hoş geldin.
# Merhaba, Cem! İç Mimarlık bölümüne hoş geldin.
# Merhaba, Ayşe! Endüstriyel Tasarım bölümüne hoş geldin.
#
# --------------------
# Proje Listesi
# --------------------
# 1. Logo Tasarımı
# 2. Poster
# --------------------
