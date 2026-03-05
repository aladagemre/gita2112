# =============================================================
# DERS 4: for ile Liste Gezme
# =============================================================
# Bu derste öğreneceğiz:
#   - for eleman in liste: ile listeyi gezme
#   - enumerate() ile indeks + eleman birlikte alma
#   - Döngü + if kombinasyonu


# --- Liste Üzerinde Gezme ---
# for döngüsü bir listede sırayla her elemanı alır.

projeler = ["Logo Tasarımı", "Poster", "Web Sitesi", "Ambalaj", "Afiş"]

print("=== Projelerim ===")
for proje in projeler:
    print("-", proje)


# --- enumerate() ile Numaralı Gezme ---
# enumerate() her elemanla birlikte sıra numarasını da verir.
# Varsayılan olarak 0'dan başlar, start=1 ile 1'den başlatabiliriz.

print()
print("=== Numaralı Proje Listesi ===")
for sira, proje in enumerate(projeler, start=1):
    print(str(sira) + ".", proje)


# --- Döngü + if Kombinasyonu ---
# Döngü içinde koşul yazarak filtreleme yapabiliriz.

puanlar = [85, 42, 91, 67, 73, 55, 98]

print()
print("=== Puan Analizi ===")
print("Tüm puanlar:", puanlar)
print()

for puan in puanlar:
    if puan >= 90:
        print(puan, "→ Mükemmel!")
    elif puan >= 70:
        print(puan, "→ İyi")
    elif puan >= 50:
        print(puan, "→ Geçer")
    else:
        print(puan, "→ Kaldı")


# --- Liste Gezme + Toplam Hesaplama ---
# Döngüyle bir listedeki sayıları toplayabiliriz.
# Bunu yapmak için önce toplam = 0 diyerek "boş bir kutu" oluştururuz.
# Döngünün her adımında bu kutuya yeni değer ekleriz.

print()
toplam = 0
for puan in puanlar:
    toplam = toplam + puan

ortalama = toplam / len(puanlar)
print("Toplam:", toplam)
print("Ortalama:", ortalama)


# --- Döngü ile Yeni Liste Oluşturma ---
# Belirli koşulu sağlayan elemanları yeni bir listeye atabiliriz.
# Önce boş bir liste oluştururuz [], sonra döngüde koşulu sağlayan elemanları append ile ekleriz.

basarili = []
for puan in puanlar:
    if puan >= 70:
        basarili.append(puan)

print()
print("Başarılı puanlar (70+):", basarili)
print("Başarılı sayısı:", len(basarili))


# --- İndeksle Liste Gezme (İki Listeyi Eşleştirme) ---
# Bazen iki farklı listeyi aynı anda gezmek isteriz.
# Bu durumda indeks numarasını kullanırız: range(len(liste))
# Aynı indeks her iki listede de aynı elemana karşılık gelir.

isimler = ["Logo", "Poster", "Web"]
puanlar2 = [88, 72, 95]

print()
print("=== İndeksle Eşleştirme ===")
for i in range(len(isimler)):
    print(isimler[i], "→", puanlar2[i], "puan")
