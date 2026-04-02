# =============================================================
# DERS 5: Mevcut Kalıpları Fonksiyona Dönüştürme
# =============================================================
# Bu derste öğreneceğiz:
#   - Hafta 3-4'ten bilinen kalıpları fonksiyona çevirme
#   - Ortalama hesaplama fonksiyonu
#   - Filtreleme fonksiyonu
#   - En yüksek/düşük bulma fonksiyonu
#   - Fonksiyonları birlikte kullanma
# =============================================================


# --- Veri ---
# Hafta 4'teki portfolyo yöneticisinden tanıdık bir yapı:
# sözlük listesi (list of dicts)

projeler = [
    {"ad": "Logo Tasarımı", "kategori": "Kurumsal", "puan": 88},
    {"ad": "Film Afişi", "kategori": "Poster", "puan": 95},
    {"ad": "Ürün Ambalajı", "kategori": "Ambalaj", "puan": 72},
    {"ad": "Web Arayüzü", "kategori": "Dijital", "puan": 91},
    {"ad": "Dergi Kapağı", "kategori": "Baskı", "puan": 64},
    {"ad": "Mobil Uygulama", "kategori": "Dijital", "puan": 85},
]


# =============================================================
# 1. Ortalama Hesaplama
# =============================================================
# ESKİ HAL (Hafta 3-4'te böyle yazıyorduk):
#
#   toplam = 0
#   for p in puanlar:
#       toplam += p
#   ortalama = toplam / len(puanlar)
#
# Her farklı liste için bu 4 satırı tekrar yazıyorduk.
# Şimdi fonksiyona çevirelim:

def ortalama_hesapla(sayilar):
    toplam = 0
    for s in sayilar:
        toplam += s
    return toplam / len(sayilar)


# Artık tek satırda kullanabiliriz!
tum_puanlar = [p["puan"] for p in projeler]
# (Bu satır her projenin puanını alıp listeye koyar.
#  Buna "list comprehension" denir, ileride öğreneceksiniz.
#  Şimdilik "puanları topla" olarak anlayın.)

print("--- Ortalama ---")
print(f"Proje ortalaması: {ortalama_hesapla(tum_puanlar):.1f}")

# Farklı bir listeyle de çağırabiliriz:
quiz_notlari = [75, 88, 92, 60]
print(f"Quiz ortalaması: {ortalama_hesapla(quiz_notlari):.1f}")


# =============================================================
# 2. Filtreleme
# =============================================================
# ESKİ HAL:
#
#   basarili = []
#   for proje in projeler:
#       if proje["puan"] >= 75:
#           basarili.append(proje)
#
# Şimdi fonksiyona çevirelim (varsayılan değerle):

def basarili_filtrele(projeler, sinir=75):
    sonuc = []
    for proje in projeler:
        if proje["puan"] >= sinir:
            sonuc.append(proje)
    return sonuc


print()
print("--- Başarılı Projeler (75+) ---")
iyiler = basarili_filtrele(projeler)
for p in iyiler:
    print(f"  {p['ad']} → {p['puan']} puan")

# Sınırı değiştirerek:
print()
print("--- Mükemmel Projeler (90+) ---")
mukemmeller = basarili_filtrele(projeler, 90)
for p in mukemmeller:
    print(f"  {p['ad']} → {p['puan']} puan")


# =============================================================
# 3. En Yüksek Puanlıyı Bulma
# =============================================================
# ESKİ HAL:
#
#   en_iyi = projeler[0]
#   for proje in projeler:
#       if proje["puan"] > en_iyi["puan"]:
#           en_iyi = proje

def en_iyi_bul(projeler):
    en_iyi = projeler[0]
    for proje in projeler:
        if proje["puan"] > en_iyi["puan"]:
            en_iyi = proje
    return en_iyi


print()
sampiyon = en_iyi_bul(projeler)
print(f"En iyi proje: {sampiyon['ad']} ({sampiyon['puan']} puan)")


# =============================================================
# 4. Kategoriye Göre Filtreleme
# =============================================================

def kategoriye_gore(projeler, kategori):
    sonuc = []
    for proje in projeler:
        if proje["kategori"] == kategori:
            sonuc.append(proje)
    return sonuc


print()
print("--- Dijital Projeler ---")
dijitaller = kategoriye_gore(projeler, "Dijital")
for p in dijitaller:
    print(f"  {p['ad']} → {p['puan']} puan")


# =============================================================
# 5. Fonksiyonları Birlikte Kullanma
# =============================================================
# Fonksiyonların sonuçlarını birbirine geçirebiliriz:

print()
print("--- Birleşik Analiz ---")

# Adım 1: Başarılıları bul
iyiler = basarili_filtrele(projeler)
print(f"Başarılı proje sayısı: {len(iyiler)}")

# Adım 2: Başarılılar arasından en iyisini seç
en_iyisi = en_iyi_bul(iyiler)
print(f"En iyisi: {en_iyisi['ad']}")

# Adım 3: Başarılıların ortalaması
iyi_puanlar = [p["puan"] for p in iyiler]
print(f"Başarılıların ortalaması: {ortalama_hesapla(iyi_puanlar):.1f}")

# Her adım tek satır! Fonksiyonlar kodu hem kısalttı
# hem de çok daha okunabilir hale getirdi.
