# =============================================================
# DERS 6: CSV Dosyaları
# =============================================================
# Bu derste öğreneceğiz:
#   - CSV nedir, neden tablo verileri için kullanılır
#   - csv.reader ile okuma
#   - csv.writer ile yazma
#   - Renk paletleri gibi tablo verisini işleme
# =============================================================


# --- Sorun: Tablo Şeklindeki Veri ---
#
# Bir renk paletinde her renk için birden fazla bilgi var:
# isim, hex kodu, sıcak/soğuk grubu...
#
# Düz .txt dosyası bunu beceremiyor, çünkü .txt sadece
# satır satır metindir. Tablo gibi kolonlar yok.
#
# Çözüm: CSV (Comma-Separated Values, virgülle ayrılmış)


# --- veri/renkler.csv Dosyasının İçeriği ---
#
# isim,hex,grup
# Mercan,#FF6B6B,sıcak
# Lacivert,#1E3A8A,soğuk
# Sarı,#FFD93D,sıcak
# ...
#
# İlk satır KOLON BAŞLIKLARI (header)
# Diğer satırlar VERİ — virgüllerle ayrılmış kolonlar


import csv


print("=== CSV Okuma ve Yazma ===")
print()


# --- Yöntem 1: csv.reader ile Okuma ---

print("--- 1. csv.reader ile okuma ---")

with open("veri/renkler.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    for satir in okuyucu:
        # satir bir LİSTEDİR, kolonlara karşılık gelir
        # Örnek: ["Mercan", "#FF6B6B", "sıcak"]
        print(satir)

print()


# --- Yöntem 2: Başlık Satırını Atlamak ---
#
# İlk satır kolon başlıklarıdır, veriden değildir.
# Çoğu zaman onu atlamak isteriz.

print("--- 2. Başlığı atlayıp veriyi gezme ---")

with open("veri/renkler.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    basliklar = next(okuyucu)   # ilk satırı al, ileri git
    print(f"Başlıklar: {basliklar}")
    print()

    for satir in okuyucu:
        isim = satir[0]
        hex_kod = satir[1]
        grup = satir[2]
        print(f"{isim:10s} {hex_kod}  ({grup})")

print()
# {isim:10s} = ismi 10 karakter genişliğinde sola yasla


# --- Yöntem 3: Filtreleme ---
#
# Sadece sıcak renkleri alalım.

print("--- 3. Filtreleme: sadece sıcak renkler ---")

sicak_renkler = []

with open("veri/renkler.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    next(okuyucu)   # başlığı atla

    for satir in okuyucu:
        if satir[2] == "sıcak":
            sicak_renkler.append(satir[0])

print(f"Sıcak renkler: {sicak_renkler}")
print(f"Toplam: {len(sicak_renkler)}")
print()


# --- Yöntem 4: Sayma (her gruptan kaç tane?) ---

print("--- 4. Gruplara göre sayma ---")

sayilar = {"sıcak": 0, "soğuk": 0, "nötr": 0}

with open("veri/renkler.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    next(okuyucu)

    for satir in okuyucu:
        grup = satir[2]
        sayilar[grup] = sayilar[grup] + 1

for grup, sayi in sayilar.items():
    print(f"{grup}: {sayi} renk")

print()


# --- CSV Yazma ---
#
# Yeni bir CSV dosyası üretelim — sadece sıcak renklerin olduğu.

print("--- 5. csv.writer ile yazma ---")

with open("sicak_palet.csv", "w", encoding="utf-8", newline="") as dosya:
    yazici = csv.writer(dosya)
    yazici.writerow(["isim", "hex"])    # başlık satırı
    yazici.writerow(["Mercan", "#FF6B6B"])
    yazici.writerow(["Sarı", "#FFD93D"])
    yazici.writerow(["Turuncu", "#FF9F45"])

print("sicak_palet.csv oluşturuldu.")
print()

# Not: Yazarken newline="" parametresi Windows'ta boş satır
# araya girmesini engeller. Sadece yazarken eklemeniz yeterli.


# --- Yazdığımızı Geri Okuyalım ---

print("--- 6. Yazdığımız dosyayı kontrol ---")

with open("sicak_palet.csv", "r", encoding="utf-8") as dosya:
    print(dosya.read())


# --- Tasarım Bağlamı ---
#
# CSV, tasarım dünyasında çok yaygın:
#   - Adobe Color paletini export ederseniz CSV alırsınız
#   - Müşteri size Excel/Google Sheets'ten CSV gönderir
#   - Anket verileri, kullanıcı geri bildirimleri CSV olur
#
# Python'la CSV okumayı bilmek = bir "veri okuyucu" olmak.


# --- Sık Yapılan Hatalar ---
#
# 1. csv import etmeyi unutmak:
#    "NameError: name 'csv' is not defined"
#    → Dosyanın başına import csv ekleyin
#
# 2. Yazarken newline="" yazmamak (Windows):
#    Her satırın arasında boş bir satır oluşur.
#
# 3. Türkçe karakter bozulması:
#    Her zaman encoding="utf-8" yazın.
#
# 4. satir[2] yerine satir[3] yazmak:
#    "IndexError: list index out of range"
#    → Kaç kolon var, kontrol edin (0'dan başlar)


# --- Özet ---
print("--- Özet ---")
print("import csv → modülü etkinleştir")
print("csv.reader(dosya) → satır satır oku, her satır liste")
print("next(okuyucu) → ilk satırı (başlığı) atla")
print("csv.writer(dosya) → yazma")
print("yazici.writerow([...]) → bir satır yaz")
