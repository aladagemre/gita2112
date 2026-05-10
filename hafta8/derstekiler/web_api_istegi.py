# Konu: HTTP isteği ile web API'sinden veri çekme (requests kütüphanesi)
# ----------------------------------------------------------------------
# Bu örnek Open-Meteo API'sinden Berlin (lat=52.52, lon=13.41) için hava durumu çeker.
# - requests.get(url) → GET isteği gönderir, bir Response nesnesi döner.
# - r.status_code     → HTTP yanıt kodu (200 = başarılı, 404 = bulunamadı, vb.)
# - r.text            → Yanıtın ham metin halidir (bu API JSON döner).
# - r.json()          → Yanıtı doğrudan Python sözlüğüne çevirir (ileri kullanım).
# Not: requests modülü standart kütüphanede DEĞİLDİR; "uv add requests" veya
#      "pip install requests" ile yüklenmelidir (zaten pyproject.toml'da tanımlı).

import requests

r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
print(r.status_code)
print(r.text)  # Sadece ilk 1000 karakteri yazdır