# =============================================================
# ÖDEV 4: Çoklu Koşul Dalları — if / elif / else  [Orta-Zor]
# =============================================================
# Bu ödevde yapacakların:
#   - Kullanıcıdan bir tasarım puanı al (0-100)
#   - Puana göre dört farklı değerlendirme mesajı yazdır
#   - if / elif / else zinciri kullan
#
# Konu: if / elif / else, >= operatörü, int(input())
# Kazanım: Birden fazla koşul dalını doğru sırayla yazabilmek
# =============================================================


print("=== Tasarım Jürisi Değerlendirmesi ===")
print()


# --- Puanlama Tablosu ---
# 90 - 100 → "Harika! Bu tasarım sergiye layık."
# 70 -  89 → "İyi iş! Küçük dokunuşlarla mükemmel olur."
# 50 -  69 → "Geliştirebilirsin. Renk ve tipografiyi gözden geçir."
#  0 -  49 → "Tekrar dene. Her büyük tasarımcı bir noktadan başladı!"


# --- Kullanıcıdan Puan Al ---
puan = int(input("Tasarım puanını gir (0-100): "))


# --- Koşul Zincirini Tamamla ---
# Python zincirleri yukarıdan aşağıya sırayla kontrol eder.
# İlk doğru koşulu bulur, o bloğu çalıştırır, geri kalanları atlar.
#
# Önemli: Eşik değerlerini büyükten küçüğe sırala!
#   Önce 90'ı kontrol et → sonra 70'i → sonra 50'yi → en son else

if puan >= 90:
    # 90 ve üzeri → en yüksek kategori (bu dal sana örnek olarak yazıldı)
    print("Harika! Bu tasarım sergiye layık.")

elif puan >= 70:   # ← eşik değeri doğru mu? Yukarıdaki tablodan kontrol et
    print("...")   # ← 70-89 arası mesajı buraya yaz

elif puan >= 50:   # ← eşik değeri doğru mu? Yukarıdaki tablodan kontrol et
    print("...")   # ← 50-69 arası mesajı buraya yaz

else:
    print("...")   # ← 0-49 arası mesajı buraya yaz


print()
print("Değerlendirme tamamlandı. Tasarım yolculuğun devam ediyor!")


# =============================================================
# Beklenen Çıktı — 4 Farklı Örnek:
# =============================================================
#
# Tasarım puanını gir (0-100): 95
# Harika! Bu tasarım sergiye layık.
# Değerlendirme tamamlandı. Tasarım yolculuğun devam ediyor!
#
# ---
#
# Tasarım puanını gir (0-100): 78
# İyi iş! Küçük dokunuşlarla mükemmel olur.
# Değerlendirme tamamlandı. Tasarım yolculuğun devam ediyor!
#
# ---
#
# Tasarım puanını gir (0-100): 61
# Geliştirebilirsin. Renk ve tipografiyi gözden geçir.
# Değerlendirme tamamlandı. Tasarım yolculuğun devam ediyor!
#
# ---
#
# Tasarım puanını gir (0-100): 35
# Tekrar dene. Her büyük tasarımcı bir noktadan başladı!
# Değerlendirme tamamlandı. Tasarım yolculuğun devam ediyor!
