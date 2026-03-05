# =============================================================
# DERS 7: Sözlükler (Dictionaries)
# =============================================================
# Bu derste öğreneceğiz:
#   - Sözlük oluşturma {anahtar: değer}
#   - Değere erişim ve güncelleme
#   - Yeni anahtar-değer ekleme
#   - .keys(), .values(), .items()
#   - Sözlük üzerinde döngü


# --- Sözlük Oluşturma ---
# Sözlük, anahtar-değer çiftleri saklar.
# Süslü parantez {} ile oluşturulur.
# Her anahtar benzersiz olmalıdır.

ogrenci = {
    "isim": "Defne",
    "bolum": "Grafik Tasarım",
    "sinif": 2,
    "ortalama": 3.45
}

print("=== Öğrenci Profil Kartı ===")
print(ogrenci)


# --- Değere Erişim ---
# Anahtarı köşeli parantez içinde yazarak değere ulaşırız.
print()
print("İsim:", ogrenci["isim"])
print("Bölüm:", ogrenci["bolum"])
print("Sınıf:", ogrenci["sinif"])
print("Ortalama:", ogrenci["ortalama"])


# --- Değer Güncelleme ---
ogrenci["ortalama"] = 3.60
print()
print("Yeni ortalama:", ogrenci["ortalama"])


# --- Yeni Anahtar-Değer Ekleme ---
ogrenci["email"] = "defne@uni.edu.tr"
ogrenci["portfolyo_sayisi"] = 8
print()
print("Güncel profil:", ogrenci)


# --- .keys(), .values(), .items() ---
print()
print("=== Sözlük Metodları ===")
# list() ile çeviriyoruz ki güzel görünsün. Yoksa dict_keys([...]) şeklinde çıkar.
print("Anahtarlar:", list(ogrenci.keys()))
print("Değerler:", list(ogrenci.values()))


# --- Sözlük Üzerinde Döngü ---
# .items() hem anahtarı hem değeri döner.
print()
print("=== Profil Kartı (Detay) ===")
for anahtar, deger in ogrenci.items():
    print(anahtar + ":", deger)


# --- Birden Fazla Sözlük ---
# Öğrenci listesi: her eleman bir sözlük
print()
print("=== Sınıf Listesi ===")

sinif = [
    {"isim": "Defne", "puan": 88},
    {"isim": "Cem", "puan": 72},
    {"isim": "Ayşe", "puan": 95},
    {"isim": "Kaan", "puan": 64},
]

for ogr in sinif:
    print(ogr["isim"], "→", ogr["puan"], "puan")
