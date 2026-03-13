# GİTA 2112 — Hafta 4: Sözlükler, Break/Continue, F-String, Matematik

> Bu belge, derste anlatılan konuların yazılı özetidir.
> Her bölümün sonunda ilgili kod dosyasına yönlendirme bulunur.
> Kod dosyalarını açıp çalıştırarak burada okuduklarınızı pratiğe dökebilirsiniz.

---

## Hafta 3'ten Hatırlamamız Gerekenler

Geçen hafta şunları öğrenmiştik:

- **Listeler** ile birden fazla şeyi bir arada tutmak (`renkler = ["kırmızı", "mavi"]`)
- **for döngüsü** ile bir listeyi gezmek veya `range()` ile sayıları saymak
- **while döngüsü** ile koşula bağlı tekrar
- **Demetler** ile sabit verileri (RGB, koordinat) korumak

Bu hafta bu bilgilerin üstüne yeni araçlar ekleyeceğiz: sözlükler, döngü kontrolü, string formatlama ve matematik işlemleri.

---

## 1. Sözlükler — Anahtar ile Değer Eşleştirme

### Sorun

Bir öğrencinin bilgilerini saklamak istiyorsunuz: adı, bölümü, sınıfı, ortalaması. Ayrı ayrı değişkenler kullanabilirsiniz:

```python
isim = "Defne"
bolum = "Grafik Tasarım"
sinif = 2
ortalama = 3.45
```

Ama bu bilgiler **birbirine ait**. Hepsi aynı öğrenciyle ilgili. Ayrı değişkenlerde tutunca aralarındaki bağlantı kaybolur. İkinci bir öğrenci eklemek istesek `isim2`, `bolum2`... mı yazacağız?

### Çözüm: Sözlük

Sözlük, bilgileri **anahtar-değer çiftleri** olarak saklar. Her bilgiye bir isim (anahtar) verirsiniz ve o isimle erişirsiniz:

```python
ogrenci = {
    "isim": "Defne",
    "bolum": "Grafik Tasarım",
    "sinif": 2,
    "ortalama": 3.45
}
```

Süslü parantez `{}` kullanılır. Her satırda `"anahtar": değer` formatı vardır.

### Değere Erişim

Anahtarı köşeli parantez içinde yazarak değere ulaşırız:

```python
print(ogrenci["isim"])       # Defne
print(ogrenci["bolum"])      # Grafik Tasarım
print(ogrenci["ortalama"])   # 3.45
```

Listelerde `[0]`, `[1]` gibi sayı kullanıyorduk. Sözlüklerde ise `["isim"]`, `["bolum"]` gibi **anlamlı isimler** kullanıyoruz. Bu, kodu çok daha okunabilir kılar.

### Değer Güncelleme ve Yeni Alan Ekleme

Mevcut bir değeri değiştirmek:

```python
ogrenci["ortalama"] = 3.60
```

Yeni bir bilgi eklemek:

```python
ogrenci["email"] = "defne@uni.edu.tr"
```

Her iki işlem de aynı yazılışla yapılır. Anahtar zaten varsa günceller, yoksa yeni ekler.

### Sözlük Üzerinde Döngü

`.items()` metodu ile hem anahtarı hem değeri alarak gezeriz:

```python
for anahtar, deger in ogrenci.items():
    print(anahtar + ":", deger)
```

### Sözlük Listesi: Gerçek Hayatta En Çok Kullanılan Yapı

Birden fazla öğrenciyi saklamak istiyorsak, her öğrenci bir sözlük olur ve hepsini bir listede tutarız:

```python
sinif = [
    {"isim": "Defne", "puan": 88},
    {"isim": "Cem", "puan": 72},
    {"isim": "Ayşe", "puan": 95},
]

for ogr in sinif:
    print(ogr["isim"], "→", ogr["puan"])
```

Bu yapı ileride çok karşınıza çıkacak. Bir veritabanı tablosu, bir Excel dosyası, bir API yanıtı — hepsi aslında bu mantıkla çalışır: **sözlüklerden oluşan bir liste**.

> **Dosya:** `ornekler/01_sozlukler.py`

---

## 2. break ve continue — Döngü Kontrolü

### break: Döngüyü Durdur

Geçen hafta `while True` + `break` kalıbını kısaca görmüştük. Şimdi bunu daha detaylı ele alıyoruz.

`break` komutu döngüyü **anında** sonlandırır. Kalan elemanları gezmez, döngüden çıkar:

```python
palet = ["kırmızı", "turuncu", "yeşil", "mavi", "mor"]
aranan = "yeşil"

for renk in palet:
    print("Bakıyorum:", renk)
    if renk == aranan:
        print("Buldum! →", aranan)
        break   # Döngüyü durdur
```

Bu kod "yeşil"i bulduğunda durur. "mavi" ve "mor"a hiç bakmaz.

### continue: Bu Turu Atla

`continue` komutu döngünün **o turundaki** geri kalan kodları atlar ve bir sonraki tura geçer. Döngü devam eder, sadece o tur atlanır:

```python
projeler = [
    {"ad": "Logo Tasarımı", "puan": 88},
    {"ad": "El İlanı", "puan": 45},
    {"ad": "Web Sitesi", "puan": 92},
]

for proje in projeler:
    if proje["puan"] < 70:
        continue    # Bu projeyi atla
    print(" ", proje["ad"], "→", proje["puan"], "puan")
```

"El İlanı" (puan 45) atlanır, diğerleri yazdırılır.

### while True + break: Kullanıcıdan Sürekli Giriş Alma

Bu kalıp, kullanıcı belirli bir şey yapana kadar tekrar tekrar sormak istediğimizde idealdir:

```python
malzemeler = []

while True:
    yeni = input("Malzeme gir ('bitti' → çık): ")
    if yeni == "bitti":
        break
    malzemeler.append(yeni)

print("Toplam", len(malzemeler), "malzeme:", malzemeler)
```

### break vs continue Özet

| Komut | Ne yapar? | Döngü devam eder mi? |
|-------|-----------|----------------------|
| `break` | Döngüyü tamamen durdurur | Hayır |
| `continue` | Bu turu atlar, sonrakine geçer | Evet |

> **Dosya:** `ornekler/02_break_continue.py`

---

## 3. String Formatlama — f-string

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

> **Dosya:** `ornekler/03_fstring.py`

---

## 4. Matematik İşlemleri ve Tip Dönüşümleri

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

> **Dosya:** `ornekler/04_matematik.py`

---

## 5. Hepsini Bir Araya Getirme

Son dosyamızda (`ornekler/05_hepsi_bir_arada.py`) bu haftanın tüm konularını birleştiren bir mini uygulama var: **Portfolyo Yöneticisi**.

Bu uygulama şunları yapıyor:

1. **Sözlük listesi** — Her proje bir sözlük (ad, kategori, puan), hepsi bir listede
2. **f-string ile listeleme** — `enumerate` + f-string ile formatlı yazdırma
3. **continue ile filtreleme** — Düşük puanlı projeleri atlama
4. **Toplam ve ortalama** — Döngüyle puan toplama, `:.1f` ile formatlama
5. **En iyi projeyi bulma** — Döngüyle karşılaştırma
6. **Kategoriye göre filtreleme** — Döngü + if ile eşleşenleri bulma
7. **Kategori sayma** — Boş sözlük oluşturup dinamik olarak doldurma

Bu dosyayı açıp satır satır okuyun. Her bölümün üstünde ne yaptığını anlatan yorumlar var. Anlamadığınız bir satır olursa, o konunun ders dosyasına geri dönüp tekrar bakın.

> **Dosya:** `ornekler/05_hepsi_bir_arada.py`

---

## 6. Bonus: getpass — Şifre Girişi

`getpass` modülü, `input()` gibi kullanıcıdan bilgi alır ama yazdığı karakterleri **ekranda göstermez**. Şifre girerken idealdir:

```python
from getpass import getpass

sifre = getpass("Şifre: ")
```

Örnek dosyamızda kullanıcı adı + şifre kontrolü yapan, 3 deneme hakkı veren basit bir giriş sistemi var.

> **Dosya:** `ornekler/06_getpass.py`

---

## Özet Tablosu

| Yapı | Yazılış | Ne İşe Yarar? | Örnek |
|------|---------|---------------|-------|
| break | `break` | Döngüyü tamamen durdurur | `if buldum: break` |
| continue | `continue` | Bu turu atlar, sonrakine geçer | `if puan < 50: continue` |
| f-string | `f"..."` | Değişkeni metin içine gömer | `f"İsim: {isim}"` |
| Sayı formatı | `:.1f` | Ondalık basamak kontrolü | `f"{puan:.1f}"` |
| int() | `int(x)` | Tam sayıya çevirir (kırpar!) | `int("42")` → `42` |
| float() | `float(x)` | Ondalıklı sayıya çevirir | `float("3.14")` → `3.14` |
| round() | `round(x, n)` | Yuvarlar | `round(3.14, 1)` → `3.1` |
| Sözlük | `{}` | Anahtar-değer çiftleri tutar | `{"isim": "Defne"}` |
| .items() | `dict.items()` | Anahtar-değer çiftlerini döner | `for k, v in d.items():` |
| getpass | `getpass("...")` | Gizli giriş alır | Şifre sorma |

---

## Sık Yapılan Hatalar

### 1. break ve continue'yu karıştırmak

```python
# break → döngüyü TAM durdurur
# continue → sadece bu turu atlar
for i in range(5):
    if i == 2:
        break       # 0, 1 yazdırır, 2'de durur
    print(i)

for i in range(5):
    if i == 2:
        continue    # 0, 1, 3, 4 yazdırır, 2'yi atlar
    print(i)
```

### 2. f-string'de f'yi unutmak

```python
isim = "Defne"
print("{isim}")     # {isim}  ← f'yi unuttun!
print(f"{isim}")    # Defne   ← doğru
```

### 3. int() kırpar, yuvarlamaz

```python
int(3.9)    # 3  ← 4 değil! Yuvarlamaz, kırpar.
round(3.9)  # 4  ← Yuvarlama istiyorsan round() kullan
```

### 4. Sözlükte olmayan anahtara erişmek

```python
ogrenci = {"isim": "Defne"}
print(ogrenci["bolum"])   # KeyError! "bolum" anahtarı yok
```

Hata mesajında `KeyError` görürseniz, anahtar adını kontrol edin.

### 5. input() her zaman string döner

```python
sayi = input("Sayı: ")    # "5" (string!)
print(sayi + 3)            # TypeError!
print(int(sayi) + 3)       # 8 (doğru)
```

---

## Ödevler Hakkında

Bu haftanın 5 ödevi var. Kolaydan zora doğru sıralanmıştır:

| Ödev | Zorluk | Konu |
|------|--------|------|
| Ödev 1 — Proje Kartı | Kolay-Orta | Sözlük işlemleri |
| Ödev 2 — Renk Arama Asistanı | Kolay | for + break, for + continue |
| Ödev 3 — Tasarımcı Kartı v2 | Kolay | f-string, sayı formatlama |
| Ödev 4 — Tasarım Hesap Makinesi | Orta | input + float + if/elif + f-string |
| Ödev 5 — Sınıf Listesi Analizi | Zor | Hepsi bir arada |

Her ödev dosyasında `...` ile işaretlenmiş yerler var. Bu yerler sizin doldurmanız gereken boşluklar. Yanlarındaki `# ←` yorumları size ne yazmanız gerektiğini söyler. Dosyanın en altındaki **Beklenen Çıktı** bölümüyle kendi çıktınızı karşılaştırın.

Tüm ödevler `hafta4/odevler/` klasöründedir. Nasıl çalıştırılacağı `odevler/BENIOKU.md` dosyasında anlatılmıştır.

---

## Bir Sonraki Adım

Bu hafta öğrendiğiniz sözlükler, döngü kontrolü, f-string ve matematik işlemleri, Python programlamanın temel yapı taşlarıdır. Bundan sonraki hemen her konuda bu yapıları kullanacaksınız.

Konuları tam kavramak için:

1. Ders dosyalarını (`ornekler/`) açıp çalıştırın
2. Kodları satır satır okuyun, yorumları atlayamayın
3. Küçük değişiklikler yapıp ne olduğunu gözlemleyin
4. Ödevleri sırayla çözün — takılırsanız ders dosyasına geri dönün
