# =============================================================
# DERS 1: İlk Fonksiyon — Tanımlama ve Çağırma
# =============================================================
# Bu derste öğreneceğiz:
#   - def ile fonksiyon tanımlama
#   - Fonksiyon çağırma
#   - Tanımlama ile çağırma farkı
#   - Fonksiyon adı seçimi
# =============================================================


# --- Sorun: Tekrar Eden Kod ---
# Aynı formatta birkaç proje başlığı yazdırmak istiyoruz.
# Her biri için aynı satırları tekrar yazıyoruz:

print("=" * 30)
print("Proje: Logo Tasarımı")
print("=" * 30)

print()

print("=" * 30)
print("Proje: Poster Tasarımı")
print("=" * 30)

print()

print("=" * 30)
print("Proje: Web Sitesi")
print("=" * 30)

# 3 proje için 9 satır print yazdık.
# 20 proje olsa? Ayıracı değiştirmek istesek?
# Her birini tek tek mi düzenleyeceğiz?


# --- Çözüm: Fonksiyon ---
# Tekrar eden kodu bir fonksiyon içine koyuyoruz.

print()
print("--- Fonksiyon ile ---")
print()


# Fonksiyon TANIMLAMA
# def = "define" = tanımla
# Parantez ve iki nokta üst üste zorunlu
# İçindeki kod girintili yazılır (if ve for'daki gibi)

def hosgeldin():
    print("*" * 30)
    print("Stüdyoya hoş geldiniz!")
    print("*" * 30)


# ÖNEMLİ: Yukarıdaki kod sadece fonksiyonu TANIMLADI.
# Henüz çalışmadı! Tarif yazıldı ama uygulanmadı.

# Fonksiyon ÇAĞIRMA — şimdi çalışır:
hosgeldin()

print()

# İstediğimiz kadar çağırabiliriz:
hosgeldin()


# --- Başka Bir Örnek ---

def cizgi_ciz():
    print("-" * 40)


print()
print("Projelerim")
cizgi_ciz()
print("1. Logo Tasarımı")
print("2. Poster")
print("3. Web Sitesi")
cizgi_ciz()
# cizgi_ciz() fonksiyonunu iki kez çağırdık.
# Çizgi stilini değiştirmek istesek sadece fonksiyonun
# içini düzenleriz — her iki çağrı otomatik güncellenir.


# --- Fonksiyon Adı Seçimi ---
# İyi isim örnekleri:
#   selamla, cizgi_ciz, puan_hesapla, baslik_yazdir
#
# Kötü isim örnekleri:
#   f, x, fonksiyon1, asdf
#
# Kurallar:
#   - Küçük harf kullanın
#   - Birden fazla kelime varsa _ ile ayırın
#   - İsim ne yaptığını anlatsın
