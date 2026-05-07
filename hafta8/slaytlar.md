# GİTA 2112 — Hafta 8

## Çevre, Dosya, Kod Okuma

- VCD Python Giriş Dersi
- 8 Mayıs 2026
- Bu hafta dilin **etrafını** öğreniyoruz

-----

## Bu Hafta Neden Farklı?

- Şimdiye kadar: **dilin içi** (değişken, döngü, fonksiyon)
- Bu hafta: **dilin etrafı** (terminal, dosya, paket, hata)
- Python'u bir **stüdyo yazılımı** gibi kullanmaya hazırlanıyoruz
- InDesign'ı kullanmak gibi: dosya aç, font ekle, kayıt yerini bil

-----

## Bu Haftanın Sekiz Bloku

1. Terminal temelleri
2. uv ile bağımlılık yönetimi
3. Dosya okuma ve yazma
4. import ve modül kavramı
5. CSV dosyaları
6. JSON dosyaları
7. Traceback (hata) okuma
8. Yabancı kod okuma

-----

## Hafta 7'den Hatırlıyoruz

- **Niyet → Storyboard → Pseudocode → Python**
- Algoritmayı 3-5 kareye bölme
- "Ne veriyorum? Ne istiyorum? Aradaki yol nasıl?"
- Bu hafta tekrar yeni Python yapılarına dönüyoruz

-----

## Ön Refleks: Hata Görünce Ne Yapılır?

- Bugün hata göreceksiniz. **Çoook hata.**
- Komut yanlış yazılır, dosya bulunmaz, paket eksiktir
- **Panik yok.**
- Python bize her zaman bir şey söyler

-----

## Refleks Tek Cümle

> **HATA → en alt satıra bak → tipini gör → tanıdık mı?**

- Traceback uzun gözükür
- Ama sadece **son satır** önemli
- Geri kalanı şimdilik atlayın

-----

## Bu Hafta 5 Hata Tipi

| Hata | Kabaca |
|---|---|
| `NameError` | Değişken adını yanlış yazdın |
| `TypeError` | Yanlış tipte işlem (metin + sayı) |
| `IndentationError` | Girinti yanlış |
| `FileNotFoundError` | Dosya yok / yanlış klasördesin |
| `ModuleNotFoundError` | Paketi henüz kurmadın |

Şimdi sadece **adlarını** tanıyın. Bölüm 7'de hepsini canlı göreceğiz.

-----

## Bölüm 1 — Terminal

### Niye bu konu?

Python dosyalarını çalıştırmak ve klasörler arasında gezinmek için.

-----

## Terminal Nedir?

- Bilgisayara **fareyle değil yazıyla** komut verdiğin pencere
- macOS: "Terminal"
- Windows: "PowerShell" ya da "Command Prompt"
- VS Code içinde: **Terminal → New Terminal**

-----

## Tasarım Benzetmesi

- Photoshop'ta **File → Open** = terminalde `open dosya.psd`
- InDesign'da export klasörü seçmek = terminalde "şu an buradayım, dosya buraya yazılır"
- Sonuç aynı, yöntem yazıyla
- Dosyanın **nerede** olduğunu bilmek dosya okumanın temelidir

-----

## Üç Komut Yeter

```bash
pwd          # Şu an hangi klasördeyim?
ls           # Bu klasörde ne var?
cd hafta8    # hafta8 klasörüne gir
cd ..        # Bir üst klasöre çık
```

Ve Python dosyası çalıştırmak için:

```bash
python3 script.py    # Mac/Linux
python script.py     # Windows
```

-----

## Göreli ve Mutlak Yol

- **Mutlak yol:** `/Users/defne/Documents/gita/hafta8/renkler.txt`
- **Göreli yol:** `renkler.txt` veya `veri/renkler.txt`

> Mutlak: "İstanbul, Şişli, Büyükdere Cad. No:5"
> Göreli: "buradan iki sokak ileride sağda"

`FileNotFoundError`'un %90 sebebi terminalin yanlış klasörde açık olmasıdır.

-----

## Bölüm 2 — uv

### Niye bu konu?

Bir başkasının (ya da Gemini'nin) projesini kurup çalıştırabilmek için.

-----

## Bağımlılık Nedir?

- Python tek başına çok şey yapar
- Ama bazı işler için **dış paketler** gerekir
  - Resim açmak için → Pillow
  - Grafik çizmek için → matplotlib
  - Veri için → pandas
- Bunlara **bağımlılık** (dependency) denir

-----

## Tasarım Benzetmesi

- InDesign dosyası açtığında "Missing fonts" uyarısı alırsın
- Çünkü dosya o fontlara **bağımlı**
- Python projesi de aynı: hangi paketlere bağımlı olduğu **listelenir**
- Bu liste `pyproject.toml` dosyasında durur

-----

## uv Üç İş Yapar

```bash
uv init renk-paleti     # Yeni proje aç
uv add pillow           # Paket ekle
uv run main.py          # Doğru ortamda çalıştır
```

- Eskiden bu üç iş için üç ayrı araç gerekirdi
- `uv` hepsini tek araçta toplar

-----

## Sanal Ortam

- Her tasarım projesinin **kendi klasörü** vardır
- Fontlar, mockuplar, görseller karışmasın diye
- Python da aynı: her projenin **kendi sanal ortamı**
- Proje A: Pillow 10.0
- Proje B: Pillow 11.2
- Çakışmazlar — `uv` otomatik yönetir

-----

## Kurulum

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Kontrol:

```bash
uv --version
```

-----

## Tipik Akış

```bash
uv init renk-paleti
cd renk-paleti
uv add pillow
uv run main.py
```

- Bir kez kur, sonra her gün üç komut
- Bu hafta için tüm ihtiyacın bu

-----

## pyproject.toml — Projenin Künyesi

```toml
[project]
name = "renk-paleti"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "pillow>=11.0.0",
]
```

- Bir poster dosyasının "boyut: 50x70cm, font: Inter" künyesi gibi
- `uv add` otomatik buraya yazar
- Açıp düzenlemen gerekmez — ama görünce tanı

-----

## Karıştırma Tuzağı

- `uv add pillow` → paketi **bir kez** ekler
- `uv run main.py` → her seferinde **çalıştırır**
- `python main.py` (uv'siz) → sanal ortamı **atlar**
- Atlarsan: `ModuleNotFoundError`

-----

## Bölüm 3 — Dosya I/O

### Niye bu konu?

Programın kapanınca her şey unutulmasın diye. Brif, palet, künye — diske yaz.

-----

## Tasarım Benzetmesi

- Illustrator dosyasını `.ai` olarak kaydedersin
- Ertesi gün açtığında her şey yerli yerinde
- Çünkü dosya **disk üstünde**, bellekte değil
- Python'da `open()` → InDesign'ın "Open" / "Close" menüsü

-----

## En Basit Dosya Okuma

```python
with open("renkler.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()

print(icerik)
```

- `"renkler.txt"` → açılacak dosya
- `"r"` → okuma modu
- `encoding="utf-8"` → Türkçe karakterler için zorunlu

-----

## with open Neden?

```python
with open("renkler.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
```

- Kullandıktan sonra **otomatik kapatır**
- Photoshop'ta dosyayı açıp kapatmayı unutmadığın gibi
- Hep böyle yaz

> Hata refleksi: dosya yoksa → `FileNotFoundError`. Tanıdık geldi mi?

-----

## Üç Mod

| Mod | Anlamı | Davranış |
|---|---|---|
| `"r"` | read | Okur. Yoksa hata. |
| `"w"` | write | Yazar. **Varsa siler!** |
| `"a"` | append | Yazar. Sonuna ekler. |

`"w"` modu sessiz silici — Photoshop'ta "Save As" yaparken eskinin üzerine yazmak gibi.

-----

## encoding="utf-8" Neden Lazım?

- Bilgisayar harfleri **sayı** olarak saklar
- Farklı yazı sistemleri farklı sayılar kullanır
- "ş, ğ, ü, ç" yerine "Ã§, Ã¶" görüyorsan çevrim yanlış
- Çözüm: her dosyada `encoding="utf-8"` yaz

```python
with open("dosya.txt", "r", encoding="utf-8") as f:
    ...
```

-----

## Satır Satır Okuma

```python
with open("renkler.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        print(satir.strip())
```

- Her `satir` bir Python `str`
- `strip()` → satır sonundaki görünmez `\n`'i temizler
- Döngüyle çok güzel uyuşur

-----

## Yazma

```python
renkler = ["kırmızı", "mavi", "turuncu"]

with open("yeni_palet.txt", "w", encoding="utf-8") as dosya:
    for renk in renkler:
        dosya.write(renk + "\n")
```

- `"\n"` → "yeni satır"
- Eklemezsen tüm renkler aynı satıra yapışır

-----

## Bölüm 4 — import

### Niye bu konu?

Python'a "şu yetenekleri de kullan" demek için.

-----

## Modül Nedir?

- Python temelde `print`, `len`, `for`, `if` bilir
- Matematik, rastgele sayı, dosya formatları → **modüllerde** durur
- Modülü kullanmak için en başta bir kez `import`

```python
import math

print(math.pi)         # 3.14159...
print(math.sqrt(64))   # 8.0
```

-----

## Tasarım Benzetmesi

- Photoshop ilk kurulduğunda temel araçlar gelir
- Bir **plugin** kurarsan yeni yetenekler eklenir
- `import` aynen budur: ekstra yetenekleri etkinleştirme komutu

> Hata refleksi: `import x` → `ModuleNotFoundError`. Ya tipo, ya `uv add x` lazım.

-----

## Standart Kütüphane Turu

| Modül | Ne için? |
|---|---|
| `math` | Matematik |
| `random` | Rastgele seçim |
| `csv` | CSV dosyaları |
| `json` | JSON dosyaları |
| `datetime` | Tarih/zaman |
| `os` | İşletim sistemi |

Hepsi **kuruluma gerek yok** — sadece `import` yaz.

-----

## import'un Üç Şekli

```python
# 1. Modül adıyla erişim (önerilen)
import math
math.sqrt(64)

# 2. Sadece bir parça al
from math import sqrt, pi
sqrt(64)

# 3. Kısa ad ver
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
```

Bu hafta **birinci şekli** kullanın — fonksiyonun nereden geldiği belli olur.

-----

## Bölüm 5 — CSV

### Niye bu konu?

Renk paleti, font listesi, fiyat tablosu — tablo verisi `.txt` ile olmaz.

-----

## CSV Nedir?

```
isim,hex,grup
Mercan,#FF6B6B,sıcak
Lacivert,#1E3A8A,soğuk
Sarı,#FFD93D,sıcak
```

- **C**omma-**S**eparated **V**alues
- İlk satır: kolon başlıkları
- Sonraki her satır: bir kayıt
- Adobe Color → Export → CSV ile elinize geçen şey

-----

## CSV Okuma

```python
import csv

with open("renkler.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    for satir in okuyucu:
        print(satir)
```

- Her satır otomatik bir **liste**
- `satir[0]` ilk hücre, `satir[1]` ikinci hücre

-----

## Başlık Satırını Atlama

```python
with open("renkler.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    next(okuyucu)              # ilk satırı atla
    for satir in okuyucu:
        isim = satir[0]
        hex_kod = satir[1]
        print(f"{isim}: {hex_kod}")
```

`next(okuyucu)` → "bir adım at, başlığı yut"

-----

## Sözlüğe Çevirmek

```python
renkler = []
for satir in okuyucu:
    renk = {
        "isim": satir[0],
        "hex": satir[1],
        "grup": satir[2],
    }
    renkler.append(renk)
```

- Liste indeksi yerine **anahtarla erişim**: daha okunaklı
- `renkler` artık sözlük listesi — tanıdık yapı

-----

## Bölüm 6 — JSON

### Niye bu konu?

Sözlük yapısını dosyaya yazıp geri okumak için. Veriyi **kalıcı** kılar.

-----

## JSON Nedir?

```json
{
  "ad": "Caz Festivali",
  "tarih": "2026-06-15",
  "renkler": ["#FF6B6B", "#1E3A8A"],
  "yayinlandi": false
}
```

- Python sözlüğüne neredeyse aynı
- Anahtarlar **çift tırnak** zorunlu
- `True/False/None` yerine `true/false/null`

-----

## Tasarım Benzetmesi

- InDesign'ın "Document Setup" penceresi
- Belge adı, sayfa boyutu, fontlar, kenar boşlukları
- Bir yerde tutulmalı → JSON
- Bir tasarım projesinin **künye dosyası**

-----

## JSON Okuma

```python
import json

with open("proje.json", "r", encoding="utf-8") as dosya:
    proje = json.load(dosya)

print(proje["ad"])              # Caz Festivali
print(proje["renkler"][0])      # #FF6B6B
```

`json.load()` → JSON dosyasını okuyup Python sözlüğü yapar.

-----

## JSON Yazma

```python
import json

proje = {
    "ad": "Caz Festivali",
    "renkler": ["#FF6B6B", "#1E3A8A"],
    "yayinlandi": False,
}

with open("proje.json", "w", encoding="utf-8") as dosya:
    json.dump(proje, dosya, ensure_ascii=False, indent=2)
```

İki **zorunlu** parametre:
- `ensure_ascii=False` → Türkçe karakterler kaçmasın
- `indent=2` → okunabilir görünsün

-----

## Sözlük ↔ Dosya Köprüsü

```
Python sözlüğü  ──json.dump──▶  JSON dosyası
JSON dosyası    ──json.load──▶  Python sözlüğü
```

- Programı kapatsan bile veri korunur
- Şimdiye kadar yapamadığımız tek şey: **kalıcı veri**

-----

## Bölüm 7 — Traceback Okuma

### Niye bu konu?

🔍 Çünkü hata mesajı **sana yardım etmek için** yazılmıştır. Okumayı bilmek = bağımsızlık.

-----

## Tasarım Benzetmesi

InDesign'da "Missing fonts" uyarısı üç şey söyler:

1. Hangi font (cinsi)
2. Hangi belgede (yer)
3. Ne yapacaksın (eylem)

Traceback aynısını yapar — sadece daha teknik dilde.

-----

## Traceback Anatomisi

```
Traceback (most recent call last):
  File "kod.py", line 5, in <module>
    print(yas)
NameError: name 'yas' is not defined
```

- **En alt satır** → hata adı + açıklama
- **"File ... line N"** → nerede
- En üst satır → atlayın

-----

## Hata 1 — NameError

```python
renkler = ["mor", "mercan"]
print(renlker)   # NameError!
```

```
NameError: name 'renlker' is not defined
```

- Olmayan değişken kullandın
- Çoğu zaman yazım yanlışı
- Bölüm 0'daki listenin 1. tipi — hatırlıyor musun?

-----

## Hata 2 — TypeError

```python
yas = 20
print("Yaşım: " + yas)    # TypeError!
```

```
TypeError: can only concatenate str (not "int") to str
```

- Metin + sayı → olmaz
- Çözüm: f-string

```python
print(f"Yaşım: {yas}")
```

-----

## Hata 3 — IndentationError

```python
def selamla():
print("Merhaba")     # girinti yok!
```

```
IndentationError: expected an indented block
```

- `if`, `for`, `def`, `while` sonrası **mutlaka girintili satır**
- VS Code genelde otomatik yapar — ama elle bozarsan bu hata gelir

-----

## Hata 4 — FileNotFoundError

```python
with open("renkler.txt", "r", encoding="utf-8") as f:
    ...
```

```
FileNotFoundError: [Errno 2] No such file or directory: 'renkler.txt'
```

- Dosya yok ya da terminal yanlış klasörde
- Çözüm: `pwd` ile kontrol et
- Dosya o klasörde mi? Adı doğru mu?

-----

## Hata 5 — ModuleNotFoundError

```python
import pillow    # ModuleNotFoundError!
```

```
ModuleNotFoundError: No module named 'pillow'
```

- Standart modülse → tipo (`pilow`, `randoom`)
- Dış paketse → `uv add pillow`

-----

## Refleks Tek Cümle (Tekrar)

> **HATA → en alt satıra bak → tipi gör → tanıdık mı?**

1. Alt satırı oku — hata adı + mesaj
2. "File ... line N" satırına git
3. O satırı oku, mesajla birleştir
4. Düzelt

-----

## Bölüm 8 — Yabancı Kod Okuma

### Niye bu konu?

H10'da Gemini sana 20 satırlık kod verecek. **Okuyabilmen** lazım.

-----

## Pasif vs Aktif Bilgi

- **Aktif** → siz yazarken kullanabildikleriniz
- **Pasif** → görünce anladıklarınız ama yazmadıklarınız
- Bu hafta üç **pasif yapı** tanıştırıyoruz
- Yazmanız gerekmiyor — **görünce tanımak** yeter

-----

## Pasif 1 — List Comprehension

```python
# Eski yol:
sonuc = []
for renk in renkler:
    if renk.startswith("#"):
        sonuc.append(renk.upper())

# Tek satır:
sonuc = [renk.upper() for renk in renkler if renk.startswith("#")]
```

Sırayla oku: `for` → `if` → değer → `[ ]`

-----

## Pasif 2 — try / except

```python
try:
    with open("renkler.txt", "r", encoding="utf-8") as f:
        icerik = f.read()
except FileNotFoundError:
    print("Dosya yok, varsayılan kullanılacak.")
    icerik = ""
```

- `try` bloğu hata verirse program çökmesin
- `except` çalışır, yedek plana geçer
- Görünce: "burada hata kontrolü var"

-----

## Pasif 3 — Tip İpuçları

```python
def alan_hesapla(en: float, boy: float) -> float:
    return en * boy
```

- `: float` → "bu parametre float olacak"
- `-> float` → "fonksiyon float döndürecek"
- **Opsiyonel notlar** — kod bunlar olmadan da çalışır
- Gemini bunları bolca yazar — paniklemeyin

-----

## Bu Haftanın Ödevleri

| Ödev | Zorluk | Konu |
|---|---|---|
| 1 | Kolay | Terminal & uv kurulumu (belgeleme) |
| 2 | Kolay-Orta | Tasarım brifi yazma |
| 3 | Orta | Renk paleti okuma + sayma |
| 4 | Orta | Proje künyesi (JSON) |
| 5 | Zor | CSV → JSON köprüsü (4 fonksiyon) |

`hafta8/odevler/` klasöründe. `odevler/BENIOKU.md` ile başla.

-----

## Hafta 9'a Önbakış

- Bu hafta: dilin etrafını **tanıdık** ettik
- Hafta 9: pekiştirme + traceback atölyesi + mini "tasarım envanteri" projesi
- Hafta 10: **Gemini ile vibecoding**
- Bu haftayı atlatabilirsen vibecoding'e hazırsın

-----

## Tek Cümlelik Özet

> Bu hafta Python öğrenmedik. **Python kullanıcısı** olduk.

- Terminal aç, dosya bul, paket kur
- Hata gör, son satıra bak, düzelt
- Yabancı kod gör, satır satır oku
- H10'a hazırız.
