# =============================================================
# ÖDEV 2: Kullanıcıdan Veri Alma — input()  [Kolay]
# =============================================================
# Bu ödevde yapacakların:
#   - Kullanıcıdan üç farklı bilgi al
#   - Sayısal girişi int() ile dönüştür
#   - Alınan bilgileri kullanarak kişiselleştirilmiş bir mesaj yazdır
#
# Konu: input(), int(input()), çoklu değişken, print()
# Kazanım: Kullanıcıyla etkileşim kuran bir program yazabilmek
# =============================================================


print("=== Renk Danışmanı ===")
print("Sana özel bir poster önerisi hazırlayacağım!")
print()


# --- Görev 1: Kullanıcıdan Bilgi Al ---
# Her input() farklı bir değişkende saklanır.
# input() her zaman metin (string) döndürür — bunu unutma!

isim = input("Adın ne? ")                          # string → örnek: "Kaan"
sevdigi_renk = input("En sevdiğin renk nedir? ")   # string → örnek: "sarı"

# Poster genişliğini sayı olarak almak istiyoruz.
# int(input(...)) → önce input çalışır, sonra int() sayıya çevirir.
poster_genisligi = int(input("Hayalindeki poster kaç cm genişliğinde olsun? "))


# --- Görev 2: Kişiselleştirilmiş Mesaj Yazdır ---
# Aşağıdaki print() satırlarını tamamla.
# print() içinde virgülle ayırırsan boşluk otomatik eklenir.
# Örnek:  print("Merhaba,", isim, "!")

print()
print("Merhaba, " + isim + "!")

# Aşağıdaki satırı tamamla — "..." yerine doğru değişkeni yaz:
print("Poster rengin için", ..., "harika bir seçim!")

# Aşağıdaki satırı tamamla — str() kullanmayı unutma:
# (poster_genisligi bir int. Metne katmak için str() gerekiyor.)
print(str(...) + " cm genişliğinde bir poster hazırlıyorum.")


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
