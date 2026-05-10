# Konu: math modülünün temel fonksiyonları
# -----------------------------------------
# Python'un standart kütüphanesindeki math modülü matematiksel sabitler ve fonksiyonlar sunar.
# - math.pi    → pi sabiti (3.14159...)
# - math.sqrt  → karekök hesaplar
# - math.floor → aşağı yuvarlar (3.7 → 3)
# - math.ceil  → yukarı yuvarlar (3.7 → 4)
# - round      → math'tan değildir, built-in (yerleşik) bir fonksiyondur; en yakın tam sayıya yuvarlar.
# Not: round() bankacı yuvarlaması (banker's rounding) kullanır; .5 değerleri çift sayıya yuvarlanır.

import math
print(math.pi)
print(math.sqrt(64))
print(math.floor(3.7))
print(math.ceil(3.7))
print(round(5))