# def dikdortgen_alan(en, boy):
#     return en * boy

# def dikdortgen_cevre(en, boy):
#     return 2 * (en + boy)

# en = 10
# boy = 20

# print("Dikdörtgen Alan:", dikdortgen_alan(en, boy))
# print("Dikdörtgen Çevre:", dikdortgen_cevre(en, boy))

# ===== 

# =======

class Dikdortgen:
    def __init__(self, en, boy):
        self.en = en
        self.boy = boy

    def alan(self):
        return self.en * self.boy

    def cevre(self):
        return 2 * (self.en + self.boy)

    def fiyat(self, m2_fiyat):
        return self.alan() * m2_fiyat

dikdortgen1 = Dikdortgen(10, 20)
print("En:", dikdortgen1.en)
print("Boy:", dikdortgen1.boy)
print("Dikdörtgen Alan:", dikdortgen1.alan())
print("Dikdörtgen Çevre:", dikdortgen1.cevre())
print("Dikdörtgen Fiyat:", dikdortgen1.fiyat(100))