# =============================================================
# ÖDEV 5: CSV'den JSON'a Köprü  [Zor — Hepsi Bir Arada]
# =============================================================
# Bu ödev, Hafta 8'in tüm konularını birleştiriyor:
#   - Dosya okuma (Bölüm 3)
#   - import (Bölüm 4)
#   - CSV (Bölüm 5)
#   - JSON (Bölüm 6)
#   - Hafta 6'dan: FONKSİYONLAR (def + return)
#
# Geçen iki haftadır kullanmadığınız `def` ve `return`'leri burada
# tekrar canlandıracağız. Bu ödev dört küçük fonksiyondan oluşuyor —
# her birini tek başına yazıp test edebilirsiniz.
#
# Konu: csv + sözlük + liste + filtre + json + fonksiyon
# Kazanım: Veriyi parça parça işleme — gerçek programların yapısı
# =============================================================


import csv
import json


# =============================================================
# Fonksiyon 1 — CSV'yi okuyup sözlük listesi olarak döndür
# =============================================================
# Bu fonksiyon: CSV dosyasını açar, başlık satırını atlar,
# her satırı bir sözlüğe çevirir, hepsini bir listede döndürür.
#
# DİKKAT: sure_gun ve butce_tl SAYI olmalı (int), str değil!

def csv_oku(dosya_yolu: str) -> list:
    projeler = []
    with open(dosya_yolu, "r", encoding="utf-8") as dosya:
        okuyucu = csv.reader(dosya)
        next(okuyucu)                          # başlık satırını atla

        for satir in okuyucu:
            # satir bir liste: ["Caz Festivali Afişi", "afiş", "7", "4500"]
            proje = {
                "isim": satir[0],
                "kategori": satir[...],        # ← kategori 2. kolon (indeks 1)
                "sure_gun": int(satir[...]),   # ← süre 3. kolon (indeks 2)
                "butce_tl": int(satir[...]),   # ← bütçe 4. kolon (indeks 3)
            }
            projeler.append(...)               # ← proje sözlüğünü listeye ekle

    return projeler


# =============================================================
# Fonksiyon 2 — Bütçeye göre filtrele
# =============================================================
# Bu fonksiyon: Sözlük listesi alır, sadece bütçesi `esik`'in
# üstünde olan projeleri içeren YENİ bir liste döndürür.

def filtrele(projeler: list, esik: int) -> list:
    sonuc = []
    for proje in projeler:
        if proje[...] > esik:                  # ← "butce_tl" anahtarı
            sonuc.append(...)                  # ← proje değişkenini ekle
    return ...                                 # ← sonuc listesini döndür


# =============================================================
# Fonksiyon 3 — Toplam bütçeyi hesapla
# =============================================================
# Bu fonksiyon: Sözlük listesi alır, hepsinin "butce_tl"
# alanlarını toplayıp tek bir sayı döndürür.

def toplam_butce(projeler: list) -> int:
    toplam = 0
    for proje in projeler:
        toplam = toplam + proje[...]           # ← "butce_tl"
    return ...                                 # ← toplam değişkeni


# =============================================================
# Fonksiyon 4 — Özet sözlüğü oluştur ve JSON'a yaz
# =============================================================
# Bu fonksiyon: Filtrelenmiş projeler ve toplam bütçeyi alır,
# bir özet sözlüğü oluşturur, JSON dosyasına kaydeder.

def json_yaz(projeler: list, butce: int, dosya_yolu: str) -> None:
    ozet = {
        "olusturma_tarihi": "2026-05-08",
        "filtre": "butce_tl > 5000",
        "proje_sayisi": len(...),              # ← projeler listesinin uzunluğu
        "toplam_butce_tl": ...,                # ← butce parametresi
        "projeler": ...,                       # ← projeler parametresi
    }

    with open(dosya_yolu, "w", encoding="utf-8") as dosya:
        json.dump(ozet, dosya, ensure_ascii=False, indent=2)


# =============================================================
# Ana Akış — Yukarıdaki 4 fonksiyonu sırayla çağır
# =============================================================

print("=== Proje Veritabanı Dönüştürücü ===")
print()


# --- Adım 1: CSV'yi oku ---
projeler = csv_oku("veri/projeler.csv")
print(f"Toplam {len(projeler)} proje okundu.")
print()


# --- Adım 2: İlk 3 projeyi göster (kontrol) ---
print("İlk 3 proje:")
sayac = 0
for proje in projeler:
    if sayac < 3:
        print(f"  - {proje['isim']}: {proje['butce_tl']} TL")
        sayac = sayac + 1
print()


# --- Adım 3: 5000 TL üstü bütçeleri filtrele ---
buyuk_projeler = filtrele(projeler, 5000)
print(f"Bütçesi 5000 TL üstü olan projeler: {len(buyuk_projeler)} adet")
for proje in buyuk_projeler:
    print(f"  - {proje['isim']} ({proje['kategori']}): {proje['butce_tl']} TL")
print()


# --- Adım 4: Toplam bütçeyi hesapla ---
butce = toplam_butce(buyuk_projeler)
print(f"Büyük projelerin toplam bütçesi: {butce} TL")
print()


# --- Adım 5: JSON'a yaz ---
json_yaz(buyuk_projeler, butce, "buyuk_projeler.json")
print("buyuk_projeler.json dosyası oluşturuldu.")


# =============================================================
# İPUCU: Fonksiyonları Tek Tek Test Etme
# =============================================================
#
# Tüm boşlukları doldurmadan önce her fonksiyonu ayrı ayrı
# deneyebilirsiniz. Örneğin sadece csv_oku'yu doldurup, ana
# akışın sonraki satırlarını yorum yapın:
#
#     projeler = csv_oku("veri/projeler.csv")
#     print(projeler[0])    # ilk projenin sözlüğüne bakın
#     # buyuk_projeler = filtrele(projeler, 5000)   ← yorum
#
# Çalışınca yorumu açıp filtrele'ye geçin. Adım adım gidin.


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Proje Veritabanı Dönüştürücü ===
#
# Toplam 10 proje okundu.
#
# İlk 3 proje:
#   - Caz Festivali Afişi: 4500 TL
#   - Roman Kapağı: 8000 TL
#   - Markalaşma Kılavuzu: 18000 TL
#
# Bütçesi 5000 TL üstü olan projeler: 5 adet
#   - Roman Kapağı (kitap): 8000 TL
#   - Markalaşma Kılavuzu (kurumsal): 18000 TL
#   - Sergi Kataloğu (kitap): 12000 TL
#   - Spor Logosu (logo): 6000 TL
#   - Mobil Uygulama Mockup (dijital): 15000 TL
#
# Büyük projelerin toplam bütçesi: 59000 TL
#
# buyuk_projeler.json dosyası oluşturuldu.
#
# Ayrıca buyuk_projeler.json içine baktığınızda:
# {
#   "olusturma_tarihi": "2026-05-08",
#   "filtre": "butce_tl > 5000",
#   "proje_sayisi": 5,
#   "toplam_butce_tl": 59000,
#   "projeler": [
#     {
#       "isim": "Roman Kapağı",
#       ...
#     },
#     ...
#   ]
# }
