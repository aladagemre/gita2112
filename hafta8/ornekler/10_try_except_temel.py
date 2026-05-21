# =========================================================
# GİTA 2112 — Hafta 9 — Örnek 01
# Konu: try / except temelleri
# Ne öğretiyor:
#   - try/except yapısının temel iskeleti
#   - Birden fazla except bloğu (farklı hata tipleri)
#   - else ve finally bloklarının rolü
#   - "Önce dene, hata olursa yakala" felsefesi
# =========================================================

# --- 1. En basit hali ----------------------------------------------------
# Bir tasarımcının müşteriden aldığı renk adını sayıya çevirmeye çalıştığını
# düşünün. "Mercan" bir sayı değil — Python bunu int()'e veremez. Eskiden
# program çökerdi. try/except ile çökmeyi engelleriz.

try:
    sayi = int("mercan")            # Bu satır ValueError fırlatır
    print("Sayıya çevirdik:", sayi)
except ValueError:
    print("Bu metni sayıya çeviremedim. Bir sayı bekliyordum.")

# Çıktı:
# Bu metni sayıya çeviremedim. Bir sayı bekliyordum.

print("---")


# --- 2. Hata çıkmazsa try bloğu normal akar ------------------------------
try:
    sayi = int("42")
    print("Sayıya çevirdim:", sayi)
except ValueError:
    print("Bu satıra hiç düşmez çünkü 42 geçerli bir sayı.")

# Çıktı:
# Sayıya çevirdim: 42

print("---")


# --- 3. Birden fazla except bloğu ----------------------------------------
# Aynı try bloğunda farklı hata tipleri olabilir. Her birini ayrı yakalarız.
# Hangi hata tipi geldiyse Python doğru except'e dallanır.

renk_paleti = ["#FF6B6B", "#1E3A8A", "#FFD93D"]

try:
    # Burada iki olası hata var:
    #   - ValueError: int("üç") gibi bir şey
    #   - IndexError: liste sınırını aşan indeks
    secim = int("2")                 # bunu istediğin gibi değiştirebilirsin
    print("Seçilen renk:", renk_paleti[secim])
except ValueError:
    print("Geçerli bir sayı vermedin.")
except IndexError:
    print("Bu indekste renk yok. Palette sadece 3 renk var.")

# Çıktı:
# Seçilen renk: #FFD93D

print("---")


# --- 4. else bloğu — hata YOKSA çalışır ---------------------------------
# try bloğu sorunsuz biterse else çalışır. "Her şey yolundaysa şunu yap."

try:
    deger = int("128")
except ValueError:
    print("Çevrim başarısız.")
else:
    print("Çevrim başarılı, değer:", deger)
    print("Bu satıra sadece HATA OLMAZSA gelinir.")

# Çıktı:
# Çevrim başarılı, değer: 128
# Bu satıra sadece HATA OLMAZSA gelinir.

print("---")


# --- 5. finally bloğu — her durumda çalışır ------------------------------
# try başarılı olsa da olmasa da finally bloğu çalışır.
# Genelde "temizlik" işleri için kullanılır (dosya kapatma, bağlantı sonlandırma).

try:
    sayi = int("abc")               # ValueError fırlatacak
except ValueError:
    print("Hata yakalandı.")
finally:
    print("İşlem tamamlandı (başarılı ya da değil, fark etmez).")

# Çıktı:
# Hata yakalandı.
# İşlem tamamlandı (başarılı ya da değil, fark etmez).

print("---")


# --- 6. Hata mesajını da yakalamak --------------------------------------
# except'in yanına "as e" yazarsak, hata nesnesini bir değişkene atarız.
# Böylece hata mesajını okuyabiliriz (debug ederken çok faydalı).

try:
    sonuc = 10 / 0                  # ZeroDivisionError fırlatır
except ZeroDivisionError as e:
    print("Bölme yapamadım. Python diyor ki:", e)

# Çıktı:
# Bölme yapamadım. Python diyor ki: division by zero
