# Slaytlar — Blok 2: Storyboard Atölyesi

> 3 senaryo, artan zorluk. Hoca ekranda gösterir, öğrenciler defterinde çizer.
> Her senaryoda 4 bölüm: (1) niyet tarifi, (2) beklenen storyboard kareleri, (3) beklenen pseudocode, (4) referans Python çözümü.

---

## SENARYO 1 — Kolay

### Hoca demosu için. Hep birlikte çiziliyor.

### Niyet

> **"Bir renk listesinde sıcak bir rengin kaç kez geçtiğini say."**
>
> (Not: "çeşit" değil "tekrar" sayıyoruz. Aynı sıcak renk iki kez geçerse iki kere saydırır.)

Veri (ekranda göster):

```python
renkler = ["kırmızı", "mavi", "turuncu", "yeşil", "sarı", "mor", "kırmızı"]
sicak_renkler = ["kırmızı", "turuncu", "sarı"]
```

Beklenen çıktı: `4` — listede kırmızı 2, turuncu 1, sarı 1 kez geçiyor, toplam 4.

### Beklenen Storyboard (4 kare)

```
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ KARE 1          │  │ KARE 2          │  │ KARE 3          │  │ KARE 4          │
│                 │  │                 │  │                 │  │                 │
│ Başlangıç:      │  │ Her rengi       │  │ Renk sıcak      │  │ Döngü bitti.    │
│ sayac = 0       │  │ tek tek ele al  │  │ mı? Evet ise    │  │ Sayacı yazdır.  │
│                 │  │ (döngü aç)      │  │ sayacı 1 artır. │  │                 │
│ Boş bir kutu.   │  │                 │  │ Hayır ise atla. │  │ Çıktı: 4        │
└─────────────────┘  └─────────────────┘  └─────────────────┘  └─────────────────┘
```

### Beklenen Pseudocode

```
sayac diye bir değişken aç, başlangıçta 0
renkler listesindeki her renk için:
    eğer renk, sıcak_renkler listesindeyse:
        sayacı 1 artır
sayacı yazdır
```

### Referans Python Çözümü

```python
renkler = ["kırmızı", "mavi", "turuncu", "yeşil", "sarı", "mor", "kırmızı"]
sicak_renkler = ["kırmızı", "turuncu", "sarı"]

sayac = 0
for renk in renkler:
    if renk in sicak_renkler:
        sayac += 1

print(sayac)   # 4
```

### Hoca Notları

- `in` operatörünü Hafta 3'te gördüler — ama belki az kullanıldı. "Listede var mı?" için `x in liste` yapısını hatırlat.
- Büyük bir kavram açma — storyboard'ı göstermek için bu senaryo tak-çıkar olsun.

---

## SENARYO 2 — Orta

### Hep birlikte, herkes defterinde çizer. Sonra defterini kameraya gösterir.

### Niyet

> **"Bir puanlar listesi al. 60'ın altında kaç puan olduğunu say ve bu düşük puanların ortalamasını bul."**

Veri:

```python
puanlar = [88, 45, 92, 58, 72, 39, 81, 65, 54]
```

Beklenen çıktı:
```
60 altı puan sayısı: 4
Ortalaması: 49.0
```

### Beklenen Storyboard (5 kare)

```
┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ KARE 1         │ │ KARE 2         │ │ KARE 3         │ │ KARE 4         │ │ KARE 5         │
│                │ │                │ │                │ │                │ │                │
│ Başlangıç:     │ │ Her puanı      │ │ Puan 60'ın     │ │ Döngü bitti.   │ │ İkisini de     │
│ sayac = 0      │ │ tek tek ele al │ │ altındaysa:    │ │ Ortalamayı     │ │ yazdır.        │
│ toplam = 0     │ │ (döngü)        │ │  sayacı artır  │ │ hesapla:       │ │                │
│                │ │                │ │  puanı topla   │ │ toplam / sayac │ │                │
│ İki boş kutu.  │ │                │ │                │ │                │ │                │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────┘ └────────────────┘
```

### Beklenen Pseudocode

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

### Referans Python Çözümü

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

**Çıktı:**
```
60 altı puan sayısı: 4
Ortalaması: 49.0
```

(60 altı puanlar: 45, 58, 39, 54. Toplam 196, sayı 4, ortalama 49.0.)

### Hoca Notları

- İki ayrı değişkeni (sayac, toplam) aynı döngüde takip etmek, öğrencilerin sık takıldığı yer. "Storyboard kare 1'de iki boş kutu var — iki başlangıç" diye vurgula.
- Bölme sıfıra düşebilir mi? Bu örnekte düşmez. Ama "Eğer hiç düşük puan yoksa?" diye düşündürtmek için ek soru sorulabilir — dersin sonunda zaman kalırsa.

---

## SENARYO 3 — Zor

### Breakout room'da ikili çalışma. 10 dakika.

### Niyet

> **"Projeler listesinde ortalamanın ÜSTÜNDE puan alan projelerin adlarını yazdır."**

Veri:

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

Beklenen çıktı:
```
Ortalama: 82.5
Ortalamanın üstündekiler:
- Logo Tasarımı
- Film Afişi
- Web Arayüzü
- Mobil Uygulama
```

### Beklenen Storyboard (6 kare)

```
┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
│ KARE 1     │ │ KARE 2     │ │ KARE 3     │ │ KARE 4     │ │ KARE 5     │ │ KARE 6     │
│            │ │            │ │            │ │            │ │            │ │            │
│ Başlangıç: │ │ Her proje  │ │ Döngü      │ │ Ortalamayı │ │ Her proje  │ │ Eğer puan  │
│ toplam = 0 │ │ için puanı │ │ bitti.     │ │ yazdır.    │ │ için       │ │ ortalamanın│
│            │ │ toplam'a   │ │ ortalama = │ │            │ │ (yeni      │ │ üstündeyse │
│ Tek boş    │ │ ekle       │ │ toplam /   │ │            │ │ döngü)     │ │ adını      │
│ kutu.      │ │ (1. döngü) │ │ proje sayı │ │            │ │            │ │ yazdır.    │
└────────────┘ └────────────┘ └────────────┘ └────────────┘ └────────────┘ └────────────┘
```

> **Önemli:** Bu senaryo iki döngü gerektirir. İlk döngü ortalamayı hesaplar, ikinci döngü karşılaştırma yapar. Tek döngüyle yapılamaz — çünkü ortalamayı bilmeden hangi proje "üstünde" olduğunu söyleyemezsiniz.

### Beklenen Pseudocode

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

### Referans Python Çözümü

```python
projeler = [
    {"ad": "Logo Tasarımı",  "puan": 88},
    {"ad": "Film Afişi",     "puan": 95},
    {"ad": "Ürün Ambalajı",  "puan": 72},
    {"ad": "Web Arayüzü",    "puan": 91},
    {"ad": "Dergi Kapağı",   "puan": 64},
    {"ad": "Mobil Uygulama", "puan": 85},
]

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

**Çıktı:**
```
Ortalama: 82.5
Ortalamanın üstündekiler:
- Logo Tasarımı
- Film Afişi
- Web Arayüzü
- Mobil Uygulama
```

### Hoca Notları — Dikkat

- **En zor kavram:** Bu senaryo iki ayrı döngü gerektiriyor. Öğrenciler tek döngüde yapmaya çalışacak ve takılacak. Breakout sırasında geçerken bu sezgiyi aşılamalısın:

  > "Bir projeyi 'ortalamanın üstünde' diye tanımlayabilmek için önce ortalamayı bilmen gerekiyor. Ortalamayı hesaplamadan karşılaştıramazsın. O yüzden iki aşama."

- **Alternatif çözüm:** Öğrenci `sum()` kullanabilirse (bilmiyoruz, Hafta 5'te resmi olarak gösterilmedi) kabul et: `ortalama = sum(p["puan"] for p in projeler) / len(projeler)`.
- **Ad ile yazdırma:** `proje["ad"]` yazımında tırnak yapısını karıştırabilirler. `f"- {proje['ad']}"` — dıştaki tırnak çift, içteki tek. Bunu model üzerinde göster.

### Breakout Öncesi Talimat (chat'e yapıştır)

```
2 kişilik breakout. 10 dakika.
Rol değişimi:
  5 dk — 1. kişi storyboard çiziyor, 2. kişi pseudocode yazıyor
  5 dk — değişin: 1. pseudocode, 2. Python'a çeviri

İkiliden biri kamerasını defter/ekranına çevirsin.
Python çalıştıracak zaman kalırsa çalıştırın.
Ana odaya dönünce defterinizi/ekranınızı göstereceksiniz.
```

---

## Blok 2 Sonu

Ana odaya döndükten sonra:

1. 2-3 ikili defterini göstersin.
2. Hoca referans çözümü ekranda açar.
3. "Sizinkiyle karşılaştırın. Farklı nerede?"

> "Şimdi 10 dakika ara. Sonra Parsons puzzle'larına geçeceğiz."
