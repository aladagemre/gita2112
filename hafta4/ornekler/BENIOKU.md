# GİTA 2112 — Hafta 4: Sözlükler, Break/Continue, F-String, Matematik

Bu klasördeki dosyalar, derste birlikte işlediğimiz konuları sıralı bir şekilde içermektedir. Her dosyayı açıp çalıştırın, kodları okuyun, yorumları dikkatlice inceleyin.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Dosyayı VS Code'da açın (örnek: `01_sozlukler.py`)
2. Sağ üstteki **▶ Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code üst menüden **Terminal → New Terminal** tıklayın, ardından şu komutu yazın:

```
cd hafta4/ornekler
python3 01_sozlukler.py
```

Dosya adını değiştirerek diğer dersleri de çalıştırabilirsiniz:

```
python3 02_break_continue.py
python3 03_fstring.py
python3 04_matematik.py
python3 05_hepsi_bir_arada.py
python3 06_getpass.py
```

> **Not:** `input()` kullanan programlar (02, 04, 05, 06) sizden klavyeyle bilgi girmenizi bekler. Terminale yazıp Enter'a basın.

---

## Dosyalar ve Konular

| Dosya | Konu |
|-------|------|
| `01_sozlukler.py` | Sözlük `{}`, anahtar-değer, `.items()` |
| `02_break_continue.py` | `break` ile döngü durdurma, `continue` ile atlama |
| `03_fstring.py` | f-string formatlama, sayı formatı, string metodları |
| `04_matematik.py` | Aritmetik operatörler, tip dönüşümleri, `round()`, `abs()` |
| `05_hepsi_bir_arada.py` | Liste + sözlük + döngü + f-string + continue birleşik örnek |
| `06_getpass.py` | Bonus: `getpass` ile şifre girişi, 3 deneme hakkı |

---

## Bu Derslerin Sonunda Neler Yapabilmelisiniz?

### Sözlükler
Anahtar-değer çifti mantığını kavramış olmalısınız. Sözlük oluşturup değer okuyabilmeli, yeni çift ekleyebilmeli ve `.items()` ile döngü kurabilmelisiniz.

### break ve continue
`break` ile döngüyü tamamen durdurabilmeli, `continue` ile belirli turları atlayabilmelisiniz. `while True` + `break` kalıbıyla kullanıcıdan tekrar tekrar giriş alabilmelisiniz.

### f-string
Değişkenleri ve ifadeleri `f"..."` ile metin içine gömebilmelisiniz. `:.1f` ile ondalık basamak, `:,.2f` ile binlik ayraç formatlayabilmelisiniz.

### Matematik ve Tip Dönüşümleri
Tüm aritmetik operatörleri (`+`, `-`, `*`, `/`, `//`, `%`, `**`) kullanabilmeli, `int()` ve `float()` ile tip dönüşümü yapabilmelisiniz. `round()` ile yuvarlama, `abs()` ile mutlak değer alabilmelisiniz.

### Birleşik Kullanım
Tüm bu konuları bir arada kullanarak küçük uygulamalar (portfolyo yöneticisi, hesap makinesi) oluşturabilmelisiniz.

---

## Bir Sonraki Adım

Bu konuları kavradıysanız harika! İlerleyen haftalarda fonksiyonlar, dosya işlemleri ve daha karmaşık veri yapılarıyla tanışacaksınız. Şimdilik buradakileri iyice pekiştirmeniz yeterli.
