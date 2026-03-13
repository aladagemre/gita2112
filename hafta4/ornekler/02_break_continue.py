# =============================================================
# DERS 2: Döngü Kontrolü — break ve continue
# =============================================================
# Bu derste öğreneceğiz:
#   - break: döngüyü tamamen durdurma
#   - continue: bu turu atlayıp sonrakine geçme
#   - while True + break kalıbı
#   - continue in while döngüsü


# --- break: Listede Arama Yapıp Bulunca Dur ---
# Bir renk paletinde belirli bir rengi arıyoruz.
# Bulduğumuz anda döngüyü durdurmak istiyoruz — gerisi gereksiz.

print("=== break Örneği: Renk Arama ===")

palet = ["kırmızı", "turuncu", "yeşil", "mavi", "mor"]
aranan = "yeşil"

for renk in palet:
    print("Bakıyorum:", renk)
    if renk == aranan:
        print("Buldum! →", aranan)
        break   # Döngüyü durdur, devam etme


# --- continue: Düşük Puanlıları Atlama ---
# Portfolyodaki projeleri listeliyoruz ama düşük puanlıları göstermek istemiyoruz.
# continue: döngünün geri kalanını atlar, sonraki tura geçer.

print()
print("=== continue Örneği: Başarılı Projeler ===")

projeler = [
    {"ad": "Logo Tasarımı", "puan": 88},
    {"ad": "El İlanı", "puan": 45},
    {"ad": "Web Sitesi", "puan": 92},
    {"ad": "Kartvizit", "puan": 60},
    {"ad": "Afiş Tasarımı", "puan": 85},
]

for proje in projeler:
    if proje["puan"] < 70:
        continue    # Bu projeyi atla, sonrakine geç
    print(" ", proje["ad"], "→", proje["puan"], "puan")


# --- while True + break: Malzeme Ekleme Programı ---
# Kullanıcı "bitti" yazana kadar malzeme ekler.
# while True: sonsuza kadar döner, ama break ile çıkarız.

print()
print("=== while True + break: Malzeme Listesi ===")

malzemeler = []

while True:
    yeni = input("Malzeme gir ('bitti' → çık): ")
    if yeni == "bitti":
        break   # Döngüden çık
    malzemeler.append(yeni)
    print("  Eklendi:", yeni)

print("Toplam", len(malzemeler), "malzeme:", malzemeler)


# --- continue in while: Negatif Girişi Atla ---
# Kullanıcıdan sayı al, negatifse atla, 0 girerse dur.
# Bu örnekte continue ile geçersiz girişi atlıyoruz.

print()
print("=== while + continue: Pozitif Sayı Toplama ===")

toplam = 0

while True:
    sayi = int(input("Sayı gir (0 → dur): "))
    if sayi == 0:
        break
    if sayi < 0:
        print("  Negatif sayı atlandı!")
        continue    # Toplama ekleme, başa dön
    toplam = toplam + sayi
    print("  Eklendi. Ara toplam:", toplam)

print("Toplam:", toplam)
