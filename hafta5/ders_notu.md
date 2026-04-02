# GİTA 2112 — Hafta 5: F-String, Matematik ve Tip Dönüşümleri

> Bu belge, derste anlatılan konuların yazılı özetidir.
> Her bölümün sonunda ilgili kod dosyasına yönlendirme bulunur.
> Kod dosyalarını açıp çalıştırarak burada okuduklarınızı pratiğe dökebilirsiniz.

---

## Hafta 4'ten Hatırlamamız Gerekenler

Geçen hafta şunları öğrenmiştik:

- **Sözlükler** ile anahtar-değer çiftleri tutmak (`{"isim": "Defne", "puan": 88}`)
- **break** ile döngüyü durdurmak, **continue** ile turu atlamak
- **Sözlük listesi** ile birden fazla kaydı bir arada tutmak

Bu hafta bu bilgilerin üstüne yeni araçlar ekleyeceğiz: string formatlama, matematik işlemleri ve tip dönüşümleri.

---

## 1. String Formatlama — f-string

### Eski Yol: + ile Birleştirme

Şimdiye kadar metinleri `+` ile birleştiriyorduk. Bu yöntemde sayıları `str()` ile çevirmek gerekiyordu:

```python
isim = "Defne"
yas = 20
print("Merhaba, ben " + isim + ". " + str(yas) + " yaşındayım.")
```

Bu hem uzun hem de hata yapmaya açık.

### Yeni Yol: f-string

`f"..."` ile başlayan bir string içinde süslü parantez `{}` kullanarak doğrudan değişken yazabiliriz:

```python
print(f"Merhaba, ben {isim}. {yas} yaşındayım.")
```

Daha kısa, daha okunabilir. Ayrıca `str()` çevirmesine gerek yok — f-string otomatik halleder.

### f-string İçinde İfade

Süslü parantezlerin içine sadece değişken değil, **ifadeler** de yazabilirsiniz:

```python
print(f"Toplam: {3 + 5}")              # 8
print(f"İsim (büyük): {isim.upper()}")  # DEFNE
print(f"5 yıl sonra: {yas + 5}")        # 25
```

### Sayı Formatlama

f-string ile sayıları istediğiniz formatta gösterebilirsiniz:

```python
fiyat = 1234.5678

print(f"{fiyat:.1f}")      # 1234.6    (1 ondalık basamak)
print(f"{fiyat:.2f}")      # 1234.57   (2 ondalık basamak)
print(f"{fiyat:,.2f}")     # 1,234.57  (binlik ayıracı + 2 ondalık)
```

| Format | Açıklama | Örnek |
|--------|----------|-------|
| `:.1f` | 1 ondalık basamak | `3.1` |
| `:.2f` | 2 ondalık basamak | `3.14` |
| `:,.2f` | Binlik ayıracı + 2 ondalık | `1,234.57` |

### .format() Yöntemi (Farkındalık)

f-string'den önce `.format()` yöntemi kullanılıyordu. Bilmenize gerek yok ama başkasının kodunda karşılaşabilirsiniz:

```python
print("Merhaba, ben {}. {} yaşındayım.".format(isim, yas))
```

### String Metodları

Kullanıcıdan `input()` ile veri alırken bu metodlar çok işe yarar:

```python
metin = "  Grafik Tasarım  "
metin.strip()       # "Grafik Tasarım"  (baş/son boşlukları siler)
metin.lower()       # "  grafik tasarım  "  (küçük harfe çevirir)
metin.upper()       # "  GRAFİK TASARIM  "  (büyük harfe çevirir)
```

Bunları zincirleme kullanabilirsiniz: `metin.strip().lower()` → `"grafik tasarım"`

Pratik kullanım — kullanıcı "EVET", "evet", " evet " yazsa bile hepsini yakalarız:

```python
cevap = input("Devam? ").strip().lower()
if cevap == "evet":
    print("Devam ediyoruz!")
```

> **Dosya:** `ornekler/01_fstring.py`

---

## 2. Matematik İşlemleri ve Tip Dönüşümleri

### Aritmetik Operatörler

Python'daki tüm matematik operatörleri:

| Operatör | Açıklama | Örnek | Sonuç |
|----------|----------|-------|-------|
| `+` | Toplama | `17 + 5` | `22` |
| `-` | Çıkarma | `17 - 5` | `12` |
| `*` | Çarpma | `17 * 5` | `85` |
| `/` | Bölme | `17 / 5` | `3.4` |
| `//` | Tam bölme | `17 // 5` | `3` |
| `%` | Mod (kalan) | `17 % 5` | `2` |
| `**` | Üs alma | `2 ** 3` | `8` |

**Önemli:** `/` her zaman ondalıklı sonuç (`float`) döner. Tam sayı sonuç istiyorsanız `//` kullanın.

### Kısayol Operatörler

Bir değişkeni kendi değeri üzerinden güncellemek için kısayollar:

```python
sayac = 10
sayac += 3    # sayac = sayac + 3  → 13
sayac -= 5    # sayac = sayac - 5  → 8
sayac *= 2    # sayac = sayac * 2  → 16
```

### Tip Dönüşümleri: int() ve float()

`input()` fonksiyonu her zaman **string** döner. Sayıyla işlem yapmak için dönüştürmeliyiz:

```python
yas = int(input("Yaşınız: "))      # string → tam sayı
fiyat = float(input("Fiyat: "))    # string → ondalıklı sayı
```

**Dikkat:** `int()` ondalık kısmı **kırpar**, yuvarlamaz:

```python
int(3.7)    # 3  (yuvarlamaz!)
int(3.2)    # 3
```

Yuvarlama istiyorsanız `round()` kullanın.

### round() ve abs()

```python
round(3.14159, 2)   # 3.14  (virgülden sonra 2 basamak)
round(3.14159, 1)   # 3.1
round(3.14159)      # 3     (en yakın tam sayıya)

abs(-15)    # 15  (mutlak değer — işareti atar)
abs(7)      # 7
```

### Tasarım Bağlamı

```python
# Ekranı 3 sütuna bölelim
genislik = 1920
sutun_genislik = genislik // 3   # 640 (tam bölme)
kalan = genislik % 3              # 0 (kalan piksel)
```

> **Dosya:** `ornekler/02_matematik.py`

---

## 3. Hepsini Bir Araya Getirme

Son dosyamızda (`ornekler/03_hepsi_bir_arada.py`) önceki haftaların ve bu haftanın konularını birleştiren bir mini uygulama var: **Portfolyo Yöneticisi**.

Bu uygulama şunları yapıyor:

1. **Sözlük listesi** — Her proje bir sözlük (ad, kategori, puan), hepsi bir listede
2. **f-string ile listeleme** — `enumerate` + f-string ile formatlı yazdırma
3. **continue ile filtreleme** — Düşük puanlı projeleri atlama
4. **Toplam ve ortalama** — Döngüyle puan toplama, `:.1f` ile formatlama
5. **En iyi projeyi bulma** — Döngüyle karşılaştırma
6. **Kategoriye göre filtreleme** — Döngü + if ile eşleşenleri bulma
7. **Kategori sayma** — Boş sözlük oluşturup dinamik olarak doldurma

Bu dosyayı açıp satır satır okuyun. Her bölümün üstünde ne yaptığını anlatan yorumlar var. Anlamadığınız bir satır olursa, o konunun ders dosyasına geri dönüp tekrar bakın.

> **Dosya:** `ornekler/03_hepsi_bir_arada.py`

---

## Özet Tablosu

| Yapı | Yazılış | Ne İşe Yarar? | Örnek |
|------|---------|---------------|-------|
| f-string | `f"..."` | Değişkeni metin içine gömer | `f"İsim: {isim}"` |
| Sayı formatı | `:.1f` | Ondalık basamak kontrolü | `f"{puan:.1f}"` |
| int() | `int(x)` | Tam sayıya çevirir (kırpar!) | `int("42")` → `42` |
| float() | `float(x)` | Ondalıklı sayıya çevirir | `float("3.14")` → `3.14` |
| round() | `round(x, n)` | Yuvarlar | `round(3.14, 1)` → `3.1` |
| abs() | `abs(x)` | Mutlak değer | `abs(-15)` → `15` |
| `//` | `a // b` | Tam bölme | `17 // 5` → `3` |
| `%` | `a % b` | Mod (kalan) | `17 % 5` → `2` |
| `**` | `a ** b` | Üs alma | `2 ** 3` → `8` |
| `+=` | `x += n` | Kısayol toplama | `sayac += 1` |
| strip() | `s.strip()` | Baş/son boşluk siler | `" ab ".strip()` → `"ab"` |
| lower() | `s.lower()` | Küçük harfe çevirir | `"ABC".lower()` → `"abc"` |
| upper() | `s.upper()` | Büyük harfe çevirir | `"abc".upper()` → `"ABC"` |

---

## Sık Yapılan Hatalar

### 1. f-string'de f'yi unutmak

```python
isim = "Defne"
print("{isim}")     # {isim}  ← f'yi unuttun!
print(f"{isim}")    # Defne   ← doğru
```

### 2. int() kırpar, yuvarlamaz

```python
int(3.9)    # 3  ← 4 değil! Yuvarlamaz, kırpar.
round(3.9)  # 4  ← Yuvarlama istiyorsan round() kullan
```

### 3. input() her zaman string döner

```python
sayi = input("Sayı: ")    # "5" (string!)
print(sayi + 3)            # TypeError!
print(int(sayi) + 3)       # 8 (doğru)
```

### 4. Bölme her zaman float döner

```python
print(10 / 2)    # 5.0 (float! 5 değil)
print(10 // 2)   # 5 (tam bölme, int döner)
```

---

## Ödevler Hakkında

Bu haftanın 3 ödevi var. Kolaydan zora doğru sıralanmıştır:

| Ödev | Zorluk | Konu |
|------|--------|------|
| Ödev 1 — Tasarımcı Kartı v2 | Kolay | f-string, sayı formatlama |
| Ödev 2 — Tasarım Hesap Makinesi | Orta | input + float + if/elif + f-string |
| Ödev 3 — Sınıf Listesi Analizi | Zor | Hepsi bir arada |

Her ödev dosyasında `...` ile işaretlenmiş yerler var. Bu yerler sizin doldurmanız gereken boşluklar. Yanlarındaki `# ←` yorumları size ne yazmanız gerektiğini söyler. Dosyanın en altındaki **Beklenen Çıktı** bölümüyle kendi çıktınızı karşılaştırın.

Tüm ödevler `hafta5/odevler/` klasöründedir. Nasıl çalıştırılacağı `odevler/BENIOKU.md` dosyasında anlatılmıştır.

---

## Bir Sonraki Adım

Bu hafta öğrendiğiniz f-string, matematik işlemleri ve tip dönüşümleri, Python programlamanın temel yapı taşlarıdır. Bundan sonraki hemen her konuda bu yapıları kullanacaksınız.

Konuları tam kavramak için:

1. Ders dosyalarını (`ornekler/`) açıp çalıştırın
2. Kodları satır satır okuyun, yorumları atlayamayın
3. Küçük değişiklikler yapıp ne olduğunu gözlemleyin
4. Ödevleri sırayla çözün — takılırsanız ders dosyasına geri dönün
