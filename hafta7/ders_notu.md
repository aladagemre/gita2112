# GİTA 2112 — Hafta 7: Kod Yazmadan Önce Düşünmek

> Bu belge, derste anlatılan konuların yazılı özetidir.
> Bu hafta yeni bir Python yapısı öğrenmiyoruz. Bu hafta **bildiğimiz yapıları ne zaman ve nasıl kullanacağımıza** karar vermeyi öğreniyoruz.
> Dosyanın sonundaki özet tablosunu derste yanınızda tutun.

---

## Neden Bu Hafta?

6 haftadır değişken, koşul, döngü, liste, sözlük, f-string, matematik ve fonksiyon öğrendiniz. Artık Python'un temel alfabesini biliyorsunuz.

Ama bir sorun var: hoca tahtada yazdığında anlıyorsunuz, **beyaz ekranla yalnız kaldığınızda ne yazacağınızı bulamıyorsunuz**. Bu normal. Eksik olan kavram değil, **süreç**.

Tasarım stüdyosunda bir afişe başlarken ne yapıyorsunuz? Doğrudan InDesign açıp tipografi seçmiyorsunuz. Önce bir eskiz defteri alıyorsunuz. Birkaç küçük kare çiziyorsunuz. Hiyerarşiyi kafanızda oturttuktan sonra ekrana geçiyorsunuz.

Bu hafta aynı şeyi kod için yapacağız. **Önce düşüneceğiz, sonra yazacağız.**

---

## 1. Kod Yazmadan Önce Düşünmek Nedir?

Tecrübeli bir programcı bir problem gördüğünde hemen klavyeye saldırmaz. Önce şu üç soruyu sorar:

1. **Ne veriyorum?** (girdi — liste mi, sayı mı, kullanıcı mı?)
2. **Ne istiyorum?** (çıktı — yazdırmak mı, döndürmek mi, saymak mı?)
3. **Aradaki yol nasıl?** (adımlar)

Bu üç soruya cevap vermeden tek satır yazmıyor.

### Tasarım Dünyasından Bir Benzetme

Bir afiş brifi düşünün. Müşteri size "bir jazz festivali afişi" dedi. Hemen Photoshop açmıyorsunuz, değil mi? Önce:

- **Brif** — ne istiyor? (hedef kitle, tarih, mekan)
- **Referanslar** — benzer işler nasıl çözülmüş?
- **Eskiz** — kaba kompozisyon (başlık nerede, tarih nerede)
- **Uygulama** — InDesign'da gerçek dosya

Kodda da aynı sıra: **niyet → eskiz (storyboard) → yalancı kod (pseudocode) → Python**.

### Üç Aşamalı Süreç

Bu hafta öğreneceğimiz süreç:

```
[1] NİYET           (Türkçe bir cümle — ne istiyorum?)
       ↓
[2] STORYBOARD      (3-5 kare — adımları görselleştir)
       ↓
[3] PSEUDOCODE      (Türkçe-Python karışımı — yarı kod)
       ↓
[4] PYTHON          (çalışan kod)
```

Dört aşama gibi görünse de son aşama genellikle en kolayı. Zor olan ilk üç aşama — ve siz şimdiye kadar sadece sonuncusunu pratik ettiniz.

---

## 2. Storyboard ile Algoritma Tasarlama

Storyboard, sinema ve animasyonda sahneleri önceden kağıda çizme tekniğidir. Her kare bir "an"ı gösterir. Sahne akışı bütün olarak kağıtta kurulur, sonra çekime geçilir.

Kodda da aynı fikri kullanabiliriz: **bir algoritmayı 3-5 kareye bölüp her karede tek bir şeye odaklanmak**.

### Örnek: "Listedeki Sıcak Renkleri Say"

Elimizde bir renk listesi var: `["kırmızı", "mavi", "turuncu", "yeşil", "sarı"]`. Sıcak olanları (kırmızı, turuncu, sarı) saymak istiyoruz.

Storyboard olarak düşünelim:

```
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  Kare 1          │  │  Kare 2          │  │  Kare 3          │  │  Kare 4          │
│                  │  │                  │  │                  │  │                  │
│  Başlangıç:      │  │  Listeyi         │  │  Her rengin      │  │  Sonunda         │
│  sayac = 0       │  │  teker teker     │  │  sıcak olup      │  │  sayacı          │
│                  │  │  geziyoruz       │  │  olmadığını      │  │  yazdırıyoruz    │
│  (boş tepsi)     │  │                  │  │  kontrol         │  │                  │
│                  │  │  (her renge      │  │  ediyoruz; sıcaksa │  │  (sonuç: 3)     │
│                  │  │  bakıyoruz)      │  │  sayacı artır    │  │                  │
└──────────────────┘  └──────────────────┘  └──────────────────┘  └──────────────────┘
```

Bu dört kareyi çizdikten sonra kod yazmak şaşırtıcı derecede kolay hale gelir. Çünkü artık kafanızda her satırın neye karşılık geldiği bellidir:

- Kare 1 → `sayac = 0`
- Kare 2 → `for renk in renkler:`
- Kare 3 → `if renk in ["kırmızı", "turuncu", "sarı"]:` + `sayac += 1`
- Kare 4 → `print(sayac)`

### Storyboard İçin Kurallar

- **Her kare tek bir şey anlatsın.** Aynı kareye "listeyi gez + say + yazdır" tıkma — üç ayrı kare olsun.
- **Başlangıç karesi önemli.** "Elimde ne var? Boş bir sayaç mı? Boş bir liste mi?" Bu unutulunca kod en baştan çöker.
- **Son kare çıktıdır.** Ne yazdırılacak / ne döndürülecek / sonuç nerede duracak?
- **Kareleri zincirleme bağlayın.** Bir kare bittikten sonra elimizde ne kaldı? Onu bir sonraki kare nasıl kullanıyor?

### Moodboard Benzetmesi

Moodboard hazırlarken her görseli rastgele yapıştırmıyorsunuz — bir hikaye kurgusu var. Storyboard da aynı: her kare bir önceki kareden miras aldığı bir durumu değiştirir. Sayaç kareden kareye büyür, liste kareden kareye küçülür, bir değişken "henüz yok" durumundan "dolu" durumuna geçer.

> **Not defterinize çizin.** Bilgisayar ekranında değil — eskiz defterinde. Kalem hızlıdır, silmek kolaydır, düşünmek serbesttir.

---

## 3. Pseudocode Nedir?

Pseudocode, Türkçe'si **yalancı kod**. Python değil, düz Türkçe de değil — ikisinin arasında bir şey. Amacı: adımları Python'un katı kurallarıyla uğraşmadan yazmak.

### Neden Pseudocode?

Python'da bir algoritmayı yazarken iki düşman aynı anda saldırır:
- **Ne yapmam gerektiğini** düşünmek (mantık)
- **Python'un bunu nasıl söylediğini** hatırlamak (sözdizimi)

Pseudocode ikinci düşmanı geçici olarak susturur. Sadece mantığa odaklanırsınız.

### Örnek: "Ortalamayı Hesapla"

**Niyet:** "Puanlar listesinin ortalamasını hesapla."

**Pseudocode:**

```
toplam diye bir değişken aç, başlangıçta 0
listedeki her puan için:
    toplamı o puan kadar artır
listenin uzunluğuna böl
sonucu döndür
```

**Python:**

```python
def ortalama(puanlar):
    toplam = 0
    for p in puanlar:
        toplam += p
    return toplam / len(puanlar)
```

Pseudocode'un her satırı Python'un bir satırına karşılık geldi. Pseudocode bitince Python yazmak neredeyse çeviri işine dönüştü.

### Pseudocode Yazım Rehberi

Aşağıdaki küçük sözlük, Türkçe düşüncelerinizi Python karşılıklarına bağlar:

| Türkçe                          | Python        |
|---------------------------------|---------------|
| ... diye bir değişken aç        | `ad = ...`    |
| Sakla                           | `= atama`     |
| Hepsi için / Her ... için       | `for ... in`  |
| Eğer ...                        | `if ...`      |
| Eğer değilse / yoksa            | `else`        |
| Yaz / Ekrana bas                | `print(...)`  |
| Döndür / Ver                    | `return ...`  |
| Say                             | `sayac += 1`  |
| Ekle                            | `liste.append(...)` |
| Listenin uzunluğu               | `len(liste)`  |

Bu tablo elinizin altında olsun. Pseudocode'u Python'a çevirirken bu tablodan bakıp yazarsanız hata riski çok azalır.

### InDesign Benzetmesi

InDesign'da bir afişin **master page** (ana sayfa) şablonunu çizersiniz: başlık şurada, görsel burada, tarih alt köşede. Boş, renksiz, tipografisiz. Bu master page pseudocode gibidir — yapı belli, detay yok.

Sonra master page'den yola çıkıp gerçek afişi üretirsiniz. Pseudocode'dan Python'a geçiş de tam olarak böyle: iskelet hazır, şimdi üstüne et giydireceksiniz.

---

## 4. Parsons Tekniği — Karışık Satırları Sıraya Koymak

Parsons puzzle'ı, programlama eğitiminde çok kullanılan bir yöntemdir. Kod satırlarını size **karışık** olarak veririz. Sizin işiniz satırları **doğru sıraya koymak**.

Bu egzersiz iki şeyi aynı anda çalıştırır:

1. **Kodun mantığını okumak** — bu satır ne yapıyor, hangi satıra dayanıyor?
2. **Bağımlılıkları görmek** — hangi satır hangi satırdan sonra gelmeli?

### Neden Faydalı?

Sıfırdan kod yazmak zordur çünkü:

- Hangi yapıları kullanacağınızı seçmek gerekiyor
- Hangi sırayla yazacağınızı planlamak gerekiyor
- Sözdizimini hatasız girmek gerekiyor

Parsons'ta sadece orta kademeye — sıralamaya — odaklanırsınız. Satırlar zaten doğru yazılmış, sizin işiniz bulmacayı çözmek.

### Parsons Satırını Okuma Taktiği

Bir satırın sırasını bulmak için şu soruları sorun:

- **Bu satır hangi değişkeni KULLANIYOR?** O değişken daha önce tanımlanmış olmalı.
- **Bu satır hangi değişkeni OLUŞTURUYOR?** Onu kullanan satırlar daha sonra gelir.
- **Bu satır bir döngünün / if'in içinde mi?** Girintili satırlar, kendilerini açan satırın altına gelir.

### Tuzak Satırlar

Bazı Parsons puzzle'larında **yanıltıcı** (kullanılmayan) satırlar olabilir. Bunlar doğru görünür ama kullanmazsanız kod çalışır, kullanırsanız yanlış sonuç verir. Her satırı yerleştirmeden önce "bu gerçekten gerekli mi?" diye sorun.

### Eskiz Benzetmesi

Bir grafik tasarım projesinde müşterinize 10 eskiz gösteriyorsunuz. İçlerinden 6-7'si güzel, 3'ü konuya uymuyor. Hepsini kullanmak zorunda değilsiniz. Parsons da aynı: verilen her satırı kullanmak zorunda değilsiniz. Yapıya uyanları alın, gerisini görmezden gelin.

---

## 5. Niyet → Kod Süreci

Şimdi hepsini birleştirelim. Bir niyet cümlesinden başlayıp Python'a kadar gidelim.

### Tam Bir Örnek

**Niyet (Türkçe):** "Bir projeler listesi al. Puanı 80 ve üstü olanların adını yazdır."

#### Adım 1 — Storyboard (defterde)

```
┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐
│ Kare 1    │  │ Kare 2    │  │ Kare 3    │  │ Kare 4    │
│           │  │           │  │           │  │           │
│ Elimde    │  │ Her       │  │ Puan 80+  │  │ Döngü     │
│ projeler  │  │ projeyi   │  │ ise adını │  │ bitince   │
│ listesi   │  │ sırayla   │  │ yazdır,   │  │ iş biter  │
│ var       │  │ ele al    │  │ değilse   │  │           │
│           │  │           │  │ atla      │  │           │
└───────────┘  └───────────┘  └───────────┘  └───────────┘
```

#### Adım 2 — Pseudocode

```
Listedeki her proje için:
    eğer projenin puanı 80 ve üstündeyse:
        projenin adını yazdır
```

#### Adım 3 — Python

```python
projeler = [
    {"ad": "Logo Tasarımı", "puan": 88},
    {"ad": "Film Afişi",    "puan": 95},
    {"ad": "Ürün Ambalajı", "puan": 72},
    {"ad": "Dergi Kapağı",  "puan": 64},
]

for proje in projeler:
    if proje["puan"] >= 80:
        print(proje["ad"])
```

**Çıktı:**
```
Logo Tasarımı
Film Afişi
```

### Dikkat Edilecek Noktalar

- **Storyboard olmadan pseudocode yazmayın.** Kafanızda canlanmamış bir mantığı yarı-koda dökmeye çalışırsanız iki kat kafa karışıklığı olur.
- **Pseudocode'dan Python'a çevirirken bir satır atlamayın.** Her pseudocode satırının bir Python karşılığı olmalı. Eksik varsa storyboard'a geri dönün.
- **Python yazınca çalışıp çalışmadığını test edin.** Storyboard ve pseudocode iyi olsa bile Python'da bir yazım hatası yapabilirsiniz. Çalıştırın, çıktıyı kontrol edin.

### Hangi Yapı Ne Zaman?

Bu hafta bildiğiniz yapıları doğru yere koymayı da konuşacağız. Küçük bir kılavuz:

| Niyette "..." geçiyorsa      | Kullanacağınız yapı       |
|------------------------------|---------------------------|
| "Hepsi için" / "her ..."     | `for` döngüsü             |
| "Eğer ..."                   | `if`                      |
| "Değilse" / "aksi halde"     | `else` / `elif`           |
| "Say" / "kaç tane"           | Sayaç değişkeni (`+= 1`)  |
| "Topla" / "ortalama"         | Toplam değişkeni (`+=`)   |
| "En yüksek" / "en düşük"     | İki takipçi değişken      |
| "Sakla" / "içine koy"        | Liste veya sözlük         |
| "Yeniden kullanılacak"       | Fonksiyon (`def`)         |

Bu tablo size bir kısayol veriyor: niyet cümlesindeki kelimeyi gördüğünüzde hangi yapıyı açacağınızı çıkarabiliyorsunuz.

---

## Özet Tablosu

| Aşama                   | Nerede yapılır?        | Amacı                                   | Çıktısı                    |
|-------------------------|------------------------|-----------------------------------------|----------------------------|
| Niyet                   | Kafada / tek cümlede   | Ne istiyorum?                           | Türkçe 1 cümle             |
| Storyboard              | Defterde, kare kare    | Adımları görselleştirmek                | 3-5 kare çizim             |
| Pseudocode              | Defterde veya editörde | Mantığı sözdiziminden ayırmak           | Türkçe-Python karışımı     |
| Python                  | Editörde               | Çalışır kod                             | `.py` dosyası              |
| Test                    | Terminal / çalıştır    | Gerçekten doğru mu?                     | Beklenen çıktı             |

---

## Sık Yapılan Hatalar

### 1. Storyboard'ı atlamak

```
Niyet → (boşluk) → Python
```

Doğrudan Python yazmaya çalışınca kafanızda henüz oturmamış bir şeyi kodlamaya çalışırsınız. Her 2-3 satırda takılırsınız. Çözüm: defteri açın, 3 kare çizin. 2 dakika harcayın, 20 dakika kazanın.

### 2. Pseudocode'u Python'a çok benzetmek

```
# YANLIŞ (pseudocode değil, yarı Python):
for p in puanlar:
    toplam = toplam + p

# DOĞRU (pseudocode — Türkçe ağırlıklı):
listedeki her puan için:
    toplamı o puan kadar artır
```

Eğer pseudocode'unuz Python'a çok benziyorsa, amacı kaybediyorsunuz. Pseudocode'un özü Türkçe düşünmek. Python çevirisi ayrı aşamada yapılır.

### 3. Başlangıç değerini unutmak

Sayaçlar, toplamlar, listeler — hepsi bir **başlangıç** değerine ihtiyaç duyar:

```python
# YANLIŞ:
for proje in projeler:
    toplam += proje["puan"]   # NameError! toplam hiç tanımlanmadı

# DOĞRU:
toplam = 0                      # Başlangıç değeri
for proje in projeler:
    toplam += proje["puan"]
```

Storyboard'daki **1. kare** (başlangıç) bunu hatırlamanız için var.

### 4. Döngünün içini unutmak

```
Pseudocode:
    her proje için:
        puanı topla

Python'a yanlış çeviri:
    for proje in projeler:
    toplam += proje["puan"]        # Girinti yok! Döngünün içinde değil.
```

Pseudocode'daki girinti Python'daki girintiye birebir karşılık gelir. Defterdeki girintiyi Python'a aktarmayı unutmayın.

### 5. Önce yazıp sonra düşünmek

Önce 20 satır yazıp sonra "acaba mantığım doğru mu?" diye düşünmek, yanlış kodun üstüne düşünmeye çalışmaktır. Verimsizdir.

**Kural:** Kod yazmadan önce 30-60 saniye defterde durun.

### 6. Parsons puzzle'ında tüm satırları kullanmaya çalışmak

Tuzak satırları da dahil etmek çözümü bozar. "Bu satır gerçekten gerekli mi?" sorusunu her satır için sorun.

### 7. Pseudocode'u derste yazmayı unutmak

Vizede de aynı hatayı yapmak istemezsiniz. Bu hafta pseudocode'u bir **alışkanlık** haline getirmeye çalışın. Zamanla şart olmaktan çıkar, ama şu an şarttır.

---

## Bu Haftanın Çıktıları

Bu hafta ödev yok — vize zaten elinizde. Bu ders vize'nin **parçası** gibi: dersten çıkar çıkmaz vize'ye geri döneceksiniz. Dersin içinde bir hatırlama + üç pratik bloğu var:

| Blok | İçerik | Süre | Hangi vize becerisi |
|------|--------|------|---------------------|
| 1 | Hatırlama + "Tahmin Et" mikroları | 20 dk | 1.1 Kod Yorumlama |
| 2 | Storyboard Atölyesi | 35 dk | 3.3 Niyet → Kod |
| 3 | Parsons Puzzle + "Tuzak Neden" | 35 dk | 1.1 + 3.1 Düzelt |
| 4 | Niyet Kartları (Kart 4, 4.5, 7) | 40 dk | 3.3 + 3.2 Değiştir |

Hoca ekran paylaşacak, siz defterinize çizeceksiniz. Sonunda kameraya gösterip chat'te sıra göndereceksiniz. Breakout room'larda ikili çalışacaksınız.

Defter + kalem derste yanınızda olsun. Çizmeyi "zaman kaybı" olarak görmeyin — bu derste çizim, yazılmış kod kadar değerlidir.

---

## Bir Sonraki Adım — Vize

Ders biter bitmez vize'ye döneceksiniz. Paket tam olarak bunun için tasarlandı. Derste göreceğiniz çözümler vize bölümlerine birebir bağlanıyor:

- **Vize 3.3(a) "ortalama_puan"** → Derste Kart 4 ile birlikte çözeceğiz.
- **Vize 3.3(b) "en_yuksek_puanli"** → Derste Kart 7 ile siz tek başınıza çözeceksiniz.
- **Vize 3.2 "Değiştir ve Genişlet"** → Derste Kart 4.5 ile değiştirme becerisini prova edeceksiniz.
- **Vize 1.1 / 1.2 "Yorumla / Hata Yakala"** → Blok 1'deki "Tahmin Et" ve Blok 3'teki "Tuzak Neden" mikroları bu becerilere provadır.

Vize sırasında takıldığınızda yapacağınız iş:
1. Niyeti tekrar okuyun (iki kere).
2. **Defteri açın.** 3-5 kare çizin.
3. Pseudocode yazın — Türkçe ağırlıklı olsun.
4. Pseudocode'u Python'a çevirin.
5. Çalıştırın, çıktıyı bekleneni karşılaştırın.

Bu sıra sizi kurtaracak. Derste defteri görecek, pratik yapacak, aynı defteri vize boyunca kullanacaksınız. Son gece kalmayın — 24 Nisan 09:00'a 7 gün var, parça parça çalışın. Başarılar.
