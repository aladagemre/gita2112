# GİTA 2112 — Hafta 8: Çevre, Dosya, Kod Okuma

> Bu belge, derste anlatılan konuların yazılı özetidir.
> Her bölümün sonunda ilgili kod dosyasına yönlendirme bulunur.
> Kod dosyalarını açıp çalıştırarak burada okuduklarınızı pratiğe dökebilirsiniz.

---

## Hafta 7'den Hatırlamamız Gerekenler

Geçen hafta yeni bir Python yapısı öğrenmedik. Onun yerine **bir kod yazmadan önce nasıl düşünmemiz gerektiğini** çalıştık:

- **Niyet → Storyboard → Pseudocode → Python** sırası
- Her algoritmayı 3-5 kareye bölerek tasarlama
- "Ne veriyorum? Ne istiyorum? Aradaki yol nasıl?" soruları
- Türkçe-Python karışımı sözde kod (pseudocode)

Bu hafta tekrar yeni Python yapıları öğrenmeye dönüyoruz — ama başka bir açıdan. Şimdiye kadar **dilin içini** öğrendik (değişken, döngü, fonksiyon). Bu hafta **dilin etrafını** öğreneceğiz: Python'un yaşadığı bilgisayar dünyasını.

---

## Bu Hafta Neyi, Neden Öğreniyoruz?

Önümüzdeki haftalarda bir tasarım/kod aracını (Gemini gibi) kullanarak proje üreteceğiz. Bu modeller hızla kod yazıyor — ama o kodu çalıştırmak, hata mesajını okumak, eksik kütüphaneyi kurmak, dosyayı doğru klasöre koymak **size düşüyor**.

Yani Python'u bir programlama dili olarak değil, **bir tasarım stüdyosu yazılımı gibi** kullanmaya hazırlanıyoruz. InDesign'da bir dosyayı açmayı, kayıt yerini değiştirmeyi, font eklemeyi nasıl biliyorsanız — Python'da da terminali açmayı, paket kurmayı, dosya okumayı, hata mesajını okumayı bileceksiniz.

Bu hafta sekiz başlık var. Bolca konu, ama her biri kısa:

1. Terminal temelleri (üç komut yetiyor)
2. `uv` ile bağımlılık yönetimi
3. Dosya okuma ve yazma
4. `import` ve modül kavramı
5. CSV dosyaları
6. JSON dosyaları
7. Hata mesajlarını (traceback) okuma kültürü
8. Yabancı bir kodu satır satır okuma alıştırması

---

## ⚡ Ön Refleks: Hata Görünce Ne Yapılır?

Bu konuya dersin sonunda detaylı gireceğiz. Ama dersin **başında** bilmeniz gereken bir şey var: bugün hata göreceksiniz. Çoook hata. Komut yanlış yazılır, dosya bulunmaz, modül kurulu değildir, girintilerde kayma olur. **Panik yok.**

Python her hata aldığında bize **traceback** denilen bir mesaj verir. Bu mesaj uzun gözükebilir ama refleks basittir:

> **HATA → en alt satıra bak → tipini gör → tanıdık mı?**

Bu hafta sık göreceğimiz beş hata tipi şunlar — şimdi sadece **isimlerini** bilmeniz yeterli:

| Hata tipi | Kabaca anlamı |
|---|---|
| `NameError` | Değişken adını yanlış yazdın |
| `TypeError` | Yanlış tipte işlem (örneğin metin + sayı) |
| `IndentationError` | Girinti yanlış |
| `FileNotFoundError` | Dosya yok ya da yanlış klasördesin |
| `ModuleNotFoundError` | Bir paketi henüz kurmadın (`uv add` ile kurulur — Bölüm 2'de) |

Bunları **şimdi öğrenmeyin**. Sadece "bu liste var" diye aklınızda tutun. Ders boyunca bir hata aldığınızda dönün, listeye bakın. Dersin sonunda bu listenin her birini gerçek bir traceback ile inceleyeceğiz.

---

## 1. Terminal Temelleri

### Terminal Nedir?

Terminal, bilgisayara **fareyle değil yazıyla** komut verdiğiniz bir penceredir. macOS'ta "Terminal", Windows'ta "PowerShell" veya "Command Prompt" diye adlandırılır. VS Code'un içinde de **Terminal → New Terminal** menüsünden açılır — biz çoğunlukla bunu kullanacağız.

Korkulacak bir şey değil. Uzun yıllar yazılımcılar fareli arayüzler olmadan da çalıştı. Aslında bir tasarım dosyasının "Save As" diyaloğunu yazıyla yapmaktan farkı yok.

### Tasarım Dünyasından Bir Benzetme

Photoshop'ta dosya menüsünden "Open" demek = terminalde `open dosya.psd` yazmak. Sonuç aynı: dosya açılır. Sadece yöntem farklı.

InDesign'da bir klasör seçip oraya export almak = terminalde "şu an bu klasördeyim, dosya buraya kaydedilecek" demektir. Dosyanın **nerede** olduğunu bilmek dosya okumanın temelidir.

### Üç Komut Yeter

Aslında bu hafta için sadece üç komutu bilmeniz yeterli:

```bash
pwd          # Şu an hangi klasördeyim? (print working directory)
ls           # Bu klasörde ne var? (Windows'ta: dir)
cd hafta8    # "hafta8" klasörüne gir (change directory)
cd ..        # Bir üst klasöre çık
```

Ve bir de Python dosyası çalıştırmak için:

```bash
python3 script.py    # Mac/Linux
python script.py     # Windows
```

### Göreli ve Mutlak Yol

Terminalde **"şu an neredesiniz"** her zaman önemlidir.

- **Mutlak yol:** `/home/defne/Documents/gita2112/hafta8/renkler.txt` — bilgisayarın en üstünden başlayan tam adres.
- **Göreli yol:** `renkler.txt` veya `veri/renkler.txt` — şu an bulunduğunuz yere göre adres.

Tasarım benzetmesi: mutlak yol = "İstanbul, Şişli, Büyükdere Cad. No:5". Göreli yol = "buradan iki sokak ileride sağda".

Kodda dosya açtığınızda göreli yol kullanırsanız, **terminalin nerede açıldığı önemli olur**. Dosya bulunamadı hatasının %90 sebebi budur.

> **Not:** Terminalin nasıl açılıp kullanılacağı `ornekler/01_terminal_temelleri.py` dosyasında ve `ornekler/BENIOKU.md` dosyasının başında ayrıntılı anlatılır.

---

## 2. uv ile Bağımlılık Takibi

### Bağımlılık Nedir?

Python tek başına bir sürü iş yapabilir, ama bazen başkalarının yazdığı kütüphaneleri kullanmak isteriz: bir resmi açmak için `Pillow`, bir grafik çizmek için `matplotlib`, bir API'ye bağlanmak için `requests`. Bunlar **bağımlılık** (dependency) denilen dış paketlerdir.

### Tasarım Dünyasından Bir Benzetme

Bir InDesign projesi açtığınızda bazen "şu fontu bulamadım" uyarısı alırsınız. InDesign size, "bu dosya şu fontlara bağımlı" der. Eğer fontu sisteme yüklemediyseniz, dosya yanlış görünür.

Python projeleri de aynıdır. Bir projeyi başkasıyla paylaştığınızda, "bu proje şu paketlere ihtiyaç duyuyor" diyen bir liste vardır. Bu liste `pyproject.toml` adlı bir dosyada tutulur.

### uv Nedir?

`uv`, modern bir Python proje yöneticisidir. Üç işi yapar:

1. **Yeni proje oluşturur** (`uv init`)
2. **Paket ekler** (`uv add pillow`)
3. **Dosyayı doğru ortamda çalıştırır** (`uv run script.py`)

Eskiden bu üç iş için üç ayrı araç (pip, virtualenv, python) kullanılırdı. `uv` hepsini tek bir komutta toplar.

### Sanal Ortam — Her Projenin Malzeme Kutusu

Her tasarım projesi için ayrı bir klasör tutarsınız: bir poster işi için "Caz Festivali", bir kitap kapağı için "Roman Tasarımı". Fontları, görselleri, mockup'ları ayrı tutarsınız. Birinin değişikliği öbürünü etkilemesin diye.

Python da aynı şeyi yapar. Her projenin **kendi sanal ortamı** (virtual environment) vardır. Bir projede `Pillow 10.0` kullanırken başka projede `Pillow 11.2` kullanabilirsiniz, çakışmazlar. `uv` bunu otomatik yönetir.

### Kurulum

**macOS / Linux** (Terminal'de):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows** (PowerShell'de):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Kurulumdan sonra terminali kapatıp açın. Şu komutla kontrol edin:

```bash
uv --version
```

Bir sürüm numarası görürseniz hazırsınız.

### Tipik Akış

```bash
uv init renk-paleti           # Yeni klasör + boş Python projesi oluşturur
cd renk-paleti
uv add pillow                 # Pillow paketini ekler ve kurar
uv run main.py                # main.py'yi doğru ortamda çalıştırır
```

Bu üç komut bu hafta için size yeterli. Hepsini görsel adımlarla `ornekler/02_uv_kullanimi.py` dosyasında göreceksiniz.

### pyproject.toml Dosyası

`uv init` çalıştırdığınızda klasörünüzde `pyproject.toml` adında bir dosya oluşur. Açıp içine bakarsanız şuna benzer bir şey görürsünüz:

```toml
[project]
name = "renk-paleti"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "pillow>=11.0.0",
]
```

Bu dosya, projenizin **künyesidir**. Adını, sürümünü ve bağımlılıklarını listeler. Bir poster dosyasının üzerinde "boyut: 50x70cm, font: Inter" yazması gibi.

`uv add pillow` dediğinizde `dependencies` listesine otomatik eklenir. Manuel açıp düzenlemeniz gerekmez (ama nasıl göründüğünü bilmelisiniz çünkü Gemini gibi araçlar bu dosyaya bakacak).

> **Dosya:** `ornekler/02_uv_kullanimi.py`

---

## 3. Dosya Okuma ve Yazma

### Neden Dosya?

Şimdiye kadar yazdığımız kod programı kapatınca her şeyi unutuyordu. Bir liste oluşturduk, bir döngüyle hesapladık — program bitti, her şey gitti.

Dosyalar bu unutkanlığı çözer. Bir tasarım brifi dosyası, bir renk paleti listesi, kullanıcıdan toplanan veriler — hepsi diske yazılır ve sonradan tekrar okunur.

### Tasarım Dünyasından Bir Benzetme

Bir Illustrator dosyasını ".ai" olarak kaydedersiniz. Ertesi gün açtığınızda her şey yerli yerinde. Hatta başka bilgisayarda bile. Çünkü dosya **disk üstünde** duruyor, bilgisayar belleğinde değil.

Python'da `open()` fonksiyonu, bu dosyayı açma/kapama işidir. Aynı InDesign'ın "Open" ve "Close" menüleri gibi.

### En Basit Hali

```python
with open("renkler.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()

print(icerik)
```

Üç parça:

- `"renkler.txt"` — açılacak dosyanın adı (göreli yol)
- `"r"` — okuma modu (read)
- `encoding="utf-8"` — Türkçe karakterler için zorunlu (aşağıda detayı var)

`with open(...) as dosya:` deyimi, dosyayı açıp kullandıktan sonra **otomatik kapatır**. Bir InDesign dosyasını açıp kapatmayı unutmadığınız gibi, bu deyim de unutmanıza izin vermez. Hep böyle yazın.

> ↪ **Hata Refleksi:** Dosya yoksa veya yanlış klasördeyseniz `FileNotFoundError` alırsınız — Bölüm 0'daki listenin 4. tipi. Tanıdık geldi mi?

### Modlar

| Mod | Anlamı | Ne yapar? |
|-----|--------|-----------|
| `"r"` | read | Dosyayı okur. Yoksa hata. |
| `"w"` | write | Dosyaya yazar. **Varsa siler ve baştan yazar!** |
| `"a"` | append | Dosyaya yazar. Varsa **sonuna ekler.** |

⚠️ `"w"` ile mevcut dosyayı açmak, **eski içeriği siler**. Photoshop'ta "Save As" yaparken aynı isimle yazıp eskinin üzerine yazmak gibi. Dikkat.

### Türkçe Karakterler — encoding="utf-8"

Bilgisayar harfleri sayı olarak saklar. Bu sayılar farklı yazı sistemlerine farklı şekilde çevrilebilir. Eğer "ş, ğ, ü, ç, ı, ö" yerine "Ã§, Ã¶, ï¬‚" gibi tuhaf işaretler görüyorsanız, çevrim yanlış demektir.

`encoding="utf-8"` Türkçe ve dünya dilleri için doğru çevrimi seçer. Bu hafta açtığınız her dosyada bunu yazın:

```python
with open("dosya.txt", "r", encoding="utf-8") as f:
    ...
```

Yazmayı unutursanız Windows'ta "ş" yerine "ﬂ" gibi tuhaf karakterler görürsünüz.

### Satır Satır Okuma

Bir dosyayı tek seferde değil, satır satır okuyabilirsiniz. Bu, döngüyle çok güzel uyuşur:

```python
with open("renkler.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        print(satir.strip())   # strip() satır sonundaki \n'i siler
```

Her bir `satir` bir Python `str`. `strip()` ile sondaki görünmez "yeni satır" karakterini temizliyoruz.

### Yazma

```python
renkler = ["kırmızı", "mavi", "turuncu"]

with open("yeni_palet.txt", "w", encoding="utf-8") as dosya:
    for renk in renkler:
        dosya.write(renk + "\n")
```

`"\n"` "yeni satır" demektir. Yazarken bunu eklemezseniz tüm renkler aynı satıra yapışır.

> **Dosyalar:** `ornekler/03_dosya_okuma.py`, `ornekler/04_dosya_yazma.py`

> **Sıradaki konu:** Renk paletleri ve font listeleri gibi **tablo** verileri için `.txt` yetmez — `.csv` kullanırız. Ama CSV dosyalarını okumak için Python'un `csv` araç kutusunu **etkinleştirmemiz** gerek. Bu yüzden önce `import` ve modül kavramına bakalım, sonra CSV'ye döneriz.

---

## 4. import ve Modül Kavramı

### Modül Nedir?

Python tek başına geldiğinde **temel** komutları bilir: `print`, `len`, `for`, `if` vb. Ama matematik fonksiyonları, rastgele sayı üretimi, dosya formatları, tarih işlemleri — bunlar **modül** denilen ek paketlerde durur.

Bir modülü kullanmak için en başta bir kez `import` yazarsınız:

```python
import math

print(math.pi)             # 3.14159...
print(math.sqrt(64))       # 8.0
```

### Tasarım Dünyasından Bir Benzetme

Photoshop ilk kurulduğunda temel araçları getirir. Ama bir **plugin** kurarsanız (örneğin yeni bir fırça paketi), o pluginin sunduğu özellikleri kullanmaya başlarsınız. `import` aynen budur: ekstra yetenekleri "etkinleştirme" komutu.

Fark şu: Python'a gelen yerleşik (standart kütüphane) modülleri zaten kuruludur, sadece `import` yazmak yeterlidir. Dış paketler için (Pillow gibi) önce `uv add` ile kurmanız gerekir.

> ↪ **Hata Refleksi:** `import x` yazıp da `ModuleNotFoundError` alıyorsanız: ya `x` standart değildir (`uv add x` gerek), ya yazımı yanlıştır. Bölüm 0'daki listenin 5. tipi.

### Standart Kütüphane Turu

Python ile birlikte ücretsiz gelen, kurulum gerektirmeyen modüllerden bazıları:

| Modül | Ne için? | Örnek |
|-------|----------|-------|
| `math` | Matematik fonksiyonları | `math.sqrt`, `math.pi`, `math.ceil` |
| `random` | Rastgele sayı/seçim | `random.choice`, `random.randint` |
| `csv` | CSV dosyaları | `csv.reader`, `csv.writer` |
| `json` | JSON dosyaları | `json.load`, `json.dump` |
| `datetime` | Tarih ve zaman | `datetime.now()` |
| `os` | İşletim sistemi | `os.listdir` |

Bu hafta `csv` ve `json`'a odaklanacağız.

### import'un Üç Yazılış Şekli

```python
# 1. En temiz — modül adıyla erişim
import math
print(math.sqrt(64))

# 2. Sadece bir parçayı al
from math import sqrt, pi
print(sqrt(64))
print(pi)

# 3. Kısa ad ver (büyük modüllerde sık)
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
```

Şimdilik **birinci yazılışı** tavsiye ediyoruz: nereden geldiği belli olur. `random.choice(...)` yazınca "bu fonksiyon `random` modülünden geliyor" diye okunur.

> **Dosya:** `ornekler/05_modul_import.py`

---

## 5. CSV Dosyaları

Renk paletleri, font listeleri, fiyat tabloları — hepsi tablo şeklindedir. Tablolar için `.txt` yetmez. Onun yerine **CSV** (Comma-Separated Values, virgülle ayrılmış değerler) kullanırız:

```
isim,hex,grup
Mercan,#FF6B6B,sıcak
Lacivert,#1E3A8A,soğuk
Sarı,#FFD93D,sıcak
```

İlk satır genellikle **kolon başlıkları**dır. Sonraki her satır bir kayıttır.

### Tasarım Dünyasından Bir Benzetme

Adobe Color'da palet oluşturup "Export → CSV" yaptığınızda elinize böyle bir dosya geçer. Excel veya Numbers ile açabilirsiniz, ama bizim için **Python'la okumak** daha güçlü — çünkü filtreleyebilir, dönüştürebilir, başka formata yazabiliriz.

### Okuma

Python'un yerleşik `csv` modülünü kullanırız (önce `import csv`):

```python
import csv

with open("renkler.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    for satir in okuyucu:
        print(satir)   # ["Mercan", "#FF6B6B", "sıcak"] gibi liste
```

Her satır otomatik olarak bir **liste** halinde gelir. Liste indeksleriyle hücrelere erişiriz: `satir[0]` ilk hücre, `satir[1]` ikinci hücre.

### Başlık Satırını Atlama

Genelde ilk satırı (başlıklar) ayrı tutarız:

```python
with open("renkler.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    next(okuyucu)              # ilk satırı atla (başlıklar)
    for satir in okuyucu:
        isim = satir[0]
        hex_kod = satir[1]
        print(f"{isim}: {hex_kod}")
```

### Sözlüğe Çevirmek

Genelde her satırı bir sözlüğe çevirmek isteriz — kolon adlarına göre erişmek daha okunaklı:

```python
with open("renkler.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    next(okuyucu)
    renkler = []
    for satir in okuyucu:
        renk = {
            "isim": satir[0],
            "hex": satir[1],
            "grup": satir[2],
        }
        renkler.append(renk)
```

Şimdi `renkler` bir **sözlük listesi** — Hafta 4'ten tanıdığınız yapı.

> ↪ **Hata Refleksi:** `satir[3]` gibi olmayan bir indeks almaya çalışırsanız `IndexError` alırsınız (Bölüm 0'da listede yok ama mantığı tanıdık: "liste sınırını aştın").

> **Dosya:** `ornekler/06_csv_islemleri.py`

---

## 6. JSON Okuma ve Yazma

### JSON Nedir?

JSON (JavaScript Object Notation), bir veriyi metin olarak saklamanın yaygın bir yoludur. Sözlüklere ve listelere benzer:

```json
{
  "ad": "Caz Festivali",
  "tarih": "2026-06-15",
  "renkler": ["#FF6B6B", "#1E3A8A"],
  "yayinlandi": false
}
```

Python sözlüğüyle JSON neredeyse aynıdır. Tek fark: JSON'da:

- Anahtarlar **çift tırnak** olmak zorunda (Python'da tek tırnak da olabilir)
- `True/False/None` yerine `true/false/null` yazılır

### Tasarım Dünyasından Bir Benzetme

Bir InDesign projesinin "Document Setup" penceresi düşünün. Belge adı, sayfa boyutu, kenar boşlukları, kullanılan fontlar... Tüm bunlar bir yere kaydedilmek zorunda. JSON, bir tasarım projesinin **künye dosyasıdır**. Sözlük yapısı sayesinde okunabilir, başkalarına gönderilebilir, sonradan değiştirilebilir.

### Okuma

```python
import json

with open("proje.json", "r", encoding="utf-8") as dosya:
    proje = json.load(dosya)

print(proje["ad"])               # Caz Festivali
print(proje["renkler"][0])       # #FF6B6B
```

`json.load(dosya)` JSON dosyasını okur ve Python sözlüğüne çevirir. Sonra sözlük gibi kullanırsınız.

### Yazma

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

İki ekstra parametreye dikkat:

- `ensure_ascii=False` — Türkçe karakterler `ş` gibi escape kodlarına dönüştürülmesin, doğrudan "ş" olarak yazılsın
- `indent=2` — dosya okunabilir görünsün (2 boşluk girinti)

### Sözlük ↔ Dosya Köprüsü

JSON'un büyük gücü budur:

```
Python sözlüğü  ──json.dump──▶  JSON dosyası
JSON dosyası    ──json.load──▶  Python sözlüğü
```

Programınızı kapatsanız bile sözlüğünüzü dosyaya yazıp geri okuyabilirsiniz. Şimdiye kadar yapamadığımız tek şey buydu: **veriyi kalıcı tutmak**.

> ↪ **Hata Refleksi:** `proje["isim"]` gibi olmayan bir anahtarı sorarsanız `KeyError` alırsınız. JSON'dan gelen sözlüklerde anahtar adlarını dikkatli yazın.

> **Dosya:** `ornekler/07_json_islemleri.py`

---

## 7. Hata Mesajlarını (Traceback) Okuma

> Dersin başında "Ön Refleks: Hata Görünce Ne Yapılır?" bölümünde 5 hata tipinin **isimlerini** verdik. Şimdi her birini bir traceback ile inceliyoruz. O zamandan beri zaten bir-iki tanesini canlı yaşamış olmalısınız.

### Traceback Nedir?

Python kodunuz çalışırken bir sorunla karşılaşırsa **traceback** denilen uzun bir hata mesajı yazar. Çoğu öğrenci bunu görünce panikler ve kapatır. Ama traceback **size yardım etmek için yazılmıştır** — son satırını okumayı bilirseniz, hatanın nerede olduğunu söyler.

### Tasarım Dünyasından Bir Benzetme

InDesign'da "Missing fonts" uyarısı görürsünüz. Üç şeyi söyler:

1. Hangi font eksik (cinsi)
2. Hangi belgede (yer)
3. Ne yapmanız gerektiği (eylem)

Traceback de aynısını yapar — sadece daha teknik bir dille. Eksiltmeden okumak yerine **son satırına** odaklanın.

### Genel Kural

```
Traceback (most recent call last):
  File "kod.py", line 5, in <module>
    print(yas)
NameError: name 'yas' is not defined
```

Üç parça:

- **En alt satır** = hatanın **adı** ve **açıklaması** (`NameError: name 'yas' is not defined`)
- **"File ... line N"** satırı = hatanın **nerede** olduğu (`kod.py` dosyasının 5. satırı)
- En üstteki "Traceback" satırı genelde sadece "şimdi bir hata göstereceğim" demek — atlayın

### Sık Görülen 5 Hata

#### 1. `NameError: name 'X' is not defined`

Olmayan bir değişkeni kullandınız. Çoğu zaman:

- Değişken adını yanlış yazdınız (`renkler` yerine `renlker`)
- Değişkeni daha tanımlamadınız
- Fonksiyonun içindeki bir değişkeni dışarıda kullandınız

#### 2. `TypeError: can only concatenate str (not "int") to str`

Bir metin ile bir sayıyı toplamaya çalıştınız:

```python
yas = 20
print("Yaşım: " + yas)   # TypeError!
```

Çözüm: `str(yas)` ile dönüştürün, ya da f-string kullanın:

```python
print(f"Yaşım: {yas}")   # Çalışır
```

#### 3. `IndentationError: expected an indented block`

Girinti hatası. `if`, `for`, `def`, `while` satırından sonra **mutlaka girintili bir satır** olmalı:

```python
def selamla():
print("Merhaba")     # IndentationError — girintili olmalı!
```

#### 4. `FileNotFoundError: [Errno 2] No such file or directory: 'renkler.txt'`

Açmaya çalıştığınız dosya bulunamadı. Çoğu zaman:

- Dosya başka bir klasörde
- Terminal başka bir klasörden çalışıyor (`pwd` ile kontrol edin)
- Dosya adını yanlış yazdınız (`renkler.csv` yerine `renkler.txt`)

#### 5. `ModuleNotFoundError: No module named 'pillow'`

`import pillow` yazdınız ama paket kurulu değil:

- Standart kütüphane modülü ise (math, random, csv, json) — tipo yapmış olabilirsiniz
- Dış paket ise — `uv add pillow` ile kurun

### Okuma Refleksi

Bir traceback gördüğünüzde refleks olarak şunu yapın:

1. **En alt satıra bakın.** Hata adı ne? Mesaj ne?
2. **"File ... line N" satırına bakın.** Hatanın olduğu satıra gidin.
3. **O satırı okuyun.** Hata mesajıyla birleştirince çoğu zaman cevap orada.

> **Dosya:** `ornekler/08_traceback_okuma.py`

---

## 8. Yabancı Bir Kodu Okuma

### Neden Önemli?

Yakında bir yapay zeka aracı (Gemini gibi) ile birlikte kod yazacağız. Model size 20 satırlık bir kod verecek. İçinde belki şimdiye kadar görmediğiniz bir-iki yapı olacak. Sizin işiniz **kodu satır satır okuyup ne yaptığını anlamak**.

Bunu yapamazsanız, model size bir hata getirdiğinde ne kontrol edeceğinizi bilemezsiniz.

### Pasif ve Aktif Bilgi

Bir dilde iki düzeyde bilgi vardır:

- **Aktif** — siz konuşurken/yazarken kullanabildikleriniz
- **Pasif** — siz konuşmadığınız ama duyduğunuzda anladıklarınız

Şu ana kadar Python'un **aktif** kısmını öğrendik. Bu hafta birkaç **pasif** yapıyı tanıştırıyoruz. Yazmanız gerekmiyor — sadece görünce "ha, bu şu demek" diyebilmeniz yeterli.

### Tanıştığımız Üç Pasif Yapı

#### 1. Liste Anlama (List Comprehension)

```python
# Eskiden böyle yazıyorduk:
sonuc = []
for renk in renkler:
    if renk.startswith("#"):
        sonuc.append(renk.upper())

# Aynı iş tek satırda:
sonuc = [renk.upper() for renk in renkler if renk.startswith("#")]
```

İkinci satırı görünce paniklemeyin. Sağdan sola değil, **sıraya göre** okuyun:

- `for renk in renkler` — listeyi gez
- `if renk.startswith("#")` — sadece bu şarta uyanları al
- `renk.upper()` — her birinin büyük halini koy
- `[...]` — yeni listeye sar

#### 2. try / except — Hatayı Yakalama

```python
try:
    with open("renkler.txt", "r", encoding="utf-8") as f:
        icerik = f.read()
except FileNotFoundError:
    print("Dosya bulunamadı, varsayılan değerler kullanılacak.")
    icerik = ""
```

`try` bloğundaki kod hata verirse Python program çökmesin diye `except` bloğundaki kodu çalıştırır. Bu hafta yazmanızı beklemiyoruz; ama bir Gemini kodu içinde bunu görürseniz "burada bir hata kontrolü var" diye okuyabilmelisiniz.

#### 3. Tip İpuçları

```python
def alan_hesapla(en: float, boy: float) -> float:
    return en * boy
```

Parametre adlarından sonra `: float` yazıyor — "bu parametre `float` türünde olacak" demek. Sondaki `-> float` — "fonksiyon `float` döndürecek" demek.

Bunlar **opsiyonel notlar**. Python kodu bunlar olmadan da çalışır. Sadece okuyana ipucu verirler. Tip ipuçlarını yazmanızı beklemiyoruz, ama Gemini bunları bolca yazar — siz okurken paniklemeyin.

### Kod Okuma Alıştırması

`ornekler/09_kod_okuma.py` dosyasında, bu üç yapıyı içeren küçük bir VCD-temalı program var. Derste birlikte satır satır okuyup yorum yazacağız.

> **Dosya:** `ornekler/09_kod_okuma.py`

---

## Özet Tablosu

| Kavram | Ne yapar? | Örnek |
|--------|-----------|-------|
| `cd`, `ls`, `pwd` | Terminal navigasyonu | `cd hafta8`, `ls` |
| `python3 dosya.py` | Bir Python dosyasını çalıştırır | `python3 01_terminal.py` |
| `uv init`, `uv add`, `uv run` | Proje ve paket yönetimi | `uv add pillow` |
| `pyproject.toml` | Projenin künye dosyası | bağımlılıkları listeler |
| `with open(...) as f:` | Dosyayı güvenli açma | `f.read()`, `f.write()` |
| `encoding="utf-8"` | Türkçe karakter desteği | her dosyada yazın |
| `csv.reader / csv.writer` | CSV dosyalarını okuma/yazma | `import csv` |
| `json.load / json.dump` | JSON dosyaları | sözlük ↔ dosya |
| `import math` | Modül etkinleştirme | `math.sqrt(64)` |
| Traceback son satırı | Hata adı + açıklama | `NameError: name 'x' is not defined` |

---

## Sık Yapılan Hatalar

### 1. Dosyayı yanlış klasörde aramak  ↪ `FileNotFoundError`

```python
with open("renkler.txt", "r", encoding="utf-8") as f:
    ...
# FileNotFoundError!
```

Terminalde `pwd` (Linux/Mac) veya `cd` (Windows) yazıp şu an hangi klasörde olduğunuzu görün. Dosya o klasörde mi? Değilse ya dosyayı oraya taşıyın ya da yolu uzatın: `"veri/renkler.txt"`.

### 2. encoding yazmamak  ↪ Hatadan önce gelir — Türkçe karakter bozulur, ama traceback vermez

```python
with open("dosya.txt", "r") as f:    # encoding eksik!
    ...
```

Windows'ta Türkçe karakterler bozulur. Her dosyada `encoding="utf-8"` yazın, alışkanlık olsun.

### 3. "w" modunu yanlışlıkla kullanmak  ↪ Hata vermez — sessizce dosyanı silip baştan yazar

```python
with open("renkler.txt", "w", encoding="utf-8") as f:
    f.write("yeni şey")
```

Eğer `renkler.txt` daha önce vardıysa, **içindeki her şey silindi**. Önce okumak istiyorsanız `"r"`, sonuna eklemek istiyorsanız `"a"`, sıfırdan yazmak istiyorsanız `"w"`. Karıştırmayın.

### 4. JSON yazarken Türkçe karakterler "\u" oluyor

```python
json.dump(proje, dosya)
# Çıktı: {"ad": "Caz Festivali", "yer": "İstanbul"}
# (Türkçe "İ" harfi İ olarak escape edilmiş — okunmaz)
```

Çözüm: `ensure_ascii=False` ekleyin.

```python
json.dump(proje, dosya, ensure_ascii=False, indent=2)
# Çıktı: {"ad": "Caz Festivali", "yer": "İstanbul"}
# (artık doğrudan Türkçe karakterler)
```

### 5. import'u dosyanın içinde yazmak  ↪ Çalışır ama alışkanlık olmasın

```python
def renk_sec():
    import random            # Çalışır ama alışkanlık olmasın
    return random.choice(...)
```

Tüm `import` ifadelerini **dosyanın en başına** koyun. Photoshop'ta plugin yüklemek gibi: programın başında bir kez yapılır.

### 6. Modül adıyla aynı isimli dosya açmak  ↪ `AttributeError` veya `ModuleNotFoundError` olabilir

```
my_project/
  json.py        # ← BU İSİM YANLIŞ!
  main.py
```

Eğer dosyanızı `json.py` veya `random.py` olarak isimlendirirseniz, Python sizin dosyanızı standart modülün önüne geçirir. `import json` yazdığınızda kendi boş dosyanızı yükler. Sonra "AttributeError" alırsınız.

Çözüm: dosya adlarınız standart modüllerle çakışmasın.

### 7. uv add ile uv run karıştırmak  ↪ `ModuleNotFoundError`

- `uv add pillow` — paketi projeye **ekler**. Bir kez yapılır.
- `uv run main.py` — programı **çalıştırır**. Her seferinde yapılır.

Yeni paket eklediniz, çalıştırıyorsunuz ama paket bulunamadı? Büyük olasılıkla `uv run` yerine düz `python` kullandınız. Sanal ortamı atladınız.

---

## Ödevler Hakkında

Bu haftanın 5 ödevi var:

| Ödev | Zorluk | Konu |
|------|--------|------|
| Ödev 1 — Terminal & uv Setup | Kolay | Terminal komutları + `uv init` + belgeleme |
| Ödev 2 — Tasarım Brifi Yazma | Kolay-Orta | input + f-string + dosya yazma/okuma |
| Ödev 3 — Renk Paleti Okuma | Orta | `with open()` + döngü + sözlükle sayma |
| Ödev 4 — Proje Künyesi (JSON) | Orta | `json.dump` + `json.load` + sözlük |
| Ödev 5 — CSV'den JSON'a Köprü | Zor | Hepsi bir arada + 4 fonksiyon yazımı |

Bu hafta 1. ödev biraz farklı: kod yazmak yerine bir kurulum yapacaksınız ve sonucu bir metin dosyasında belgeleyeceksiniz. Diğer ödevler `...` ile boşluklu Python dosyalarıdır — şimdiye kadar yaptığınız gibi doldurup çalıştıracaksınız.

Tüm ödevler `hafta8/odevler/` klasöründedir. `odevler/BENIOKU.md` dosyası nasıl çalıştırılacağını anlatır.

---

## Ek Bölümler: try/except ve Class

Aşağıdaki bölümler vibecoding hazırlığı için kritik iki konuyu kapsar. Gemini'nin ürettiği kodun neredeyse tamamında bu iki yapı var — okuyup anlayabilmek için buradalar.

---

## Ek Bölüm 1 — try / except Temelleri

### Hata Almak Normaldir

Şimdiye kadar bir hata aldığınızda programınız çökerdi. Traceback gelir, kırmızı yazı görünür, program orada biter. **Bu hep böyle olmak zorunda değil.**

Bazen biz **hata olabileceğini önceden biliyoruz** ve programın çökmesini istemiyoruz. Örneğin:

- Kullanıcı bir sayı yerine "abc" yazabilir
- Dosya o klasörde olmayabilir
- İnternete bağlanılamayabilir

Bu durumlarda Python'a "olur ki bir hata çıkarsa şunu yap" diyebiliriz. Bunun adı **try / except** bloğudur.

### Tasarım Dünyasından Bir Benzetme

InDesign'da bir belge açtığınızda "Missing fonts" uyarısı geldiğinde program kapanmaz. Bir diyalog kutusu açılır: "şu fontlar yok, ne yapmak istersin?" InDesign **hata aldı** ama **çökmedi** — sizinle konuştu.

`try / except` aynı şey. "Bu kod çökerse, onu yakala ve şu davranışı göster." Bir tasarım yazılımının **hata diyaloğu** gibi.

### En Basit Hali

```python
try:
    sayi = int("mercan")          # Bu satır ValueError fırlatır
    print("Çevirdim:", sayi)
except ValueError:
    print("Bu metin sayıya dönüşmüyor.")
```

Çıktı:
```
Bu metin sayıya dönüşmüyor.
```

İki blok var:

- `try:` — "şunu denemek istiyorum" bloğu
- `except ValueError:` — "eğer ValueError çıkarsa şunu yap" bloğu

Eğer try bloğu sorunsuz biterse, except bloğu çalıştırılmaz. Eğer try bloğu hata fırlatırsa, Python derhal except bloğuna atlar.

### Birden Fazla except Bloğu

```python
renkler = ["#FF6B6B", "#1E3A8A", "#FFD93D"]

try:
    secim = int("2")              # ValueError olasılığı
    print("Renk:", renkler[secim]) # IndexError olasılığı
except ValueError:
    print("Geçerli bir sayı vermedin.")
except IndexError:
    print("Bu indekste renk yok.")
```

### else ve finally

```python
try:
    deger = int("128")
except ValueError:
    print("Çevrim başarısız.")
else:
    print(f"Çevrim başarılı: {deger}")   # SADECE hata olmadıysa çalışır
finally:
    print("Bu satır HER DURUMDA çalışır.")
```

- `else` — try sorunsuz biterse çalışır
- `finally` — hata olsun ya da olmasın çalışır (dosya kapatma gibi temizlik işleri için)

### Hata Mesajını Yakalama

```python
try:
    sonuc = 10 / 0
except ZeroDivisionError as e:
    print("Python ne diyor?:", e)
# Çıktı: Python ne diyor?: division by zero
```

### Sık Yapılan Hatalar ↪ TypeError

| Hata | Sebep | Çözüm |
|---|---|---|
| try bloğu hiç çalışmıyor | Yanlış girinti | İçeride en az bir satır olsun, doğru girintide |
| except yakalanmıyor | Yanlış hata tipi yazdınız | Tracebackten doğru tipi okuyun |
| Sadece `except:` yazmak | Çok geniş — sessizce bug'ları gizler | Spesifik tip yazın (`except ValueError`) |

> ↪ **Vibecoding Bağlantısı:** Gemini size try/except'li bir kod verirse hangi hata tipini yakaladığını okuyabilmelisiniz.

> **Dosya:** `ornekler/10_try_except_temel.py`

---

## Ek Bölüm 2 — try / except ile Dosya ve Kullanıcı Girişi

### 2.1 Dosya İşlemleri — FileNotFoundError

```python
try:
    with open("musteri_paleti.txt", "r", encoding="utf-8") as dosya:
        icerik = dosya.read()
    print(icerik)
except FileNotFoundError:
    print("Müşteri paleti dosyası yok. Varsayılan renklerle devam ediliyor.")
```

**EAFP felsefesi:** "Önce dosyayı kontrol et, varsa aç" yerine **doğrudan dene, hata olursa yakala**. Python'da bu deseni tercih ederiz.

### "Yoksa Varsayılan" Deseni

```python
varsayilan_renkler = ["#000000", "#FFFFFF"]

try:
    with open("musteri.txt", "r", encoding="utf-8") as dosya:
        renkler = [satir.strip() for satir in dosya]
except FileNotFoundError:
    renkler = varsayilan_renkler
    print("Dosya yok, varsayılan siyah-beyaz kullanıldı.")
```

### 2.2 Kullanıcı Girdisi — ValueError

```python
ham = input("Bir RGB değeri gir (0-255): ")
try:
    deger = int(ham)
    print("Geçerli:", deger)
except ValueError:
    print("Sayı bekliyordum, metin geldi.")
```

### "Geçerli Girdi Alana Kadar Sor" Deseni

```python
while True:
    ham = input("Sayfa sayısı gir (>0): ")
    try:
        sayfa = int(ham)
        if sayfa <= 0:
            print("Sıfırdan büyük olmalı.")
            continue
        break                       # geçerli girdi — döngüden çık
    except ValueError:
        print("Sayı yazmalısın.")

print(f"{sayfa} sayfa.")
```

> ↪ **Vibecoding Bağlantısı:** Gemini "kullanıcıdan sayı al" derken neredeyse her zaman bu `while True + try/except` desenini üretir.

> **Dosyalar:** `ornekler/11_try_except_dosya.py`, `ornekler/12_try_except_kullanici.py`

---

## Ek Bölüm 3 — Sınıflar (class) Derinleşme

### Hatırlatma

Derste hızlıca `Dikdortgen` sınıfını görmüştük — hoca yazdı, siz izlediniz. Bu bölümde **siz yazacaksınız**.

### Sınıf Nedir?

Bir sınıf, **kendi veri tipinizi tasarlama** aracıdır. Python'da hazır tipler var: `int`, `str`, `list`, `dict`. Ama bazen kendinize özel bir tip lazım — bir `Palet`, bir `Renk`, bir `Font`, bir `Brif`.

Sınıf bir **kalıp**tır. Bir poster mockup'ı düşünün — boş şablon. Gerçek poster yapmak için mockup'ı kopyalayıp içine içerik koyarsınız.

- **Sınıf** = mockup (kalıp)
- **Nesne (instance)** = mockup'tan üretilen gerçek poster

```python
class Palet:                       # ← Bu KALIP
    def __init__(self, isim, renkler):
        self.isim = isim
        self.renkler = renkler

# Kalıptan iki nesne yarat:
sicak = Palet("Yaz", ["#FF6B6B", "#FFD93D"])
soguk = Palet("Kış", ["#1E3A8A", "#3B82F6"])

print(sicak.isim)         # Yaz
print(soguk.isim)         # Kış
```

### `__init__` ve `self`

`__init__` nesne yaratılırken otomatik çalışan **yapıcı (constructor)**dır. `self` her metodun ilk parametresidir — "bu nesnenin kendisi" demek. Çağırırken `self`'i **yazmazsınız**.

### Tam Bir Örnek

```python
class Palet:
    def __init__(self, isim: str, renkler: list):
        self.isim = isim
        self.renkler = renkler

    def renk_ekle(self, renk: str):
        self.renkler.append(renk)

    def renk_sayisi(self) -> int:
        return len(self.renkler)

    def birincil(self) -> str:
        return self.renkler[0]

    def bilgi_ver(self):
        print(f"Palet: {self.isim}")
        print(f"  Renk sayısı: {self.renk_sayisi()}")
        print(f"  Birincil renk: {self.birincil()}")


sicak = Palet("Yaz Sıcağı", ["#FF6B6B", "#FFD93D", "#FF8C42"])
sicak.renk_ekle("#E63946")
sicak.bilgi_ver()
```

### Sınıf + JSON — Vibecoding'de En Çok Görülecek Desen

```python
import json

class Palet:
    def __init__(self, isim, renkler):
        self.isim = isim
        self.renkler = renkler

    def to_dict(self):
        return {"isim": self.isim, "renkler": self.renkler}

# Kaydet
orijinal = Palet("Bahar", ["#A8DADC", "#E63946"])

try:
    with open("palet.json", "w", encoding="utf-8") as dosya:
        json.dump(orijinal.to_dict(), dosya, ensure_ascii=False, indent=2)
except PermissionError:
    print("Yazma izni yok.")

# Geri yükle
try:
    with open("palet.json", "r", encoding="utf-8") as dosya:
        sozluk = json.load(dosya)
    geri_yuklenen = Palet(sozluk["isim"], sozluk["renkler"])
    print(f"Yüklendi: {geri_yuklenen.isim}")
except FileNotFoundError:
    print("Palet dosyası yok.")
```

Dört şeyi birden kullanan tam vibecoding deseni: `class` + `to_dict()` + `json.dump/load` + `try/except`.

### Sık Yapılan Hatalar ↪ AttributeError / TypeError

| Hata | Sebep | Çözüm |
|---|---|---|
| `AttributeError: 'Palet' object has no attribute 'X'` | `__init__` içinde `self.X = ...` yazmayı unuttun | `__init__`'i kontrol et |
| `TypeError: __init__() missing 1 required positional argument` | Nesne yaratırken parametre eksik | Tüm parametreleri ver |
| `self.metot_adi()` yerine `metot_adi()` | `self.` unutuldu | Hep `self.` ile başlat |
| Metoda `self` koymayı unutmak | `def alan():` yerine `def alan(self):` | Her metodun ilk parametresi `self` |

> ↪ **Vibecoding Bağlantısı:** Gemini size "müşteri brifi yöneten bir sınıf yaz" diyene kadar 5 dakika sürmez. Onun `__init__`'ini okuyamazsanız sınıfı kullanamazsınız.

> **Dosyalar:** `ornekler/13_class_palet.py`, `ornekler/14_class_ve_dosya.py`

---

## Ek Bölüm 4 — Yabancı Kod Okuma Atölyesi (Genişletilmiş)

`ornekler/15_yabanci_kod_atolye.py` dosyasında 6 snippet var. Her birinin başında:

```python
# === SNIPPET X ===
# Bu kodu Gemini verdi. Ne yapıyor?
```

Sınıfta yapacağınız: snippet'i okuyun → "ne yapar?" sorusunu cevaplayın → çalıştırın → doğrulayın.

### Bu Snippetlerde Geçen Yapılar

| Yapı | Nerede gördük? | Aktif/Pasif? |
|---|---|---|
| List comprehension | H8 | Pasif tanıma |
| `try / except` | Ek Bölüm 1-2 | Aktif |
| `class` | Ek Bölüm 3 | Aktif |
| `sorted` + `lambda` | Bu bölüm | Pasif tanıma |
| `requests.get()` | H8 | Hatırlama |
| `if __name__ == "__main__":` | Bu bölüm | Pasif tanıma |

### Yeni Pasif Yapılar — Sadece Tanıyın

**`sorted` + `lambda`:**
```python
projeler = [{"ad": "A", "butce": 1000}, {"ad": "B", "butce": 5000}]
sirali = sorted(projeler, key=lambda p: p["butce"], reverse=True)
```
`lambda` "tek satırlık adsız fonksiyon". Sadece okuyup "bütçeye göre sıralıyor" diyebilmeniz yeterli.

**`if __name__ == "__main__":`:**
```python
def selamla(isim):
    print(f"Merhaba {isim}")

if __name__ == "__main__":
    selamla("Defne")
```
"Bu dosya doğrudan çalıştırılırsa başlangıç noktası burası" demek. Şimdilik sadece tanıyın.

> **Dosya:** `ornekler/15_yabanci_kod_atolye.py`

---

## Bir Sonraki Adım

Önümüzdeki hafta (Hafta 9) Gemini ile **vibecoding** yapacağız — yapay zekanın ürettiği koda komuta etmeyi öğreneceğiz.

Konuları kavramak için:

1. Ders dosyalarını (`ornekler/`) sırayla açıp çalıştırın
2. Terminalde `pwd`, `ls`, `cd` komutlarını kendi bilgisayarınızda deneyin
3. `uv` kurulumunu mutlaka derste değil, **evde** sakince yapın
4. Ödevleri sırayla çözün — takılırsanız ders notuna geri dönün
