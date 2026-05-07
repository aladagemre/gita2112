# GİTA 2112 — Hafta 8: Çevre, Dosya, Kod Okuma

Bu klasördeki dosyalar, derste birlikte işlediğimiz konuları sıralı bir şekilde içermektedir. Her dosyayı açıp çalıştırın, kodları okuyun, yorumları dikkatlice inceleyin.

Bu hafta diğer haftalardan bir farkı var: bazı dosyalar **çalıştırılmak için değil, okunmak için** yazıldı. Özellikle `01_terminal_temelleri.py` ve `02_uv_kullanimi.py` daha çok bir rehber gibidir — içlerindeki komutları kendi terminalinizde denemelisiniz, dosyayı doğrudan çalıştırmak yeterli değildir.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Dosyayı VS Code'da açın (örnek: `03_dosya_okuma.py`)
2. Sağ üstteki **Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code üst menüden **Terminal → New Terminal** tıklayın, ardından şu komutu yazın:

```
cd hafta8/ornekler
python3 03_dosya_okuma.py
```

Dosya adını değiştirerek diğer dersleri de çalıştırabilirsiniz:

```
python3 04_dosya_yazma.py
python3 05_modul_import.py
python3 06_csv_islemleri.py
python3 07_json_islemleri.py
```

> **Windows için:** `python3` yerine sadece `python` yazmanız gerekebilir.

---

## Dosyalar ve Konular

| Dosya | Konu | Çalıştırılır mı? |
|-------|------|------------------|
| `01_terminal_temelleri.py` | Terminal komutları rehberi | Hayır — okuma + terminalde dene |
| `02_uv_kullanimi.py` | `uv init`, `uv add`, `uv run` rehberi | Hayır — okuma + terminalde dene |
| `03_dosya_okuma.py` | `with open()`, `read`, satır satır okuma | Evet |
| `04_dosya_yazma.py` | Yazma, append, encoding | Evet |
| `05_modul_import.py` | `math`, `random`, `datetime`, `os` turu | Evet |
| `06_csv_islemleri.py` | `csv.reader` ile renk paleti tablosu | Evet |
| `07_json_islemleri.py` | `json.load`, `json.dump`, sözlük ↔ dosya | Evet |
| `08_traceback_okuma.py` | 5 farklı hata tipini görme | Evet — hata verir, normal! |
| `09_kod_okuma.py` | Kod okuma alıştırması | Evet — ama önce yorumları yazın |

---

## Yardımcı Veri Dosyaları

`veri/` alt klasöründe ders boyunca okunacak hazır dosyalar var:

- `renkler.txt` — satır satır renk isimleri
- `renkler.csv` — virgülle ayrılmış renk paleti tablosu
- `proje.json` — örnek bir proje künyesi

Bu dosyalara dokunmanıza gerek yok; ders kodları otomatik okuyor. Yine de açıp formata bakmanızı tavsiye ederiz.

> **Not:** Ders sırasında bazı örnekler **yeni dosyalar oluşturur** (örn. `yeni_palet.txt`, `proje_guncel.json`, `notlar.txt`, `sicak_palet.csv`). Klasörünüz biraz dolacak — bu normal. Sonradan istemediklerinizi silebilirsiniz; `git` kullanıyorsanız zaten `.gitignore` ile yok sayılırlar.

---

## Bu Derslerin Sonunda Neler Yapabilmelisiniz?

### Terminal Kullanımı
Terminal penceresini açabilmeli, bulunduğunuz klasörü görebilmeli (`pwd`/`cd`), klasör içeriğini listeleyebilmeli (`ls`/`dir`), ve bir Python dosyasını terminalden çalıştırabilmelisiniz.

### uv ile Proje Yönetimi
Yeni bir Python projesi oluşturabilmeli (`uv init`), bir paket ekleyebilmeli (`uv add`), ve `uv run` ile dosyanızı çalıştırabilmelisiniz. `pyproject.toml` dosyasını açıp anlayabilmelisiniz.

### Dosya Okuma ve Yazma
`with open(...)` deyimini doğru yazabilmeli, okuma/yazma/append modlarını ayırt edebilmeli, satır satır dosya gezebilmeli, ve `encoding="utf-8"` parametresini her zaman ekleyebilmelisiniz.

### CSV ve JSON
`csv` modülüyle bir tabloyu satır satır okuyabilmeli, `json.load` ile bir dosyayı sözlüğe çevirebilmeli, `json.dump` ile bir sözlüğü dosyaya yazabilmelisiniz.

### Modüller
`import` ifadesinin ne yaptığını açıklayabilmeli, `math` ve `random` modüllerinden basit fonksiyonlar çağırabilmelisiniz.

### Hata Mesajlarını Okuma
Bir traceback gördüğünüzde paniklemeden son satırına bakabilmeli, hatanın hangi dosya ve satırda olduğunu okuyabilmeli, en sık 5 hata tipinin (NameError, TypeError, IndentationError, FileNotFoundError, ModuleNotFoundError) ne anlama geldiğini bilmelisiniz.

### Kod Okuma
Yabancı bir kodu satır satır okuyabilmeli, list comprehension ve `try/except` gibi henüz yazmadığınız ama göreceğiniz yapıları **anlama düzeyinde** çözebilmelisiniz.

---

## Bir Sonraki Adım

Bu hafta öğrendikleriniz, programlama becerinizden çok **bir Python kullanıcısı olma** becerinizi geliştirir. Önümüzdeki haftalarda yapay zeka destekli kod üretiminde size yardımcı olacak. Şimdilik bu rahatlığa kavuşmaya odaklanın: dosyalarla çalışmak, hata mesajlarını okumak, terminali kullanmak.
