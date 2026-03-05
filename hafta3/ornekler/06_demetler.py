# =============================================================
# DERS 6: Demetler (Tuples)
# =============================================================
# Bu derste öğreneceğiz:
#   - Demet oluşturma ()
#   - İndeksle erişim
#   - Demetin değiştirilemezliği (immutable)
#   - Liste vs demet karşılaştırma
#   - RGB renk kodları senaryosu


# --- Demet Oluşturma ---
# Demet (tuple), listeye benzer ama DEĞİŞTİRİLEMEZ.
# Normal parantez () ile oluşturulur.

koordinat = (100, 250)
print("Koordinat:", koordinat)

boyutlar = (1920, 1080)
print("Ekran boyutları:", boyutlar)


# --- İndeksle Erişim ---
# Tıpkı listeler gibi indeksle erişebiliriz.
print()
print("Genişlik:", boyutlar[0])   # 1920
print("Yükseklik:", boyutlar[1])  # 1080
print("Eleman sayısı:", len(boyutlar))


# --- RGB Renk Kodları ---
# Tasarımda renkler genellikle RGB (Kırmızı, Yeşil, Mavi) ile ifade edilir.
# Her değer 0-255 arasıdır. Renk değerleri sabit olmalı → demet ideal!

print()
print("=== RGB Renk Paleti ===")

kirmizi = (255, 0, 0)
yesil = (0, 128, 0)
mavi = (0, 0, 255)
turuncu = (255, 165, 0)
mor = (128, 0, 128)

print("Kırmızı RGB:", kirmizi)
print("Yeşil RGB:", yesil)
print("Mavi RGB:", mavi)
print("Turuncu RGB:", turuncu)
print("Mor RGB:", mor)


# --- Değiştirilemezlik ---
# Listeyi değiştirebiliriz ama demeti değiştiremeyiz!

liste_renk = [255, 0, 0]
liste_renk[0] = 200      # Bu çalışır
print()
print("Liste değiştirildi:", liste_renk)

# demet_renk = (255, 0, 0)
# demet_renk[0] = 200    # Bu HATA verir! TypeError!
# Demetler oluşturulduktan sonra değiştirilemez.
# Merak ediyorsan yukarıdaki iki satırın başındaki # işaretlerini kaldır ve ne olduğunu gör!
print("Demet değiştirilemez — bu bir güvenlik özelliğidir!")


# --- Demetleri Döngüyle Kullanma ---
# Demet listesi: birden fazla demeti bir listede tutabiliriz.

print()
print("=== Renk Paleti Detay ===")
palet = [
    ("Kırmızı", 255, 0, 0),
    ("Yeşil", 0, 128, 0),
    ("Mavi", 0, 0, 255),
    ("Turuncu", 255, 165, 0),
]

# Her demet 4 elemanlı: ("Kırmızı", 255, 0, 0)
# for döngüsü bu 4 elemanı sırayla renk_adi, r, g, b değişkenlerine atar.
# Tıpkı enumerate'te sira, proje diye ikiye ayırdığımız gibi.
for renk_adi, r, g, b in palet:
    print(renk_adi + ":", "R=" + str(r), "G=" + str(g), "B=" + str(b))


# --- Liste vs Demet Özet ---
print()
print("=== Liste vs Demet ===")
print("Liste [] → değiştirilebilir (mutable)")
print("Demet () → değiştirilemez (immutable)")
print("Sabit veriler (RGB, koordinat) → demet kullan")
print("Değişecek veriler (alışveriş listesi) → liste kullan")
