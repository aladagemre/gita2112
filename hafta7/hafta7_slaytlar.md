# Hafta 7

## Kod Yazmadan Önce Düşünmek

GITA2112 — Bilgisayar Programlamaya Giriş

18 Nisan 2026

---

## Bugünün Planı

- **Blok 1** — 6 haftanın hatırlaması + Tahmin Et
- **Blok 2** — Storyboard Atölyesi
- **Blok 3** — Parsons Puzzle
- **Blok 4** — Niyet → Pseudocode → Kod (vize 3.3 provası)

Toplam 150 dk, üç ara.

Defter + kalem yanınızda olsun.

---

## Bu Hafta Yeni Python Yok

Yeni bir **süreç** var:

```
NİYET → STORYBOARD → PSEUDOCODE → PYTHON
(Türkçe) (Çizim)    (Yarı kod)   (Gerçek kod)
```

Bir afiş brifinden Photoshop'a nasıl geçiyorsanız, niyetten koda da aynı şekilde geçeceksiniz.

---

# Blok 1

## Hatırlama Haritası

20 dakika. 6 haftanın özeti + Tahmin Et mikroları.

---

## Açılış Sorusu

Python'u öğrenmeye başlayalı 6 hafta oldu.

**Chat'e tek kelime yazın:**

Aklınıza ilk gelen Python kavramı nedir?

---

## Hafta 2 — Temeller

### Değişken, print, input, if/elif/else

```python
isim = input("Adınız? ")
yas = int(input("Yaşınız? "))

if yas >= 18:
    print(f"Merhaba {isim}, hoş geldin.")
else:
    print(f"{isim}, henüz 18 yaşından küçüksün.")
```

**Tasarım bağlantısı:** Etkileşimli bir form — input, if, print.

---

## Tahmin Et — Hafta 2

Yukarıdaki kod çalıştı. Kullanıcı adını **"Defne"**, yaşını **"17"** yazdı.

**Ekrana ne yazar?**

Tek satır halinde chat'e yazın.

---

## Cevap — Hafta 2

```
Defne, henüz 18 yaşından küçüksün.
```

Öğrenci 17 olduğu için **else** dalı çalışır.

Bu tür soru vize'de Bölüm **1.1 (Kod Yorumlama)** olarak çıkacak.

---

## Hafta 3 — Listeler ve Döngüler

### Liste, for, while, range

```python
renkler = ["kırmızı", "mavi", "sarı", "yeşil"]

for renk in renkler:
    print(f"Palette var: {renk}")
```

**Tasarım bağlantısı:** Moodboard, renk paleti, grid kareleri — hepsi liste. For = tek tek filtre uygulamak.

---

## Tahmin Et — Hafta 3

```python
for i in range(3):
    print(i * 2)
```

Ekrana ne yazar?

(3 satır)

---

## Cevap — Hafta 3

```
0
2
4
```

`range(3)` 0'dan başlar, 3 **dahil değil**. Her sayı 2 ile çarpılır.

---

## Hafta 4 — Sözlük ve Sözlük Listesi

### Sözlük, break, continue, sözlük listesi

```python
projeler = [
    {"ad": "Logo", "puan": 88},
    {"ad": "Afiş", "puan": 95},
]

for p in projeler:
    print(f"{p['ad']}: {p['puan']}")
```

**Tasarım bağlantısı:** Her proje bir InDesign sayfası. Sözlük = şablon. Liste = sayfaların bütünü.

---

## Tahmin Et — Hafta 4

Yukarıdaki `projeler` listesi için:

```python
print(projeler[1]["ad"])
```

Ekrana ne yazar?

---

## Cevap — Hafta 4

```
Afiş
```

Index `1` **ikinci** sözlüktür; onun `"ad"` anahtarı `"Afiş"`.

---

## Hafta 5 — f-string, Matematik, Tip

### String formatlama, int/float, kısayol operatörler

```python
isim = "Defne"
puan = 87.345

print(f"{isim}: {puan:.1f} puan")
# Defne: 87.3 puan

a = 17
print(a // 5)   # 3   (tam bölme)
print(a % 5)    # 2   (mod)
```

**Tasarım bağlantısı:** Grid hesapları, oran-orantı, veri formatlama.

---

## Tahmin Et — Hafta 5

```python
print("5" + 3)
```

Ekrana ne yazar?

---

## Cevap — Hafta 5

```
TypeError: can only concatenate str (not "int") to str
```

String + int birleştirilemez. Tip hatası.

Doğrusu: `print("5" + str(3))` → `53` veya `print(int("5") + 3)` → `8`.

---

## Hafta 6 — Fonksiyonlar

### def, parametre, return, varsayılan değerler

```python
def ortalama(sayilar):
    toplam = 0
    for s in sayilar:
        toplam += s
    return toplam / len(sayilar)

print(ortalama([85, 90, 78]))   # 84.3...
```

**Tasarım bağlantısı:** Illustrator sembolü — bir kez tasarla, her yerde kullan.

---

## Tahmin Et — Hafta 6

```python
def topla(a, b):
    return a + b

sonuc = topla(2, 3) + topla(4, 1)
```

`sonuc` kaç olur?

---

## Cevap — Hafta 6

```
10
```

İki çağrı ayrı ayrı çalışır: `5 + 5 = 10`.

Fonksiyonlar **değer döndürür**; o değer başka hesaplarda kullanılabilir.

---

## Bu Hafta (7) — Süreç

Şimdiye kadar hoca yazdı, siz aynısını yazdınız. Ama beyaz ekran karşınıza gelince — kimse başlayamıyor.

**Bu hafta:**

```
NİYET → STORYBOARD → PSEUDOCODE → PYTHON
```

Defter + kalem yanınızda.

---

## Zihin Haritası

```
               ┌─ Hafta 2 ──── değişken, print, input, if
               │
               ├─ Hafta 3 ──── liste, for, while
               │
    PYTHON ────┼─ Hafta 4 ──── sözlük, sözlük listesi, break
               │
               ├─ Hafta 5 ──── f-string, matematik, tip
               │
               ├─ Hafta 6 ──── fonksiyon (def, return)
               │
               └─ Hafta 7 ──── SÜREÇ: niyet → kod
```

Chat'e: "Bir dala eklemek istediğiniz kavram var mı?"

---

## Ara — 5 dk

09:20 — 09:25

Defter + kalem hazırlayın.

9:25'te storyboard atölyesine geçiyoruz.

---

# Blok 2

## Storyboard Atölyesi

35 dakika. Defterinize çizeceksiniz.

---

## Neden Storyboard?

Bir afiş tasarlarken ne yapıyorsunuz?

- Doğrudan InDesign açıyor musunuz?
- Yoksa önce **eskiz** mi çiziyorsunuz?

Kod yazmadan önce de aynısı:

**4-6 kare. Her karede tek bir şey.**

Bu, **çizim değil** — düşünce haritası. Kutu + iki kelime.

---

## Süreç Diyagramı

```
 NİYET
   ↓
 STORYBOARD  ← defterinize
   ↓
 PSEUDOCODE  ← Türkçe ağırlıklı
   ↓
 PYTHON      ← gerçek kod
   ↓
 TEST        ← çalıştır, çıktıyı gör
```

---

## Senaryo 1 — Kolay (Hoca Demosu)

### Niyet

> **"Bir renk listesinde sıcak bir rengin kaç kez geçtiğini say."**

*(Not: "çeşit" değil "tekrar" sayıyoruz.)*

```python
renkler = ["kırmızı", "mavi", "turuncu", "yeşil", "sarı", "mor", "kırmızı"]
sicak_renkler = ["kırmızı", "turuncu", "sarı"]
```

Beklenen çıktı: `4`

---

## Senaryo 1 — Storyboard

```
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│ KARE 1   │  │ KARE 2   │  │ KARE 3   │  │ KARE 4   │
│          │  │          │  │          │  │          │
│ Başlangıç│  │ Her renk │  │ Renk     │  │ Döngü    │
│ sayac=0  │  │ için     │  │ sıcak mı?│  │ bitti.   │
│          │  │ (döngü)  │  │ Evet →   │  │ Sayacı   │
│ Boş kutu │  │          │  │ +1       │  │ yazdır.  │
└──────────┘  └──────────┘  └──────────┘  └──────────┘
```

---

## Senaryo 1 — Pseudocode

```
sayac diye bir değişken aç, başlangıçta 0
renkler listesindeki her renk için:
    eğer renk, sıcak_renkler listesindeyse:
        sayacı 1 artır
sayacı yazdır
```

---

## Senaryo 1 — Python

```python
renkler = ["kırmızı", "mavi", "turuncu", "yeşil", "sarı", "mor", "kırmızı"]
sicak_renkler = ["kırmızı", "turuncu", "sarı"]

sayac = 0
for renk in renkler:
    if renk in sicak_renkler:
        sayac += 1

print(sayac)   # 4
```

---

## Senaryo 2 — Orta (Hep Birlikte)

### Niyet

> **"Bir puanlar listesi al. 60'ın altında kaç puan olduğunu say ve bu düşük puanların ortalamasını bul."**

```python
puanlar = [88, 45, 92, 58, 72, 39, 81, 65, 54]
```

Beklenen çıktı:
```
60 altı puan sayısı: 4
Ortalaması: 49.0
```

**Defterinize 4-5 kare çizin. 3 dakika.**

---

## Senaryo 2 — Storyboard

```
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│ KARE 1 │ │ KARE 2 │ │ KARE 3 │ │ KARE 4 │ │ KARE 5 │
│        │ │        │ │        │ │        │ │        │
│ sayac=0│ │ Her    │ │ <60 ise│ │ Döngü  │ │ İkisini│
│toplam=0│ │ puan   │ │ sayacı │ │ bitti. │ │ yazdır │
│        │ │ için   │ │ artır, │ │ ort =  │ │        │
│ İki    │ │        │ │ topla  │ │ toplam │ │        │
│ boş    │ │        │ │        │ │ /sayac │ │        │
└────────┘ └────────┘ └────────┘ └────────┘ └────────┘
```

---

## Senaryo 2 — Pseudocode

```
sayac = 0 (başlangıç)
toplam = 0 (başlangıç)
puanlar listesindeki her puan için:
    eğer puan 60'tan küçükse:
        sayacı 1 artır
        puanı toplama ekle
ortalama = toplam / sayac
"60 altı puan sayısı: {sayac}" yazdır
"Ortalaması: {ortalama}" yazdır
```

---

## Senaryo 2 — Python

```python
puanlar = [88, 45, 92, 58, 72, 39, 81, 65, 54]

sayac = 0
toplam = 0

for puan in puanlar:
    if puan < 60:
        sayac += 1
        toplam += puan

ortalama = toplam / sayac
print(f"60 altı puan sayısı: {sayac}")
print(f"Ortalaması: {ortalama}")
```

**Çıktı:** `4`, `49.0` (45+58+39+54 = 196, 196/4 = 49.0)

---

## Senaryo 3 — Zor (Breakout)

### Niyet

> **"Projeler listesinde ortalamanın ÜSTÜNDE puan alan projelerin adlarını yazdır."**

```python
projeler = [
    {"ad": "Logo Tasarımı",  "puan": 88},
    {"ad": "Film Afişi",     "puan": 95},
    {"ad": "Ürün Ambalajı",  "puan": 72},
    {"ad": "Web Arayüzü",    "puan": 91},
    {"ad": "Dergi Kapağı",   "puan": 64},
    {"ad": "Mobil Uygulama", "puan": 85},
]
```

Beklenen ortalama: `82.5`. Üstündekiler: Logo, Film Afişi, Web Arayüzü, Mobil Uygulama.

---

## Senaryo 3 — Kritik Kavrama

> Bu senaryo **iki döngü** gerektirir.
>
> İlk döngü ortalamayı hesaplar, ikinci döngü karşılaştırma yapar.
>
> **Tek döngüyle yapılamaz** — çünkü ortalamayı bilmeden hangi proje "üstünde" olduğunu söyleyemezsiniz.

---

## Senaryo 3 — Storyboard (6 kare)

```
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│ KARE 1  │ │ KARE 2  │ │ KARE 3  │ │ KARE 4  │ │ KARE 5  │ │ KARE 6  │
│         │ │         │ │         │ │         │ │         │ │         │
│toplam=0 │ │ Her     │ │ Döngü   │ │ Ortalama│ │ Her     │ │ >ortsa  │
│         │ │ proje   │ │ bitti.  │ │ yazdır  │ │ proje   │ │ adını   │
│ Tek boş │ │ puanı   │ │ ort =   │ │         │ │ için    │ │ yazdır  │
│ kutu    │ │ topla   │ │ toplam/n│ │         │ │ (2.dön) │ │         │
└─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
```

---

## Senaryo 3 — Pseudocode

```
toplam = 0
projeler listesindeki her proje için:
    toplamı projenin puanı kadar artır
ortalama = toplam / projeler sayısı
"Ortalama: {ortalama}" yazdır

"Ortalamanın üstündekiler:" yazdır
projeler listesindeki her proje için:
    eğer projenin puanı ortalamadan büyükse:
        "- {projenin adı}" yazdır
```

---

## Senaryo 3 — Python

```python
# 1. döngü — ortalamayı hesapla
toplam = 0
for proje in projeler:
    toplam += proje["puan"]

ortalama = toplam / len(projeler)
print(f"Ortalama: {ortalama}")

# 2. döngü — ortalamanın üstündekileri yazdır
print("Ortalamanın üstündekiler:")
for proje in projeler:
    if proje["puan"] > ortalama:
        print(f"- {proje['ad']}")
```

---

## Senaryo 3 — Breakout Talimatı

```
2 kişilik breakout. 10 dakika.

Rol değişimi:
  5 dk — 1. kişi storyboard, 2. kişi pseudocode
  5 dk — değişin: 1. pseudocode, 2. Python

İkiliden biri kamerasını defter/ekranına çevirsin.
Zaman kalırsa Python'u çalıştırın.

Ana odaya dönünce defterinizi göstereceksiniz.
```

---

## Ara — 10 dk

10:00 — 10:10

Kahve, esneme, pencere aç.

10:10'da Parsons puzzle'larına geçiyoruz.

---

# Blok 3

## Parsons Puzzle

35 dakika. Karışık kod satırlarını doğru sıraya koyacaksınız.

---

## İki Taktik

1. **Tanımlamayı bulun** — hangi satır bir değişken yaratıyor? O satır önce gelmeli.

2. **Girintilere dikkat** — girintili satırlar bir başka satırın **içindedir**.

Çalıştırmadan önce **zihinde yürütün**: bu kod çalıştığında ne olurdu?

---

## Puzzle 1 — Kolay

### Görev

> **"Bir puanlar listesinin toplamını hesaplayıp yazdır."**

Beklenen çıktı: `Toplam: 340`

### Karışık Satırlar

```
A.   toplam = toplam + puan
B.   puanlar = [85, 90, 78, 87]
C.   print(f"Toplam: {toplam}")
D.   for puan in puanlar:
E.   toplam = 0
```

---

## Puzzle 1 — Tahmin Et

Sıralamadan **önce**:

Bu 5 satır doğru sırada olsa ekrana **ne yazardı?**

Chat'e tek sayı.

---

## Puzzle 1 — Doğru Sıra

```
B → E → D → A → C
```

- **B** — veri tanımlama (liste)
- **E** — toplam başlangıcı, **döngüden ÖNCE**
- **D** — döngü aç
- **A** — döngü içinde, **girintili** (+= her turda)
- **C** — döngü **bittikten sonra** yazdır

---

## Puzzle 1 — Python

```python
puanlar = [85, 90, 78, 87]
toplam = 0
for puan in puanlar:
    toplam = toplam + puan
print(f"Toplam: {toplam}")
```

**Neden E, D'den önce?** Toplamı 0'a döngüden **önce** atamazsak her turda sıfırlanır.

---

## Puzzle 2 — Orta (Bireysel)

### Görev

> **"Renk listesindeki 'mavi'nin kaç kez geçtiğini bul ve yazdır."**

Beklenen çıktı: `mavi sayısı: 3`

### Karışık Satırlar

```
A.   print(f"mavi sayısı: {sayac}")
B.   renkler = ["mavi", "kırmızı", "mavi", "sarı", "mavi", "yeşil"]
C.   if renk == "mavi":
D.   sayac = 0
E.   for renk in renkler:
F.   sayac = sayac + 1
G.   sayac = sayac - 1   ← TUZAK
```

---

## Puzzle 2 — Tahmin Et

Doğru sırada bu kod **kaç yazar?**

Chat'e tek sayı.

---

## Puzzle 2 — Doğru Sıra

```
B → D → E → C → F → A
```

**J kullanılmaz — tuzak.**

- **C + F** için **iki kat girinti** (8 boşluk):
  ```python
  for renk in renkler:
      if renk == "mavi":
          sayac = sayac + 1
  ```

---

## Puzzle 2 — Tuzak Mikrosu

G satırı (`sayac = sayac - 1`) **neden mantık hatası?**

Tek cümleyle chat'e yazın — **neden yanlış?**

---

## Puzzle 2 — Tuzak Cevabı

G satırı sayacı her mavide **+1 sonra -1** yapar.

Sonuç hep **0** — sayma mantığına aykırı.

> Vize Bölüm 1.2 / 3.1 böyle "hatayı açıkla" soruları içerir. "Yanlış" demek yetmez — **neden** yanlış?

---

## Puzzle 2 — Python

```python
renkler = ["mavi", "kırmızı", "mavi", "sarı", "mavi", "yeşil"]
sayac = 0
for renk in renkler:
    if renk == "mavi":
        sayac = sayac + 1
print(f"mavi sayısı: {sayac}")
```

---

## Puzzle 3 — Zor (Breakout)

### Görev

> **"`en_yuksek_puan` fonksiyonu yaz: en yüksek puanı döndürsün. Çağır, yazdır."**

```python
projeler = [
    {"ad": "Logo",   "puan": 88},
    {"ad": "Afiş",   "puan": 95},
    {"ad": "Ambalaj","puan": 72},
]
```

Beklenen çıktı: `En yüksek puan: 95`

---

## Puzzle 3 — Karışık Satırlar

```
A.   def en_yuksek_puan(projeler):
B.   for proje in projeler:
C.       if proje["puan"] > en_yuksek:
D.           en_yuksek = proje["puan"]
E.       return en_yuksek
F.   en_yuksek = 0
G.   sonuc = en_yuksek_puan(projeler)
H.   print(f"En yüksek puan: {sonuc}")
I.   projeler = [{"ad": "Logo", "puan": 88}, ...]
J.   en_yuksek = 100   ← TUZAK
```

---

## Puzzle 3 — Tahmin Et

Bu fonksiyon doğru kurulursa `sonuc` **ne olur?**

Chat'e tek sayı.

---

## Puzzle 3 — Doğru Sıra

```
A → F → B → C → D → E → I → G → H
```

**J tuzak, kullanılmaz.**

E satırı (`return`) **for döngüsünün dışında** olmalı — aksi halde ilk turda fonksiyon biter, sadece ilk projeyi görür.

---

## Puzzle 3 — Girinti Haritası

```python
def en_yuksek_puan(projeler):          # A — 0 boşluk
    en_yuksek = 0                      # F — 4 boşluk
    for proje in projeler:             # B — 4 boşluk
        if proje["puan"] > en_yuksek:  # C — 8 boşluk
            en_yuksek = proje["puan"]  # D — 12 boşluk
    return en_yuksek                   # E — 4 boşluk (döngü DIŞI)

projeler = [...]                       # I — 0 boşluk
sonuc = en_yuksek_puan(projeler)       # G — 0 boşluk
print(f"En yüksek puan: {sonuc}")      # H — 0 boşluk
```

---

## Puzzle 3 — Tuzak Mikrosu

J satırı konulursa fonksiyon ne döndürür ve **neden?**

Chat'e tek cümle.

---

## Puzzle 3 — Tuzak Cevabı

**J ile:** `en_yuksek = 100` başlangıç.

- Hiçbir gerçek puan 100'den büyük değil
- Döngü güncelleme yapmaz
- Fonksiyon **100** döner — yanlış

**Kural:** "En yüksek" ararken başlangıç **çok küçük** olmalı (0 veya ilk eleman). Çok büyük başlangıç döngüyü boşa çevirir.

---

## Puzzle 3 — Python

```python
def en_yuksek_puan(projeler):
    en_yuksek = 0
    for proje in projeler:
        if proje["puan"] > en_yuksek:
            en_yuksek = proje["puan"]
    return en_yuksek

projeler = [
    {"ad": "Logo",   "puan": 88},
    {"ad": "Afiş",   "puan": 95},
    {"ad": "Ambalaj","puan": 72},
]
sonuc = en_yuksek_puan(projeler)
print(f"En yüksek puan: {sonuc}")
```

---

## Ara — 5 dk

10:45 — 10:50

Son blok geliyor: **Niyet Kartları — vize 3.3 provası.**

Defter yanınızda olsun.

---

# Blok 4

## Niyet → Pseudocode → Kod

40 dakika. **Vize Bölüm 3.3 birebir provası.**

---

## Blok 4 Akışı

1. **Kart 1** — ısınma (7 dk)
2. **Kart 4** — vize 3.3(a) provası (9 dk)
3. **Kart 4.5** — vize 3.2 provası, "değiştir" (3 dk)
4. **Kart 2** — kısa köprü (2 dk)
5. **Kart 7** — vize 3.3(b) provası, **bireysel** (12 dk)
6. **Kapanış** (3 dk)

Bu blokta yapacağımız iki kart + bir egzersiz **vize'de birebir sorulacak**.

---

## Ortak Veri

Tüm kartlarda aynı (vize verisi ile **birebir aynı**):

```python
projeler = [
    {"ad": "Logo Tasarımı",   "puan": 88},
    {"ad": "Film Afişi",      "puan": 95},
    {"ad": "Ürün Ambalajı",   "puan": 72},
    {"ad": "Web Arayüzü",     "puan": 91},
    {"ad": "Dergi Kapağı",    "puan": 64},
    {"ad": "Mobil Uygulama",  "puan": 85},
]
```

---

## Kart 1 — Isınma

### Niyet

> **"Projeler listesini gez. Her projenin adını yazdır."**

**Defterinize storyboard çizin. 2 dakika.**

---

## Kart 1 — Çözüm

```
projeler listesindeki her proje için:
    projenin adını yazdır
```

```python
for proje in projeler:
    print(proje["ad"])
```

**Çıktı:** Her projenin adı alt alta.

---

## Kart 4 — Vize 3.3(a) Provası

### Niyet

> **"Tüm projelerin puan ortalamasını hesapla ve yazdır."**

Bu kart **vize'de ayniyle var**. Adı: `ortalama_puan`.

**Defterinize storyboard + pseudocode. 2 dakika.**

---

## Kart 4 — Pseudocode

```
toplam = 0
projeler listesindeki her proje için:
    toplamı projenin puanına ekle
ortalama = toplam / projeler sayısı
ortalamayı yazdır
```

---

## Kart 4 — Python (Düz)

```python
toplam = 0
for proje in projeler:
    toplam += proje["puan"]

ortalama = toplam / len(projeler)
print(f"Ortalama: {ortalama}")
```

**Çıktı:** `Ortalama: 82.5`

---

## Kart 4 — Python (Fonksiyon)

Vize'de bu fonksiyon haliyle istenecek:

```python
def ortalama_puan(projeler):
    toplam = 0
    for proje in projeler:
        toplam += proje["puan"]
    return toplam / len(projeler)

print(f"Ortalama: {ortalama_puan(projeler)}")
```

**Defterinizde bu sayfa kalıcı olsun.**

---

## Kart 4.5 — Vize 3.2 Provası

### Niyet (Kart 4'ün ÜZERİNDEN)

> **"Kart 4'ü az önce çözdünüz. Şimdi bu çözümü DEĞİŞTİRİN: sadece puanı 80 ve üzeri olan projelerin ortalamasını hesaplayın."**

Yeni baştan kod yazmak **yok** — mevcut kodu **değiştireceğiz**.

**Chat'e:** "Kart 4'teki koda hangi 3 değişiklik gerekir?"

---

## Kart 4.5 — Üç Değişiklik

Beklenen cevap:

1. **`if` ekle** — sadece 80+ olanları topla
2. **`sayac` ekle** — kaç tane olduğunu say
3. **`len(projeler)` yerine `sayac`** ile böl

---

## Kart 4.5 — Python

```python
toplam = 0
sayac = 0
for proje in projeler:
    if proje["puan"] >= 80:
        toplam += proje["puan"]
        sayac += 1

ortalama = toplam / sayac
print(f"80+ ortalaması: {ortalama}")
```

**Çıktı:** `80+ ortalaması: 89.75`

*(88 + 95 + 91 + 85 = 359; 359 / 4 = 89.75)*

---

## Kart 4.5 — Kritik Mesaj

> **Vize Bölüm 3.2 tam bu tarz.**
>
> Size çalışan bir kod verecekler, "şunu ekle / şunu çıkar" diyecekler.
>
> **Yeni baştan yazmayın** — mevcut yapıyı değiştirin. Yeniden yazmak sizi yavaşlatır.

---

## Kart 2 — Kısa Köprü

### Niyet

> **"Puanı 80'in üstünde olan projelerin adını yazdır."**

```python
for proje in projeler:
    if proje["puan"] > 80:
        print(proje["ad"])
```

Bu yapıyı Kart 7'de kullanacağız. Filtre + yazdırma.

---

## Kart 7 — Vize 3.3(b) Provası (BİREYSEL)

### Niyet

> **"En yüksek puanlı projenin adını yazdır."**

Bu kart **vize'de ayniyle var**. Adı: `en_yuksek_puanli`.

---

## Kart 7 — Çözüm Sizde

**Kendiniz çözeceksiniz. 10 dakika.**

- Defterinize storyboard
- Pseudocode
- Python
- Çalıştırın

**Takılanlar DM atsın, chat'e yazmayın.**

İpucu: "En yüksek" ararken **iki takipçi** değişken gerekir — hem puan hem ad.

---

## Kart 7 — Çözüm (10 dk sonra açılır)

```python
en_iyi_ad = ""
en_iyi_puan = 0

for proje in projeler:
    if proje["puan"] > en_iyi_puan:
        en_iyi_puan = proje["puan"]
        en_iyi_ad = proje["ad"]

print(f"En yüksek puan: {en_iyi_ad} ({en_iyi_puan})")
```

**Çıktı:** `En yüksek puan: Film Afişi (95)`

---

## Kart 7 — Kritik Nokta

**İki değişken birlikte güncellenmeli:**

```python
if proje["puan"] > en_iyi_puan:
    en_iyi_puan = proje["puan"]   # ✗ Yalnız bu güncellenirse
    en_iyi_ad = proje["ad"]        # ad yanlış kişide kalır
```

Birini yazıp diğerini unutmak **en sık hata**.

---

## Kapanış

Bu hafta yeni Python öğrenmedik. Yeni bir **süreç** öğrendik:

```
NİYET → STORYBOARD → PSEUDOCODE → PYTHON
```

Dersten çıkar çıkmaz vize'ye döneceksiniz.

---

## Vize'de Takıldığınızda

1. Niyeti iki kez okuyun
2. **Defteri açın**
3. 3-5 kare storyboard
4. Pseudocode (Türkçe ağırlıklı)
5. Python'a çevirin
6. Çalıştırın, çıktıyı kontrol

---

## Vize Bölüm Eşleşmesi

| Vize Bölümü | Derste Hangi Kart |
|---|---|
| **1.1** Kod Yorumlama | Blok 1 "Tahmin Et" |
| **1.2 / 3.1** Hata Yakala | Blok 3 "Tuzak Neden" |
| **3.2** Değiştir | Kart 4.5 |
| **3.3(a)** ortalama_puan | Kart 4 |
| **3.3(b)** en_yuksek_puanli | Kart 7 |

---

## Son Notlar

- **24 Nisan 09:00 teslim** — 7 gün var, parça parça çalışın
- **Son gece bırakmayın** — mantığınız dağılır
- **LLM yasak**, ders notu + `gita2112/` klasörü serbest
- **DM atabilirsiniz** — pazartesi boyunca buralardayım

Başarılar.
