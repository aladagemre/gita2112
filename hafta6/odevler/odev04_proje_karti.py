# =============================================================
# ÖDEV 4: Proje Kartı Oluşturucu  [Orta]
# =============================================================
# Bu ödevde yapacakların:
#   - Varsayılan parametre değerli fonksiyon yazma
#   - Fonksiyon içinde f-string ile formatlı yazdırma
#   - Fonksiyonu farklı argüman kombinasyonlarıyla çağırma
#
# Konu: Varsayılan değer + f-string + fonksiyon çağırma
# Kazanım: Esnek ve yeniden kullanılabilir fonksiyon yazabilmek
# =============================================================


print("=== Proje Kartı Oluşturucu ===")
print()


# --- Görev 1: Çizgi Fonksiyonu ---
# Varsayılan uzunluk 30, varsayılan karakter "-"

def cizgi(uzunluk=..., karakter=...):  # ← varsayılan değerleri yaz: 30 ve "-"
    print(karakter * uzunluk)


# Test:
print("--- Çizgi Testleri ---")
cizgi()              # 30 tane -
cizgi(40)            # 40 tane -
cizgi(20, "=")       # 20 tane =


# --- Görev 2: Proje Kartı Fonksiyonu ---
# ad ve kategori zorunlu, puan ve durum varsayılan değerli.
# Varsayılan puan: 0, varsayılan durum: "Devam Ediyor"
# Çıktı formatı:
#   ==============================
#   Proje: Logo Tasarımı
#   Kategori: Kurumsal
#   Puan: 88
#   Durum: Tamamlandı
#   ==============================

print()
print("--- Proje Kartları ---")


def proje_karti(ad, kategori, puan=..., durum=...):  # ← varsayılan değerleri yaz: 0 ve "Devam Ediyor"
    cizgi(30, "=")
    print(f"  Proje: {ad}")
    print(f"  Kategori: {kategori}")
    print(f"  Puan: {...}")  # ← puan parametresini yaz
    print(f"  Durum: {...}")  # ← durum parametresini yaz
    cizgi(30, "=")


# Çağır — tüm parametrelerle:
print()
proje_karti("Logo Tasarımı", "Kurumsal", 88, "Tamamlandı")

# Çağır — sadece zorunlu parametrelerle (varsayılanlar kullanılır):
print()
proje_karti("Web Sitesi", "Dijital")

# Çağır — puan ver ama durum varsayılan kalsın:
print()
proje_karti("Film Afişi", "Poster", 92)


# --- Görev 3: Döngü ile Kart Oluşturma ---
# Proje listesindeki her proje için kart oluştur.

print()
print("--- Tüm Projeler ---")

projeler = [
    {"ad": "Logo", "kategori": "Kurumsal", "puan": 88, "durum": "Tamamlandı"},
    {"ad": "Poster", "kategori": "Baskı", "puan": 75, "durum": "Revize"},
    {"ad": "Uygulama", "kategori": "Dijital", "puan": 91, "durum": "Tamamlandı"},
]

for p in projeler:
    print()
    proje_karti(...)  # ← p["ad"], p["kategori"], p["puan"], p["durum"]


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Proje Kartı Oluşturucu ===
#
# --- Çizgi Testleri ---
# ------------------------------
# ----------------------------------------
# ====================
#
# --- Proje Kartları ---
#
# ==============================
#   Proje: Logo Tasarımı
#   Kategori: Kurumsal
#   Puan: 88
#   Durum: Tamamlandı
# ==============================
#
# ==============================
#   Proje: Web Sitesi
#   Kategori: Dijital
#   Puan: 0
#   Durum: Devam Ediyor
# ==============================
#
# ==============================
#   Proje: Film Afişi
#   Kategori: Poster
#   Puan: 92
#   Durum: Devam Ediyor
# ==============================
#
# --- Tüm Projeler ---
#
# ==============================
#   Proje: Logo
#   Kategori: Kurumsal
#   Puan: 88
#   Durum: Tamamlandı
# ==============================
#
# ==============================
#   Proje: Poster
#   Kategori: Baskı
#   Puan: 75
#   Durum: Revize
# ==============================
#
# ==============================
#   Proje: Uygulama
#   Kategori: Dijital
#   Puan: 91
#   Durum: Tamamlandı
# ==============================
