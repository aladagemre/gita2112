# =============================================================
# ÖDEV 2: Renk Arama Asistanı  [Kolay]
# =============================================================
# Bu ödevde yapacakların:
#   - for + break: listede arama yapıp bulunca dur
#   - for + continue: belirli elemanları atlayıp kalanları yazdır
#
# Konu: break ve continue kullanımı
# Kazanım: Döngü akışını kontrol edebilmek
# =============================================================


# --- Görev 1: Renk Bul ve Dur (break) ---
# Aşağıdaki palette "turkuaz" rengini ara.
# Her rengi kontrol ederken "Bakıyorum: ..." yazdır.
# Bulunca "Buldum! → turkuaz" yazdır ve döngüyü durdur.

print("=== Görev 1: Renk Ara ===")

palet = ["kırmızı", "sarı", "turkuaz", "mor", "lacivert"]
aranan = "turkuaz"

for renk in palet:
    print("Bakıyorum:", renk)
    if ...:  # ← renk == aranan mı?
        print("Buldum! →", aranan)
        ...  # ← break


# --- Görev 2: Kısa İsimli Renkleri Atla (continue) ---
# 5 harften kısa olan renkleri atla, sadece uzun olanları yazdır.
# İpucu: len(renk) < 5 ise continue

print()
print("=== Görev 2: Uzun İsimli Renkler ===")

renkler = ["kırmızı", "mavi", "turuncu", "mor", "yeşil", "lacivert"]

for renk in renkler:
    if ...:  # ← len(renk) < 5 ise atla
        continue
    print(" ", renk, "(" + str(len(renk)) + " harf)")


# --- Görev 3: Malzeme Toplama (while True + break) ---
# Kullanıcıdan malzeme ismi al. "tamam" yazarsa dur.
# Her girişi listeye ekle.

print()
print("=== Görev 3: Malzeme Toplama ===")

malzemeler = []

while True:
    yeni = input("Malzeme gir ('tamam' → bitir): ")
    if ...:  # ← yeni == "tamam" mı?
        ...  # ← break
    malzemeler.append(yeni)
    print("  Eklendi:", yeni)

print("Malzeme listesi:", malzemeler)


# =============================================================
# Beklenen Çıktı (Görev 1 ve 2 — Görev 3 kullanıcı girişine bağlı):
# =============================================================
#
# === Görev 1: Renk Ara ===
# Bakıyorum: kırmızı
# Bakıyorum: sarı
# Bakıyorum: turkuaz
# Buldum! → turkuaz
#
# === Görev 2: Uzun İsimli Renkler ===
#   kırmızı (7 harf)
#   turuncu (7 harf)
#   yeşil (5 harf)
#   lacivert (8 harf)
