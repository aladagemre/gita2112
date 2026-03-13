# =============================================================
# ÖDEV 3: Tasarımcı Kartı v2  [Kolay]
# =============================================================
# Bu ödevde yapacakların:
#   - f-string ile formatlı metin yazdır
#   - Sayı formatlama (:.1f, :,.2f)
#   - String metodları kullan
#
# Konu: f-string ve string formatlama
# Kazanım: f-string ile temiz, okunabilir çıktı üretebilmek
# =============================================================


print("=== Tasarımcı Kartı ===")
print()


# --- Görev 1: Profil Bilgisi ---
# Aşağıdaki değişkenleri f-string ile yazdır.

isim = "Defne Yılmaz"
yas = 22
bolum = "Grafik Tasarım"
universite = "Mimar Sinan"

# Çıktı formatı: "İsim: Defne Yılmaz"
print(f"İsim: {isim}")
print(...)   # ← f"Yaş: {yas}"
print(...)   # ← f"Bölüm: {bolum}"
print(...)   # ← f"Üniversite: {universite}"


# --- Görev 2: Portfolyo Özeti ---
# Sayı formatlama kullan.

proje_sayisi = 12
ortalama_puan = 87.6543
toplam_kazanc = 15750.0

print()
print("--- Portfolyo Özeti ---")
print(f"Proje sayısı: {proje_sayisi}")
print(...)   # ← f"Ortalama puan: {ortalama_puan:.1f}"  (1 ondalık)
print(...)   # ← f"Toplam kazanç: {toplam_kazanc:,.2f} TL"  (binlik ayraç + 2 ondalık)


# --- Görev 3: f-string İçinde İfade ---
# Süslü parantez içinde hesaplama yap.

dogum_yili = 2004

print()
print("--- Hesaplamalar ---")
print(...)   # ← f"Doğum yılı: {dogum_yili}"
print(...)   # ← f"5 yıl sonra: {yas + 5} yaşında"
print(...)   # ← f"İsim (büyük harf): {isim.upper()}"


# --- Görev 4: String Metodları ---
# Aşağıdaki metni temizle ve dönüştür.

kirli_metin = "   grafik TASARIM   "

print()
print("--- String Temizleme ---")
print(f"Orijinal: '{kirli_metin}'")
print(...)   # ← f"Temiz: '{kirli_metin.strip()}'"
print(...)   # ← f"Küçük harf: '{kirli_metin.strip().lower()}'"
print(...)   # ← f"Büyük harf: '{kirli_metin.strip().upper()}'"


# =============================================================
# Beklenen Çıktı:
# =============================================================
#
# === Tasarımcı Kartı ===
#
# İsim: Defne Yılmaz
# Yaş: 22
# Bölüm: Grafik Tasarım
# Üniversite: Mimar Sinan
#
# --- Portfolyo Özeti ---
# Proje sayısı: 12
# Ortalama puan: 87.7
# Toplam kazanç: 15,750.00 TL
#
# --- Hesaplamalar ---
# Doğum yılı: 2004
# 5 yıl sonra: 27 yaşında
# İsim (büyük harf): DEFNE YILMAZ
#
# --- String Temizleme ---
# Orijinal: '   grafik TASARIM   '
# Temiz: 'grafik TASARIM'
# Küçük harf: 'grafik tasarım'
# Büyük harf: 'GRAFİK TASARIM'
