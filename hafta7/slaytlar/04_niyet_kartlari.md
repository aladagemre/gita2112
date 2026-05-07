# Slaytlar — Blok 4: Niyet Kartları

> Vize Bölüm 3.3 doğrudan provası. 10 kart, artan zorluk.
> Her kart: (1) niyet, (2) öğrenciden beklenen pseudocode, (3) referans Python, (4) öğrenci takılırsa hocanın ipucu.
> **Ana akış (Blok 4, 40 dk):** Kart 1 (ısınma) → **Kart 4** (vize 3.3a provası, birlikte) → **Kart 4.5** (vize 3.2 provası, "değiştir" mikro) → Kart 2 (kısa köprü) → **Kart 7** (vize 3.3b provası, bireysel).
> **Bonus:** Kart 3, 5, 6, 8, 9, 10 zaman kalırsa veya evde pratik için. Ayrıntı için sonda "Kart Kullanım Rehberi" tablosuna bak.

---

## KART 1 — Çok kolay (hep birlikte)

### Niyet

> **"Projeler listesini gez. Her projenin adını yazdır."**

Veri (tüm kartlarda ortak — **vize verisi ile birebir aynı**):
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

### Beklenen Pseudocode

```
projeler listesindeki her proje için:
    projenin adını yazdır
```

### Referans Python

```python
for proje in projeler:
    print(proje["ad"])
```

**Çıktı:**
```
Logo Tasarımı
Film Afişi
Ürün Ambalajı
Web Arayüzü
Dergi Kapağı
Mobil Uygulama
```

### İpucu (takılırsa)

> "Niyet cümlesinde 'her' kelimesi var — hangi yapıyı açar? (for). Döngünün içinde ne yazdırıyoruz? Projenin adını — projenin sözlüğünden adını nasıl çekeriz?"

---

## KART 2 — Kolay (hep birlikte)

### Niyet

> **"Puanı 80'in üstünde olan projelerin adını yazdır."**

### Beklenen Pseudocode

```
projeler listesindeki her proje için:
    eğer projenin puanı 80'den büyükse:
        projenin adını yazdır
```

### Referans Python

```python
for proje in projeler:
    if proje["puan"] > 80:
        print(proje["ad"])
```

**Çıktı:**
```
Logo Tasarımı
Film Afişi
Web Arayüzü
Mobil Uygulama
```

### İpucu

> "Kart 1'e bir koşul ekledik. 'üstünde' kelimesi ne demek — > mi, >= mi? Niyet 'üstü' diyor, sınır dahil değil."

> **Hoca notu:** 80 dahil değil dedik. 80 puan alan yok bu veride, ama öğrencinin `>=` yazması vize cevap anahtarı mantığında daha sık. Hem > hem >= doğru sayılır, ama niyette 'üstü' yazıyor, bu yüzden > daha doğru. Tartışmayı kaybolmasın — "niyet cümlesi ne diyor?" sorusuyla geri yönlendir.

---

## KART 3 — Kolay-orta (birlikte / hızlı)

### Niyet

> **"Puanı 90 ve üzeri olan proje sayısını say ve yazdır."**

### Beklenen Pseudocode

```
sayac = 0
projeler listesindeki her proje için:
    eğer projenin puanı 90'a eşit veya büyükse:
        sayacı 1 artır
sayacı yazdır
```

### Referans Python

```python
sayac = 0
for proje in projeler:
    if proje["puan"] >= 90:
        sayac += 1
print(f"90+ puanlı proje sayısı: {sayac}")
```

**Çıktı:**
```
90+ puanlı proje sayısı: 2
```
(Film Afişi 95, Web Arayüzü 91 — ikisi.)

### İpucu

> "Sayma işlemi için neye ihtiyacımız var? Bir sayaç. Sayaç nereye açılır — döngünün içine mi dışına mı? Niyet 've üzeri' diyor — `>` mi `>=` mi?"

---

## KART 4 — Orta

### Niyet

> **"Tüm projelerin puan ortalamasını hesapla ve yazdır."**

### Beklenen Pseudocode

```
toplam = 0
projeler listesindeki her proje için:
    toplamı projenin puanına ekle
ortalama = toplam / projeler sayısı
ortalamayı yazdır
```

### Referans Python

```python
toplam = 0
for proje in projeler:
    toplam += proje["puan"]

ortalama = toplam / len(projeler)
print(f"Ortalama: {ortalama}")
```

**Çıktı:**
```
Ortalama: 82.5
```

### İpucu

> "Ortalama için iki şey gerek: toplam ve kaç tane. Toplamı nasıl bulacağız? len() neye bakıyor?"

> **Vize uyarısı (hoca için):** Bu kart **birebir vize 3.3(a) görevi** — `ortalama_puan(projeler)` fonksiyonunun ta kendisi. Vize'de fonksiyon içine koyulacak; ders provasında düz kod yeterli. Zaman kalırsa fonksiyona çevir:
>
> ```python
> def ortalama_puan(projeler):
>     toplam = 0
>     for proje in projeler:
>         toplam += proje["puan"]
>     return toplam / len(projeler)
>
> print(f"Ortalama: {ortalama_puan(projeler)}")
> ```
>
> Bu kart Blok 4'ün **ana birlikte çözüm** kartıdır. Atlanmamalı.

---

## KART 4.5 — "Değiştir" mikro egzersizi (2 dk, birlikte) — vize 3.2 provası

### Niyet (Kart 4'ün ÜSTÜNDEN)

> **"Kart 4'ü az önce çözdünüz (tüm projelerin ortalaması = 82.5). Şimdi bu çözümü DEĞİŞTİRİN: sadece puanı 80 ve üzeri olan projelerin ortalamasını hesaplayın."**

Bu kart yeni baştan kod yazmak değil — **mevcut kodu değiştirmek**. Vize Bölüm 3.2 birebir bu beceriyi ölçüyor.

### Değişiklik (öğrencinin zihinde yapması gereken)

"Kart 4'teki kodu hatırla. Tek ne değişecek?" — chat'e cevap iste. Beklenen: "içine bir `if` ekleyeceğiz" ve "`len(projeler)` yerine **sayaç**".

### Beklenen Pseudocode (değişen satırlar **kalın**)

```
toplam = 0
**sayac = 0**
projeler listesindeki her proje için:
    **eğer projenin puanı 80'e eşit veya büyükse:**
        toplama projenin puanını ekle
        **sayacı 1 artır**
ortalama = toplam / **sayac**
ortalamayı yazdır
```

### Referans Python

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

**Çıktı:**
```
80+ ortalaması: 89.75
```
((88 + 95 + 91 + 85) / 4 = 359 / 4 = 89.75)

### Hoca Notu

Bu egzersiz 2 dakika. **Tüm öğrencilerin yeniden kod yazmasını bekleme** — Kart 4'ün kodunu göster, hangi 3 değişikliğin yapılması gerektiğini sor, chat'ten cevap topla, ekranda birlikte değiştir. Vize 3.2'de de böyle "değiştir" denir, yeniden yaz denmez.

> **Kritik mesaj:** "Vize'de Bölüm 3.2 tam bu tarz. Size çalışan bir kod verecekler, 'şunu ekle / şunu çıkar' diyecekler. Yeni baştan yazmayacaksınız — mevcut yapıyı değiştireceksiniz."

---

## KART 5 — Orta (bonus, vize dışı)

### Niyet

> **"Puanı 75'in altında olan projelerin ortalama puanını bul. (Sadece düşük puanlıların ortalaması.)"**

### Beklenen Pseudocode

```
toplam = 0
sayac = 0
projeler listesindeki her proje için:
    eğer projenin puanı 75'ten küçükse:
        toplama puanı ekle
        sayacı 1 artır
ortalama = toplam / sayac
ortalamayı yazdır
```

### Referans Python

```python
toplam = 0
sayac = 0
for proje in projeler:
    if proje["puan"] < 75:
        toplam += proje["puan"]
        sayac += 1

ortalama = toplam / sayac
print(f"Düşük puanlıların ortalaması: {ortalama}")
```

**Çıktı:**
```
Düşük puanlıların ortalaması: 68.0
```
(72 ve 64 — (72+64)/2 = 68.0)

### İpucu

> "Burada iki değişken takip ediyoruz: filtreye uyan toplam, filtreye uyan sayısı. `len(projeler)` kullanabilir miyiz? Hayır — çünkü hepsinin değil, sadece düşük olanların sayısına ihtiyacımız var."

> **Kenar durum:** Eğer hiç düşük puanlı yoksa `0/0` olur — hata verir. Derste belirt ama düzeltmeyi isteme; vizede kenar durum yok.

---

## KART 6 — Orta (bonus)

### Niyet

> **"Puanı 80 ve üzeri olan projelerin adlarını bir listeye topla. Sonra listeyi yazdır."**

### Beklenen Pseudocode

```
yuksek_puanlilar = boş liste
projeler listesindeki her proje için:
    eğer projenin puanı 80'e eşit veya büyükse:
        projenin adını yuksek_puanlilar listesine ekle
yuksek_puanlilar'ı yazdır
```

### Referans Python

```python
yuksek_puanlilar = []
for proje in projeler:
    if proje["puan"] >= 80:
        yuksek_puanlilar.append(proje["ad"])

print(yuksek_puanlilar)
```

**Çıktı:**
```
['Logo Tasarımı', 'Film Afişi', 'Web Arayüzü', 'Mobil Uygulama']
```

### İpucu

> "Boş bir listeyle başla. Döngüde filtreye uyan projenin **adını** listeye ekle. Kart 2'de adları *yazdırıyorduk* — burada yazdırmıyoruz, *topluyoruz*. Fark: ekrana hemen mi verdik, yoksa bir yerde biriktirip sonda mı yazdık?"

> **Hoca notu:** Bu kart Kart 10'un (listeye ayırma) hazırlık kartıdır. `append()` ve "birikim listesi" mantığı Kart 10'da tekrar kullanılır.

---

## KART 7 — Zor

### Niyet

> **"En yüksek puanlı projenin adını yazdır."**

### Beklenen Pseudocode

```
en_iyi_ad = boş
en_iyi_puan = 0
projeler listesindeki her proje için:
    eğer projenin puanı en_iyi_puan'dan büyükse:
        en_iyi_puan = projenin puanı
        en_iyi_ad = projenin adı
en_iyi_ad'ı yazdır
```

### Referans Python

```python
en_iyi_ad = ""
en_iyi_puan = 0

for proje in projeler:
    if proje["puan"] > en_iyi_puan:
        en_iyi_puan = proje["puan"]
        en_iyi_ad = proje["ad"]

print(f"En yüksek puan: {en_iyi_ad} ({en_iyi_puan})")
```

**Çıktı:**
```
En yüksek puan: Film Afişi (95)
```

### İpucu

> "En yüksek bulmak için iki takipçiye ihtiyacımız var: **şimdiye kadarki en yüksek puan** ve **onu alan projenin adı**. İkisi birlikte güncellenmeli — biri güncellenip diğeri güncellenmezse karışır."

> **Vize uyarısı:** Bu kart **birebir vize 3.3(b) görevi** — `en_yuksek_puanli(projeler)` fonksiyonu. Kartı öğrenciler **kendileri çözsün**: Blok 4'ün bireysel pratiğe ayrılmış kartı budur.

> **Başlangıç değeri hakkında hoca notu:** `en_iyi_puan = 0` başlangıcı **bizim verimizde çalışır** çünkü tüm puanlar pozitif. Ama tüm puanlar negatif olsaydı yanlış sonuç verirdi (0'dan büyük puan olmaz → hiç güncellenmez). Vize cevap anahtarı da `0` kullanıyor, kabul ediliyor. Alternatif (daha sağlam) çözüm:
>
> ```python
> en_iyi_ad   = projeler[0]["ad"]
> en_iyi_puan = projeler[0]["puan"]
> for proje in projeler[1:]:
>     if proje["puan"] > en_iyi_puan:
>         en_iyi_puan = proje["puan"]
>         en_iyi_ad   = proje["ad"]
> ```
>
> Bir öğrenci bu alternatifi kullanırsa tam puan ver, takdir et. Ama derste ilk çözüm olarak `= 0`'ı göster — öğrencinin kafasında bir tek kalıp olsun.

---

## KART 8 — Zor (fonksiyonlu)

### Niyet

> **"`ortalamanin_ustu` adlı bir fonksiyon yaz. Bir projeler listesi alsın, ortalamanın üstündeki projelerin sayısını döndürsün. Sonra çağır ve sonucu yazdır."**

### Beklenen Pseudocode

```
fonksiyon ortalamanin_ustu(projeler):
    toplam = 0
    her proje için:
        toplama puanı ekle
    ortalama = toplam / proje sayısı

    sayac = 0
    her proje için:
        eğer projenin puanı ortalamadan büyükse:
            sayacı artır
    sayacı döndür

sonuc = ortalamanin_ustu(projeler) çağır
sonucu yazdır
```

### Referans Python

```python
def ortalamanin_ustu(projeler):
    # İlk döngü: ortalamayı hesapla
    toplam = 0
    for proje in projeler:
        toplam += proje["puan"]
    ortalama = toplam / len(projeler)

    # İkinci döngü: ortalamanın üstündekileri say
    sayac = 0
    for proje in projeler:
        if proje["puan"] > ortalama:
            sayac += 1

    return sayac

sonuc = ortalamanin_ustu(projeler)
print(f"Ortalamanın üstünde {sonuc} proje var.")
```

**Çıktı:**
```
Ortalamanın üstünde 4 proje var.
```

### İpucu

> "İki döngü: önce ortalamayı bulan, sonra ortalamayla karşılaştıran. Tek döngüde olmaz — çünkü ortalamayı bilmeden karşılaştıramazsın. Fonksiyon bu iki döngüyü içeriyor, sonunda tek bir sayı döndürüyor."

---

## KART 9 — Zor (bonus, fonksiyonlu)

### Niyet

> **"`yuksek_puanli_isimler(projeler, sinir)` adlı bir fonksiyon yaz: sınırın üstünde (dahil) puanlı projelerin adlarını liste olarak döndürsün. Sonra 80 ve 90 için çağır, iki sonucu ayrı ayrı yazdır."**

### Beklenen Pseudocode

```
fonksiyon yuksek_puanli_isimler(projeler, sinir):
    sonuc = boş liste
    her proje için:
        eğer projenin puanı sinir'e eşit veya büyükse:
            projenin adını sonuc listesine ekle
    sonuc'u döndür

liste1 = yuksek_puanli_isimler(projeler, 80) çağır
liste2 = yuksek_puanli_isimler(projeler, 90) çağır
ikisini ayrı ayrı yazdır
```

### Referans Python

```python
def yuksek_puanli_isimler(projeler, sinir):
    sonuc = []
    for proje in projeler:
        if proje["puan"] >= sinir:
            sonuc.append(proje["ad"])
    return sonuc

print("80+:", yuksek_puanli_isimler(projeler, 80))
print("90+:", yuksek_puanli_isimler(projeler, 90))
```

**Çıktı:**
```
80+: ['Logo Tasarımı', 'Film Afişi', 'Web Arayüzü', 'Mobil Uygulama']
90+: ['Film Afişi', 'Web Arayüzü']
```

### İpucu

> "İki parametre var: listeyi ve sınırı alıyoruz. Filtreleme yaparken `proje["puan"] >= sinir` — değişken adıyla karşılaştır, sabitle değil. Aynı fonksiyonu farklı sınırlarla çağırınca farklı sonuç alıyoruz — işte esnekliğin değeri burada."

> **Zorluk:** Fonksiyonu sınırdan bağımsız yazıp sonra 80, 90 ile çağırmak. Öğrenciler genelde kodun içine `80` yazıp sabitler — bunu fark ettir. "Fonksiyon esnek olmalı, sınırı argüman olarak alıyoruz."

---

## KART 10 — Zor (bonus, zaman kalırsa)

### Niyet

> **"Bir eşik puan al (örneğin 80). Eşiğin üstündekileri ve altındakileri ayrı listelere ayır. İki listeyi yazdır."**

### Beklenen Pseudocode

```
ustundekiler = boş liste
altindakiler = boş liste

her proje için:
    eğer projenin puanı 80'den büyük veya eşitse:
        projeyi ustundekiler listesine ekle
    yoksa:
        projeyi altindakiler listesine ekle

"Üstündekiler:" yazdır, sonra listesini gez
"Altındakiler:" yazdır, sonra listesini gez
```

### Referans Python

```python
esik = 80
ustundekiler = []
altindakiler = []

for proje in projeler:
    if proje["puan"] >= esik:
        ustundekiler.append(proje)
    else:
        altindakiler.append(proje)

print("Üstündekiler:")
for p in ustundekiler:
    print(f"  - {p['ad']} ({p['puan']})")

print("Altındakiler:")
for p in altindakiler:
    print(f"  - {p['ad']} ({p['puan']})")
```

**Çıktı:**
```
Üstündekiler:
  - Logo Tasarımı (88)
  - Film Afişi (95)
  - Web Arayüzü (91)
  - Mobil Uygulama (85)
Altındakiler:
  - Ürün Ambalajı (72)
  - Dergi Kapağı (64)
```

### İpucu

> "İki boş listeyle başla. Döngüde her projeyi tek tek ele al ve doğru listeye at. `append()` kullanılıyor — listeye eklemek için. Sonunda her iki listeyi ayrı ayrı yazdır."

---

## Kart Kullanım Rehberi (hoca için)

Blok 4 = **40 dakika** (150 dk'lık dersin son bloğu). Ana omurga: Kart 1 → Kart 4 → Kart 7. Diğerleri bonus.

### Ana akış (zorunlu)

| Kart   | Rol                    | Süre   | Kim çözer            |
|--------|------------------------|--------|----------------------|
| Intro  | Blok 4 açılışı         | 4 dk   | Hoca anlatır         |
| **1**  | Isınma (for + dict)    | 7 dk   | Hep birlikte         |
| **4**  | **Vize 3.3(a) provası** (ortalama)  | 9 dk  | Birlikte çöz + chat onayı |
| **4.5**| **Vize 3.2 provası** ("değiştir": 80+ ortalaması) | 3 dk | Chat'ten değişiklik, birlikte yaz |
| **2**  | Köprü (> filtre)       | 2 dk   | Hızlı hatırlatma     |
| **7**  | **Vize 3.3(b) provası** (en yüksek) | 12 dk  | **Bireysel** — defter + ekran paylaşımı |
| Kapanış| Toparlama + motivasyon | 3 dk   | Hoca                 |

**Toplam:** 4 + 7 + 9 + 3 + 2 + 12 + 3 = **40 dk**

### Bonus kartlar (sadece zaman kalırsa veya evde pratik için)

| Kart | Konu                              | Not                        |
|------|-----------------------------------|----------------------------|
| 3    | Sayaç (>= 90)                     | Sayma mantığı, chat üstü   |
| 5    | Filtreli ortalama (< 75)          | Kenar durum (0/0) uyarısı  |
| 6    | Liste biriktirme (append)         | Kart 10 ön hazırlığı       |
| 8    | Fonksiyon + iki döngü (ortalama üstü) | Vize düzeyi fonksiyon pratiği |
| 9    | Fonksiyon + parametre (sınır)     | Çoklu çağrı, esneklik      |
| 10   | İkiye ayırma (append + else)      | Zaman kalırsa ekran demosu |

**Not:** Kart 2, 3 ve 5-6-8-9-10 çözümlerini slaytlarda hazır tuttum; ders sırasında atlasa bile öğrenci kart dosyasını PDF olarak alacağı için evde pratik yapabilir. Ders notunda bu öneriyi tekrar ettim.

## Kapanış

Son 3 dakikada:

> "Bu kartlardan **iki tanesi** vize'de birebir çıkacak. Hangi iki kart olduğunu söylemiyorum — ama provasını yaptınız. Bugünkü üç ana kartı tekrar gözden geçirin: ortalama hesabı ve en yüksek bulma. Evde bir kez daha yazın, bakmadan."

(Bu, pedagojik küçük bir spoiler — öğrenci "Kart 4 ve Kart 7"ye odaklanır, vize direkt verilmiş olmaz.)
