# GİTA 2112 — Hafta 5: F-String, Matematik ve Tip Dönüşümleri

Bu klasördeki dosyalar, derste birlikte işlediğimiz konuları sıralı bir şekilde içermektedir. Her dosyayı açıp çalıştırın, kodları okuyun, yorumları dikkatlice inceleyin.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Dosyayı VS Code'da açın (örnek: `01_fstring.py`)
2. Sağ üstteki **Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code üst menüden **Terminal → New Terminal** tıklayın, ardından şu komutu yazın:

```
cd hafta5/ornekler
python3 01_fstring.py
```

Dosya adını değiştirerek diğer dersleri de çalıştırabilirsiniz:

```
python3 02_matematik.py
python3 03_hepsi_bir_arada.py
```

> **Not:** `input()` kullanan programlar (02) sizden klavyeyle bilgi girmenizi bekler. Terminale yazıp Enter'a basın.

---

## Dosyalar ve Konular

| Dosya | Konu |
|-------|------|
| `01_fstring.py` | f-string formatlama, sayı formatı, string metodları |
| `02_matematik.py` | Aritmetik operatörler, tip dönüşümleri, `round()`, `abs()` |
| `03_hepsi_bir_arada.py` | Liste + sözlük + döngü + f-string + continue birleşik örnek |

---

## Bu Derslerin Sonunda Neler Yapabilmelisiniz?

### f-string
Değişkenleri ve ifadeleri `f"..."` ile metin içine gömebilmelisiniz. `:.1f` ile ondalık basamak, `:,.2f` ile binlik ayraç formatlayabilmelisiniz.

### Matematik ve Tip Dönüşümleri
Tüm aritmetik operatörleri (`+`, `-`, `*`, `/`, `//`, `%`, `**`) kullanabilmeli, `int()` ve `float()` ile tip dönüşümü yapabilmelisiniz. `round()` ile yuvarlama, `abs()` ile mutlak değer alabilmelisiniz.

### Birleşik Kullanım
Tüm bu konuları önceki haftaların konularıyla bir arada kullanarak küçük uygulamalar (portfolyo yöneticisi, hesap makinesi) oluşturabilmelisiniz.

---

## Bir Sonraki Adım

Bu konuları kavradıysanız harika! Gelecek hafta **fonksiyonlar** öğreneceksiniz — kendi yeniden kullanılabilir kod bloklarınızı oluşturabileceksiniz. Şimdilik buradakileri iyice pekiştirmeniz yeterli.
