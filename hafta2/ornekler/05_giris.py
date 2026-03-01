# =============================================================
# DERS 5: Koşullu İfadeler — if / else ve "and" Operatörü
# =============================================================
# Bu derste öğreneceğiz:
#   - if / else ile karar verme
#   - == ile eşitlik karşılaştırması
#   - and ile iki koşulu birden kontrol etme
#   - Girintinin (indentation) önemi


# --- Kullanıcıdan Giriş Bilgisi Alma ---
kullanici = input("Kullanıcı adınız:")
parola = input("Parolanız:")

# --- if / else Yapısı ---
# Söz dizimi:
#   if KOŞUL:
#       koşul doğruysa çalışacak kod   ← 2 boşluk/tab girintili!
#   else:
#       koşul yanlışsa çalışacak kod   ← 2 boşluk/tab girintili!
#
# == operatörü: iki değerin eşit olup olmadığını kontrol eder.
#   "admin" == "admin"  → True
#   "admin" == "hacker" → False

# Önce sadece parolayı kontrol eden basit bir if/else örneği:
if parola == "1234":
    print("Parola doğru!")
else:
    print("Parola hatalı.")

# Şimdi bunu genişletelim: hem kullanıcı adı hem parola doğru olmalı.
# and operatörü: her iki koşul da True ise sonuç True olur.
#   True and True  → True
#   True and False → False

if kullanici == "admin" and parola == "1234":
    # Her iki koşul da sağlandıysa burası çalışır
    print("Giriş başarılı")
else:
    # En az bir koşul yanlışsa burası çalışır
    print("Kullanıcı adı veya parola hatalı.")
