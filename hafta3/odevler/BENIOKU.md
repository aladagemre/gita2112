# Ödevler — Nasıl Yapılır?

Her ödev dosyasını bir kod editöründe aç, `...` ile işaretli yerleri doldur, sonra çalıştır.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Ödev dosyasını VS Code'da açın (örnek: `odev01_liste_temel.py`)
2. Sağ üstteki **▶ Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code'da **Terminal → New Terminal** menüsünü açın, ardından şu komutu yazın:

```
cd hafta3/odevler
python3 odev01_liste_temel.py
```

Diğer ödevler için dosya adını değiştirin:

```
python3 odev02_for_range.py
python3 odev03_for_liste.py
python3 odev04_while.py
python3 odev05_sozluk.py
python3 odev06_birlesik.py
```

> **Not:** `input()` kullanan ödevlerde (Ödev 4) program sizden bilgi girmenizi bekler. Terminale yazıp Enter'a basın.

---

## Çalışma Akışı

1. Dosyayı aç
2. `...` yerlerini doldur
3. Çalıştır — çıktıyı dosya sonundaki **Beklenen Çıktı** yorumuyla karşılaştır
4. Çıktılar eşleşene kadar düzenle

---

## Ödev 1 — Tasarım Malzemeleri (`odev01_liste_temel.py`)

Liste oluştur, eleman ekle/sil, indeksle eriş ve güncelle.

```python
malzemeler = ["kağıt", "boya", "fırça", "cetvel"]  # en az 4 eleman
malzemeler.append("makas")      # eleman ekle
malzemeler.remove("fırça")      # eleman sil
print(malzemeler[0])            # indeksle eriş
malzemeler[0] = "kalem"         # güncelle
```

---

## Ödev 2 — Katman Oluşturucu (`odev02_for_range.py`)

`range()` fonksiyonunu farklı parametrelerle kullan.

```python
for katman in range(1, 9):      # 1'den 8'e
for katman in range(2, 11, 2):  # çift sayılar
for sayi in range(5, 0, -1):    # geri sayım
```

---

## Ödev 3 — Renk Paleti Analizi (`odev03_for_liste.py`)

Listeyi döngüyle gez, koşulla filtrele, ortalama hesapla.

```python
for sira, renk in enumerate(renkler, start=1):
    print(str(sira) + ".", renk)

toplam = toplam + deger
ortalama = toplam / len(parlaklik)
```

---

## Ödev 4 — Renk Tahmin Oyunu (`odev04_while.py`)

`while True` + `break` deseniyle kullanıcıdan tahmin al.

```python
deneme = 0
while True:
    tahmin = input("Tahminin: ")
    deneme = deneme + 1
    if tahmin == gizli_renk:
        print("Tebrikler!", deneme, "denemede bildin!")
        break
```

---

## Ödev 5 — Proje Kartı (`odev05_sozluk.py`)

Sözlük oluştur, değer oku/ekle/güncelle, döngüyle yazdır.

```python
proje = {"ad": "Logo Tasarımı", "kategori": "Kurumsal"}
proje["puan"] = 88                  # yeni alan ekle
proje["sure_gun"] = proje["sure_gun"] + 7  # güncelle

for anahtar, deger in proje.items():
    print(anahtar + ":", deger)
```

---

## Ödev 6 — Sınıf Listesi Analizi (`odev06_birlesik.py`) ⭐ Zor

Liste + sözlük + döngü + if hepsini bir arada kullan.

```python
# Ortalama hesapla
for ogr in ogrenciler:
    toplam = toplam + ogr["puan"]

# En iyiyi bul
en_iyi = ogrenciler[0]
for ogr in ogrenciler:
    if ogr["puan"] > en_iyi["puan"]:
        en_iyi = ogr
```

---

## Genel İpuçları

| Durum | Ne yapmalısın? |
|---|---|
| `...` yerine ne yazacağını bilmiyorsan | Dosyadaki `# ←` ipuçlarını oku |
| `Ellipsis` çıktısı aldıysan | `...` yerine değişken/ifade yazmayı unuttun |
| Sonsuz döngüye girdiysen | `Ctrl+C` ile durdur, sayacı kontrol et |
| `KeyError` hatası aldıysan | Sözlük anahtarını kontrol et (yazım hatası?) |
| `IndexError` hatası aldıysan | İndeks numarasını kontrol et (`len()` ile) |
| Program hata verdi | Hata mesajının altındaki satır numarasına bak |
