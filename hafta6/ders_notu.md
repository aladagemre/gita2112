# GİTA 2112 — Hafta 6: Fonksiyonlar

> Bu belge, derste anlatılan konuların yazılı özetidir.
> Her bölümün sonunda ilgili kod dosyasına yönlendirme bulunur.
> Kod dosyalarını açıp çalıştırarak burada okuduklarınızı pratiğe dökebilirsiniz.

---

## Hafta 5'ten Hatırlamamız Gerekenler

Geçen hafta şunları öğrenmiştik:

- **f-string** ile değişkenleri metin içine gömmek (`f"Puan: {puan:.1f}"`)
- **Matematik işlemleri** ve tip dönüşümleri (`int()`, `float()`, `round()`)
- **String metodları** (`strip()`, `lower()`, `upper()`)
- **Kısayol operatörler** (`+=`, `-=`, `*=`)

Bu hafta bu bilgilerin üstüne yeni ve çok önemli bir yapı ekleyeceğiz: **fonksiyonlar**.

---

## 1. Fonksiyon Nedir?

Fonksiyon, bir işi yapan ve **tekrar tekrar kullanılabilen** kod parçasıdır. En basit haliyle şöyle görünür:

```python
def topla(a, b):
    return a + b

print(topla(3, 5))   # 8
```

Bu kadar! `def` ile tanımlıyoruz, parantez içinde ne alacağını belirtiyoruz, `return` ile sonucu veriyoruz.

Ama acele etmeyelim — bunu adım adım öğreneceğiz. Önce daha basitinden başlayalım.

### Tasarım Dünyasından Bir Benzetme

Illustrator'da bir **Sembol (Symbol)** tanımladığınızda, onu istediğiniz yere yerleştirirsiniz. Rengi değiştirmek istediğinizde tek bir yerde değiştirince hepsi güncellenir.

İşte **fonksiyon**, kodun sembolüdür: bir kez tanımlarsınız, istediğiniz kadar kullanırsınız.

---

## 2. İlk Fonksiyonumuz — Parametresiz

En basit fonksiyon, hiçbir bilgi almadan hep aynı işi yapar:

```python
def selamla():
    print("Merhaba!")

selamla()   # Merhaba!
selamla()   # Merhaba!
```

Burada iki şey var:

- **Tanımlama** (`def selamla():`) — Fonksiyonu oluşturur ama **çalıştırmaz**. Bir tarif yazmak gibi.
- **Çağırma** (`selamla()`) — Fonksiyonu **çalıştırır**. Tarifi uygulamak gibi.

Sadece `def` yazmak hiçbir şey yapmaz! Fonksiyonu mutlaka çağırmalısınız.

### Fonksiyon Tanımının Yapısı

```python
def fonksiyon_adi():
    # Fonksiyonun içi (girintili)
    print("Bu fonksiyonun içinde")
```

- `def` — "define" (tanımla) kelimesinin kısaltması
- Fonksiyon adı — anlamlı bir isim verin: `selamla`, `cizgi_ciz`, `puan_hesapla`
- `()` ve `:` — zorunlu, unutmayın
- Girintili satırlar — fonksiyonun gövdesi (`if` ve `for` ile aynı mantık)

> **Dosya:** `ornekler/01_ilk_fonksiyon.py`

---

## 3. Parametre — Fonksiyona Bilgi Göndermek

Parametresiz fonksiyon hep aynı şeyi yapar. Peki ya her seferinde farklı bir isimle selamlama istesek?

**Parametre**, fonksiyona dışarıdan gönderdiğimiz bilgidir:

```python
def selamla(isim):
    print(f"Merhaba {isim}!")

selamla("Defne")   # Merhaba Defne!
selamla("Cem")     # Merhaba Cem!
```

InDesign'daki bir **şablon** gibi düşünün: başlık alanı boş, her sayfa için farklı başlık yazıyorsunuz. Parametre, fonksiyondaki o boş alandır.

### Parametre ve Argüman

- **Parametre** — Tanımdaki değişken adı: `def selamla(isim):`
- **Argüman** — Çağırırken verdiğiniz değer: `selamla("Defne")`

Parametreyi "boş kutu", argümanı "kutunun içine koyduğunuz şey" olarak düşünebilirsiniz.

---

## 4. Birden Fazla Parametre

Fonksiyonlar birden fazla bilgi alabilir. Virgülle ayırarak yazılır:

```python
def proje_bilgisi(ad, puan):
    print(f"{ad}: {puan} puan")

proje_bilgisi("Logo Tasarımı", 88)
proje_bilgisi("Film Afişi", 95)
```

**Sıra önemlidir!** İlk argüman ilk parametreye, ikinci argüman ikinci parametreye gider.

`proje_bilgisi(88, "Logo Tasarımı")` yazsanız Python hata vermez ama çıktı yanlış olur: `88: Logo Tasarımı puan`.

> **Dosya:** `ornekler/02_parametreler.py`

---

## 5. return — Fonksiyondan Sonuç Almak

Şimdiye kadar fonksiyonlarımız hep `print` ile ekrana yazdı. Peki ya sonucu bir değişkende saklamak istersek?

### print vs return

```python
# print ile — sonucu KULLANAMAZSINIZ
def topla_yazdir(a, b):
    print(a + b)

sonuc = topla_yazdir(3, 5)   # 8 yazdırır ama...
print(sonuc)                  # None!
```

```python
# return ile — sonucu KULLANABİLİRSİNİZ
def topla(a, b):
    return a + b

sonuc = topla(3, 5)
print(sonuc)           # 8
print(sonuc * 2)       # 16 — başka hesapta kullanabilirsiniz!
```

Farkı anlamak kritiktir:

| | `print` | `return` |
|---|---|---|
| Ne yapar? | Ekrana yazar | Değeri dışarı verir |
| Sonucu kullanabilir miyiz? | Hayır | Evet |
| Fonksiyon ne döner? | `None` | Verdiğimiz değeri |

**Tasarım benzetmesi:** `print` = tasarımınızı ekranda göstermek. `return` = tasarım dosyasını kaydetmek. Ekranda gösterdiyseniz ama kaydetmediyseniz, dosya elinizde yok — başkasına gönderemezsiniz.

### return ile Fonksiyon Biter

`return` çalıştığında fonksiyon **anında biter**. Altındaki satırlar çalışmaz:

```python
def topla(a, b):
    return a + b
    print("Bu satır ASLA çalışmaz!")
```

### return Edilen Değeri Her Yerde Kullanma

```python
def poster_alani(en, boy):
    return en * boy

alan = poster_alani(50, 70)        # Değişkene atama
print(f"Alan: {alan} cm2")          # f-string içinde

toplam = poster_alani(50, 70) + poster_alani(30, 40)  # Hesapta
```

> **Dosya:** `ornekler/03_return.py`

---

## 6. Varsayılan Değerler — Opsiyonel Parametreler

Bazı parametrelere **varsayılan değer** verebiliriz. Çağırırken belirtmezsek varsayılan kullanılır:

```python
def cizgi(n=30):
    print("-" * n)

cizgi()     # ------------------------------ (30 tane)
cizgi(10)   # ---------- (10 tane)
```

Photoshop'taki fırça ayarları gibi düşünün: varsayılan boyut 10px'tir. Değiştirmezseniz 10px kullanır, isterseniz başka değer verirsiniz.

### Birden fazla varsayılan

```python
def cizgi(uzunluk=30, karakter="-"):
    print(karakter * uzunluk)

cizgi()              # 30 tane -
cizgi(20)            # 20 tane -
cizgi(20, "=")       # 20 tane =
cizgi(karakter="*")  # 30 tane *
```

### Sıralama Kuralı

Zorunlu parametreler **önce**, varsayılan değerliler **sonra** gelmelidir:

```python
# DOGRU:
def proje_karti(ad, puan, durum="Devam Ediyor"):
    print(f"{ad} ({durum}) - {puan}")

# YANLIS (hata verir):
def proje_karti(durum="Devam Ediyor", ad, puan):
    print(f"{ad} ({durum}) - {puan}")
```

Kural: "Önce boş kutular (zorunlu), sonra dolu kutular (varsayılan)."

> **Dosya:** `ornekler/04_varsayilan_degerler.py`

---

## 7. Koşullu Fonksiyonlar — if/elif ile Karar Veren Fonksiyonlar

Fonksiyonların içinde `if/elif/else` kullanarak farklı sonuçlar döndürebiliriz:

```python
def basari_durumu(puan):
    if puan >= 90:
        return "Mukemmel"
    elif puan >= 75:
        return "Basarili"
    elif puan >= 60:
        return "Gecti"
    else:
        return "Kaldi"

print(basari_durumu(92))   # Mukemmel
print(basari_durumu(68))   # Gecti
```

Her `return` çalıştığında fonksiyon biter, bu yüzden sadece bir tanesi çalışır.

### Boolean Döndüren Fonksiyonlar

`True` veya `False` döndüren fonksiyonlar `if` ile birlikte çok okunabilir kod üretir:

```python
def gecti_mi(puan, sinir=60):
    return puan >= sinir

if gecti_mi(85):
    print("Tebrikler!")

if gecti_mi(55, sinir=50):
    print("Siniri gecti!")
```

---

## 8. Mevcut Kalıpları Fonksiyona Dönüştürme

Hafta 3-4'te tekrar tekrar yazdığımız kalıpları artık fonksiyona çevirebiliriz.

### Ortalama Hesaplama

```python
# ESKİ — Her seferinde 4 satır yazıyorduk
toplam = 0
for p in puanlar:
    toplam += p
ortalama = toplam / len(puanlar)
```

```python
# YENİ — Bir kez tanımla, istediğin kadar kullan
def ortalama_hesapla(sayilar):
    toplam = 0
    for s in sayilar:
        toplam += s
    return toplam / len(sayilar)

print(ortalama_hesapla([85, 90, 78]))     # 84.3...
print(ortalama_hesapla([75, 88, 92]))     # 85.0
```

Fonksiyonu bir kez yazdık, iki farklı listeyle kullandık.

### Filtreleme

```python
def basarili_bul(projeler, sinir=75):
    sonuc = []
    for proje in projeler:
        if proje["puan"] >= sinir:
            sonuc.append(proje)
    return sonuc
```

Varsayılan değer sayesinde `sinir` belirtmezsek 75, belirtirsek istediğimiz değeri kullanır.

### Fonksiyonları Birlikte Kullanma

Fonksiyonların sonuçlarını birbirine verebiliriz — her adım tek satır:

```python
iyiler = basarili_bul(tum_projeler)       # 1. Basarililari bul
en_iyisi = en_iyi_bul(iyiler)             # 2. En iyisini sec
```

> **Dosya:** `ornekler/05_kaliplar.py`

---

## 9. Hepsini Bir Araya Getirme

Son dosyamızda bu haftanın tüm konularını birleştiren bir mini uygulama var: **Tasarım Stüdyosu Yönetim Sistemi**.

Bu uygulama, Hafta 4'teki "hepsi bir arada" örneğinin **fonksiyonlarla yeniden yazılmış** halidir:

1. **Fonksiyon tanımları** — Her işlem ayrı bir fonksiyon
2. **Ana program** — Fonksiyonları çağırarak iş yapan kısa ve temiz kod
3. **Karşılaştırma** — Geçen haftaki düz kod, şimdi organize ve okunabilir

Dosyayı açıp satır satır okuyun. Özellikle fonksiyonların tanımlandığı bölüm ile çağrıldığı bölümü ayrı ayrı inceleyin.

> **Dosya:** `ornekler/06_hepsi_bir_arada.py`

---

## Özet Tablosu

| Kavram | Yazılış | Ne İşe Yarar? | Örnek |
|--------|---------|---------------|-------|
| Fonksiyon tanımlama | `def f():` | Yeniden kullanılabilir kod bloğu oluşturur | `def selamla():` |
| Fonksiyon çağırma | `f()` | Tanımlanmış fonksiyonu çalıştırır | `selamla()` |
| Parametre | `def f(x):` | Fonksiyona dışarıdan değer alır | `def selamla(isim):` |
| Argüman | `f(deger)` | Çağırırken parametre için değer verir | `selamla("Defne")` |
| return | `return deger` | Fonksiyondan değer döndürür | `return toplam / n` |
| Varsayılan değer | `def f(x=10):` | Belirtilmezse kullanılacak değer | `def cizgi(n=30):` |

---

## Sık Yapılan Hatalar

### 1. Fonksiyonu çağırmayı unutmak

```python
def selamla():
    print("Merhaba!")

# ... hiçbir şey olmaz çünkü çağırmadık!
# Çözüm:
selamla()
```

`if` ve `for` yazıp otomatik çalışmasına alışığız. Fonksiyon farklı — tanımlamak çalışmak demek değil, mutlaka çağırmalısınız.

### 2. Parantezi unutmak

```python
selamla     # Hiçbir şey olmaz! Fonksiyonun adına bakıyor sadece.
selamla()   # Doğru — parantez = "çalıştır" demek
```

### 3. print ile return'u karıştırmak

```python
# YANLIŞ — print kullanır, sonuç None olur
def topla(a, b):
    print(a + b)

sonuc = topla(3, 5)     # 8 yazdırır ama...
print(sonuc)             # None!

# DOĞRU — return kullanır
def topla(a, b):
    return a + b

sonuc = topla(3, 5)
print(sonuc)             # 8
```

**Kural:** Sonucu sadece görmek istiyorsanız `print`. Sonucu kullanmak istiyorsanız `return`.

### 4. Parametre sayısını yanlış vermek

```python
def selamla(isim, bolum):
    print(f"Merhaba {isim}, {bolum} bolumune hos geldin!")

selamla("Defne")   # TypeError! 2 parametre bekliyor, 1 verdiniz
```

### 5. Fonksiyon içindeki değişkeni dışarıda kullanmak

```python
def hesapla():
    sonuc = 42

hesapla()
print(sonuc)   # NameError! Fonksiyon icindeki degisken disarida yasamaz.
```

Çözüm: `return` kullanın.

```python
def hesapla():
    return 42

deger = hesapla()
print(deger)   # 42
```

### 6. Varsayılan değerli parametreyi başa koymak

```python
# YANLIŞ:
def proje_karti(durum="Devam Ediyor", ad, puan):
    ...
# SyntaxError!

# DOĞRU:
def proje_karti(ad, puan, durum="Devam Ediyor"):
    ...
```

### 7. return'den sonra kod yazmak

```python
def topla(a, b):
    return a + b
    print("Hesaplandı!")   # Bu satır ASLA çalışmaz!
```

`return` çalışınca fonksiyon biter. Yazdırma işlemini `return`'den önce yapın.

---

## Ödevler Hakkında

Bu haftanın 5 ödevi var. Kolaydan zora doğru sıralanmıştır:

| Ödev | Zorluk | Konu |
|------|--------|------|
| Ödev 1 — Stüdyo Selamlama | Kolay | def + parametre + çağırma |
| Ödev 2 — Tasarım Hesaplayıcı | Kolay-Orta | return + parametre + matematik |
| Ödev 3 — Harf Notu Sistemi | Orta | if/elif + return + döngüde çağırma |
| Ödev 4 — Proje Kartı Oluşturucu | Orta | Varsayılan değer + f-string |
| Ödev 5 — Portfolyo Analiz Sistemi | Zor | Hepsi bir arada |

Her ödev dosyasında `...` ile işaretlenmiş yerler var. Bu yerler sizin doldurmanız gereken boşluklar. Yanlarındaki `# ←` yorumları size ne yazmanız gerektiğini söyler. Dosyanın en altındaki **Beklenen Çıktı** bölümüyle kendi çıktınızı karşılaştırın.

Tüm ödevler `hafta6/odevler/` klasöründedir. Nasıl çalıştırılacağı `odevler/BENIOKU.md` dosyasında anlatılmıştır.

---

## Bir Sonraki Adım

Bu hafta öğrendiğiniz fonksiyonlar, Python programlamanın en temel soyutlama aracıdır. Bundan sonraki hemen her konuda fonksiyonlar kullanacaksınız.

Konuları tam kavramak için:

1. Ders dosyalarını (`ornekler/`) açıp çalıştırın
2. Kodları satır satır okuyun, yorumları atlamayın
3. Küçük değişiklikler yapıp ne olduğunu gözlemleyin
4. Ödevleri sırayla çözün — takılırsanız ders dosyasına geri dönün
