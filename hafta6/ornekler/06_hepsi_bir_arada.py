# =============================================================
# DERS 6: Birleşik Örnek — Tasarım Stüdyosu Yönetim Sistemi
# =============================================================
# Bu derste öğreneceğiz:
#   - Birden fazla fonksiyonun birlikte kullanımı
#   - Fonksiyon tanımları + ana program yapısı
#   - Hafta 4'teki portfolyo yöneticisinin fonksiyonlu hali
#   - Kodun fonksiyonlarla nasıl organize edildiğini görme
#
# Karşılaştırma: Hafta 4'te aynı işi düz kodla yapmıştık.
# Şimdi her işlem ayrı bir fonksiyon. Daha kısa, daha temiz.
# =============================================================


# =====================
# FONKSİYON TANIMLARI
# =====================
# Tüm fonksiyonları programın başında tanımlıyoruz.
# Ana program altta, fonksiyonları çağırarak çalışır.

def proje_listele(projeler):
    """Projeleri numaralı liste olarak yazdırır."""
    for sira, proje in enumerate(projeler, start=1):
        print(f"  {sira}. {proje['ad']} ({proje['kategori']}) → {proje['puan']} puan")


def ortalama_hesapla(sayilar):
    """Bir sayı listesinin ortalamasını döndürür."""
    toplam = 0
    for s in sayilar:
        toplam += s
    return toplam / len(sayilar)


def basarili_filtrele(projeler, sinir=75):
    """Belirli sınırın üstündeki projeleri döndürür."""
    sonuc = []
    for proje in projeler:
        if proje["puan"] >= sinir:
            sonuc.append(proje)
    return sonuc


def en_iyi_bul(projeler):
    """En yüksek puanlı projeyi döndürür."""
    en_iyi = projeler[0]
    for proje in projeler:
        if proje["puan"] > en_iyi["puan"]:
            en_iyi = proje
    return en_iyi


def basari_durumu(puan):
    """Puana göre başarı durumunu döndürür."""
    if puan >= 90:
        return "Mükemmel"
    elif puan >= 75:
        return "Başarılı"
    elif puan >= 60:
        return "Geçti"
    else:
        return "Kaldı"


def kategori_dagilimi(projeler):
    """Her kategoride kaç proje olduğunu sayan sözlük döndürür."""
    sayac = {}
    for proje in projeler:
        kat = proje["kategori"]
        if kat in sayac:
            sayac[kat] = sayac[kat] + 1
        else:
            sayac[kat] = 1
    return sayac


def basari_raporu(projeler):
    """Başarılı ve düşük puanlı projeleri ayırarak döndürür."""
    basarili = []
    dusuk = []
    for proje in projeler:
        if proje["puan"] >= 75:
            basarili.append(proje["ad"])
        else:
            dusuk.append(proje["ad"])
    return basarili, dusuk
    # Bir fonksiyon birden fazla değer döndürebilir!
    # Virgülle ayırarak yazılır.


# =====================
# ANA PROGRAM
# =====================
# Fonksiyonlar yukarıda tanımlı. Şimdi onları çağırarak
# programımızı çalıştırıyoruz. Ne kadar temiz ve okunabilir
# olduğuna dikkat edin!

projeler = [
    {"ad": "Logo Tasarımı", "kategori": "Kurumsal", "puan": 88},
    {"ad": "Film Afişi", "kategori": "Poster", "puan": 95},
    {"ad": "Ürün Ambalajı", "kategori": "Ambalaj", "puan": 72},
    {"ad": "Web Arayüzü", "kategori": "Dijital", "puan": 91},
    {"ad": "Dergi Kapağı", "kategori": "Baskı", "puan": 64},
    {"ad": "Mobil Uygulama", "kategori": "Dijital", "puan": 85},
]


print("=" * 45)
print("    TASARIM STÜDYOSU YÖNETİM SİSTEMİ")
print("=" * 45)


# --- Tüm Projeleri Listele ---
print()
print("--- Tüm Projeler ---")
proje_listele(projeler)


# --- Ortalama ---
tum_puanlar = [p["puan"] for p in projeler]
ort = ortalama_hesapla(tum_puanlar)
print()
print(f"Proje sayısı: {len(projeler)}")
print(f"Ortalama puan: {ort:.1f}")


# --- Başarılı Projeler ---
print()
print("--- Başarılı Projeler (75+) ---")
iyiler = basarili_filtrele(projeler)
proje_listele(iyiler)
# proje_listele fonksiyonunu burada da kullandık!
# Aynı fonksiyon, farklı liste — yeniden kullanılabilirlik.


# --- En İyi Proje ---
sampiyon = en_iyi_bul(projeler)
print()
print(f"En iyi proje: {sampiyon['ad']} → {sampiyon['puan']} puan")


# --- Başarı Durumları ---
print()
print("--- Başarı Durumları ---")
for proje in projeler:
    durum = basari_durumu(proje["puan"])
    print(f"  {proje['ad']} → {durum}")


# --- Kategori Dağılımı ---
print()
print("--- Kategori Dağılımı ---")
dagilim = kategori_dagilimi(projeler)
for kat, sayi in dagilim.items():
    print(f"  {kat}: {sayi} proje")


# --- Başarı Raporu ---
print()
print("--- Başarı Raporu ---")
basarili_listesi, dusuk_listesi = basari_raporu(projeler)
# İki değer döndüren fonksiyonun sonucunu iki değişkene atadık.
print(f"Başarılı (75+): {basarili_listesi}")
print(f"Geliştirilmeli: {dusuk_listesi}")


print()
print("=" * 45)
