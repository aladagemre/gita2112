# =============================================================
# DERS 3: Dosya Okuma
# =============================================================
# Bu derste öğreneceğiz:
#   - with open(...) deyimi
#   - encoding="utf-8" zorunluluğu
#   - .read() ile tüm dosyayı okuma
#   - .readlines() ile liste olarak okuma
#   - for ile satır satır gezme
# =============================================================


# --- Sorun: Bilgi Programdan Sonra Kayboluyor ---
#
# Şimdiye kadar her renk listesi, her sayı, her bilgi
# Python kodunun içinde yazılıydı:
#
#   renkler = ["Mercan", "Lacivert", "Sarı"]
#
# Ama gerçek hayatta veri DIŞARIDAN gelir:
#   - Müşteri size bir liste yolladı
#   - Photoshop'tan bir renk paleti export ettiniz
#   - Anketten cevaplar topladınız
#
# Bu verileri DOSYADAN okumayı öğrenmek zorundayız.


print("=== Dosya Okuma Örnekleri ===")
print()


# --- Yöntem 1: Tüm Dosyayı Tek Seferde Oku (.read) ---
#
# En basit hali: dosyayı aç, içindeki her şeyi tek bir
# uzun metin olarak al.

print("--- 1. read() ile tek seferde okuma ---")

with open("veri/renkler.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()

print(icerik)
print(f"İçeriğin tipi: {type(icerik).__name__}")
print(f"Karakter sayısı: {len(icerik)}")
print()

# Önemli noktalar:
#   - "veri/renkler.txt" → göreli yol
#   - "r" → read (okuma) modu
#   - encoding="utf-8" → Türkçe karakter desteği
#   - with ... as dosya → bittiğinde dosyayı otomatik kapatır


# --- Yöntem 2: Satır Satır Gez (for döngüsü) ---
#
# Çoğu zaman dosyayı tek seferde değil, satır satır
# işleriz. Bu özellikle uzun dosyalarda önemlidir.

print("--- 2. for ile satır satır okuma ---")

with open("veri/renkler.txt", "r", encoding="utf-8") as dosya:
    sayac = 1
    for satir in dosya:
        # satir sonunda görünmez bir "\n" karakteri vardır
        # strip() onu temizler
        renk = satir.strip()
        print(f"{sayac}. {renk}")
        sayac += 1

print()


# --- Yöntem 3: Tüm Satırları Liste Olarak Al (.readlines) ---
#
# Bazen dosyanın tüm satırlarını LİSTE olarak isteriz.
# Sonra liste üzerinde alışık olduğumuz işlemleri yapabiliriz.

print("--- 3. readlines() ile liste olarak okuma ---")

with open("veri/renkler.txt", "r", encoding="utf-8") as dosya:
    satirlar = dosya.readlines()

# satirlar artık bir liste — her elemanı bir satır
# Ama her elemanın sonunda \n var, strip() ile temizleyelim
renkler = [s.strip() for s in satirlar]

print(f"Liste: {renkler}")
print(f"Toplam renk sayısı: {len(renkler)}")
print()

# Not: Yukarıdaki [s.strip() for s in satirlar] yapısı
# "list comprehension" denilen bir Python kısayoludur.
# Tek satırda for döngüsü + listeye ekleme yapar.
# Şimdilik yazmanız beklenmiyor, sadece görünce anlayın.


# --- Bilgi Sayma Örneği ---
#
# Dosyadaki renklerden kaç tanesi "T" harfiyle başlıyor?
# Bunu bulmak için liste üzerinde döngü kuruyoruz.

print("--- 4. Veri üzerinde işlem yapma ---")

t_ile_baslayanlar = []
for renk in renkler:
    if renk.startswith("T"):
        t_ile_baslayanlar.append(renk)

print(f"T ile başlayanlar: {t_ile_baslayanlar}")
print(f"Sayı: {len(t_ile_baslayanlar)}")
print()


# --- Tasarım Bağlamı ---
#
# Düşünün: bir müşteri size 200 renkten oluşan bir Pantone
# listesi verdi. Sıcak olanları ayırmanız lazım.
# Listeyi tek tek elle ayırmak saatler alır.
# Dosyadan okuyup döngüyle filtrelemek 10 satır kod, saniyede biter.


# --- encoding'i Unutursanız Ne Olur? ---
#
# Aşağıdaki satırı yorum dışı (#) bırakırsanız Windows'ta
# muhtemelen şöyle bir şey görürsünüz: "ﬂarı" yerine "Sarı"
# Türkçe karakterler bozulur. Mac'te genelde sorun olmaz
# ama her dosyada encoding="utf-8" yazma alışkanlığı edinin.
#
# with open("veri/renkler.txt", "r") as dosya:        # encoding YOK
#     print(dosya.read())


# --- Özet ---
print("--- Özet ---")
print("with open(...) as dosya: → güvenli açma deyimi")
print('"r" modu → okuma')
print('encoding="utf-8" → Türkçe karakter')
print(".read() → tek seferde tüm metin")
print("for satir in dosya: → satır satır gezme")
print(".readlines() → tüm satırlar liste olarak")
