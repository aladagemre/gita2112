# =============================================================
# DERS 2: Matematik İşlemleri ve Tip Dönüşümleri
# =============================================================
# Bu derste öğreneceğiz:
#   - Aritmetik operatörler: +, -, *, /, //, %, **
#   - Kısayol operatörler: +=, -=
#   - int() vs float() dönüşümleri
#   - round() ve abs()
#   - Mini hesap makinesi örneği


# --- Tüm Operatörler ---
print("=== Aritmetik Operatörler ===")

a = 17
b = 5

print(f"{a} + {b} = {a + b}")      # Toplama → 22
print(f"{a} - {b} = {a - b}")      # Çıkarma → 12
print(f"{a} * {b} = {a * b}")      # Çarpma  → 85
print(f"{a} / {b} = {a / b}")      # Bölme   → 3.4 (her zaman float döner)
print(f"{a} // {b} = {a // b}")    # Tam bölme → 3 (ondalık kısmı atar)
print(f"{a} % {b} = {a % b}")      # Mod (kalan) → 2
print(f"{a} ** {b} = {a ** b}")    # Üs alma → 1419857


# --- Kısayol Operatörler ---
# Bir değişkeni kendi üzerine artırma/azaltma kısayolları.

print()
print("=== Kısayol Operatörler ===")

sayac = 10
print(f"Başlangıç: {sayac}")

sayac += 3   # sayac = sayac + 3
print(f"+= 3 sonrası: {sayac}")

sayac -= 5   # sayac = sayac - 5
print(f"-= 5 sonrası: {sayac}")

sayac *= 2   # sayac = sayac * 2
print(f"*= 2 sonrası: {sayac}")


# --- Tip Dönüşümleri ---
# int(): tam sayıya çevirir (ondalık kısmı KIRPAR, yuvarlamaz!)
# float(): ondalıklı sayıya çevirir

print()
print("=== Tip Dönüşümleri ===")

print(f"int(3.7)  = {int(3.7)}")    # 3 (yuvarlamaz, kırpar!)
print(f"int(3.2)  = {int(3.2)}")    # 3
print(f"int('42') = {int('42')}")   # 42 (string → int)

print(f"float(5)    = {float(5)}")      # 5.0
print(f"float('3.14') = {float('3.14')}")  # 3.14 (string → float)

# input() her zaman string döner, sayıyla işlem yapmak için dönüştürmeliyiz:
# yas = int(input("Yaşınız: "))
# fiyat = float(input("Fiyat: "))


# --- round() ve abs() ---
print()
print("=== round() ve abs() ===")

pi = 3.14159
print(f"round(3.14159, 2) = {round(pi, 2)}")   # 3.14
print(f"round(3.14159, 1) = {round(pi, 1)}")   # 3.1
print(f"round(3.14159)    = {round(pi)}")       # 3

print(f"abs(-15)  = {abs(-15)}")    # 15
print(f"abs(7)    = {abs(7)}")      # 7


# --- Tasarım Bağlamı: Piksel Hesaplama ---
print()
print("=== Tasarım: Piksel Hesaplama ===")

genislik = 1920
yukseklik = 1080
toplam_piksel = genislik * yukseklik

print(f"Ekran: {genislik}x{yukseklik}")
print(f"Toplam piksel: {toplam_piksel:,}")

# Grid bölümleme: ekranı 3 sütuna böl
sutun_sayisi = 3
sutun_genislik = genislik // sutun_sayisi
kalan = genislik % sutun_sayisi

print(f"{sutun_sayisi} sütunlu grid: her sütun {sutun_genislik}px")
print(f"Kalan piksel: {kalan}px")


# --- Mini Hesap Makinesi ---
# input + if/elif + float + f-string hepsini birleştiriyoruz.

print()
print("=== Mini Hesap Makinesi ===")

sayi1 = float(input("Birinci sayı: "))
islem = input("İşlem (+, -, *, /): ")
sayi2 = float(input("İkinci sayı: "))

if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 - sayi2
elif islem == "*":
    sonuc = sayi1 * sayi2
elif islem == "/":
    if sayi2 == 0:
        print("Hata: Sıfıra bölme yapılamaz!")
        sonuc = None
    else:
        sonuc = sayi1 / sayi2
else:
    print(f"Geçersiz işlem: {islem}")
    sonuc = None

if sonuc is not None:
    print(f"Sonuç: {sayi1} {islem} {sayi2} = {sonuc:.2f}")
