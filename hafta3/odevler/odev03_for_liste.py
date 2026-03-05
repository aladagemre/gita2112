# =============================================================
# ÖDEV 3: for + Liste + if — Renk Paleti Analizi  [Orta]
# =============================================================
# Bu ödevde yapacakların:
#   - Listeyi for döngüsüyle gez
#   - Döngü içinde if ile koşul kontrolü yap
#   - Toplam ve ortalama hesapla
#
# Konu: for + liste + if
# Kazanım: Liste üzerinde döngü ve filtreleme yapabilmek
# =============================================================


print("=== Renk Paleti Analizi ===")
print()


# --- Veri ---
# Her rengin bir parlaklık değeri var (0-100 arası)
renkler = ["kırmızı", "mavi", "yeşil", "sarı", "mor", "turuncu"]
parlaklik = [85, 40, 72, 95, 30, 68]


# --- Görev 1: Tüm Renkleri Listele ---
# enumerate() ile numaralı olarak yazdır (1'den başlayarak).
# İpucu: for sira, renk in enumerate(renkler, start=1):

print("--- Renk Listesi ---")
for sira, renk in enumerate(...):  # ← enumerate(renkler, start=1) ile tamamla
    print(str(sira) + ".", renk)


# --- Görev 2: Parlaklık Değerlerini Analiz Et ---
# Her parlaklık değerini kontrol et:
#   - 70 ve üzeri → "Parlak"
#   - 50-69 arası → "Orta"
#   - 50'nin altı → "Koyu"

# İki listeyi aynı anda gezmek istediğimizde indeks numarasını kullanırız.
# range(len(renkler)) → 0, 1, 2, 3, 4, 5 üretir (6 renk var)
# renkler[i] ve parlaklik[i] aynı i ile eşleşir.
print()
print("--- Parlaklık Analizi ---")
for i in range(len(renkler)):
    renk = renkler[i]
    deger = parlaklik[i]

    if ...:          # ← 70 ve üzeri mi?
        durum = "Parlak"
    elif ...:        # ← 50 ve üzeri mi?
        durum = "Orta"
    else:
        durum = "Koyu"

    print(renk, "→", deger, "→", durum)


# --- Görev 3: Ortalama Parlaklık ---
# parlaklik listesindeki tüm değerleri topla ve ortalamasını hesapla.

toplam = 0
for deger in parlaklik:
    toplam = ...  # ← toplam + deger

ortalama = ...  # ← toplam / len(parlaklik)

print()
print("Ortalama parlaklık:", ortalama)


# --- Görev 4: Parlak Renkleri Filtrele ---
# Parlaklığı 70 ve üzeri olan renkleri yeni bir listeye ekle.

parlak_renkler = []
for i in range(len(renkler)):
    if ...:  # ← parlaklik[i] >= 70 mi?
        parlak_renkler.append(renkler[i])

print("Parlak renkler:", parlak_renkler)


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Renk Paleti Analizi ===
#
# --- Renk Listesi ---
# 1. kırmızı
# 2. mavi
# 3. yeşil
# 4. sarı
# 5. mor
# 6. turuncu
#
# --- Parlaklık Analizi ---
# kırmızı → 85 → Parlak
# mavi → 40 → Koyu
# yeşil → 72 → Parlak
# sarı → 95 → Parlak
# mor → 30 → Koyu
# turuncu → 68 → Orta
#
# Ortalama parlaklık: 65.0
# Parlak renkler: ['kırmızı', 'yeşil', 'sarı']
