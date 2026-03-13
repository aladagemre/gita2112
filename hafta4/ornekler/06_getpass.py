# =============================================================
# DERS 6 (Bonus): Şifre Girişi — getpass
# =============================================================
# Bu derste öğreneceğiz:
#   - getpass modülünü kullanma
#   - Basit giriş sistemi
#   - 3 deneme hakkı: while + break + sayaç

from getpass import getpass

# --- Basit Giriş Sistemi ---
# getpass() fonksiyonu input() gibi çalışır ama
# yazdığınız karakterleri ekranda GÖSTERMEz.
# Şifre girerken ideal!

dogru_kullanici = "tasarimci"
dogru_sifre = "gita2112"
max_deneme = 3
deneme = 0

print("=== Giriş Sistemi ===")

while deneme < max_deneme:
    deneme += 1
    print(f"\nDeneme {deneme}/{max_deneme}")

    kullanici = input("Kullanıcı adı: ")
    sifre = getpass("Şifre: ")

    if kullanici == dogru_kullanici and sifre == dogru_sifre:
        print(f"Hoş geldin, {kullanici}!")
        break
    else:
        kalan = max_deneme - deneme
        if kalan > 0:
            print(f"Hatalı giriş! {kalan} deneme hakkın kaldı.")
        else:
            print("Giriş başarısız. Hesap kilitlendi.")
