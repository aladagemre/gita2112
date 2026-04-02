# GİTA 2112 — Hafta 4: Sözlükler ve Break/Continue

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

Bu hafta bu bilgilerin üstüne yeni araçlar ekleyeceğiz: sözlükler ve döngü kontrolü.

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

## 3. Hepsini Bir Araya Getirme

Son dosyamızda (`ornekler/03_hepsi_bir_arada.py`) bu haftanın tüm konularını birleştiren bir mini uygulama var: **Proje Takip Sistemi**.

Bu uygulama şunları yapıyor:

1. **Sözlük listesi** — Her proje bir sözlük (ad, kategori, puan), hepsi bir listede
2. **continue ile filtreleme** — Düşük puanlı projeleri atlama
3. **Toplam ve ortalama** — Döngüyle puan toplama
4. **En iyi projeyi bulma** — Döngüyle karşılaştırma
5. **Kategoriye göre filtreleme** — Döngü + if ile eşleşenleri bulma
6. **Kategori sayma** — Boş sözlük oluşturup dinamik olarak doldurma

Bu dosyayı açıp satır satır okuyun. Her bölümün üstünde ne yaptığını anlatan yorumlar var. Anlamadığınız bir satır olursa, o konunun ders dosyasına geri dönüp tekrar bakın.

> **Dosya:** `ornekler/03_hepsi_bir_arada.py`

---

## 4. Bonus: getpass — Şifre Girişi

`getpass` modülü, `input()` gibi kullanıcıdan bilgi alır ama yazdığı karakterleri **ekranda göstermez**. Şifre girerken idealdir:

```python
from getpass import getpass

sifre = getpass("Şifre: ")
```

Örnek dosyamızda kullanıcı adı + şifre kontrolü yapan, 3 deneme hakkı veren basit bir giriş sistemi var.

> **Dosya:** `ornekler/04_getpass.py`

---

## Özet Tablosu

| Yapı | Yazılış | Ne İşe Yarar? | Örnek |
|------|---------|---------------|-------|
| Sözlük | `{}` | Anahtar-değer çiftleri tutar | `{"isim": "Defne"}` |
| .items() | `dict.items()` | Anahtar-değer çiftlerini döner | `for k, v in d.items():` |
| break | `break` | Döngüyü tamamen durdurur | `if buldum: break` |
| continue | `continue` | Bu turu atlar, sonrakine geçer | `if puan < 50: continue` |
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

### 2. Sözlükte olmayan anahtara erişmek

```python
ogrenci = {"isim": "Defne"}
print(ogrenci["bolum"])   # KeyError! "bolum" anahtarı yok
```

Hata mesajında `KeyError` görürseniz, anahtar adını kontrol edin.

### 3. Sözlük anahtarında yazım hatası

```python
ogrenci = {"isim": "Defne"}
print(ogrenci["İsim"])   # KeyError! Büyük/küçük harf fark eder
```

### 4. Sözlük listesinde değere erişmek

```python
sinif = [{"isim": "Defne"}, {"isim": "Cem"}]

# YANLIŞ:
print(sinif["isim"])    # TypeError! sinif bir liste, sözlük değil

# DOĞRU:
print(sinif[0]["isim"])  # Defne — önce indeksle listeden al, sonra anahtarla sözlükten
```

---

## Ödevler Hakkında

Bu haftanın 3 ödevi var. Kolaydan zora doğru sıralanmıştır:

| Ödev | Zorluk | Konu |
|------|--------|------|
| Ödev 1 — Proje Kartı | Kolay-Orta | Sözlük işlemleri |
| Ödev 2 — Renk Arama Asistanı | Kolay | for + break, for + continue |
| Ödev 3 — Tasarım Ekibi Analizi | Zor | Hepsi bir arada |

Her ödev dosyasında `...` ile işaretlenmiş yerler var. Bu yerler sizin doldurmanız gereken boşluklar. Yanlarındaki `# ←` yorumları size ne yazmanız gerektiğini söyler. Dosyanın en altındaki **Beklenen Çıktı** bölümüyle kendi çıktınızı karşılaştırın.

Tüm ödevler `hafta4/odevler/` klasöründedir. Nasıl çalıştırılacağı `odevler/BENIOKU.md` dosyasında anlatılmıştır.

---

## Bir Sonraki Adım

Bu hafta öğrendiğiniz sözlükler ve döngü kontrolü, Python programlamanın temel yapı taşlarıdır. Gelecek hafta bu yapıların üzerine **f-string formatlama**, **matematik işlemleri** ve **tip dönüşümleri** ekleyeceğiz.

Konuları tam kavramak için:

1. Ders dosyalarını (`ornekler/`) açıp çalıştırın
2. Kodları satır satır okuyun, yorumları atlayamayın
3. Küçük değişiklikler yapıp ne olduğunu gözlemleyin
4. Ödevleri sırayla çözün — takılırsanız ders dosyasına geri dönün
