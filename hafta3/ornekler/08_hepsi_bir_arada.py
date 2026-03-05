# =============================================================
# DERS 8: Birleşik Örnek — Mini Portfolyo Yöneticisi
# =============================================================
# Bu derste öğreneceğiz:
#   - Liste + sözlük birlikte kullanım
#   - Döngü + koşul kombinasyonu
#   - Toplam ve ortalama hesaplama
#   - Tüm Hafta 3 konularını birleştirme


# --- Proje Verileri ---
# Her proje bir sözlük, tüm projeler bir listede tutuluyor.

projeler = [
    {"ad": "Logo Tasarımı", "kategori": "Kurumsal", "puan": 88},
    {"ad": "Film Afişi", "kategori": "Poster", "puan": 95},
    {"ad": "Ürün Ambalajı", "kategori": "Ambalaj", "puan": 72},
    {"ad": "Web Arayüzü", "kategori": "Dijital", "puan": 91},
    {"ad": "Dergi Kapağı", "kategori": "Baskı", "puan": 64},
    {"ad": "Mobil Uygulama", "kategori": "Dijital", "puan": 85},
]


# --- Tüm Projeleri Listeleme ---
# "=" * 45 → 45 tane "=" işareti yazdırır (görsel çizgi oluşturur)
print("=" * 45)
print("       MİNİ PORTFOLYO YÖNETİCİSİ")
print("=" * 45)
print()

print("--- Tüm Projeler ---")
for sira, proje in enumerate(projeler, start=1):
    print(str(sira) + ".", proje["ad"], "(" + proje["kategori"] + ")", "→", proje["puan"], "puan")


# --- Ortalama Hesaplama ---
toplam_puan = 0
for proje in projeler:
    toplam_puan = toplam_puan + proje["puan"]

ortalama = toplam_puan / len(projeler)
print()
print("Proje sayısı:", len(projeler))
print("Toplam puan:", toplam_puan)
# round(sayı, 1) → virgülden sonra 1 basamak gösterir. Örnek: 82.5
print("Ortalama puan:", round(ortalama, 1))


# --- En Yüksek Puanlı Proje ---
en_iyi = projeler[0]
for proje in projeler:
    if proje["puan"] > en_iyi["puan"]:
        en_iyi = proje

print()
print("En iyi proje:", en_iyi["ad"], "→", en_iyi["puan"], "puan")


# --- Kategoriye Göre Filtreleme ---
print()
aranan_kategori = "Dijital"
print("--- " + aranan_kategori + " Kategorisi ---")

for proje in projeler:
    if proje["kategori"] == aranan_kategori:
        print("-", proje["ad"], "→", proje["puan"], "puan")


# --- Başarı Durumu ---
print()
print("--- Başarı Durumu ---")
basarili = []
dusuk = []

for proje in projeler:
    if proje["puan"] >= 75:
        basarili.append(proje["ad"])
    else:
        dusuk.append(proje["ad"])

print("Başarılı (75+):", basarili)
print("Geliştirilmeli:", dusuk)


# --- Kategori Dağılımı ---
# Her kategoride kaç proje var?
# Bu kalıp: "daha önce gördüm mü?" deseni
#   1. Her projenin kategorisini al
#   2. Bu kategoriyi daha önce saydık mı? (in ile kontrol)
#   3. Saydıysak → 1 artır. Saymadıysak → ilk kez ekle, 1 yap.
print()
print("--- Kategori Dağılımı ---")

kategori_sayisi = {}
for proje in projeler:
    kat = proje["kategori"]
    if kat in kategori_sayisi:
        kategori_sayisi[kat] = kategori_sayisi[kat] + 1
    else:
        kategori_sayisi[kat] = 1

for kat, sayi in kategori_sayisi.items():
    print(kat + ":", sayi, "proje")

print()
print("=" * 45)
