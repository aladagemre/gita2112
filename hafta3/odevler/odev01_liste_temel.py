# =============================================================
# ÖDEV 1: Listeler — Tasarım Malzemeleri  [Kolay]
# =============================================================
# Bu ödevde yapacakların:
#   - Bir liste oluştur ve elemanlarını yazdır
#   - append() ile eleman ekle, remove() ile sil
#   - İndeksle erişim ve güncelleme yap
#
# Konu: Liste oluşturma, indeks, append, remove
# Kazanım: Liste oluşturup temel işlemleri yapabilmek
# =============================================================


print("=== Tasarım Malzeme Listesi ===")
print()


# --- Görev 1: Liste Oluştur ---
# En az 4 malzeme içeren bir liste oluştur.
# Örnek malzemeler: "kağıt", "boya", "fırça", "cetvel", "yapıştırıcı"

malzemeler = ["...", "...", "...", "..."]  # ← her "..." yerine bir malzeme adı yaz


# --- Görev 2: Listeyi Yazdır ---
print("Malzemelerim:", malzemeler)
print("Toplam malzeme:", len(malzemeler))


# --- Görev 3: Eleman Ekle ---
# append() ile listeye 2 yeni malzeme ekle.

...  # ← malzemeler.append("yeni_malzeme") şeklinde yaz
...  # ← bir tane daha ekle

print()
print("Eklemeden sonra:", malzemeler)


# --- Görev 4: Eleman Sil ---
# remove() ile bir malzemeyi listeden çıkar.

...  # ← malzemeler.remove("bir_malzeme") şeklinde yaz

print("Silmeden sonra:", malzemeler)


# --- Görev 5: İndeksle Erişim ---
# İlk, son ve ikinci malzemeyi ayrı ayrı yazdır.

print()
print("İlk malzeme:", ...)      # ← malzemeler[0]
print("Son malzeme:", ...)      # ← malzemeler[-1]
print("İkinci malzeme:", ...)   # ← malzemeler[1]


# --- Görev 6: Güncelleme ---
# İlk malzemeyi başka bir malzemeyle değiştir.

...  # ← malzemeler[0] = "yeni_değer"

print()
print("Güncel liste:", malzemeler)
print("Toplam:", len(malzemeler), "malzeme")


# =============================================================
# Beklenen Çıktı (örnek — senin malzemelerin farklı olabilir):
# =============================================================
#
# === Tasarım Malzeme Listesi ===
#
# Malzemelerim: ['kağıt', 'boya', 'fırça', 'cetvel']
# Toplam malzeme: 4
#
# Eklemeden sonra: ['kağıt', 'boya', 'fırça', 'cetvel', 'makas', 'yapıştırıcı']
# Silmeden sonra: ['kağıt', 'boya', 'fırça', 'cetvel', 'yapıştırıcı']
#
# İlk malzeme: kağıt
# Son malzeme: yapıştırıcı
# İkinci malzeme: boya
#
# Güncel liste: ['kalem', 'boya', 'fırça', 'cetvel', 'yapıştırıcı']
# Toplam: 5 malzeme
