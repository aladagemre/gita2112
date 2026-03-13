# GİTA 2112 — Hafta 3: Listeler, Döngüler ve Demetler

> Bu belge, derste anlatılan konuların yazılı özetidir.
> Her bölümün sonunda ilgili kod dosyasına yönlendirme bulunur.
> Kod dosyalarını açıp çalıştırarak burada okuduklarınızı pratiğe dökebilirsiniz.

---

## Hafta 2'den Hatırlamamız Gerekenler

Geçen hafta şunları öğrenmiştik:

- **print()** ile ekrana bir şey yazdırmak
- **Değişkenler** ile bilgileri saklamak (`isim = "Defne"`, `yas = 20`)
- **input()** ile kullanıcıdan bilgi almak
- **if / elif / else** ile koşullara göre farklı şeyler yapmak

Bu hafta bu bilgilerin hepsini kullanacağız — üstüne yeni yapılar ekleyeceğiz. Eğer geçen haftanın konularında takıldığınız bir yer varsa, önce orayı pekiştirmenizi öneririm.

---

## 1. Listeler — Birden Fazla Şeyi Bir Arada Tutmak

### Sorun

Diyelim ki bir tasarım projesi için renk paleti hazırlıyorsunuz. Dört renginiz var:

```python
renk1 = "kırmızı"
renk2 = "mavi"
renk3 = "yeşil"
renk4 = "sarı"
```

Bu çalışır, ama 20 renk olsa 20 ayrı değişken mi oluşturacaksınız? İşte **liste** tam da bu sorunu çözer.

### Çözüm: Liste

Liste, birden fazla değeri **tek bir değişkende** tutan bir yapıdır. Köşeli parantez `[]` ile oluşturulur:

```python
renkler = ["kırmızı", "mavi", "yeşil", "sarı"]
```

Artık dört renk tek bir yerde. İstediğimiz zaman herhangi birine ulaşabiliriz.

### Elemanlara Erişim: İndeks

Listedeki her elemanın bir sıra numarası vardır. Buna **indeks** denir. Dikkat: **indeksler 0'dan başlar**, 1'den değil.

```
  indeks:   0          1        2        3
  renkler: ["kırmızı", "mavi", "yeşil", "sarı"]
```

```python
print(renkler[0])    # kırmızı  (ilk eleman)
print(renkler[2])    # yeşil    (üçüncü eleman)
print(renkler[-1])   # sarı     (son eleman)
```

Sondan saymak için negatif indeks kullanırız: `-1` son eleman, `-2` sondan ikinci.

### Listenin Uzunluğu: len()

Listede kaç eleman olduğunu öğrenmek için `len()` kullanırız:

```python
print(len(renkler))  # 4
```

> **Dosya:** `ornekler/01_listeler.py`

---

## 2. Liste İşlemleri — Ekleme, Silme, Arama

Bir liste oluşturduktan sonra içeriğini değiştirebiliriz. En sık kullanılan işlemler:

### Eleman Ekleme: .append()

Listenin **sonuna** yeni bir eleman ekler:

```python
malzemeler = ["kağıt", "boya", "fırça"]
malzemeler.append("yapıştırıcı")
# Sonuç: ["kağıt", "boya", "fırça", "yapıştırıcı"]
```

### Eleman Silme: .remove()

Verdiğiniz değeri listede bulur ve çıkarır:

```python
malzemeler.remove("boya")
# Sonuç: ["kağıt", "fırça", "yapıştırıcı"]
```

### Eleman Güncelleme: İndeksle Atama

Bir elemanın değerini değiştirmek için indeksini kullanırız:

```python
malzemeler[0] = "karton"
# Sonuç: ["karton", "fırça", "yapıştırıcı"]
```

### Arama: in Operatörü

Bir elemanın listede olup olmadığını kontrol eder. Sonuç `True` veya `False` olur — Hafta 2'deki boolean değerleri hatırlayın:

```python
print("fırça" in malzemeler)   # True
print("kalem" in malzemeler)   # False
```

Bunu `if` ile birlikte de kullanabiliriz:

```python
if "fırça" in malzemeler:
    print("Fırça mevcut!")
```

### Sıralama: .sort()

Listeyi alfabetik (metin) veya küçükten büyüğe (sayı) sıralar:

```python
puanlar = [85, 92, 78, 95, 60]
puanlar.sort()
# Sonuç: [60, 78, 85, 92, 95]
```

> **Dosya:** `ornekler/02_liste_islemleri.py`

---

## 3. for Döngüsü — Bir İşi Tekrar Tekrar Yapmak

### Sorun

Ekrana "Katman 1", "Katman 2", ... , "Katman 10" yazdırmak istiyorsunuz. On tane `print` mi yazacaksınız?

```python
print("Katman 1")
print("Katman 2")
print("Katman 3")
# ... 10'a kadar böyle devam mı?
```

Bu hem uzun hem de hataya açık. İşte **döngü** bu tekrarı otomatikleştirir.

### for + range()

`for` döngüsü, belirli bir sayıda tekrar yapmak için kullanılır. `range()` fonksiyonu ise sayı dizisi üretir:

```python
for katman in range(1, 11):
    print("Katman", katman)
```

Bu iki satır, 10 ayrı print yazmakla aynı işi yapar. `range(1, 11)` ifadesi 1'den 10'a kadar sayıları üretir. **Bitiş değeri dahil değildir** — yani 11 yazıyoruz ama 10'a kadar sayar.

### range() Kullanımları

`range()` fonksiyonunun farklı kullanımları vardır:

| Kullanım | Ürettiği Sayılar | Açıklama |
|----------|-------------------|----------|
| `range(5)` | 0, 1, 2, 3, 4 | Sıfırdan başlar, 5 tane üretir |
| `range(1, 11)` | 1, 2, 3, ..., 10 | 1'den 10'a kadar |
| `range(0, 11, 2)` | 0, 2, 4, 6, 8, 10 | İkişer ikişer sayar |
| `range(10, 0, -1)` | 10, 9, 8, ..., 1 | Geri sayım |

Üçüncü parametre **adım büyüklüğüdür**. Negatif adım verilirse geriye doğru sayar.

### Girintinin Önemi

`for` satırından sonra gelen ve **girintili yazılan** satırlar döngünün içindedir. Girintisiz satır döngünün dışındadır:

```python
for i in range(3):
    print("İçeride:", i)   # 3 kez çalışır
print("Dışarıda")          # 1 kez çalışır (döngüden sonra)
```

Bu kural `if/else`'ten tanıdık gelecektir — orada da girinti aynı şekilde çalışıyordu.

> **Dosya:** `ornekler/03_for_dongusu.py`

---

## 4. for ile Liste Gezme — Listelerin Gerçek Gücü

Şimdiye kadar `range()` ile sayı dizisi ürettik. Ama `for` döngüsünün asıl gücü **bir listenin elemanlarını tek tek gezmektir**:

```python
projeler = ["Logo Tasarımı", "Poster", "Web Sitesi"]

for proje in projeler:
    print("-", proje)
```

Çıktı:

```
- Logo Tasarımı
- Poster
- Web Sitesi
```

Her turda `proje` değişkeni listenin sıradaki elemanını alır. İlk turda `"Logo Tasarımı"`, ikinci turda `"Poster"`, üçüncü turda `"Web Sitesi"`.

### Numaralı Listeleme: enumerate()

Hem sıra numarasını hem elemanı birlikte almak istiyorsak `enumerate()` kullanırız:

```python
for sira, proje in enumerate(projeler, start=1):
    print(str(sira) + ".", proje)
```

Çıktı:

```
1. Logo Tasarımı
2. Poster
3. Web Sitesi
```

`start=1` diyerek numaralandırmayı 1'den başlatıyoruz. Yazmazsak 0'dan başlar.

### Döngü İçinde if Kullanma

Döngü ile koşulu birleştirerek **filtreleme** yapabiliriz. Hafta 2'den bildiğimiz `if/elif/else` yapısını döngünün içine koyuyoruz:

```python
puanlar = [85, 42, 91, 67, 73]

for puan in puanlar:
    if puan >= 70:
        print(puan, "→ Başarılı")
    else:
        print(puan, "→ Yetersiz")
```

### Toplam ve Ortalama Hesaplama

Bir listedeki sayıları toplamak için sık kullanılan bir kalıp vardır:

```python
toplam = 0                  # Boş bir kutu oluştur
for puan in puanlar:
    toplam = toplam + puan  # Her turda kutuya ekle

ortalama = toplam / len(puanlar)
```

Mantık şöyle: önce `toplam = 0` diyerek boş bir kutu oluşturuyoruz. Döngünün her adımında bu kutuya bir puan daha ekliyoruz. Döngü bitince kutunun içinde toplam var.

### Filtreleyerek Yeni Liste Oluşturma

Belirli koşulu sağlayan elemanları yeni bir listede toplayabiliriz:

```python
basarili = []               # Boş liste oluştur
for puan in puanlar:
    if puan >= 70:
        basarili.append(puan)   # Koşulu sağlayanı ekle

print(basarili)  # [85, 91, 73]
```

### İki Listeyi Eşleştirme: range(len())

Bazen iki farklı listenin aynı sıradaki elemanlarını birlikte kullanmak isteriz. Bu durumda indeks numarasıyla gezeriz:

```python
isimler = ["Logo", "Poster", "Web"]
puanlar = [88, 72, 95]

for i in range(len(isimler)):
    print(isimler[i], "→", puanlar[i], "puan")
```

`range(len(isimler))` ifadesi `range(3)` yani `0, 1, 2` üretir. `i` değişkeni her turda bir indeks numarası olur ve aynı `i` ile her iki listeden de eleman alırız.

> **Dosya:** `ornekler/04_for_liste.py`

---

## 5. while Döngüsü — Koşul Sağlandığı Sürece Tekrarla

`for` döngüsü **kaç kez tekrar edeceğini önceden bildiğimiz** durumlarda idealdir. Peki ya kaç kez tekrar edeceğimizi bilmiyorsak? Mesela kullanıcı doğru şifreyi girene kadar sormak istiyorsak?

İşte `while` döngüsü budur: **koşul doğru olduğu sürece** çalışmaya devam eder.

### Temel Kullanım

```python
sayac = 5
while sayac > 0:
    print(sayac)
    sayac = sayac - 1   # Her turda 1 azalt
```

Her turda ekrana sayacın değerini yazar: 5, 4, 3, 2, 1. Sonra `sayac` 0 olunca `0 > 0` koşulu `False` olur ve döngü biter.

**Çok önemli:** `sayac = sayac - 1` satırını yazmazsanız koşul hiçbir zaman `False` olmaz ve program sonsuza kadar çalışır. Buna **sonsuz döngü** denir. Böyle bir durumda `Ctrl+C` ile programı durdurabilirsiniz.

### break ile Döngüden Çıkma

`break` komutu döngüyü **anında** sonlandırır:

```python
while True:
    cevap = input("Çıkmak için 'evet' yaz: ")
    if cevap == "evet":
        break           # Döngüyü sonlandır
    print("Devam ediyoruz...")
```

`while True` ifadesi "sonsuza kadar çalış" demektir — ama içerideki `break` sayesinde koşul sağlandığında çıkarız. Bu kalıp, kullanıcıdan tekrar tekrar bilgi almak istediğimizde çok kullanışlıdır.

### for mu, while mı?

| Durum | Hangisini kullanmalı? |
|-------|-----------------------|
| Kaç kez döneceğini biliyorsun | `for` |
| Bir listeyi geziyorsun | `for` |
| Kullanıcı bir şey yapana kadar bekle | `while` |
| Koşula bağlı, ne zaman biteceği belirsiz | `while` |

> **Dosya:** `ornekler/05_while_dongusu.py`

---

## 6. Demetler (Tuples) — Değiştirilemeyen Listeler

### Liste ile Demet Arasındaki Fark

Demet, listeye çok benzer. Tek farkı: **oluşturulduktan sonra değiştirilemez**. Normal parantez `()` ile oluşturulur:

```python
koordinat = (100, 250)    # Demet
koordinat2 = [100, 250]   # Liste
```

Listeye yeni eleman ekleyebilir, çıkarabilir, değiştirebilirsiniz. Demete **hiçbir şey yapamazsınız** — sadece okuyabilirsiniz.

### Neden Değiştirilemeyen Bir Şey Kullanalım?

Bazı veriler değişmemeli. Mesela tasarımda kullandığınız bir rengin RGB kodu:

```python
kirmizi = (255, 0, 0)     # Kırmızı rengin RGB değerleri
mavi = (0, 0, 255)        # Mavi rengin RGB değerleri
```

Bu değerler sabittir. Birisi yanlışlıkla `kirmizi[0] = 100` yazarsa Python hata verir ve sizi korur. Liste olsaydı sessizce değişirdi.

### Ne Zaman Liste, Ne Zaman Demet?

| Veri | Yapı | Neden? |
|------|------|--------|
| Alışveriş listesi | Liste `[]` | Eleman eklenip çıkarılacak |
| RGB renk kodu | Demet `()` | Sabit, değişmemeli |
| Proje isimleri | Liste `[]` | Yeni proje eklenebilir |
| Ekran çözünürlüğü | Demet `()` | 1920x1080 sabittir |

### İndeksle Erişim

Tıpkı listelerde olduğu gibi indeksle erişiriz:

```python
boyutlar = (1920, 1080)
print(boyutlar[0])   # 1920
print(boyutlar[1])   # 1080
```

> **Dosya:** `ornekler/06_demetler.py`

---

## Özet Tablosu

| Yapı | Yazılış | Ne İşe Yarar? | Örnek |
|------|---------|---------------|-------|
| Liste | `[]` | Birden fazla değeri sıralı tutar | `["kırmızı", "mavi"]` |
| Demet | `()` | Sabit değerleri tutar (değiştirilemez) | `(255, 0, 0)` |
| for + range | `for i in range(n):` | Belirli sayıda tekrar | `for i in range(10):` |
| for + liste | `for x in liste:` | Liste elemanlarını gezme | `for renk in renkler:` |
| while | `while koşul:` | Koşul sağlandığı sürece tekrar | `while sayac > 0:` |

---

## Sık Yapılan Hatalar

### 1. İndeks 0'dan başlar

```python
renkler = ["kırmızı", "mavi", "yeşil"]
print(renkler[1])   # "mavi" — "kırmızı" değil!
print(renkler[0])   # "kırmızı" — ilk eleman 0'dır
```

### 2. range() bitiş değeri dahil değildir

```python
for i in range(1, 5):
    print(i)
# Çıktı: 1, 2, 3, 4 — 5 yok!
```

5'i de dahil etmek istiyorsanız `range(1, 6)` yazmalısınız.

### 3. while döngüsünde sayacı güncellemeyi unutmak

```python
sayac = 5
while sayac > 0:
    print(sayac)
    # sayac = sayac - 1   ← Bu satır unutulursa sonsuz döngü!
```

Sonsuz döngüye girerseniz `Ctrl+C` ile durdurun.

### 4. Demeti değiştirmeye çalışmak

```python
renk = (255, 0, 0)
renk[0] = 200   # TypeError! Demet değiştirilemez
```

Değiştirmeniz gerekiyorsa demet yerine liste kullanın.

---

## Ödevler Hakkında

Bu haftanın 4 ödevi var. Kolaydan zora doğru sıralanmıştır:

| Ödev | Zorluk | Konu |
|------|--------|------|
| Ödev 1 — Tasarım Malzemeleri | Kolay | Liste oluşturma, ekleme, silme |
| Ödev 2 — Katman Oluşturucu | Kolay | for + range() |
| Ödev 3 — Renk Paleti Analizi | Orta | for + liste + if |
| Ödev 4 — Renk Tahmin Oyunu | Orta-Zor | while True + break |

Her ödev dosyasında `...` ile işaretlenmiş yerler var. Bu yerler sizin doldurmanız gereken boşluklar. Yanlarındaki `# ←` yorumları size ne yazmanız gerektiğini söyler. Dosyanın en altındaki **Beklenen Çıktı** bölümüyle kendi çıktınızı karşılaştırın.

Tüm ödevler `hafta3/odevler/` klasöründedir. Nasıl çalıştırılacağı `odevler/BENIOKU.md` dosyasında anlatılmıştır.

---

## Bir Sonraki Adım

Bu hafta öğrendiğiniz listeler, döngüler ve demetler, Python programlamanın temel yapı taşlarıdır. Gelecek hafta bu yapıların üzerine **sözlükler**, **f-string formatlama**, **continue**, **matematik işlemleri** ve daha fazlasını ekleyeceğiz.

Konuları tam kavramak için:

1. Ders dosyalarını (`ornekler/`) açıp çalıştırın
2. Kodları satır satır okuyun, yorumları atlayamayın
3. Küçük değişiklikler yapıp ne olduğunu gözlemleyin
4. Ödevleri sırayla çözün — takılırsanız ders dosyasına geri dönün
