# GİTA 2112 — Python'a Giriş

Bu klasördeki dosyalar, derste birlikte işlediğimiz konuları sıralı bir şekilde içermektedir. Her dosyayı açıp çalıştırın, kodları okuyun, yorumları dikkatlice inceleyin.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Dosyayı VS Code'da açın (örnek: `01_merhaba.py`)
2. Sağ üstteki **▶ Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code üst menüden **Terminal → New Terminal** tıklayın, ardından şu komutu yazın:

```
cd hafta2/ornekler
python3 01_merhaba.py
```

Dosya adını değiştirerek diğer dersleri de çalıştırabilirsiniz:

```
python3 02_degiskenler.py
python3 03_hosgeldin.py
```

> **Not:** `input()` kullanan programlar (03 ve sonrası) sizden klavyeyle bilgi girmesini bekler. Terminale yazıp Enter'a basın.

---

## Dosyalar ve Konular

| Dosya | Konu |
|-------|------|
| `01_merhaba.py` | `print()`, string, temel aritmetik |
| `02_degiskenler.py` | Değişken tanımlama, veri tipleri |
| `03_hosgeldin.py` | `input()` ile kullanıcıdan veri alma |
| `04_deneme.py` | Çoklu `input()`, `int()` dönüşümü |
| `05_giris.py` | `if / else`, `and` operatörü |
| `06_puan.py` | `if / elif / else` zinciri |
| `07_ehliyet.py` | Boolean değişkenler, iç içe `if` |

---

## Bu Derslerin Sonunda Neler Yapabilmelisiniz?

### Ekrana Çıktı Verme
`print()` fonksiyonunu kullanarak ekrana metin, sayı ve hesaplama sonuçları yazdırabilmelisiniz. Bir sayıyı metinle birleştirmek istediğinizde `str()` dönüşümüne neden ihtiyaç duyduğunuzu açıklayabilmelisiniz.

### Değişken Kullanma
Değişkenlerin ne işe yaradığını kavramış olmanızı bekliyorum. `str`, `int` ve `float` veri tiplerini birbirinden ayırt edebilmeli, hangi durumda hangisini kullanacağınızı biliyor olmalısınız.

### Kullanıcıdan Veri Alma
`input()` fonksiyonunun her zaman **metin (string)** döndürdüğünü bilmeniz kritiktir. Kullanıcıdan sayı almanız gerektiğinde `int(input(...))` yazabilmeli, birden fazla bilgiyi ayrı değişkenlerde saklayabilmelisiniz.

### Koşullu İfadeler
`if / else` ve `if / elif / else` yapılarını doğru girintileme ile yazabilmelisiniz. `==`, `>=`, `<=` gibi karşılaştırma operatörlerini ve `and` mantıksal operatörünü kullanarak birden fazla koşulu tek satırda ifade edebilmelisiniz.

### Boolean Mantığı
Bir karşılaştırmanın sonucunun `True` ya da `False` değeri ürettiğini, bu değerin bir değişkende saklanabileceğini görmüş oldunuz. İç içe `if` yapısında dıştaki koşul sağlanmadan içerideki bloğun hiç çalışmadığını açıklayabilmelisiniz.

---

## Bir Sonraki Adım

Bu konuları kavradıysanız harika! İlerleyen haftalarda `or`, `not`, döngüler, listeler ve fonksiyonlar gibi yeni kavramlarla tanışacaksınız. Şimdilik buradakileri iyice pekiştirmeniz yeterli.
