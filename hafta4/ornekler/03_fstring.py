# =============================================================
# DERS 3: String Formatlama — f-string
# =============================================================
# Bu derste öğreneceğiz:
#   - Eski yol: + ile birleştirme
#   - Yeni yol: f-string (f"...")
#   - f-string içinde ifade kullanma
#   - Sayı formatlama (:.1f, :,.2f)
#   - .format() farkındalık
#   - String metodları: .lower(), .upper(), .strip()


# --- Eski Yol vs Yeni Yol ---
# Eski yolda + ile birleştirirken sayıları str() ile çevirmek gerekiyordu.
# f-string ile bu dertten kurtuluyoruz.

isim = "Defne"
yas = 20
bolum = "Grafik Tasarım"

print("=== Eski Yol vs f-string ===")

# Eski yol (+ ile birleştirme):
print("Merhaba, ben " + isim + ". " + str(yas) + " yaşındayım.")

# Yeni yol (f-string):
print(f"Merhaba, ben {isim}. {yas} yaşındayım.")

# f-string çok daha okunabilir!


# --- f-string İçinde İfade ---
# Süslü parantezlerin içine değişken dışında ifadeler de yazabilirsiniz.

print()
print("=== f-string İçinde İfade ===")
print(f"Toplam: {3 + 5}")
print(f"İsim (büyük harf): {isim.upper()}")
print(f"Bölüm uzunluğu: {len(bolum)} karakter")
print(f"5 yıl sonra: {yas + 5} yaşında")


# --- Sayı Formatlama ---
# f-string ile sayıları istediğimiz formatta gösterebiliriz.

print()
print("=== Sayı Formatlama ===")

fiyat = 1234.5678
oran = 0.8534

# :.1f → virgülden sonra 1 basamak
print(f"Fiyat (1 basamak): {fiyat:.1f}")

# :.2f → virgülden sonra 2 basamak
print(f"Fiyat (2 basamak): {fiyat:.2f}")

# :,.2f → binlik ayıracı + 2 basamak
print(f"Fiyat (binlik): {fiyat:,.2f}")

# Yüzde gösterimi: sayıyı 100 ile çarp
print(f"Oran: {oran * 100:.1f}%")


# --- Çoklu Değişken: Portfolyo Bilgisi ---

print()
print("=== Portfolyo Kartı ===")

proje_adi = "Logo Tasarımı"
kategori = "Kurumsal"
sure_gun = 14
puan = 88.5

print(f"Proje: {proje_adi}")
print(f"Kategori: {kategori}")
print(f"Süre: {sure_gun} gün")
print(f"Puan: {puan:.1f} / 100")


# --- .format() Yöntemi (Farkındalık) ---
# f-string'den önce .format() kullanılıyordu.
# Bilmenize gerek yok ama karşılaşınca tanıyın.

print()
print("=== .format() Yöntemi ===")
print("Merhaba, ben {}. {} yaşındayım.".format(isim, yas))
# Aynı şey, ama f-string daha kolay.


# --- String Metodları ---
# Kullanıcıdan input() ile veri alırken bu metodlar çok işe yarar.

print()
print("=== String Metodları ===")

metin = "  Grafik Tasarım  "

print(f"Orijinal: '{metin}'")
print(f".strip():  '{metin.strip()}'")      # Baş/son boşlukları siler
print(f".lower():  '{metin.strip().lower()}'")  # Küçük harfe çevirir
print(f".upper():  '{metin.strip().upper()}'")  # Büyük harfe çevirir

# Pratik kullanım: input kontrolü
# Kullanıcı "EVET", "evet", " evet " yazsa bile hepsini yakalarız:
# cevap = input("Devam? ").strip().lower()
# if cevap == "evet":
#     print("Devam ediyoruz!")
