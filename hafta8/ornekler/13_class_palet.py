# =========================================================
# GİTA 2112 — Hafta 9 — Örnek 04
# Konu: Class (sınıf) — Palet sınıfı
# Ne öğretiyor:
#   - class anahtar kelimesi
#   - __init__ ile yeni nesne oluşturma (yapıcı)
#   - self kavramı — "bu nesnenin kendisi"
#   - Metot tanımlama (sınıfın içindeki fonksiyonlar)
#   - Aynı sınıftan birden fazla nesne yaratma
#
# Hatırlatma:
#   H8'de Dikdörtgen sınıfını görmüştünüz:
#       class Dikdortgen:
#           def __init__(self, en, boy): ...
#           def alan(self): ...
#   Aynı kalıp ama bu sefer renk listesi tutan bir sınıf yazıyoruz.
# =========================================================


class Palet:
    """Bir renk paletini temsil eder.

    Her palette bir isim ve bir renk listesi vardır.
    Renkler hex kodu (örn: '#FF6B6B') olarak tutulur.
    """

    def __init__(self, isim: str, renkler: list):
        # __init__ "yapıcı" demek. Yeni bir Palet nesnesi yaratılırken
        # otomatik çalışır. İçinde nesnenin başlangıç verisini ayarlarız.
        self.isim = isim
        self.renkler = renkler

    def renk_ekle(self, renk: str):
        """Palete yeni bir renk ekler."""
        self.renkler.append(renk)

    def renk_sayisi(self) -> int:
        """Palette kaç renk olduğunu döndürür."""
        return len(self.renkler)

    def birincil(self) -> str:
        """Birincil rengi (ilk renk) döndürür."""
        return self.renkler[0]

    def bilgi_ver(self):
        """Palet hakkında özet bilgi yazdırır."""
        print(f"Palet: {self.isim}")
        print(f"  Renk sayısı: {self.renk_sayisi()}")
        print(f"  Birincil renk: {self.birincil()}")
        print(f"  Tüm renkler: {', '.join(self.renkler)}")


# --- Kullanım ------------------------------------------------------------

# 1. İlk palet — sıcak tonlar
sicak = Palet("Yaz Sıcağı", ["#FF6B6B", "#FFD93D", "#FF8C42"])

# 2. İkinci palet — soğuk tonlar
soguk = Palet("Kış Tonları", ["#1E3A8A", "#3B82F6", "#93C5FD"])

# 3. Üçüncü palet — boş başlıyor
yeni_proje = Palet("Yeni Proje", [])

# Her nesnenin kendi verisi var. self bunu sağlıyor.
sicak.bilgi_ver()
print("---")
soguk.bilgi_ver()
print("---")

# Yeni projeye yavaş yavaş renk ekleyelim
yeni_proje.renk_ekle("#000000")
yeni_proje.renk_ekle("#FFFFFF")
yeni_proje.renk_ekle("#FF0066")

yeni_proje.bilgi_ver()
print("---")

# Sıcak palete bir renk daha ekleyelim — soğuk paleti etkilemez
sicak.renk_ekle("#E63946")
print(f"Sıcak palete renk eklendi. Yeni sayı: {sicak.renk_sayisi()}")
print(f"Soğuk palet hala: {soguk.renk_sayisi()} renkli (etkilenmedi).")

# Çıktı:
# Palet: Yaz Sıcağı
#   Renk sayısı: 3
#   Birincil renk: #FF6B6B
#   Tüm renkler: #FF6B6B, #FFD93D, #FF8C42
# ---
# Palet: Kış Tonları
#   Renk sayısı: 3
#   Birincil renk: #1E3A8A
#   Tüm renkler: #1E3A8A, #3B82F6, #93C5FD
# ---
# Palet: Yeni Proje
#   Renk sayısı: 3
#   Birincil renk: #000000
#   Tüm renkler: #000000, #FFFFFF, #FF0066
# ---
# Sıcak palete renk eklendi. Yeni sayı: 4
# Soğuk palet hala: 3 renkli (etkilenmedi).
