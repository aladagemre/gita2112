# =============================================================
# DERS 2: Liste İşlemleri
# =============================================================
# Bu derste öğreneceğiz:
#   - .append() ile eleman ekleme
#   - .remove() ile eleman silme
#   - İndeksle değer güncelleme
#   - in operatörü ile arama
#   - .sort() ile sıralama


# --- Başlangıç Listesi ---
malzemeler = ["kağıt", "boya", "fırça", "makas"]
print("Malzeme listesi:", malzemeler)


# --- .append() — Sona Eleman Ekleme ---
malzemeler.append("yapıştırıcı")
print("Yapıştırıcı eklendi:", malzemeler)

malzemeler.append("cetvel")
print("Cetvel eklendi:", malzemeler)


# --- .remove() — Eleman Silme ---
# remove() verilen değeri bulur ve listeden çıkarır.
malzemeler.remove("makas")
print("Makas çıkarıldı:", malzemeler)


# --- İndeksle Güncelleme ---
# Bir elemanın değerini indeks ile değiştirebiliriz.
print("Güncelleme öncesi:", malzemeler[1])  # boya
malzemeler[1] = "akrilik boya"
print("Güncelleme sonrası:", malzemeler[1])  # akrilik boya
print("Güncel liste:", malzemeler)


# --- in Operatörü — Arama ---
# "eleman in liste" ifadesi True veya False döner.
print()
print("kağıt listede mi?", "kağıt" in malzemeler)          # True
print("kalem listede mi?", "kalem" in malzemeler)          # False

aranan = "fırça"
if aranan in malzemeler:
    print(aranan, "mevcut!")
else:
    print(aranan, "bulunamadı.")


# --- .sort() — Sıralama ---
# sort() listeyi alfabetik (veya küçükten büyüğe) sıralar.
# Not: Türkçe karakterler (ç, ş, ü...) sıralamayı beklenmedik şekilde etkileyebilir.
print()
print("Sıralama öncesi:", malzemeler)
malzemeler.sort()
print("Sıralama sonrası:", malzemeler)

# Sayı listesi sıralama
puanlar = [85, 92, 78, 95, 60]
print()
print("Puanlar (ham):", puanlar)
puanlar.sort()
print("Puanlar (sıralı):", puanlar)
