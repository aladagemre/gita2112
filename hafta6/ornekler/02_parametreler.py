# =============================================================
# DERS 2: Parametreler — Fonksiyona Bilgi Göndermek
# =============================================================
# Bu derste öğreneceğiz:
#   - Parametre nedir? (fonksiyonun "boş kutusu")
#   - Argüman nedir? (çağırırken verdiğimiz değer)
#   - Tek parametreli fonksiyon
#   - Birden fazla parametreli fonksiyon
#   - Parametre sırasının önemi
# =============================================================


# --- Sorun ---
# Ders 1'deki hosgeldin() hep aynı mesajı yazıyordu.
# Her proje için farklı başlık istiyoruz.


# --- Tek Parametreli Fonksiyon ---

def proje_basligi(proje_adi):
    print("=" * 30)
    print(f"Proje: {proje_adi}")
    print("=" * 30)


# proje_adi = parametre (fonksiyon tanımında)
# "Logo Tasarımı" = argüman (çağırırken verilen değer)

proje_basligi("Logo Tasarımı")
print()
proje_basligi("Poster")
print()
proje_basligi("Web Sitesi")

# Her çağrıda proje_adi farklı bir değere sahip olur.
# Aynı fonksiyon, farklı verilerle farklı sonuç üretir.


# --- Birden Fazla Parametre ---
print()
print("--- Proje Kartları ---")
print()


def proje_karti(ad, kategori, puan):
    print(f"Proje: {ad}")
    print(f"Kategori: {kategori}")
    print(f"Puan: {puan}")
    print("-" * 20)


proje_karti("Logo Tasarımı", "Kurumsal", 88)
proje_karti("Film Afişi", "Poster", 95)
proje_karti("Mobil Uygulama", "Dijital", 82)


# --- Sıra Önemlidir! ---
# İlk argüman → ilk parametre (ad)
# İkinci argüman → ikinci parametre (kategori)
# Üçüncü argüman → üçüncü parametre (puan)

# YANLIŞ sıra — ad ve kategori yer değiştirir:
print("--- Yanlış sıra örneği ---")
proje_karti("Kurumsal", "Logo Tasarımı", 88)
# Çıktı: Proje: Kurumsal, Kategori: Logo Tasarımı
# Python hata vermez ama anlam yanlış olur!


# --- Fonksiyon + Döngü ---
# Fonksiyonları döngüyle birlikte kullanmak çok güçlüdür.
print()
print("--- Tüm Renkleri Göster ---")
print()


def renk_bilgisi(renk_adi, hex_kodu):
    print(f"Renk: {renk_adi}")
    print(f"HEX: {hex_kodu}")
    print("----------")


# Bir listeden döngüyle çağıralım
renkler = [
    ("Turkuaz", "#40E0D0"),
    ("Mercan", "#FF7F50"),
    ("Lavanta", "#E6E6FA"),
]

for renk_adi, hex_kodu in renkler:
    renk_bilgisi(renk_adi, hex_kodu)
# Demet listesini for ile geziyoruz (Hafta 3'ten hatırlayın).
# Her demet iki elemanlı: renk adı ve HEX kodu.
# Bunları doğrudan fonksiyona geçiriyoruz.
