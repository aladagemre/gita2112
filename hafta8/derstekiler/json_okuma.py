# Konu: JSON dosyası okuma (en sade hali)
# ----------------------------------------
# Bu örnek bir JSON dosyasını okur ve Python veri yapısına (list/dict) dönüştürür.
# - json.load() → açık bir dosya nesnesinden okur.
# - json.loads() → string'den okur (ekstra "s" → string).
# Sonuç: renkler değişkeni bir liste içinde sözlükler tutar.
#         (Her renk: {"isim": ..., "hex": ..., "grup": ...})

import json

with open("renkler.json", "r", encoding="utf-8") as json_dosya:
    renkler = json.load(json_dosya)
    print(renkler)