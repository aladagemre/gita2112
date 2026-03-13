# =============================================================
# ÖDEV 2: Kullanıcıdan Veri Alma — input() — CEVAP ANAHTARI
# =============================================================


print("=== Renk Danışmanı ===")
print("Sana özel bir poster önerisi hazırlayacağım!")
print()


# --- Görev 1: Kullanıcıdan Bilgi Al ---

isim = input("Adın ne? ")
sevdigi_renk = input("En sevdiğin renk nedir? ")
poster_genisligi = int(input("Hayalindeki poster kaç cm genişliğinde olsun? "))


# --- Görev 2: Kişiselleştirilmiş Mesaj Yazdır ---

print()
print("Merhaba, " + isim + "!")
print("Poster rengin için", sevdigi_renk, "harika bir seçim!")
print(str(poster_genisligi) + " cm genişliğinde bir poster hazırlıyorum.")


print()
print("Posterini dört gözle bekliyorum!")


# =============================================================
# Beklenen Çıktı (örnek giriş: Kaan, sarı, 90):
# =============================================================
#
# === Renk Danışmanı ===
# Sana özel bir poster önerisi hazırlayacağım!
#
# Adın ne? Kaan
# En sevdiğin renk nedir? sarı
# Hayalindeki poster kaç cm genişliğinde olsun? 90
#
# Merhaba, Kaan!
# Poster rengin için sarı harika bir seçim!
# 90 cm genişliğinde bir poster hazırlıyorum.
#
# Posterini dört gözle bekliyorum!
