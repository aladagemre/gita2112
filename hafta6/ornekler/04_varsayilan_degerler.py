# =============================================================
# DERS 4: Varsayılan Değerler ve Boolean Döndüren Fonksiyonlar
# =============================================================
# Bu derste öğreneceğiz:
#   - Varsayılan (default) parametre değerleri
#   - Parametrelerin sıralama kuralı
#   - Koşul içeren fonksiyonlar
#   - Boolean döndüren fonksiyonlar
#   - İsimli argümanlar (keyword arguments)
# =============================================================


# --- Varsayılan Değerler ---
# Bazı parametrelere "varsayılan değer" verebiliriz.
# Çağırırken o parametreyi belirtmezsek varsayılan kullanılır.

def cizgi(uzunluk=30, karakter="-"):
    print(karakter * uzunluk)


print("--- Çizgi Örnekleri ---")
cizgi()              # ------------------------------ (her iki varsayılan)
cizgi(50)            # 50 tane - (uzunluk değişti, karakter varsayılan)
cizgi(20, "=")       # ==================== (her ikisi de özel)
cizgi(karakter="*")  # ****************************** (sadece karakter değişti)

# Son satırdaki "karakter=" yazımına dikkat:
# Bu, "isimli argüman" (keyword argument) kullanımıdır.
# Sırayı atlamak istediğimizde parametre adını yazarız.


# --- Sıralama Kuralı ---
# Zorunlu parametreler ÖNCE, varsayılan değerliler SONRA gelir.

def proje_karti(ad, puan, durum="Devam Ediyor"):
    print(f"  {ad} ({durum}) → {puan} puan")


print()
print("--- Proje Kartları ---")
proje_karti("Logo", 88)                        # durum = "Devam Ediyor"
proje_karti("Poster", 95, "Tamamlandı")        # durum = "Tamamlandı"
proje_karti("Web Sitesi", 72, "Revize Gerekli") # durum = "Revize Gerekli"

# ad ve puan zorunlu (her çağrıda verilmeli)
# durum opsiyonel (vermezsen "Devam Ediyor" olur)


# --- Koşul İçeren Fonksiyon ---

def basari_durumu(puan):
    if puan >= 90:
        return "Mükemmel"
    elif puan >= 75:
        return "Başarılı"
    elif puan >= 60:
        return "Geçti"
    else:
        return "Kaldı"


print()
print("--- Başarı Durumları ---")
print(basari_durumu(92))   # Mükemmel
print(basari_durumu(80))   # Başarılı
print(basari_durumu(68))   # Geçti
print(basari_durumu(45))   # Kaldı

# Her return çalıştığında fonksiyon biter.
# Puan 92 ise ilk return çalışır, geri kalanlar atlanır.


# --- Bir Listede Kullanalım ---
print()
print("--- Puan Tablosu ---")

puanlar = [88, 45, 92, 71, 63, 95]

for p in puanlar:
    print(f"  {p} puan → {basari_durumu(p)}")

# Fonksiyonu bir kez tanımladık, 6 farklı puanla çağırdık.
# Her çağrıda farklı sonuç döner.


# --- Boolean Döndüren Fonksiyon ---
# True veya False döndüren fonksiyonlar çok kullanışlıdır.

def gecti_mi(puan, sinir=60):
    return puan >= sinir


print()
print("--- Geçti mi? ---")
print(f"75 puan: {gecti_mi(75)}")       # True
print(f"45 puan: {gecti_mi(45)}")       # False
print(f"55/50: {gecti_mi(55, 50)}")     # True (sınır 50 yapıldı)

# if ile kullanımı — çok okunabilir!
print()
notu = 85
if gecti_mi(notu):
    print(f"{notu} puanla dersi geçtiniz!")
else:
    print(f"{notu} puanla dersi geçemediniz.")


# --- Pratik Örnek: Tasarım Boyutu Kontrolü ---

def baskiya_uygun_mu(genislik, yukseklik, min_dpi=300):
    # A4 boyutu: 21 x 29.7 cm
    # Minimum piksel = boyut * DPI / 2.54 (cm → inç çevirimi)
    min_piksel_x = 21 * min_dpi / 2.54
    min_piksel_y = 29.7 * min_dpi / 2.54
    return genislik >= min_piksel_x and yukseklik >= min_piksel_y


print()
print("--- Baskıya Uygunluk ---")

if baskiya_uygun_mu(3000, 4000):
    print("3000x4000: Baskıya uygun!")
else:
    print("3000x4000: Çözünürlük yetersiz.")

if baskiya_uygun_mu(800, 600):
    print("800x600: Baskıya uygun!")
else:
    print("800x600: Çözünürlük yetersiz.")
