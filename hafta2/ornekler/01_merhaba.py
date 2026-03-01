# =============================================================
# DERS 1: print() Fonksiyonu, String ve Temel Aritmetik
# =============================================================
# Bu derste öğreneceğiz:
#   - print() ile ekrana çıktı verme
#   - Metin (string) yazdırma
#   - Sayılarla basit matematik
#   - Metni sayıyla birleştirme


# --- Metin Yazdırma ---
# print() fonksiyonu parantez içindeki şeyi ekrana yazar.
# Tırnak içindeki ifadelere "string" (metin) denir.
print("Merhaba Dünya!")
print("Ben Emre, Python programlama dilini öğreniyorum.")


# --- Sayı ve Matematiksel İşlemler ---
# Tırnak kullanmadan sayı yazarsak Python onu matematik olarak hesaplar.
# Temel operatörler: + (toplama), - (çıkarma), * (çarpma), / (bölme)
print(1 + 1)       # Sonuç: 2
print(2 * 3 + 5)   # Önce çarpma (2*3=6), sonra toplama (6+5=11) → Sonuç: 11


# --- String Birleştirme (+) ---
# İki metni + operatörü ile birleştirebiliriz.
print("Bu ders: " + "GİTA 2112")  # Çıktı: Bu ders: GİTA 2112

# Dikkat: Sayıyı metinle birleştirmek için önce str() ile metne çevirmek gerekir.
# str(11) → "11"  (sayıdan metne dönüşüm)
print("Sonuç: " + str(2 * 3 + 5))  # Çıktı: Sonuç: 11


# --- Farklı print Kullanımları ---
print("Selam")   # En basit kullanım
