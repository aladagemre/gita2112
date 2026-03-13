# =============================================================
# ÖDEV 1: Sözlükler — Proje Kartı  [Kolay-Orta]
# =============================================================
# Bu ödevde yapacakların:
#   - Sözlük oluştur ve değerlere eriş
#   - Yeni anahtar-değer çifti ekle
#   - Değer güncelle
#   - Sözlük üzerinde döngü kur
#
# Konu: Sözlük CRUD + döngü
# Kazanım: Sözlük oluşturup okuma/yazma/güncelleme yapabilmek
# =============================================================


print("=== Proje Kartı Yöneticisi ===")
print()


# --- Görev 1: Sözlük Oluştur ---
# Bir tasarım projesini tanımlayan sözlük oluştur.
# Anahtarlar: "ad", "kategori", "sure_gun", "tamamlandi"

proje = {
    "ad": ...,            # ← proje adı (str), örnek: "Logo Tasarımı"
    "kategori": ...,      # ← kategori (str), örnek: "Kurumsal"
    "sure_gun": ...,      # ← kaç gün sürdü (int), örnek: 14
    "tamamlandi": ...,    # ← tamamlandı mı (bool), örnek: True
}


# --- Görev 2: Değerlere Eriş ---
# Sözlükten tek tek değerleri yazdır.

print("--- Proje Bilgileri ---")
print("Proje Adı:", ...)       # ← proje["ad"]
print("Kategori:", ...)        # ← proje["kategori"]
print("Süre:", ..., "gün")     # ← proje["sure_gun"]
print("Tamamlandı:", ...)      # ← proje["tamamlandi"]


# --- Görev 3: Yeni Alan Ekle ---
# Sözlüğe "puan" ve "musteri" anahtarlarını ekle.

...  # ← proje["puan"] = bir sayı (0-100)
...  # ← proje["musteri"] = bir isim (str)

print()
print("--- Eklenen Bilgiler ---")
print("Puan:", proje["puan"])
print("Müşteri:", proje["musteri"])


# --- Görev 4: Değer Güncelle ---
# Projenin süresini 7 gün artır (mevcut + 7).

proje["sure_gun"] = ...  # ← proje["sure_gun"] + 7

print()
print("Güncel süre:", proje["sure_gun"], "gün")


# --- Görev 5: Döngü ile Tüm Bilgileri Yazdır ---
# .items() ile sözlüğün tamamını yazdır.

print()
print("--- Tam Proje Kartı ---")
for anahtar, deger in ...:  # ← proje.items()
    print(anahtar + ":", deger)


# =============================================================
# Beklenen Çıktı (örnek — senin değerlerin farklı olabilir):
# =============================================================
#
# === Proje Kartı Yöneticisi ===
#
# --- Proje Bilgileri ---
# Proje Adı: Logo Tasarımı
# Kategori: Kurumsal
# Süre: 14 gün
# Tamamlandı: True
#
# --- Eklenen Bilgiler ---
# Puan: 88
# Müşteri: ABC Şirketi
#
# Güncel süre: 21 gün
#
# --- Tam Proje Kartı ---
# ad: Logo Tasarımı
# kategori: Kurumsal
# sure_gun: 21
# tamamlandi: True
# puan: 88
# musteri: ABC Şirketi
