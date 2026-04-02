# Ödevler — Nasıl Yapılır?

Her ödev dosyasını bir kod editöründe aç, `...` ile işaretli yerleri doldur, sonra çalıştır.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Ödev dosyasını VS Code'da açın (örnek: `odev01_sozluk.py`)
2. Sağ üstteki **Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code'da **Terminal → New Terminal** menüsünü açın, ardından şu komutu yazın:

```
cd hafta4/odevler
python3 odev01_sozluk.py
```

Diğer ödevler için dosya adını değiştirin:

```
python3 odev02_break_continue.py
python3 odev03_birlesik.py
```

> **Not:** `input()` kullanan ödevlerde (Ödev 2 Görev 3) program sizden bilgi girmenizi bekler. Terminale yazıp Enter'a basın.

---

## Çalışma Akışı

1. Dosyayı aç
2. `...` yerlerini doldur
3. Çalıştır — çıktıyı dosya sonundaki **Beklenen Çıktı** yorumuyla karşılaştır
4. Çıktılar eşleşene kadar düzenle

---

## Ödev 1 — Proje Kartı (`odev01_sozluk.py`)

Sözlük oluştur, değer oku/ekle/güncelle, döngüyle yazdır.

```python
proje = {"ad": "Logo Tasarımı", "kategori": "Kurumsal"}
proje["puan"] = 88
for anahtar, deger in proje.items():
    print(anahtar + ":", deger)
```

---

## Ödev 2 — Renk Arama Asistanı (`odev02_break_continue.py`)

for + break ile arama yap, continue ile atla, while True + break ile giriş al.

```python
if renk == aranan:
    print("Buldum! →", aranan)
    break

if len(renk) < 5:
    continue
```

---

## Ödev 3 — Tasarım Ekibi Analizi (`odev03_birlesik.py`) — Zor

Liste + sözlük + döngü + if + continue hepsini bir arada kullan.

```python
for sira, t in enumerate(tasarimcilar, start=1):
    print(str(sira) + ".", t["isim"], "→", t["puan"], "puan")

if t["puan"] < 75:
    continue
```

---

## Genel İpuçları

| Durum | Ne yapmalısın? |
|---|---|
| `...` yerine ne yazacağını bilmiyorsan | Dosyadaki `# ←` ipuçlarını oku |
| `Ellipsis` çıktısı aldıysan | `...` yerine değişken/ifade yazmayı unuttun |
| Sonsuz döngüye girdiysen | `Ctrl+C` ile durdur, break kontrolünü kontrol et |
| `KeyError` hatası aldıysan | Sözlük anahtarını kontrol et (yazım hatası?) |
| Program hata verdi | Hata mesajının altındaki satır numarasına bak |
