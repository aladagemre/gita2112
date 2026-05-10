# Konu: CSV dosyası okuma + sözlük dönüşümü + JSON dosyasına yazma
# -----------------------------------------------------------------
# Bu örnek çok adımlı bir veri işleme akışı gösterir:
#   1) renkler.csv dosyası csv.reader ile okunur.
#   2) next(okuyucu) ile başlık (header) satırı atlanır.
#   3) Her satır bir sözlüğe (dict) çevrilir ve renkler listesine eklenir.
#      → Bu yapı "list of dicts" olarak bilinir; JSON ile birebir uyumludur.
#   4) Renkler "sıcak" / "soğuk" gruplarına göre sayılır.
#   5) Sonuç JSON formatında renkler.json dosyasına yazılır.
# json.dump parametreleri:
#   - ensure_ascii=False → Türkçe karakterler "\u..." olarak değil olduğu gibi yazılır.
#   - indent=4           → İnsan okuyabilir biçimde girintili yazar.

import csv
import json

renkler = []

with open("renkler.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    next(okuyucu)  # Başlık satırını atla
    for satir in okuyucu:
        renk = {
            "isim": satir[0],
            "hex": satir[1],
            "grup": satir[2]
        }
        renkler.append(renk)

print(renkler)

sicak = 0
soguk = 0

for renk in renkler:
    if renk["grup"] == "sıcak":
        sicak += 1
    else:
        soguk += 1

print(f"Sıcak renk sayısı: {sicak}")
print(f"Soğuk renk sayısı: {soguk}")

with open("renkler.json", "w", encoding="utf-8") as json_dosya:
    json.dump(renkler, json_dosya, ensure_ascii=False, indent=4)