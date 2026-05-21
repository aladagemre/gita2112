# =========================================================
# GİTA 2112 — Hafta 9 — Örnek 02
# Konu: try / except ile dosya işlemleri
# Ne öğretiyor:
#   - FileNotFoundError'ı yakalama
#   - "Önce kontrol et" yerine "dene, hata olursa yakala" felsefesi
#   - Kullanıcıya anlamlı Türkçe hata mesajı verme
#   - Dosya yokken programın çökmemesi
# =========================================================

# --- 1. Dosya yoksa ne olur? --------------------------------------------
# Olmayan bir dosyayı açmaya çalışırsak Python FileNotFoundError fırlatır.
# Bunu yakalarsak program çökmez, kullanıcıya nazik bir mesaj verebiliriz.

dosya_adi = "olmayan_palet.txt"

try:
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        icerik = dosya.read()
    print("Dosya içeriği:")
    print(icerik)
except FileNotFoundError:
    print(f"'{dosya_adi}' bulunamadı. Dosya adını ve klasörü kontrol et.")

# Çıktı:
# 'olmayan_palet.txt' bulunamadı. Dosya adını ve klasörü kontrol et.

print("---")


# --- 2. Var olan dosyayı oluştur, sonra oku -----------------------------
# Önce küçük bir palet dosyası yazıyoruz. Sonra onu okumayı deneyeceğiz.
# Bu sefer dosya var, try bloğu sorunsuz çalışır.

with open("palet_demo.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Mercan\n")
    dosya.write("Lacivert\n")
    dosya.write("Hardal\n")

try:
    with open("palet_demo.txt", "r", encoding="utf-8") as dosya:
        renkler = dosya.read()
    print("Palet okundu:")
    print(renkler)
except FileNotFoundError:
    print("Bu satıra düşmemeli — dosyayı yukarıda oluşturduk.")

# Çıktı:
# Palet okundu:
# Mercan
# Lacivert
# Hardal


print("---")


# --- 3. "Dosya yoksa varsayılan değer kullan" deseni --------------------
# Tasarım yazılımlarında sık görülen bir desen: kullanıcı ayar dosyası
# kaydetmemişse fabrika ayarlarını yükle. Aynı şey burada.

varsayilan_renkler = ["#000000", "#FFFFFF"]

try:
    with open("musteri_paleti.txt", "r", encoding="utf-8") as dosya:
        renkler = [satir.strip() for satir in dosya]
    print("Müşteri paleti yüklendi.")
except FileNotFoundError:
    renkler = varsayilan_renkler
    print("Müşteri paleti yok, varsayılan siyah-beyaz kullanılıyor.")

print("Renkler:", renkler)

# Çıktı (musteri_paleti.txt yoksa):
# Müşteri paleti yok, varsayılan siyah-beyaz kullanılıyor.
# Renkler: ['#000000', '#FFFFFF']

print("---")


# --- 4. Hatayı yakalamak yerine açıklamak -------------------------------
# "as e" ile hatanın kendisini değişkene alıp ekrana basabiliriz.
# Bu, kullanıcıya neyin yanlış olduğunu net göstermek için faydalı.

try:
    with open("yine_olmayan.json", "r", encoding="utf-8") as dosya:
        veri = dosya.read()
except FileNotFoundError as e:
    print("Dosya açılamadı.")
    print("Python'un mesajı:", e)
    print("Çözüm önerisi: dosyanın aynı klasörde olduğundan emin ol.")

# Çıktı:
# Dosya açılamadı.
# Python'un mesajı: [Errno 2] No such file or directory: 'yine_olmayan.json'
# Çözüm önerisi: dosyanın aynı klasörde olduğundan emin ol.

print("---")


# --- 5. Yazma hatası — PermissionError ----------------------------------
# Bazı klasörlere yazma izniniz olmayabilir. Bu PermissionError fırlatır.
# Pratikte FileNotFoundError ve PermissionError'ı birlikte yakalamak yaygın.
# Aşağıdaki kod sistem klasörüne yazmaya çalışıyor — büyük olasılıkla başarısız olur.

try:
    with open("/kok_dizini_olamaz/test.txt", "w", encoding="utf-8") as dosya:
        dosya.write("test")
    print("Yazma başarılı.")
except FileNotFoundError:
    print("Klasör bulunamadı.")
except PermissionError:
    print("Bu klasöre yazma iznin yok.")

# Çıktı (sistemine göre değişebilir):
# Klasör bulunamadı.
