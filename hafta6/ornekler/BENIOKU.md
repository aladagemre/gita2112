# GİTA 2112 — Hafta 6: Fonksiyonlar

Bu klasördeki dosyalar, derste birlikte işlediğimiz konuları sıralı bir şekilde içermektedir. Her dosyayı açıp çalıştırın, kodları okuyun, yorumları dikkatlice inceleyin.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Dosyayı VS Code'da açın (örnek: `01_ilk_fonksiyon.py`)
2. Sağ üstteki **Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code üst menüden **Terminal → New Terminal** tıklayın, ardından şu komutu yazın:

```
cd hafta6/ornekler
python3 01_ilk_fonksiyon.py
```

Dosya adını değiştirerek diğer dersleri de çalıştırabilirsiniz:

```
python3 02_parametreler.py
python3 03_return.py
```

---

## Dosyalar ve Konular

| Dosya | Konu |
|-------|------|
| `01_ilk_fonksiyon.py` | `def` ile fonksiyon tanımlama ve çağırma |
| `02_parametreler.py` | Parametre ve argüman, birden fazla parametre |
| `03_return.py` | `return` ile değer döndürme, `print` vs `return` farkı |
| `04_varsayilan_degerler.py` | Varsayılan parametreler, koşullu return, boolean fonksiyonlar |
| `05_kaliplar.py` | Hafta 3-4 kalıplarını fonksiyona dönüştürme |
| `06_hepsi_bir_arada.py` | Tüm kavramları birleştiren mini uygulama |

---

## Bu Derslerin Sonunda Neler Yapabilmelisiniz?

### Fonksiyon Tanımlama ve Çağırma
`def` anahtar kelimesiyle fonksiyon tanımlayabilmeli, tanımlama ile çağırma arasındaki farkı kavramış olmalısınız. Bir fonksiyonu birden fazla kez çağırabilmelisiniz.

### Parametreler
Fonksiyonlara parametre ekleyerek esnek hale getirebilmelisiniz. Birden fazla parametre tanımlayabilmeli ve çağırırken doğru sırada argüman verebilmelisiniz.

### return ile Değer Döndürme
`print` ile `return` arasındaki farkı açıklayabilmelisiniz. Fonksiyondan döndürülen değeri bir değişkene atayabilmeli, başka hesaplamalarda kullanabilmelisiniz.

### Varsayılan Değerler
Parametrelere varsayılan değer vererek fonksiyonları daha esnek yapabilmelisiniz. Zorunlu ve opsiyonel parametrelerin sıralama kuralını bilmelisiniz.

### Kalıpları Fonksiyona Dönüştürme
Daha önce yazdığınız tekrar eden kalıpları (ortalama hesaplama, filtreleme, en yüksek bulma) fonksiyona çevirebilmelisiniz.

---

## Bir Sonraki Adım

Bu konuları kavradıysanız harika! Fonksiyonlar, Python programlamanın en temel soyutlama aracıdır. Bundan sonraki hemen her konuda fonksiyonlar kullanacaksınız. Şimdilik buradakileri iyice pekiştirmeniz yeterli.
