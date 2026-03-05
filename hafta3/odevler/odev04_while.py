# =============================================================
# ÖDEV 4: while True + break — Renk Tahmin Oyunu  [Orta-Zor]
# =============================================================
# Bu ödevde yapacakların:
#   - while True + break deseniyle döngü kur
#   - input() ile kullanıcıdan sürekli veri al
#   - Deneme sayısını sayaçla takip et
#
# Konu: while True + break + input
# Kazanım: Koşula dayalı döngü kurup kullanıcı etkileşimi sağlayabilmek
# =============================================================


print("=== Renk Tahmin Oyunu ===")
print("Aklımdaki rengi tahmin et!")
print("İpucu: Gökkuşağı renklerinden biri.")
print()


# --- Oyun Ayarları ---
gizli_renk = "mavi"  # Doğru cevap


# --- Görev 1: Sayaç Tanımla ---
# Deneme sayısını takip edecek bir değişken oluştur, 0'dan başlasın.

deneme = ...  # ← 0 ile başlat


# --- Görev 2: Tahmin Döngüsü ---
# while True döngüsü kur.
# Kullanıcıdan tahmin al.
# Doğru tahmin → tebrik mesajı + break
# Yanlış tahmin → tekrar dene mesajı
# Her denemede sayacı 1 artır.

while True:
    tahmin = input("Tahminin: ")
    deneme = ...  # ← deneme + 1

    if ...:  # ← tahmin == gizli_renk mi?
        print("Tebrikler!", deneme, "denemede bildin!")  # ← bu satır hazır, değiştirme
        ...  # ← break yaz (döngüden çıkar)
    else:
        print(...)  # ← "Yanlış! Tekrar dene." mesajı


# --- Görev 3: Sonuç ---
# Döngüden çıktıktan sonra performans mesajı yazdır.

print()
if deneme == 1:
    print(...)  # ← "İlk denemede bildin, harikasın!" mesajı
elif deneme <= 3:
    print(...)  # ← "Fena değil!" mesajı
else:
    print(...)  # ← "Biraz zorlandın ama sonunda bildin!" mesajı


# =============================================================
# Beklenen Çıktı (örnek oyun akışı):
# =============================================================
#
# === Renk Tahmin Oyunu ===
# Aklımdaki rengi tahmin et!
# İpucu: Gökkuşağı renklerinden biri.
#
# Tahminin: kırmızı
# Yanlış! Tekrar dene.
# Tahminin: yeşil
# Yanlış! Tekrar dene.
# Tahminin: mavi
# Tebrikler! 3 denemede bildin!
#
# Fena değil!
