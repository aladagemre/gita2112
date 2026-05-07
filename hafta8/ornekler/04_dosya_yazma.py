# =============================================================
# DERS 4: Dosya Yazma
# =============================================================
# Bu derste öğreneceğiz:
#   - "w" modu: yazma (eski içeriği siler!)
#   - "a" modu: append (sonuna ekler)
#   - .write() ile yazma
#   - "\n" yeni satır karakteri
#   - Bir listeyi dosyaya yazma
# =============================================================


# --- Sorun: Sonucu Saklamak ---
#
# Geçen derste dosyadan okuduk. Peki ya yeni bir tasarım
# brifi yazıp diske KAYDETMEK istesek?
#
# Bir öğrenci anketi topladık, sonuçları bir dosyaya
# yazıp daha sonra açmak istiyoruz?
#
# Bu derste dosyaya YAZMAYI öğreneceğiz.


print("=== Dosya Yazma Örnekleri ===")
print()


# --- Yazma Modları ---
#
#   "w" — write (sıfırdan yaz, varsa sil ve baştan yaz)
#   "a" — append (var olan dosyanın SONUNA ekle)
#
# DİKKAT: "w" ile mevcut bir dosyayı açmak içeriği SİLER.
# Photoshop'ta "Save As" yapıp aynı isimle üstüne yazmak gibi.


# --- Örnek 1: Yeni Bir Renk Paleti Yazma ---

print("--- 1. Tek satırlık yazma ---")

with open("yeni_palet.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Mercan\n")
    dosya.write("Lacivert\n")
    dosya.write("Sarı\n")

print("yeni_palet.txt dosyası oluşturuldu.")
print()

# "\n" yeni satır karakteridir. Yazmazsanız tüm renkler
# birbirine yapışır: "MercanLacivertSarı"


# --- Örnek 2: Listeyi Döngüyle Yazma ---

print("--- 2. Listeyi yazma (döngü ile) ---")

projeler = [
    "Caz Festivali Afişi",
    "Kitap Kapağı",
    "Web Sitesi",
    "Logo Tasarımı",
]

with open("projelerim.txt", "w", encoding="utf-8") as dosya:
    for proje in projeler:
        dosya.write(proje + "\n")

print(f"{len(projeler)} proje dosyaya yazıldı.")
print()


# --- Örnek 3: Dosya Sonuna Ekleme (append) ---
#
# Var olan bir dosyaya yeni bir şey eklemek istiyorsanız
# "w" değil "a" kullanın. "w" eskisini siler, "a" sonuna ekler.

print("--- 3. Dosya sonuna ekleme (a modu) ---")

# Önce mevcut dosyaya yeni bir proje ekleyelim:
with open("projelerim.txt", "a", encoding="utf-8") as dosya:
    dosya.write("Sergi Kataloğu\n")

# Şimdi okuyup gösterelim:
with open("projelerim.txt", "r", encoding="utf-8") as dosya:
    print(dosya.read())


# --- Örnek 4: Format ile Yazma (f-string) ---

print("--- 4. f-string ile zengin yazma ---")

ogrenciler = [
    {"isim": "Defne", "puan": 88},
    {"isim": "Cem", "puan": 76},
    {"isim": "Ayşe", "puan": 92},
]

with open("notlar.txt", "w", encoding="utf-8") as dosya:
    dosya.write("=== Hafta 8 Notlari ===\n")
    dosya.write("\n")
    for ogrenci in ogrenciler:
        satir = f"{ogrenci['isim']}: {ogrenci['puan']} puan\n"
        dosya.write(satir)

# Yazdığımız dosyayı tekrar okuyalım:
with open("notlar.txt", "r", encoding="utf-8") as dosya:
    print(dosya.read())


# --- Tasarım Bağlamı ---
#
# Bir müşteri brifi, proje notları, font listesi, renk paleti...
# Hepsini Python ile üretip dosyaya yazabilirsiniz.
# Sonra Word veya InDesign'da açıp tasarıma katabilirsiniz.


# --- "w" vs "a" Sık Karıştırılan Tuzak ---
#
# Aşağıdaki kod sadece "Cem"i bırakır, diğerlerini siler!
# Çünkü her seferinde "w" modunu kullandı:
#
#   for isim in ["Defne", "Cem", "Ayşe"]:
#       with open("isimler.txt", "w", encoding="utf-8") as dosya:
#           dosya.write(isim + "\n")
#
# Çözüm 1: Döngünün dışına çıkar, dosyayı bir kez aç
# Çözüm 2: "w" yerine "a" kullan


# --- Doğru Kalıp ---

print("--- 5. Doğru kalıp: dosyayı bir kez aç ---")

with open("isimler_dogru.txt", "w", encoding="utf-8") as dosya:
    for isim in ["Defne", "Cem", "Ayşe"]:
        dosya.write(isim + "\n")

with open("isimler_dogru.txt", "r", encoding="utf-8") as dosya:
    print(dosya.read())


# --- Özet ---
print("--- Özet ---")
print('"w" modu → sıfırdan yaz (eski silinir)')
print('"a" modu → sonuna ekle')
print(".write(metin) → metni dosyaya yaz")
print('"\\n" → yeni satır karakteri')
print("Döngüde dosyayı bir kez açın, içinde tek tek yazın")
