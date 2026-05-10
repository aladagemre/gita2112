# Konu: JSON dosyası okuma + güncelleme + tekrar yazma (round-trip)
# ------------------------------------------------------------------
# Bu örnek bir JSON dosyasının tam yaşam döngüsünü gösterir:
#   1) json.load() ile dosya Python sözlüğüne (dict) çevrilir.
#   2) Sözlük üzerinde değişiklik yapılır (proje["ad"] güncellenir).
#   3) json.dump() ile dosya tekrar yazılır.
# Önemli: Aynı dosyaya yazmak için ayrı bir "with open(..., 'w')" bloğu açtık.
#          Aynı dosyayı hem okuma hem yazma için aynı anda açmak risklidir.
# ensure_ascii=False sayesinde "Defne Aydın" gibi Türkçe değerler bozulmaz.

import json

with open("proje.json", "r", encoding="utf-8") as json_dosya:
    proje = json.load(json_dosya)

print(proje["ad"])
print(proje["renkler"][0])

proje["ad"] = "Yeni Proje"
print(proje)

with open("proje.json", "w", encoding="utf-8") as json_dosya:
    json.dump(proje, json_dosya, ensure_ascii=False, indent=4)
