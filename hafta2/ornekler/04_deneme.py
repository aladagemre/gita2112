# =============================================================
# DERS 4: Çoklu input() ve Tür Dönüşümü — int()
# =============================================================
# Bu derste öğreneceğiz:
#   - Birden fazla input() kullanma
#   - input() her zaman string döndürür
#   - int() ile string'i tam sayıya çevirme


# --- Birden Fazla Bilgi Alma ---
# Her input() ayrı bir değişkende saklanır, sırayla sorulur.

isim = input("Adın ne? ")          # string → örnek: "Ali"
renk = input("En sevdiğin renk? ") # string → örnek: "mavi"

# --- int() ile Tür Dönüşümü ---
# input() her zaman metin (string) döndürür.
# Sayıyla işlem yapacaksak int() ile tam sayıya çevirmemiz gerekir.
#
# int(input("..."))  →  önce input çalışır, sonra int() dönüştürür
sayi = int(input("Bir sayı söyle: "))  # string → int


# --- Değerleri Kullanma ---
print("Merhaba", isim, "!")
print("Senin için", sayi, "tane", renk, "balon hazırladım")
