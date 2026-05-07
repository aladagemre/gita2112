# =============================================================
# DERS 8: Traceback (Hata Mesajı) Okuma Kültürü
# =============================================================
# Bu derste öğreneceğiz:
#   - Bir traceback'in nasıl okunduğu
#   - 5 sık görülen hata tipi
#   - Her hatanın neden olduğu ve nasıl çözüleceği
#
# UYARI: Bu dosya KASITLI hata üretmek için yazılmıştır.
# Aşağıdaki örnek bloklarını sırayla AÇIP DENEYİN.
# Açma/kapama için yorum satırlarını (#) kaldırıp tekrar koyun.
# =============================================================


print("=== Traceback Okuma Atölyesi ===")
print()


# --- Traceback'in Yapısı ---
#
# Bir hata mesajı genelde 3 parçadan oluşur:
#
# Traceback (most recent call last):    ← "şimdi hata göstereceğim"
#   File "kod.py", line 5, in <module>  ← NEREDE (dosya + satır)
#     print(yas)                         ← O satırın içeriği
# NameError: name 'yas' is not defined  ← NE TÜR HATA + AÇIKLAMA
#
# Refleksiniz: ÖNCE EN ALT SATIRA BAKIN.
# Sonra "File ... line N" satırına bakıp o satıra gidin.


# =============================================================
# Hata 1: NameError
# =============================================================
# Olmayan / yanlış yazılmış değişken kullanma.

print("--- Hata 1: NameError ---")
print("Yorum satırını açın, çalıştırın, hatayı okuyun.")
print()

# AŞAĞIDAKI 2 SATIRDAKİ # İŞARETİNİ KALDIRIN VE ÇALIŞTIRIN:
# yas = 20
# print(yass)   # ← yass yanlış, yas doğru. NameError!

# Beklenen hata:
# NameError: name 'yass' is not defined
#
# Çözüm: Değişken adını kontrol edin.
# Tipo bulmak için: Ctrl+F ile dosyada arayın.


# =============================================================
# Hata 2: TypeError
# =============================================================
# Uyumsuz tipleri birleştirme.

print("--- Hata 2: TypeError ---")
print()

# AŞAĞIDAKI 2 SATIRDAKİ # İŞARETİNİ KALDIRIN VE ÇALIŞTIRIN:
# yas = 20
# mesaj = "Yaşım: " + yas   # str + int olmaz!

# Beklenen hata:
# TypeError: can only concatenate str (not "int") to str
#
# Çözüm 1: str(yas) ile dönüştür
# Çözüm 2: f-string kullan: f"Yaşım: {yas}"


# =============================================================
# Hata 3: IndentationError
# =============================================================
# Girinti hatası.

print("--- Hata 3: IndentationError ---")
print()

# !!! DİKKAT: IndentationError SYNTAX hatasıdır. Yani Python dosyayı
# OKURKEN hata verir — dosyadaki HİÇBİR satır çalışmaz, üstündeki
# print'ler bile.
# Bu yüzden bu denemeyi YALNIZ BAŞINA, ayrı bir dosyada yapın
# (örneğin: deneme.py oluşturup içine 4 satırı yazın).
#
# Aşağıdaki 4 satırı KOPYALAYIP başka bir dosyaya yapıştırın
# ve oradan çalıştırın:
#
# def selamla():
# print("Merhaba")   # ← girintili olması gerekirdi
#
# selamla()

# Beklenen hata:
# IndentationError: expected an indented block after function definition
#
# Çözüm: def, for, if, while sonrası SATIR girintili olmalı.
# Tab ya da 4 boşluk kullanın, ikisini karıştırmayın.


# =============================================================
# Hata 4: FileNotFoundError
# =============================================================
# Açmaya çalıştığın dosya yok.

print("--- Hata 4: FileNotFoundError ---")
print()

# AŞAĞIDAKI 2 SATIRDAKİ # İŞARETİNİ KALDIRIN VE ÇALIŞTIRIN:
# with open("yokboyle.txt", "r", encoding="utf-8") as f:
#     icerik = f.read()

# Beklenen hata:
# FileNotFoundError: [Errno 2] No such file or directory: 'yokboyle.txt'
#
# Çözüm:
# 1. Dosya adını doğru mu yazdınız?
# 2. Dosya bu klasörde mi? (terminalde pwd + ls ile bakın)
# 3. Göreli yol doğru mu? Mesela "veri/yokboyle.txt" olabilir mi?


# =============================================================
# Hata 5: ModuleNotFoundError
# =============================================================
# Kurulu olmayan paketi import etmek.

print("--- Hata 5: ModuleNotFoundError ---")
print()

# AŞAĞIDAKI 1 SATIRDAKİ # İŞARETİNİ KALDIRIN VE ÇALIŞTIRIN:
# import yokboyle_paket

# Beklenen hata:
# ModuleNotFoundError: No module named 'yokboyle_paket'
#
# Çözüm:
# 1. Paket adını doğru mu yazdınız?
# 2. Standart kütüphane mi (math, random, csv, json)?
#    → Tipo olabilir.
# 3. Dış paket mi (pillow, requests)?
#    → uv add paket-adi ile kurun.


# =============================================================
# Bonus: KeyError
# =============================================================
# Sözlükte olmayan anahtarı çağırma.

print("--- Bonus: KeyError ---")
print()

proje = {"ad": "Caz Festivali", "tarih": "2026-06-15"}

# AŞAĞIDAKI 1 SATIRDAKİ # İŞARETİNİ KALDIRIN VE ÇALIŞTIRIN:
# print(proje["mekan"])   # "mekan" anahtarı yok!

# Beklenen hata:
# KeyError: 'mekan'
#
# Çözüm:
# 1. Anahtar adını doğru mu yazdınız?
# 2. proje.keys() ile mevcut anahtarları görebilirsiniz.


# --- Pratik İpucu: Hata Mesajını GOOGLE'A YAPIŞTIRIN ---
#
# Hata mesajının son satırını kopyalayıp Google'a (veya
# Gemini'ye) yapıştırmak çoğu zaman cevaba 10 saniyede ulaştırır.
# Stackoverflow'da binlerce kişi aynı hatayı yaşamıştır.
#
# Ama önce KENDİ HATANIZI OKUYUN. Neyi söylediğini anlamadan
# yapıştırırsanız hep yardıma muhtaç olursunuz.


# --- Hata Çözme Refleksleri ---
#
# 1. Paniğe kapılmayın. Hata mesajı yardımcıdır.
# 2. EN ALT SATIRA bakın — hata adı ve açıklaması.
# 3. "File ... line N" satırına bakın — hatanın yeri.
# 4. O satıra gidin, tek tek inceleyin.
# 5. Çözemediyseniz hata mesajını arayın (Google, hoca, arkadaş).


# --- Bu Dosyayı Çalıştırırsanız ---
print("Bu dosya hata üretmek için tasarlandı.")
print("Şu an düz çalışıyor çünkü hatalar yorum satırında.")
print("Sırayla yorumları kaldırıp her hatanın çıktısını okuyun.")
