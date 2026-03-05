# GİTA 2112 — Hafta 3: Listeler, Döngüler, Demetler ve Sözlükler

Bu klasördeki dosyalar, derste birlikte işlediğimiz konuları sıralı bir şekilde içermektedir. Her dosyayı açıp çalıştırın, kodları okuyun, yorumları dikkatlice inceleyin.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Dosyayı VS Code'da açın (örnek: `01_listeler.py`)
2. Sağ üstteki **▶ Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code üst menüden **Terminal → New Terminal** tıklayın, ardından şu komutu yazın:

```
cd hafta3/ornekler
python3 01_listeler.py
```

Dosya adını değiştirerek diğer dersleri de çalıştırabilirsiniz:

```
python3 02_liste_islemleri.py
python3 03_for_dongusu.py
```

> **Not:** `input()` kullanan programlar (05 ve sonrası) sizden klavyeyle bilgi girmenizi bekler. Terminale yazıp Enter'a basın.

---

## Dosyalar ve Konular

| Dosya | Konu |
|-------|------|
| `01_listeler.py` | Liste oluşturma, indeks erişimi, `len()` |
| `02_liste_islemleri.py` | `append()`, `remove()`, `in`, `sort()` |
| `03_for_dongusu.py` | `for` + `range()`, adımlı sayma, geri sayım |
| `04_for_liste.py` | `for` ile liste gezme, `enumerate()`, filtreleme |
| `05_while_dongusu.py` | `while` döngüsü, `break`, tahmin oyunu |
| `06_demetler.py` | Demet `()`, değiştirilemezlik, RGB renk kodları |
| `07_sozlukler.py` | Sözlük `{}`, anahtar-değer, `.items()` |
| `08_hepsi_bir_arada.py` | Liste + sözlük + döngü + koşul birleşik örnek |

---

## Bu Derslerin Sonunda Neler Yapabilmelisiniz?

### Listeler
Köşeli parantez `[]` ile liste oluşturabilmeli, indeksle elemanlara erişebilmeli, `append()` ve `remove()` ile liste üzerinde ekleme/çıkarma yapabilmelisiniz. `in` operatörüyle bir elemanın listede olup olmadığını kontrol edebilmelisiniz.

### for Döngüsü
`range()` fonksiyonunu farklı parametrelerle (başlangıç, bitiş, adım) kullanabilmelisiniz. Bir listeyi `for` döngüsüyle gezebilmeli, `enumerate()` ile hem sıra numarasını hem elemanı alabilmelisiniz.

### while Döngüsü
`while` döngüsünün koşul doğru olduğu sürece çalıştığını kavramış olmalısınız. Sayaç değişkeni kullanarak sonsuz döngüyü önleyebilmeli, `break` ile döngüden çıkabilmelisiniz.

### Demetler
Demetlerin listelerden farkını (değiştirilemezlik) açıklayabilmelisiniz. Sabit verilerin (RGB renk kodları, koordinatlar) neden demet ile saklanması gerektiğini anlıyor olmalısınız.

### Sözlükler
Anahtar-değer çifti mantığını kavramış olmalısınız. Sözlük oluşturup değer okuyabilmeli, yeni çift ekleyebilmeli ve `.items()` ile döngü kurabilmelisiniz.

### Ek Kavramlar
Derslerde ayrıca `end=" "` (print davranışını değiştirme), `round()` (yuvarlama), `range(len(liste))` (indeksle gezme) ve `"=" * 45` (string tekrarlama) gibi küçük araçlarla da tanıştınız. Bunları ezberlemek zorunda değilsiniz ama karşınıza çıktığında tanıyabilmelisiniz.

---

## Bir Sonraki Adım

Bu konuları kavradıysanız harika! İlerleyen haftalarda fonksiyonlar, dosya işlemleri ve daha karmaşık veri yapılarıyla tanışacaksınız. Şimdilik buradakileri iyice pekiştirmeniz yeterli.
