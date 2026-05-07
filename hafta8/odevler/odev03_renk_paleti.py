# =============================================================
# ÖDEV 3: Renk Paleti Okuma  [Orta]
# =============================================================
# Bu ödevde yapacakların:
#   - with open() ile bir .txt dosyasını oku
#   - Satır satır gez ve listeye ekle
#   - Filtre uygula ve sayım yap
#
# Konu: Dosya okuma + döngü + sözlükle sayma
# Kazanım: Bir veri dosyasını okuyup üzerinde analiz yapmak
# =============================================================


print("=== Müşteri Renk Paleti Analizi ===")
print()


# --- Görev 1: Dosyayı Aç ve Renkleri Listeye Al ---
# veri/musteri_renkleri.txt dosyasını oku.
# Her satır bir rengi içerir. \n karakterini strip() ile temizle.
# Sonuçları "renkler" adlı bir listede topla.

renkler = []

with open(..., "r", encoding="utf-8") as dosya:    # ← dosya yolunu yaz: "veri/musteri_renkleri.txt"
    for satir in dosya:
        renk = satir...()                           # ← strip() metodu
        renkler.append(...)                         # ← renk değişkenini listeye ekle


# --- Görev 2: Toplam Renk Sayısını Yazdır ---

print(f"Toplam renk sayısı: {...}")                # ← len() kullan
print()


# --- Görev 3: M Harfiyle Başlayanları Listele ---
# .startswith("M") metodunu kullan.

print("M harfiyle başlayan renkler:")
m_ile_baslayanlar = []

for renk in renkler:
    if renk.startswith(...):                        # ← "M" yaz
        m_ile_baslayanlar.append(...)               # ← renk değişkenini ekle

for renk in m_ile_baslayanlar:
    print(f"  - {...}")                             # ← renk değişkenini yaz

print()


# --- Görev 4: Her Rengin Kaç Kere Geçtiğini Say ---
# Sözlük kullanın. Anahtar = renk adı, değer = kaç kere geçti.

sayilar = {}

for renk in renkler:
    if renk in sayilar:
        sayilar[renk] = sayilar[renk] + ...         # ← 1 ekle
    else:
        sayilar[renk] = ...                         # ← ilk defa görüldü, 1 olsun

print("Her rengin geçiş sayısı:")
for renk, sayi in sayilar.items():
    print(f"  {renk}: {...} kez")                   # ← sayi değişkenini yaz


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Müşteri Renk Paleti Analizi ===
#
# Toplam renk sayısı: 14
#
# M harfiyle başlayan renkler:
#   - Mercan
#   - Mor
#   - Mercan
#   - Mor
#
# Her rengin geçiş sayısı:
#   Mercan: 2 kez
#   Lacivert: 1 kez
#   Mor: 2 kez
#   Bej: 2 kez
#   Turuncu: 1 kez
#   Yeşil: 1 kez
#   Pembe: 1 kez
#   Kömür: 1 kez
#   Sarı: 2 kez
#   Turkuaz: 1 kez
