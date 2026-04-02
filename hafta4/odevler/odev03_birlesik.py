# =============================================================
# ÖDEV 3: Birleşik — Tasarım Ekibi Analizi  [Zor]
# =============================================================
# Bu ödevde yapacakların:
#   - Sözlük listesi üzerinde döngü kur
#   - continue ile filtreleme yap
#   - Toplam ve ortalama hesapla
#   - En yüksek puanlıyı bul
#
# Konu: Liste + sözlük + döngü + if + continue
# Kazanım: Birden fazla veri yapısını bir arada kullanabilmek
# =============================================================


print("=== Tasarım Ekibi Analizi ===")
print()


# --- Veri ---
# Her tasarımcı bir sözlük, tümü bir listede.
tasarimcilar = [
    {"isim": "Defne", "alan": "Grafik", "puan": 88},
    {"isim": "Cem", "alan": "Web", "puan": 72},
    {"isim": "Ayşe", "alan": "Grafik", "puan": 95},
    {"isim": "Kaan", "alan": "Ambalaj", "puan": 64},
    {"isim": "Elif", "alan": "Grafik", "puan": 81},
    {"isim": "Burak", "alan": "Web", "puan": 55},
]


# --- Görev 1: Tüm Tasarımcıları Listele ---
# enumerate() ile numaralı yazdır.
# Çıktı formatı: "1. Defne (Grafik) → 88 puan"

print("--- Tasarımcı Listesi ---")
for sira, t in enumerate(...):  # ← enumerate(tasarimcilar, start=1) ile tamamla
    print(str(sira) + ".", t["isim"], "(" + t["alan"] + ")", "→", t["puan"], "puan")


# --- Görev 2: Ortalama Puan ---
# Tüm puanları topla ve ortalamasını hesapla.

toplam = 0
for t in tasarimcilar:
    toplam = ...  # ← toplam + t["puan"]

ortalama = ...  # ← toplam / len(tasarimcilar)

print()
print("Ekip ortalaması:", round(ortalama, 1))


# --- Görev 3: Başarılı Tasarımcılar (continue ile) ---
# Puanı 75'in altında olanları atla, sadece başarılıları yazdır.
# İpucu: if puan < 75 → continue

print()
print("--- Başarılı Tasarımcılar ---")
for t in tasarimcilar:
    if ...:  # ← t["puan"] < 75 ise atla
        continue
    print(" ", t["isim"], "→", t["puan"], "puan")


# --- Görev 4: En Yüksek Puanlı ---
# Listede en yüksek puana sahip tasarımcıyı bul.
# İpucu: İlk elemanı en_iyi olarak kabul et, döngüyle karşılaştır.

en_iyi = tasarimcilar[0]
for t in tasarimcilar:
    if ...:  # ← t["puan"] > en_iyi["puan"] mi?
        en_iyi = ...  # ← t

print()
print("En başarılı:", en_iyi["isim"], "→", en_iyi["puan"], "puan")


# --- Görev 5: Alana Göre Filtreleme ---
# Sadece "Grafik" alanındaki tasarımcıları yazdır.

print()
print("--- Grafik Tasarımcıları ---")
for t in tasarimcilar:
    if ...:  # ← t["alan"] == "Grafik" mı?
        print(" ", t["isim"], "→", t["puan"], "puan")


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Tasarım Ekibi Analizi ===
#
# --- Tasarımcı Listesi ---
# 1. Defne (Grafik) → 88 puan
# 2. Cem (Web) → 72 puan
# 3. Ayşe (Grafik) → 95 puan
# 4. Kaan (Ambalaj) → 64 puan
# 5. Elif (Grafik) → 81 puan
# 6. Burak (Web) → 55 puan
#
# Ekip ortalaması: 75.8
#
# --- Başarılı Tasarımcılar ---
#   Defne → 88 puan
#   Ayşe → 95 puan
#   Elif → 81 puan
#
# En başarılı: Ayşe → 95 puan
#
# --- Grafik Tasarımcıları ---
#   Defne → 88 puan
#   Ayşe → 95 puan
#   Elif → 81 puan
