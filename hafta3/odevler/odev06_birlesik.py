# =============================================================
# ÖDEV 6: Birleşik — Sınıf Listesi Analizi  [Zor]
# =============================================================
# Bu ödevde yapacakların:
#   - Sözlük listesi üzerinde döngü kur
#   - Toplam ve ortalama hesapla
#   - Koşulla filtreleme yap
#   - En yüksek puanlıyı bul
#
# Konu: Liste + sözlük + döngü + if
# Kazanım: Birden fazla veri yapısını bir arada kullanabilmek
# =============================================================


print("=== Sınıf Listesi Analizi ===")
print()


# --- Veri ---
# Her öğrenci bir sözlük, tümü bir listede.
ogrenciler = [
    {"isim": "Defne", "bolum": "Grafik Tasarım", "puan": 88},
    {"isim": "Cem", "bolum": "İç Mimarlık", "puan": 72},
    {"isim": "Ayşe", "bolum": "Grafik Tasarım", "puan": 95},
    {"isim": "Kaan", "bolum": "Endüstriyel Tasarım", "puan": 64},
    {"isim": "Elif", "bolum": "Grafik Tasarım", "puan": 81},
    {"isim": "Burak", "bolum": "İç Mimarlık", "puan": 55},
]


# --- Görev 1: Tüm Öğrencileri Listele ---
# enumerate() ile numaralı yazdır.
# Çıktı formatı: "1. Defne (Grafik Tasarım) → 88 puan"

print("--- Öğrenci Listesi ---")
for sira, ogr in enumerate(...):  # ← enumerate(ogrenciler, start=1) ile tamamla
    print(str(sira) + ".", ogr["isim"], "(" + ogr["bolum"] + ")", "→", ogr["puan"], "puan")


# --- Görev 2: Ortalama Puan ---
# Tüm puanları topla ve ortalamasını hesapla.

toplam = 0
for ogr in ogrenciler:
    toplam = ...  # ← toplam + ogr["puan"]

ortalama = ...  # ← toplam / len(ogrenciler)

print()
# round(ortalama, 1) → virgülden sonra 1 basamak gösterir
print("Sınıf ortalaması:", ...)  # ← round(ortalama, 1) ile yazdır


# --- Görev 3: Başarılı Öğrenciler ---
# Puanı 75 ve üzeri olanların isimlerini yeni listeye ekle.

basarili = []
for ogr in ogrenciler:
    if ...:  # ← ogr["puan"] >= 75 mi?
        basarili.append(...)  # ← ogr["isim"]

print("Başarılı öğrenciler:", basarili)


# --- Görev 4: En Yüksek Puanlı ---
# Listede en yüksek puana sahip öğrenciyi bul.
# İpucu: İlk öğrenciyi en_iyi olarak kabul et, döngüyle karşılaştır.

en_iyi = ogrenciler[0]
for ogr in ogrenciler:
    if ...:  # ← ogr["puan"] > en_iyi["puan"] mi?
        en_iyi = ...  # ← ogr

print()
print("En başarılı:", ...)  # ← en_iyi["isim"] + puan


# --- Görev 5: Bölüme Göre Filtreleme ---
# Sadece "Grafik Tasarım" bölümündeki öğrencileri yazdır.

print()
print("--- Grafik Tasarım Öğrencileri ---")
for ogr in ogrenciler:
    if ...:  # ← ogr["bolum"] == "Grafik Tasarım" mı?
        print(...)  # ← isim ve puan yazdır


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Sınıf Listesi Analizi ===
#
# --- Öğrenci Listesi ---
# 1. Defne (Grafik Tasarım) → 88 puan
# 2. Cem (İç Mimarlık) → 72 puan
# 3. Ayşe (Grafik Tasarım) → 95 puan
# 4. Kaan (Endüstriyel Tasarım) → 64 puan
# 5. Elif (Grafik Tasarım) → 81 puan
# 6. Burak (İç Mimarlık) → 55 puan
#
# Sınıf ortalaması: 75.8
# Başarılı öğrenciler: ['Defne', 'Ayşe', 'Elif']
#
# En başarılı: Ayşe → 95 puan
#
# --- Grafik Tasarım Öğrencileri ---
# Defne → 88 puan
# Ayşe → 95 puan
# Elif → 81 puan
