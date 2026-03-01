# Ödevler — Nasıl Yapılır?

Her ödev dosyasını bir kod editöründe aç, `...` ile işaretli yerleri doldur, sonra çalıştır.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Ödev dosyasını VS Code'da açın (örnek: `odev01_degiskenler.py`)
2. Sağ üstteki **▶ Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code'da **Terminal → New Terminal** menüsünü açın, ardından şu komutu yazın:

```
python3 odev01_degiskenler.py
```

Diğer ödevler için dosya adını değiştirin:

```
python3 odev02_input.py
python3 odev03_if_else.py
python3 odev04_elif.py
python3 odev05_ic_ice_if.py
```

> **Not:** `input()` kullanan ödevlerde (Ödev 2 ve sonrası) program sizden bilgi girmesini bekler. Terminale yazıp Enter'a basın.

---

## Çalışma Akışı

1. Dosyayı aç
2. `...` yerlerini doldur
3. Çalıştır — çıktıyı dosya sonundaki **Beklenen Çıktı** yorumuyla karşılaştır
4. Çıktılar eşleşene kadar düzenle

---

## Ödev 1 — Tasarımcı Kartı (`odev01_degiskenler.py`)

Değişkenlere kendi bilgilerini yaz, sonra `print()` satırlarındaki `...` yerlerini doldur.

```python
# Değişkenleri doldur:
isim = "Defne"         # kendi adın
sehir = "İzmir"        # yaşadığın şehir
yas = 20               # kaç yaşındasın
sevdigi_renk = "mavi"  # en sevdiğin renk
not_ortalamasi = 3.25  # not ortalaması

# print() içindeki ... yerine değişken adını yaz:
print("Ad:", isim)
print("Not ortalamam: " + str(not_ortalamasi))
```

> **Dikkat:** `...` Python'da "boş" demek değildir. Silip yerine değişken adını yaz.

---

## Ödev 2 — Renk Danışmanı (`odev02_input.py`)

Kullanıcıdan bilgi alan program. `input()` satırları zaten yazılı, sadece `print()` satırlarındaki `...` yerlerini doldur.

```python
# ... yerine doğru değişkeni yaz:
print("Poster rengin için", sevdigi_renk, "harika bir seçim!")
print(str(poster_genisligi) + " cm genişliğinde bir poster hazırlıyorum.")
```

---

## Ödev 3 — Baskı Makinesi (`odev03_if_else.py`)

`if / else` yapısı kurulu, sadece `print()` içindeki `...` yerlerini tamamla.
Mesajın içine değişkenleri de dahil etmeyi unutma.

```python
if poster_genisligi <= maksimum_genislik:
    print("Harika!", poster_genisligi, "cm posterın makineye sığıyor. Baskıya hazır!")
else:
    print("Dikkat!", poster_genisligi, "cm makinemizin limitini (", maksimum_genislik, "cm) aşıyor.")
```

---

## Ödev 4 — Tasarım Jürisi (`odev04_elif.py`)

`elif` dallarındaki `...` yerlerini doldur: eşik değerini ve mesajı yaz.

```python
elif puan >= 70:                          # eşik değeri
    print("İyi iş! Küçük dokunuşlarla mükemmel olur.")  # mesaj
```

Puanlama tablosu dosyanın içinde açıkça yazıyor — oradan eşik değerlerini al.

---

## Ödev 5 — Portfolyo Başvurusu (`odev05_ic_ice_if.py`) ⭐ Zor

> Bu ödevde bir `if` bloğunun içine başka bir `if` yazmanız gerekiyor — buna "iç içe if" (nested if) deniyor. Dıştaki koşul sağlanmadan içerideki kontrol hiç çalışmaz.

İki `...` yeri var:

1. Boolean değişkeni tamamla:
   ```python
   yeterli_proje_mi = proje_sayisi >= 5
   ```

2. `if` bloklarındaki mesajları yaz. Eksik sayıyı hesaplamak için:
   - Eksik proje: `5 - proje_sayisi`
   - Kaç yıl kaldı: `18 - yas`

---

## Genel İpuçları

| Durum | Ne yapmalısın? |
|---|---|
| Sayıyı metne katmak istiyorsan | `str(sayi)` kullan |
| Değişkeni mesajın içine almak istiyorsan | `print("Merhaba,", isim)` yaz |
| Program hata verdi | Hata mesajının altındaki satır numarasına bak |
| Çıktı `Ellipsis` çıktı | `...` yerine değişken adını yazmayı unuttun |
