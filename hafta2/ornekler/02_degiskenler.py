# =============================================================
# DERS 2: Değişkenler
# =============================================================
# Bu derste öğreneceğiz:
#   - Değişken nedir ve nasıl tanımlanır?
#   - String (metin) ve int (tam sayı) veri tipleri
#   - Değişkenleri print() ile kullanma


# --- Değişken Nedir? ---
# Değişken, bir bilgiyi saklamak için kullandığımız isimli bir kutudur.
# Söz dizimi:  değişken_adı = değer
#
# Python'da üç temel veri tipi:
#   str  → Metin         → Tırnak içinde yazılır: "Zeynep"
#   int  → Tam sayı      → Tırnak olmadan yazılır: 18
#   float → Ondalık sayı → Tırnak olmadan yazılır: 3.14

isim = "Zeynep"      # str  → metin değişkeni
yas = 18             # int  → tam sayı değişkeni
sehir = "İstanbul"  # str  → metin değişkeni
pi = 3.14            # float → ondalık sayı değişkeni


# --- Değişkenleri Kullanma ---
# print() içinde birden fazla şeyi virgülle ayırarak yan yana yazdırabiliriz.
# Python aralarına otomatik olarak boşluk koyar.
print("Merhaba, ben", isim)   # Çıktı: Merhaba, ben Zeynep
print("Yaşım:", yas)           # Çıktı: Yaşım: 18
print("Şehrim:", sehir)        # Çıktı: Şehrim: İstanbul
print("Pi sayısı:", pi)       # Çıktı: Pi sayısı: 3.14