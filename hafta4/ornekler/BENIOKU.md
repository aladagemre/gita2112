# GİTA 2112 — Hafta 4: Sözlükler ve Break/Continue

Bu klasördeki dosyalar, derste birlikte işlediğimiz konuları sıralı bir şekilde içermektedir. Her dosyayı açıp çalıştırın, kodları okuyun, yorumları dikkatlice inceleyin.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Dosyayı VS Code'da açın (örnek: `01_sozlukler.py`)
2. Sağ üstteki **Run** düğmesine tıklayın
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
python3 03_hepsi_bir_arada.py
python3 04_getpass.py
```

> **Not:** `input()` kullanan programlar (02, 04) sizden klavyeyle bilgi girmenizi bekler. Terminale yazıp Enter'a basın.

---

## Dosyalar ve Konular

| Dosya | Konu |
|-------|------|
| `01_sozlukler.py` | Sözlük `{}`, anahtar-değer, `.items()` |
| `02_break_continue.py` | `break` ile döngü durdurma, `continue` ile atlama |
| `03_hepsi_bir_arada.py` | Liste + sözlük + döngü + continue birleşik örnek |
| `04_getpass.py` | Bonus: `getpass` ile şifre girişi, 3 deneme hakkı |

---

## Bu Derslerin Sonunda Neler Yapabilmelisiniz?

### Sözlükler
Anahtar-değer çifti mantığını kavramış olmalısınız. Sözlük oluşturup değer okuyabilmeli, yeni çift ekleyebilmeli ve `.items()` ile döngü kurabilmelisiniz.

### break ve continue
`break` ile döngüyü tamamen durdurabilmeli, `continue` ile belirli turları atlayabilmelisiniz. `while True` + `break` kalıbıyla kullanıcıdan tekrar tekrar giriş alabilmelisiniz.

### Birleşik Kullanım
Tüm bu konuları bir arada kullanarak küçük uygulamalar (proje takip sistemi) oluşturabilmelisiniz.

---

## Bir Sonraki Adım

Bu konuları kavradıysanız harika! Gelecek hafta f-string formatlama, matematik işlemleri ve tip dönüşümleri öğreneceksiniz. Şimdilik buradakileri iyice pekiştirmeniz yeterli.
