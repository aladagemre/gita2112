# =============================================================
# ÖDEV 2: Tasarım Hesap Makinesi  [Orta]
# =============================================================
# Bu ödevde yapacakların:
#   - input() ile kullanıcıdan sayı ve işlem al
#   - float() ile tip dönüşümü yap
#   - if/elif ile işlem seç
#   - f-string ile sonucu formatla
#   - Sıfıra bölme kontrolü yap
#
# Konu: input + float + if/elif + f-string
# Kazanım: Kullanıcı girişiyle çalışan hesap makinesi yapabilmek
# =============================================================


print("=== Tasarım Hesap Makinesi ===")
print("İşlemler: +, -, *, /")
print()


# --- Görev 1: Kullanıcıdan Giriş Al ---
# İki sayı ve bir işlem al. Sayıları float'a çevir.

sayi1 = ...  # ← float(input("Birinci sayı: "))
islem = ...  # ← input("İşlem (+, -, *, /): ")
sayi2 = ...  # ← float(input("İkinci sayı: "))


# --- Görev 2: İşlemi Hesapla ---
# if/elif ile hangi işlemin seçildiğini kontrol et.
# Bölme işleminde sayi2 == 0 kontrolü yap!

if islem == "+":
    sonuc = ...  # ← sayi1 + sayi2
elif islem == "-":
    sonuc = ...  # ← sayi1 - sayi2
elif islem == "*":
    sonuc = ...  # ← sayi1 * sayi2
elif islem == "/":
    if ...:  # ← sayi2 == 0 mı?
        print("Hata: Sıfıra bölme yapılamaz!")
        sonuc = None
    else:
        sonuc = ...  # ← sayi1 / sayi2
else:
    print(f"Geçersiz işlem: {islem}")
    sonuc = None


# --- Görev 3: Sonucu Yazdır ---
# sonuc None değilse f-string ile yazdır.
# Format: "Sonuç: 10.0 + 3.0 = 13.00"

if sonuc is not None:
    print(...)  # ← f"Sonuç: {sayi1} {islem} {sayi2} = {sonuc:.2f}"


# =============================================================
# Beklenen Çıktı (kullanıcı girişine bağlı):
# =============================================================
#
# === Tasarım Hesap Makinesi ===
# İşlemler: +, -, *, /
#
# Birinci sayı: 1920
# İşlem (+, -, *, /): /
# İkinci sayı: 3
# Sonuç: 1920.0 / 3.0 = 640.00
#
# --- Sıfıra Bölme Durumu ---
# Birinci sayı: 100
# İşlem (+, -, *, /): /
# İkinci sayı: 0
# Hata: Sıfıra bölme yapılamaz!
