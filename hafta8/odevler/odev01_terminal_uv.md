# ÖDEV 1 — Terminal ve uv Kurulumu  [Kolay]

Bu ödev kod yazmak değildir. Bilgisayarınıza `uv` aracını kuracak, basit bir proje oluşturacak ve attığınız adımları bir metin dosyasında belgeleyeceksiniz.

**Konu:** Terminal kullanımı + `uv init` + `uv add` + dosya belgeleme
**Kazanım:** Bir Python projesini sıfırdan başlatmayı bilmek.

---

## Görev 1 — uv'yi Kur

Terminali açın (VS Code → Terminal → New Terminal):

**macOS / Linux için:**
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell) için:**
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Kurulumdan sonra **terminali kapatıp tekrar açın**, sonra şunu deneyin:

```
uv --version
```

Bir sürüm numarası (örnek: `uv 0.5.x`) görmelisiniz.

> Sorun yaşarsanız: kurulum çıktısının son satırlarına bakın, çoğu zaman "kapatıp aç" der. Hala olmazsa derste hocaya gösterin.

---

## Görev 2 — Yeni Bir Proje Oluştur

Belgelerinize gidin ve yeni bir uv projesi başlatın:

**Mac / Linux:**
```
cd ~/Documents
uv init odev1_proje
cd odev1_proje
```

**Windows:**
```
cd C:\Users\KULLANICI_ADINIZ\Documents
uv init odev1_proje
cd odev1_proje
```

Şimdi `ls` (Windows'ta `dir`) yazıp neler oluştuğunu görün. En az şu dosyalar olmalı:

- `pyproject.toml`
- `main.py`
- `README.md`

---

## Görev 3 — Bir Paket Ekle

`requests` adlı paketi projeye ekleyin:

```
uv add requests
```

Bu komut çıktısının son satırlarında "Added requests" gibi bir mesaj göreceksiniz.

---

## Görev 4 — pyproject.toml'u Aç

VS Code'da `pyproject.toml` dosyasını açın. İçeriği şuna benzer olmalı:

```toml
[project]
name = "odev1-proje"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.32.0",
]
```

Bu içeriği kopyalayın — bir sonraki adımda kullanacaksınız.

---

## Görev 5 — Programı Çalıştır

Aynı klasörde `main.py` dosyasını açın. İçinde şuna benzer bir kod olur:

```python
def main():
    print("Hello from odev1-proje!")


if __name__ == "__main__":
    main()
```

Şimdi terminalde:

```
uv run main.py
```

Çıktıda `Hello from odev1-proje!` görmelisiniz. Tebrikler — ilk uv projeniz çalıştı.

---

## Görev 6 — Belgeleyin

Aynı klasörde `kurulum_notlari.txt` adında bir metin dosyası oluşturun (VS Code → New File). İçine şu bilgileri yazın:

```
=== uv Kurulum Notları ===

İşletim sistemim: ___________ (macOS / Windows / Linux)
uv versiyonu: ___________ (uv --version çıktısından)

--- Görev 2: Proje oluşturuldu ---
Proje klasörü: ___________
ls çıktısı:
___________
___________

--- Görev 3: requests paketi eklendi ---
Komut çıktısının son satırı:
___________

--- Görev 4: pyproject.toml içeriği ---
[Buraya pyproject.toml dosyasının tam içeriğini kopyala-yapıştır]

--- Görev 5: main.py çıktısı ---
___________

--- Notlar / yaşadığım zorluklar ---
___________
___________
```

Boş bırakılmış yerleri kendi sisteminizden gelen bilgilerle doldurun.

---

## Teslim

Bu ödev için 2 dosya teslim edeceksiniz:

1. `kurulum_notlari.txt` — yukarıda doldurduğunuz dosya
2. `pyproject.toml` — projenizdeki dosya

Bu iki dosyayı bir klasöre koyup zip yapın, derste paylaşılan klasöre yükleyin.

---

## Yardım

Takıldığınız her yerde:

1. Hata mesajının **son satırını** okuyun
2. O mesajı kopyalayıp Google'da arayın
3. Hala olmadıysa derste hocaya gösterin

> Bu ödev hata yaşamak için tasarlanmıştır. Korkmayın — terminal hatası ölümcül değildir, sadece can sıkar.
