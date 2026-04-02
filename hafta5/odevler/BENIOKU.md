# Ödevler — Nasıl Yapılır?

Her ödev dosyasını bir kod editöründe aç, `...` ile işaretli yerleri doldur, sonra çalıştır.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Ödev dosyasını VS Code'da açın (örnek: `odev01_fstring.py`)
2. Sağ üstteki **Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code'da **Terminal → New Terminal** menüsünü açın, ardından şu komutu yazın:

```
cd hafta5/odevler
python3 odev01_fstring.py
```

Diğer ödevler için dosya adını değiştirin:

```
python3 odev02_hesap_makinesi.py
python3 odev03_birlesik.py
```

> **Not:** `input()` kullanan ödevlerde (Ödev 2) program sizden bilgi girmenizi bekler. Terminale yazıp Enter'a basın.

---

## Çalışma Akışı

1. Dosyayı aç
2. `...` yerlerini doldur
3. Çalıştır — çıktıyı dosya sonundaki **Beklenen Çıktı** yorumuyla karşılaştır
4. Çıktılar eşleşene kadar düzenle

---

## Ödev 1 — Tasarımcı Kartı v2 (`odev01_fstring.py`)

f-string ile formatlı yazdır, sayı formatla, string metodları kullan.

```python
print(f"İsim: {isim}")
print(f"Ortalama puan: {ortalama_puan:.1f}")
print(f"Büyük harf: {kirli_metin.strip().upper()}")
```

---

## Ödev 2 — Tasarım Hesap Makinesi (`odev02_hesap_makinesi.py`)

input + float + if/elif + f-string ile hesap makinesi yap.

```python
sayi1 = float(input("Birinci sayı: "))
if islem == "+":
    sonuc = sayi1 + sayi2
print(f"Sonuç: {sayi1} {islem} {sayi2} = {sonuc:.2f}")
```

---

## Ödev 3 — Sınıf Listesi Analizi (`odev03_birlesik.py`) — Zor

Liste + sözlük + döngü + if + f-string + continue hepsini bir arada kullan.

```python
for sira, ogr in enumerate(ogrenciler, start=1):
    print(f"{sira}. {ogr['isim']} ({ogr['bolum']}) → {ogr['puan']} puan")

if ogr["puan"] < 75:
    continue
```

---

## Genel İpuçları

| Durum | Ne yapmalısın? |
|---|---|
| `...` yerine ne yazacağını bilmiyorsan | Dosyadaki `# ←` ipuçlarını oku |
| `Ellipsis` çıktısı aldıysan | `...` yerine değişken/ifade yazmayı unuttun |
| `KeyError` hatası aldıysan | Sözlük anahtarını kontrol et (yazım hatası?) |
| `ValueError` hatası aldıysan | float() veya int() dönüşümünde geçersiz giriş |
| Program hata verdi | Hata mesajının altındaki satır numarasına bak |
