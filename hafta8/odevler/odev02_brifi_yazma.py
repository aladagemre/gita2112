# =============================================================
# ÖDEV 2: Tasarım Brifi Yazma  [Kolay-Orta]
# =============================================================
# Bu ödevde yapacakların:
#   - Kullanıcıdan input ile bilgi al
#   - f-string ile metin oluştur
#   - Dosyaya yaz ("w" modu)
#   - Yazdığını geri okuyup ekrana bas
#
# Konu: input + f-string + dosya yazma + dosya okuma
# Kazanım: Kullanıcıdan veri alıp diske kalıcı kaydetmek
# =============================================================


print("=== Tasarım Brifi Oluşturucu ===")
print("Lütfen proje bilgilerini girin:")
print()


# --- Görev 1: Kullanıcıdan Bilgi Al ---

proje_adi = input("Proje adı: ")
musteri = input("Müşteri adı: ")
tarih = input(...)                                 # ← prompt yazısı: "Teslim tarihi (GG.AA.YYYY): "
renkler_metin = input("Renkler (virgülle ayır): ")  # örn: Mercan, Lacivert, Sarı


# --- Görev 2: Brif Metnini Oluştur ---
# Aşağıdaki şablonu f-string ile doldur.
#
# YENİ NOT — ÜÇLÜ TIRNAK ("""..."""):
# Şimdiye kadar tek tırnak f-string'ler gördünüz: f"Merhaba {isim}".
# Birden fazla satır yazmak istediğinizde tek tırnak yetmez.
# Üçlü tırnak başlar başlamaz Python "burası bir metin bloğu, satır
# atlasanız bile devam ediyor" diye anlar. f"""...""" yine f-string'dir,
# içindeki {} süslü parantezleri değişkenle değiştirilir.
# Sondaki """ metni bitirir.

brif = f"""=== TASARIM BRİFİ ===

Proje Adı : {...}
Müşteri   : {...}
Teslim    : {...}
Renkler   : {...}

Bu brif {tarih} tarihinde teslim edilmek üzere
{musteri} için hazırlanmıştır.
"""
# Yukarıdaki ... yerlerini sırayla şu değişkenlerle doldur:
#   proje_adi, musteri, tarih, renkler_metin


# --- Görev 3: Dosyaya Yaz ---
# proje_brifi.txt adında bir dosya oluştur, brif metnini yaz.

with open("proje_brifi.txt", ..., encoding="utf-8") as dosya:   # ← "w" modu
    dosya.write(...)                                              # ← brif değişkenini yaz

print()
print("proje_brifi.txt dosyası oluşturuldu.")
print()


# --- Görev 4: Yazdığını Geri Oku ve Göster ---
# Dosyayı tekrar aç, içeriğini oku, ekrana bas.

with open("proje_brifi.txt", ..., encoding="utf-8") as dosya:   # ← "r" modu
    icerik = dosya.read()

print("--- Dosyanın İçeriği ---")
print(icerik)


# =============================================================
# Beklenen Çıktı (örnek girdilere göre):
# =============================================================
#
# Eğer şu girdileri verdiyseniz:
#   Proje adı: Caz Festivali Afişi
#   Müşteri adı: Bilgi Üniversitesi
#   Teslim tarihi (GG.AA.YYYY): 15.06.2026
#   Renkler (virgülle ayır): Mercan, Lacivert, Sarı
#
# Çıktı şöyle olur:
#
# === Tasarım Brifi Oluşturucu ===
# Lütfen proje bilgilerini girin:
#
# Proje adı: Caz Festivali Afişi
# Müşteri adı: Bilgi Üniversitesi
# Teslim tarihi (GG.AA.YYYY): 15.06.2026
# Renkler (virgülle ayır): Mercan, Lacivert, Sarı
#
# proje_brifi.txt dosyası oluşturuldu.
#
# --- Dosyanın İçeriği ---
# === TASARIM BRİFİ ===
#
# Proje Adı : Caz Festivali Afişi
# Müşteri   : Bilgi Üniversitesi
# Teslim    : 15.06.2026
# Renkler   : Mercan, Lacivert, Sarı
#
# Bu brif 15.06.2026 tarihinde teslim edilmek üzere
# Bilgi Üniversitesi için hazırlanmıştır.
#
# Ayrıca: proje_brifi.txt adlı dosya klasörünüzde oluşmuş olmalı.
# VS Code'un sol kenarındaki dosya gezgininde göreceksiniz.
