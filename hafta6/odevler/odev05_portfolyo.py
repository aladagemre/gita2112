# =============================================================
# ÖDEV 5: Portfolyo Analiz Sistemi  [Zor]
# =============================================================
# Bu ödevde yapacakların:
#   - Birden fazla fonksiyon tanımlama (return ile)
#   - Varsayılan parametre kullanma
#   - Döngü içinde fonksiyon çağırma
#   - Fonksiyon sonuçlarını birbirine geçirme
#
# Konu: Tüm fonksiyon kavramları + liste + sözlük + döngü
# Kazanım: Birden fazla fonksiyonu bir arada kullanabilmek
# =============================================================


print("=== Portfolyo Analiz Sistemi ===")
print()


# --- Veri ---
projeler = [
    {"ad": "Logo Tasarımı", "kategori": "Kurumsal", "puan": 88},
    {"ad": "Film Afişi", "kategori": "Poster", "puan": 95},
    {"ad": "Ürün Ambalajı", "kategori": "Ambalaj", "puan": 72},
    {"ad": "Web Arayüzü", "kategori": "Dijital", "puan": 91},
    {"ad": "Dergi Kapağı", "kategori": "Baskı", "puan": 64},
    {"ad": "Mobil Uygulama", "kategori": "Dijital", "puan": 85},
]


# --- Görev 1: Ortalama Hesaplama Fonksiyonu ---
# Bir sayı listesinin ortalamasını döndürsün.

def ortalama_hesapla(sayilar):
    toplam = 0
    for s in sayilar:
        toplam = ...  # ← toplam + s
    return ...  # ← toplam / len(sayilar)


# --- Görev 2: Başarılı Filtreleme Fonksiyonu ---
# Sınırın üstündeki projeleri yeni bir listede döndürsün.
# Varsayılan sınır: 75

def basarili_filtrele(projeler, sinir=...):  # ← varsayılan değer: 75
    sonuc = []
    for proje in projeler:
        if ...:  # ← proje["puan"] >= sinir
            sonuc.append(proje)
    return sonuc


# --- Görev 3: En İyi Projeyi Bulma Fonksiyonu ---
# En yüksek puanlı proje sözlüğünü döndürsün.

def en_iyi_bul(projeler):
    en_iyi = projeler[0]
    for proje in projeler:
        if ...:  # ← proje["puan"] > en_iyi["puan"]
            en_iyi = ...  # ← proje
    return en_iyi


# --- Görev 4: Başarı Durumu Fonksiyonu ---
# 90+ → "Mükemmel", 75+ → "Başarılı", 60+ → "Geçti", altı → "Kaldı"

def basari_durumu(puan):
    if puan >= 90:
        return "Mükemmel"
    elif puan >= 75:
        return ...  # ← "Başarılı"
    elif ...:  # ← puan >= 60
        return "Geçti"
    else:
        return ...  # ← "Kaldı"


# =====================
# ANA PROGRAM
# =====================
# Yukarıdaki fonksiyonları çağırarak analiz yap.


# --- Tüm Projeleri Listele ---
print("--- Tüm Projeler ---")
for sira, proje in enumerate(projeler, start=1):
    durum = ...  # ← basari_durumu(proje["puan"]) çağır
    print(f"  {sira}. {proje['ad']} → {proje['puan']} puan ({durum})")


# --- Ortalama ---
tum_puanlar = [p["puan"] for p in projeler]
ort = ...  # ← ortalama_hesapla(tum_puanlar) çağır
print()
print(f"Ortalama puan: {ort:.1f}")


# --- Başarılı Projeler ---
print()
print("--- Başarılı Projeler (75+) ---")
iyiler = ...  # ← basarili_filtrele(projeler) çağır
for p in iyiler:
    print(f"  {p['ad']} → {p['puan']} puan")


# --- Mükemmel Projeler ---
print()
print("--- Mükemmel Projeler (90+) ---")
mukemmeller = ...  # ← basarili_filtrele(projeler, 90) çağır
for p in mukemmeller:
    print(f"  {p['ad']} → {p['puan']} puan")


# --- En İyi Proje ---
sampiyon = ...  # ← en_iyi_bul(projeler) çağır
print()
print(f"En iyi proje: {sampiyon['ad']} → {sampiyon['puan']} puan")


# --- Başarılıların Ortalaması ---
iyi_puanlar = [p["puan"] for p in iyiler]
iyi_ort = ...  # ← ortalama_hesapla(iyi_puanlar) çağır
print(f"Başarılıların ortalaması: {iyi_ort:.1f}")


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Portfolyo Analiz Sistemi ===
#
# --- Tüm Projeler ---
#   1. Logo Tasarımı → 88 puan (Başarılı)
#   2. Film Afişi → 95 puan (Mükemmel)
#   3. Ürün Ambalajı → 72 puan (Geçti)
#   4. Web Arayüzü → 91 puan (Mükemmel)
#   5. Dergi Kapağı → 64 puan (Geçti)
#   6. Mobil Uygulama → 85 puan (Başarılı)
#
# Ortalama puan: 82.5
#
# --- Başarılı Projeler (75+) ---
#   Logo Tasarımı → 88 puan
#   Film Afişi → 95 puan
#   Web Arayüzü → 91 puan
#   Mobil Uygulama → 85 puan
#
# --- Mükemmel Projeler (90+) ---
#   Film Afişi → 95 puan
#   Web Arayüzü → 91 puan
#
# En iyi proje: Film Afişi → 95 puan
# Başarılıların ortalaması: 89.8
