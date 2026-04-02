# =============================================================
# ÖDEV 3: Harf Notu Sistemi  [Orta]
# =============================================================
# Bu ödevde yapacakların:
#   - Fonksiyon içinde if/elif/else kullanma
#   - Her daldan farklı değer return etme
#   - Döngü içinde fonksiyon çağırma
#
# Konu: if/elif + return + döngüde fonksiyon çağırma
# Kazanım: Koşullu değer döndüren fonksiyon yazabilmek
# =============================================================


print("=== Harf Notu Sistemi ===")
print()


# --- Görev 1: Harf Notu Fonksiyonu ---
# Puana göre harf notu döndüren fonksiyon:
#   90 ve üstü → "AA"
#   80 ve üstü → "BA"
#   70 ve üstü → "BB"
#   60 ve üstü → "CB"
#   altı       → "FF"

def harf_notu(puan):
    if puan >= 90:
        return "AA"
    elif ...:  # ← puan >= 80
        return ...  # ← "BA"
    elif ...:  # ← puan >= 70
        return ...  # ← "BB"
    elif ...:  # ← puan >= 60
        return ...  # ← "CB"
    else:
        return ...  # ← "FF"


# Test edelim:
print("--- Tek Tek Test ---")
print(f"95 → {harf_notu(95)}")
print(f"82 → {harf_notu(82)}")
print(f"71 → {harf_notu(71)}")
print(f"65 → {harf_notu(65)}")
print(f"45 → {harf_notu(45)}")


# --- Görev 2: Öğrenci Listesinde Kullanma ---
# Her öğrencinin puanını harf notuna çevir.

print()
print("--- Öğrenci Karnesi ---")

ogrenciler = [
    {"isim": "Defne", "puan": 92},
    {"isim": "Cem", "puan": 78},
    {"isim": "Ayşe", "puan": 85},
    {"isim": "Kaan", "puan": 55},
    {"isim": "Elif", "puan": 67},
]

for ogr in ogrenciler:
    not_harfi = ...  # ← harf_notu(ogr["puan"]) fonksiyonunu çağır
    print(f"  {ogr['isim']}: {ogr['puan']} puan → {not_harfi}")


# --- Görev 3: Geçti mi? Fonksiyonu ---
# Puan 60 ve üstü ise True, altıysa False döndürsün.

print()

def gecti_mi(puan):
    return ...  # ← puan >= 60


# Geçen ve kalan öğrencileri say
gecen = 0
kalan = 0

for ogr in ogrenciler:
    if gecti_mi(ogr["puan"]):  # ← fonksiyon True/False döndürür
        gecen += 1
    else:
        kalan += 1

print(f"Geçen: {gecen} öğrenci")
print(f"Kalan: {kalan} öğrenci")


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Harf Notu Sistemi ===
#
# --- Tek Tek Test ---
# 95 → AA
# 82 → BA
# 71 → BB
# 65 → CB
# 45 → FF
#
# --- Öğrenci Karnesi ---
#   Defne: 92 puan → AA
#   Cem: 78 puan → BB
#   Ayşe: 85 puan → BA
#   Kaan: 55 puan → FF
#   Elif: 67 puan → CB
#
# Geçen: 4 öğrenci
# Kalan: 1 öğrenci
