# =========================================================
# GİTA 2112 — Hafta 9 — Örnek 06
# Konu: Yabancı kod okuma atölyesi
# Ne öğretiyor:
#   - Bir başkasının (örneğin Gemini'nin) yazdığı kodu satır satır okuma
#   - Bilmediğin yapıları paniklemeden tanıyabilme
#   - Snippet'in ne yaptığını tahmin edip çalıştırarak doğrulama
#
# Nasıl çalışılacak:
#   1. Her snippet'i tek başına okuyun. Yorum YAZMAYIN.
#   2. "Bu kod ne yapıyor?" sorusunu kendinize sorun.
#   3. Sınıfta birlikte satır satır deşeceğiz.
#   4. İsterseniz tek bir snippet'i kopyalayıp yeni bir dosyada çalıştırın.
#
# Not: Tüm snippet'ler bağımsızdır. Bu dosyayı doğrudan çalıştırırsanız hepsi
# tek tek çalışır. Snippet 5 internet bağlantısı ister.
# =========================================================


# === SNIPPET 1 ===
# Bu kodu Gemini verdi. Ne yapıyor?
print("\n=== SNIPPET 1 ===")

renkler = ["#FF6B6B", "#1E3A8A", "#FFD93D", "#06D6A0", "#118AB2"]
sicak_olanlar = [r for r in renkler if r.startswith("#F")]
print("Sıcak görünenler:", sicak_olanlar)
print("Toplam:", len(sicak_olanlar), "renk")


# === SNIPPET 2 ===
# Bu kodu Gemini verdi. Ne yapıyor?
print("\n=== SNIPPET 2 ===")

dosya_yolu = "olmayabilir.txt"
try:
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        satirlar = f.readlines()
    print(f"{len(satirlar)} satır okundu.")
except FileNotFoundError:
    print(f"'{dosya_yolu}' yok. Boş listeyle devam.")
    satirlar = []


# === SNIPPET 3 ===
# Bu kodu Gemini verdi. Ne yapıyor?
print("\n=== SNIPPET 3 ===")

class Font:
    def __init__(self, ad, puan):
        self.ad = ad
        self.puan = puan
    def buyut(self, miktar):
        self.puan = self.puan + miktar
        return self

baslik = Font("Inter", 24)
baslik.buyut(8).buyut(4)
print(f"{baslik.ad} - {baslik.puan}pt")


# === SNIPPET 4 ===
# Bu kodu Gemini verdi. Ne yapıyor?
print("\n=== SNIPPET 4 ===")

projeler = [
    {"ad": "Caz Festivali", "butce": 12000},
    {"ad": "Roman Kapağı", "butce": 4500},
    {"ad": "Kurumsal Kimlik", "butce": 28000},
    {"ad": "Sergi Posteri", "butce": 8000},
]
sirali = sorted(projeler, key=lambda p: p["butce"], reverse=True)
for p in sirali:
    print(f"{p['ad']}: {p['butce']} TL")


# === SNIPPET 5 ===
# Bu kodu Gemini verdi. Ne yapıyor?
# Not: İnternet yoksa hata yakalanır, program çökmez.
print("\n=== SNIPPET 5 ===")

import requests

try:
    cevap = requests.get(
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=41.01&longitude=28.97&current=temperature_2m",
        timeout=5,
    )
    veri = cevap.json()
    sicaklik = veri["current"]["temperature_2m"]
    print(f"İstanbul şu an: {sicaklik}°C")
except requests.exceptions.RequestException:
    print("İnternete ulaşılamadı. Demo dışı tutuluyor.")
except KeyError:
    print("API yanıtının formatı beklenenden farklı.")


# === SNIPPET 6 ===
# Bu kodu Gemini verdi. Ne yapıyor?
print("\n=== SNIPPET 6 ===")

def selamla(isim):
    print(f"Merhaba {isim}, tasarım stüdyosuna hoş geldin.")

if __name__ == "__main__":
    selamla("Defne")
    selamla("Can")
