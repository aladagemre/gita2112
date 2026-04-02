# Ödevler — Nasıl Yapılır?

Her ödev dosyasını bir kod editöründe aç, `...` ile işaretli yerleri doldur, sonra çalıştır.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Ödev dosyasını VS Code'da açın (örnek: `odev01_selamlama.py`)
2. Sağ üstteki **Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code'da **Terminal → New Terminal** menüsünü açın, ardından şu komutu yazın:

```
python3 odev01_selamlama.py
```

Diğer ödevler için dosya adını değiştirin:

```
python3 odev02_geometri.py
python3 odev03_harf_notu.py
python3 odev04_proje_karti.py
python3 odev05_portfolyo.py
```

---

## Çalışma Akışı

1. Dosyayı aç
2. `...` yerlerini doldur
3. Çalıştır — çıktıyı dosya sonundaki **Beklenen Çıktı** yorumuyla karşılaştır
4. Çıktılar eşleşene kadar düzenle

---

## Ödev 1 — Stüdyo Selamlama (`odev01_selamlama.py`)

Fonksiyon tanımlama ve çağırma. `def` satırındaki parametre adlarını ve `print` içindeki `...` yerlerini doldur.

- **Görev 1:** Tek parametreli `selamla(isim)` fonksiyonu
- **Görev 2:** İki parametreli `detayli_selamla(isim, bolum)` fonksiyonu
- **Görev 3:** `cizgi(uzunluk)` fonksiyonu

---

## Ödev 2 — Tasarım Hesaplayıcı (`odev02_geometri.py`)

`return` ile değer döndüren fonksiyonlar. Fonksiyonların içindeki `return ...` satırlarını tamamla.

- **Görev 1:** `dikdortgen_alan()` — poster alanı hesaplama
- **Görev 2:** `sticker_alani()` — daire alanı hesaplama
- **Görev 3:** `indirimli_fiyat()` — indirim hesaplama
- **Görev 4:** Sonuçları karşılaştırma

---

## Ödev 3 — Harf Notu Sistemi (`odev03_harf_notu.py`)

Koşullu `return` ile farklı değerler döndürme. `elif` koşullarını ve `return` değerlerini doldur.

- **Görev 1:** `harf_notu(puan)` fonksiyonu (if/elif/else)
- **Görev 2:** Döngüde fonksiyon çağırma
- **Görev 3:** Boolean döndüren `gecti_mi(puan)` fonksiyonu

---

## Ödev 4 — Proje Kartı Oluşturucu (`odev04_proje_karti.py`)

Varsayılan parametre değerleri. `def` satırındaki varsayılan değerleri ve fonksiyon çağrılarını tamamla.

- **Görev 1:** Varsayılan değerli `cizgi()` fonksiyonu
- **Görev 2:** `proje_karti()` — zorunlu + opsiyonel parametreler
- **Görev 3:** Döngü ile kart oluşturma

---

## Ödev 5 — Portfolyo Analiz Sistemi (`odev05_portfolyo.py`) — Zor

Tüm fonksiyon kavramlarını birleştiren kapsamlı ödev. Dört fonksiyon tanımlayıp ana programda kullan.

- `ortalama_hesapla()` — ortalama hesaplama
- `basarili_filtrele()` — filtreleme (varsayılan değerli)
- `en_iyi_bul()` — en yüksek puanlıyı bulma
- `basari_durumu()` — koşullu return

> **İpucu:** Bu ödev Hafta 4 Ödev 5'in fonksiyonlarla yeniden yazılmış halidir. O ödevi çözdüyseniz mantığı biliyorsunuz — şimdi sadece fonksiyona çevirmeniz gerekiyor.

---

## Genel İpuçları

| Durum | Ne yapmalısın? |
|---|---|
| Fonksiyon çalışmıyor | `()` ile çağırdığından emin ol |
| Sonuç `None` çıkıyor | `print` yerine `return` kullan |
| `SyntaxError: invalid syntax` | `def` satırında `:` var mı kontrol et |
| `TypeError: takes N arguments` | Parametre ve argüman sayısını eşleştir |
| `NameError: name 'x' is not defined` | Değişken fonksiyonun içinde mi? `return` ile dışarı çıkar |
| Çıktı `Ellipsis` çıktı | `...` yerine doğru kodu yazmayı unuttun |
