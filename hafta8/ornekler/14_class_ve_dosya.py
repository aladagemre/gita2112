# =========================================================
# GİTA 2112 — Hafta 9 — Örnek 05
# Konu: Class + JSON dosyası
# Ne öğretiyor:
#   - Bir nesneyi sözlüğe çevirme (to_dict deseni)
#   - Sözlüğü JSON'a yazma (kalıcı saklama)
#   - JSON'dan okuyup geri nesne yaratma
#   - try/except ile dosya hatasını yönetme
# =========================================================

import json


class Palet:
    """Renk paleti — H9 Örnek 04'tekiyle aynı, ama kaydetme/yükleme de yapıyor."""

    def __init__(self, isim: str, renkler: list):
        self.isim = isim
        self.renkler = renkler

    def renk_sayisi(self) -> int:
        return len(self.renkler)

    def to_dict(self) -> dict:
        """Nesneyi bir sözlüğe çevirir. JSON'a yazmak için bu lazım."""
        return {
            "isim": self.isim,
            "renkler": self.renkler,
        }

    def bilgi_ver(self):
        print(f"Palet '{self.isim}' — {self.renk_sayisi()} renk")
        for renk in self.renkler:
            print(f"  - {renk}")


# --- 1. Yeni bir palet oluştur ve JSON'a kaydet -------------------------

orijinal = Palet("Bahar Esintisi", ["#A8DADC", "#F1FAEE", "#E63946", "#1D3557"])

# Nesneyi sözlüğe çevir
sozluk = orijinal.to_dict()
print("Sözlük hali:", sozluk)

# JSON dosyasına yaz (try/except ile sarmalıyoruz)
dosya_yolu = "palet_kaydi.json"

try:
    with open(dosya_yolu, "w", encoding="utf-8") as dosya:
        json.dump(sozluk, dosya, ensure_ascii=False, indent=2)
    print(f"Palet '{dosya_yolu}' dosyasına kaydedildi.")
except PermissionError:
    print("Bu klasöre yazma iznin yok.")

print("---")


# --- 2. JSON'dan okuyup yeni nesne oluştur ------------------------------

try:
    with open(dosya_yolu, "r", encoding="utf-8") as dosya:
        yuklenen_sozluk = json.load(dosya)
    print("Diskten okunan sözlük:", yuklenen_sozluk)

    # Sözlükten yeni bir Palet nesnesi yarat
    yuklenen_palet = Palet(
        isim=yuklenen_sozluk["isim"],
        renkler=yuklenen_sozluk["renkler"],
    )
    print()
    print("Yüklenen palet:")
    yuklenen_palet.bilgi_ver()

except FileNotFoundError:
    print(f"'{dosya_yolu}' dosyası bulunamadı. Önce kaydetmeyi denedin mi?")
except json.JSONDecodeError:
    print("Dosya JSON formatında değil. İçeriği bozuk olabilir.")

print("---")


# --- 3. Olmayan bir dosyadan okumayı dene ------------------------------
# Bu kez bilinçli olarak olmayan bir dosya açıyoruz — hata yakalamayı gör.

try:
    with open("bozuk_dosya.json", "r", encoding="utf-8") as dosya:
        bozuk = json.load(dosya)
except FileNotFoundError:
    print("Beklenen: dosya yok. Program çökmüyor, devam ediyoruz.")
except json.JSONDecodeError as e:
    print("JSON parse hatası:", e)

print("---")
print("Tüm işlemler tamamlandı.")
