# =============================================================
# ÖDEV 4: Çoklu Koşul Dalları — if / elif / else — CEVAP ANAHTARI
# =============================================================


print("=== Tasarım Jürisi Değerlendirmesi ===")
print()


# --- Kullanıcıdan Puan Al ---

puan = int(input("Tasarım puanını gir (0-100): "))


# --- Koşul Zinciri ---

if puan >= 90:
    print("Harika! Bu tasarım sergiye layık.")

elif puan >= 70:
    print("İyi iş! Küçük dokunuşlarla mükemmel olur.")

elif puan >= 50:
    print("Geliştirebilirsin. Renk ve tipografiyi gözden geçir.")

else:
    print("Tekrar dene. Her büyük tasarımcı bir noktadan başladı!")


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
