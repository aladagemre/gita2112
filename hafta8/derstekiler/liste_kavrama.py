# Konu: List Comprehension (Liste Kavrama)
# -----------------------------------------
# Bu örnek aynı işlemi iki farklı yolla yapar:
#   1) Klasik for-döngüsü + if filtresi + append (uzun yol).
#   2) List comprehension: tek satırda hem dönüştürme hem filtreleme yapar.
# Genel kalıp:
#       [<ifade> for <eleman> in <iterable> if <kosul>]
# Burada:
#   - "renk.startswith('#')" filtresi ile sadece hex kodları seçilir.
#   - "renk.upper()" dönüşümü ile harfler büyütülür.
# List comprehension daha hızlı, daha okunabilir ve Pythonic kabul edilir.

renkler = ["#ff0000", "#00ff00", "#0000ff", "sarı", "turuncu", "#ffff00", "mor", "#ff00ff"]

# Eski yol:
sonuc = []
for renk in renkler:
    if renk.startswith("#"):
        sonuc.append(renk.upper())

# Tek satır:
sonuc = [renk.upper() for renk in renkler if renk.startswith("#")]

print(sonuc)