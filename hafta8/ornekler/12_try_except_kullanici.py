# =========================================================
# GİTA 2112 — Hafta 9 — Örnek 03
# Konu: try / except ile kullanıcı girişi
# Ne öğretiyor:
#   - input() ile gelen metni int()/float()'a çevirirken ValueError
#   - Döngü içinde try/except — "kullanıcı geçerli girdi verene kadar sor"
#   - Kullanıcıya net hata mesajı verme
# Not:
#   - Bu dosya input() kullanır. Çalıştırırken terminalde yazı bekler.
#   - Denemek için 'mercan', '-5', '12' gibi farklı şeyler dene.
# =========================================================

# --- 1. En basit hali ---------------------------------------------------
# Kullanıcıdan bir renk için RGB değeri istiyoruz (0-255 arası).
# Kullanıcı 'mavi' gibi bir şey yazarsa int() patlar.

ham_giris = input("Bir RGB değeri gir (0-255): ")

try:
    deger = int(ham_giris)
    print("Aldığın değer:", deger)
except ValueError:
    print("Bu bir sayı değildi. 'mavi' gibi bir şey yazdın olabilir.")

print("---")


# --- 2. Geçerli aralık kontrolü ----------------------------------------
# Kullanıcı sayı verdi ama 300 yazdı. 300 RGB için geçersiz.
# Bunu da yakalayalım: hem ValueError hem aralık kontrolü.

ham_giris = input("RGB değeri (0-255): ")

try:
    deger = int(ham_giris)
    if deger < 0 or deger > 255:
        print(f"{deger} aralık dışında. 0-255 arası bekliyorum.")
    else:
        print(f"Geçerli RGB: {deger}")
except ValueError:
    print("Sayı bekliyordum ama metin geldi.")

print("---")


# --- 3. Döngü içinde try/except — geçerli girdi alana kadar sor --------
# Çoğu zaman kullanıcı yanlış yazarsa "tekrar dene" deriz. Bunun için
# while True + try/except + break deseni kullanılır.

while True:
    ham_giris = input("Bir tasarım için sayfa sayısı gir (>0): ")
    try:
        sayfa = int(ham_giris)
        if sayfa <= 0:
            print("Sıfırdan büyük olmalı. Tekrar dene.")
            continue
        break                       # geçerli girdi — döngüden çık
    except ValueError:
        print("Sayı yazmalısın. Tekrar dene.")

print(f"Tamam, {sayfa} sayfalık bir tasarım yapacağız.")

print("---")


# --- 4. Birden fazla soru, her biri kendi try/except ile ----------------
# Bir müşteri brifi alıyoruz. Her alan farklı tipte.

# 4a. Proje adı (sadece metin, hata fırlatmaz)
proje_adi = input("Proje adı: ")

# 4b. Bütçe (sayı olmalı — burada try/except)
while True:
    ham = input("Bütçe (TL, ör: 5000): ")
    try:
        butce = float(ham)
        break
    except ValueError:
        print("Sayı olmalı (örnek: 5000 ya da 5000.50).")

# 4c. Renk sayısı (tam sayı — burada da try/except)
while True:
    ham = input("Kaç renk kullanılacak (tam sayı): ")
    try:
        renk_sayisi = int(ham)
        if renk_sayisi <= 0:
            print("Sıfırdan büyük olmalı.")
            continue
        break
    except ValueError:
        print("Tam sayı olmalı.")

# Özeti yazdır
print()
print("=== BRİF ÖZETİ ===")
print(f"Proje: {proje_adi}")
print(f"Bütçe: {butce} TL")
print(f"Renk sayısı: {renk_sayisi}")
