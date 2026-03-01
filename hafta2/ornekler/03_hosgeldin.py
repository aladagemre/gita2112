# =============================================================
# DERS 3: Kullanıcıdan Veri Alma — input()
# =============================================================
# Bu derste öğreneceğiz:
#   - input() ile kullanıcıdan bilgi isteme
#   - Girilen değeri değişkende saklama
#   - Değişkeni print() ile kullanma


# --- input() Nasıl Çalışır? ---
# input("soru metni") → ekrana soruyu yazar, kullanıcının yazmasını bekler,
# kullanıcı Enter'a basınca yazdığı metni geri döndürür.
#
# Dönen değer her zaman string (metin) türündedir.
# Bunu bir değişkende saklarız:

isim = input("Adınız nedir? ")   # Kullanıcının yazdığı metin isim değişkenine kaydolur

# Artık isim değişkeni içinde kullanıcının girdiği değer var.
# Not: + ile birleştirirsek ünlem işareti boşluksuz gelir.
print("Hoş geldin, " + isim + "!")  # Çıktı: Hoş geldin, Ali!
