# =============================================================
# ÖDEV 3: Koşullu İfade — if / else  [Orta]
# =============================================================
# Bu ödevde yapacakların:
#   - Kullanıcıdan bir poster genişliği al
#   - Genişlik baskı makinesine sığıyor mu kontrol et
#   - Sonuca göre farklı mesaj yazdır
#
# Konu: if / else, <= karşılaştırma operatörü, int(input())
# Kazanım: Tek koşula göre iki farklı davranış yazabilmek
# =============================================================


print("=== Baskı Makinesi Kontrolü ===")
print("Bu program posterinin baskı makinesine sığıp sığmadığını kontrol eder.")
print()


# --- Sabit Bilgi ---
# Baskı makinemizin kabul ettiği maksimum genişlik 70 cm'dir.
# Bu değeri bir değişkende saklıyoruz — ileride değiştirmek kolaylaşır.
maksimum_genislik = 70   # int → cm cinsinden makine limiti


# --- Kullanıcıdan Girdi Al ---
# Kullanıcı genişliği sayı olarak gireceği için int(input()) kullanıyoruz.
poster_genisligi = int(input("Posterinin genişliği kaç cm? "))


# --- Koşulu Yaz ---
# if / else yapısını hatırlıyoruz:
#
#   if KOŞUL:
#       koşul doğruysa çalışacak kod
#   else:
#       koşul yanlışsa çalışacak kod
#
# <= operatörü: sol taraf sağ taraftan küçük veya eşitse True döner.
#   50 <= 70 → True   (50, 70'ten küçük — sığar)
#   90 <= 70 → False  (90, 70'ten büyük — sığmaz)

if poster_genisligi <= maksimum_genislik:
    # "Harika! [kaç cm] posterın makineye sığıyor. Baskıya hazır!" yaz
    # poster_genisligi değişkenini mesajın içine dahil et
    print("Harika!", ...)  # ← ... yerine geri kalan mesajı tamamla

else:
    # "Dikkat! [kaç cm] makinemizin limitini ([limit] cm) aşıyor." yaz
    # poster_genisligi ve maksimum_genislik değişkenlerini kullan
    print("Dikkat!", ...)  # ← ... yerine geri kalan mesajı tamamla


# =============================================================
# Beklenen Çıktı — Örnek 1 (sığan poster):
# =============================================================
#
# === Baskı Makinesi Kontrolü ===
# Bu program posterinin baskı makinesine sığıp sığmadığını kontrol eder.
#
# Posterinin genişliği kaç cm? 50
# Harika! 50 cm posterın makineye sığıyor. Baskıya hazır!
#
# =============================================================
# Beklenen Çıktı — Örnek 2 (tam sınır değeri):
# =============================================================
#
# Posterinin genişliği kaç cm? 70
# Harika! 70 cm posterın makineye sığıyor. Baskıya hazır!
#
# =============================================================
# Beklenen Çıktı — Örnek 3 (sığmayan poster):
# =============================================================
#
# Posterinin genişliği kaç cm? 90
# Dikkat! 90 cm makinemizin limitini (70 cm) aşıyor. Boyutu küçültmen gerekiyor.
