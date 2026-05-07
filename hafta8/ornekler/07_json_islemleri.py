# =============================================================
# DERS 7: JSON Okuma ve Yazma
# =============================================================
# Bu derste öğreneceğiz:
#   - JSON nedir, sözlüğe benzerliği
#   - json.load ile dosyadan sözlüğe
#   - json.dump ile sözlükten dosyaya
#   - Türkçe karakterler ve indent ayarları
# =============================================================


import json


# --- Sorun: Sözlüğümüzü Nasıl Kaydederiz? ---
#
# Hafta 4'te sözlükleri öğrendik:
#
#   proje = {"ad": "Caz Festivali", "renk": "Mercan"}
#
# Program kapanınca sözlük kayboluyor. Diske yazsak nasıl
# yazarız? .txt dosyası sözlük yapısını anlamaz.
#
# Çözüm: JSON formatı. Sözlüğümüzü dosyaya yazıp geri okumamızı
# sağlar. Üstelik insan tarafından okunabilir.


print("=== JSON Okuma ve Yazma ===")
print()


# --- 1. JSON Dosyasını Okuma ---
#
# veri/proje.json dosyasının içeriği:
#
# {
#   "ad": "Caz Festivali Afişi",
#   "tarih": "2026-06-15",
#   "tasarimci": "Defne Aydın",
#   "boyut": {"en_cm": 50, "boy_cm": 70},
#   "renkler": ["#FF6B6B", "#1E3A8A", "#FFD93D"],
#   "fontlar": ["Inter", "Playfair Display"],
#   "yayinlandi": false,
#   "notlar": "İlk taslak — geri bildirim bekleniyor."
# }

print("--- 1. json.load ile dosyayı sözlüğe çevirme ---")

with open("veri/proje.json", "r", encoding="utf-8") as dosya:
    proje = json.load(dosya)

# proje artık bir Python sözlüğü!
print(f"Tipi: {type(proje).__name__}")
print(f"Proje adı: {proje['ad']}")
print(f"Tasarımcı: {proje['tasarimci']}")
print(f"Boyut: {proje['boyut']['en_cm']} x {proje['boyut']['boy_cm']} cm")
print(f"Birinci renk: {proje['renkler'][0]}")
print()


# --- 2. Sözlüğü Sıradan Bir Sözlük Gibi Kullanma ---

print("--- 2. Sözlük üzerinde işlem yapma ---")

# Tüm renkleri yazdıralım:
print("Renkler:")
for renk in proje["renkler"]:
    print(f"  - {renk}")

# Yayınlanmış mı?
if proje["yayinlandi"]:
    print("Bu proje yayınlanmış.")
else:
    print("Bu proje henüz yayınlanmamış.")

print()


# --- 3. Sözlüğü Düzenleyip Geri Yazma ---

print("--- 3. Düzenle ve kaydet ---")

# Bir renk daha ekleyelim:
proje["renkler"].append("#FF9F45")

# Yayın durumunu güncelleyelim:
proje["yayinlandi"] = True

# Yeni bir alan ekleyelim:
proje["son_guncelleme"] = "2026-05-08"

# Dosyaya yazalım — yeni isimle ki orijinali bozulmasın:
with open("proje_guncel.json", "w", encoding="utf-8") as dosya:
    json.dump(proje, dosya, ensure_ascii=False, indent=2)

print("proje_guncel.json oluşturuldu.")
print()

# İki önemli parametre:
#   ensure_ascii=False → Türkçe "İ" gibi harfler bozulmasın
#   indent=2           → dosya okunabilir görünsün (2 boşluk girinti)


# --- 4. Yazdığımız Dosyayı Kontrol Edelim ---

print("--- 4. Kayıtlı dosyanın içeriği ---")

with open("proje_guncel.json", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()

print(icerik)


# --- 5. Sıfırdan Bir JSON Yazma ---

print("--- 5. Yeni bir proje sıfırdan oluştur ---")

yeni_proje = {
    "ad": "Sergi Kataloğu",
    "tarih": "2026-09-01",
    "sayfa_sayisi": 64,
    "renkler": ["#2B2D42", "#E8DAB2"],
    "tamamlandi": False,
}

with open("yeni_proje.json", "w", encoding="utf-8") as dosya:
    json.dump(yeni_proje, dosya, ensure_ascii=False, indent=2)

print("yeni_proje.json yazıldı.")

# Tekrar okuyup sözlüğe çevirelim:
with open("yeni_proje.json", "r", encoding="utf-8") as dosya:
    geri_okunan = json.load(dosya)

print(f"Geri okunan veri: {geri_okunan}")
print(f"Tipi: {type(geri_okunan).__name__}")
print()


# --- Sözlük ↔ Dosya Köprüsü ---
#
#         json.dump
# Sözlük  ──────▶  Dosya
#
#         json.load
# Dosya   ──────▶  Sözlük
#
# Bu döngü sayesinde verilerinizi:
#   - Programlar arasında paylaşabilirsiniz
#   - Yarın açınca aynı haliyle bulabilirsiniz
#   - Başka bir kişiyle paylaşabilirsiniz


# --- Tasarım Bağlamı ---
#
# JSON formatı tasarım dünyasında çok yaygın:
#   - Figma dosyalarının iç yapısı
#   - Adobe Creative Cloud profil tercihleri
#   - InDesign şablon yapılandırmaları
#   - Web sitelerinin font/renk teması
#
# Bir tasarım sisteminin "design tokens" denilen renk/tipo
# değerleri çoğunlukla JSON dosyasında tutulur.


# --- Sık Yapılan Hatalar ---
#
# 1. ensure_ascii=False unutmak:
#    Türkçe "İ" yerine "İ" gibi tuhaf karakterler yazılır.
#
# 2. indent=2 olmadan yazmak:
#    Dosya tek satıra sıkışır, okunmaz hale gelir.
#    Çalışır ama insan dostu değil.
#
# 3. JSON içinde tek tırnak kullanmak:
#    JSON SADECE çift tırnak kullanır.
#    "ad" doğru, 'ad' yanlış.
#
# 4. JSON içinde Python'un True/False yazılışı:
#    Python: True / False / None
#    JSON:   true / false / null
#    Bu farkı sadece elle JSON yazarken görürsünüz;
#    json.dump otomatik halleder.


# --- Özet ---
print("--- Özet ---")
print("import json")
print("json.load(dosya) → JSON dosyasını sözlüğe çevirir")
print("json.dump(sozluk, dosya, ensure_ascii=False, indent=2) → kaydeder")
print("Sözlük ↔ JSON dosyası: birebir karşılık gelir")
