# GİTA 2112 — Hafta 10

## Bir Projeyi Sıfırdan Geliştirmek

### 5 Aşamalı Belge Akışı

-----

## Bu Hafta Farklı

- Geçen hafta tek bir **sayfa** yaptık
- Bu hafta bir **yöntem** öğreniyoruz
- Bir sayfayı değil — **aklınıza gelen her projeyi** yapabileceksiniz
- Araç: **Antigravity** (geçen haftadan tanıdık)

> "Sayfa değil, yöntem"

-----

## Önce: Ders Değerlendirme Anketleri 📋

Dönem sonu **ders değerlendirme anketleri** açıldı.

- Lütfen doldurmayı unutmayın
- Birkaç dakikanızı alır
- Geri bildiriminiz dersin gelişmesine **doğrudan** katkı sağlar

> Dürüst geri bildirim en değerlisi — teşekkürler

-----

## Büyük Şeyler Tek Promptla Olmaz

Bir profesyonel tek prompt yazmaz.
Önce **planlar**, sonra kodlatır.

```
Önce ne yapacağımızı belge belge planlarız
Kod EN SON gelir
```

Bugün bunun küçük halini yapacağız.

-----

## 5 Aşama

| # | Aşama | Soru | Çıktı |
|---|-------|------|-------|
| 1 | **Fikir** | Ne, kime, neden? | Problem tanımı |
| 2 | **Gereksinim** | Kullanıcı ne yapabilmeli? | Özellik listesi |
| 3 | **Tasarım** | Ne nerede duracak? | Ekran krokisi |
| 4 | **Yol Haritası** | Hangi sırayla? | Numaralı adımlar |
| 5 | **Kodlat** | Hadi yapalım | Çalışan araç |

-----

## İki Altın Kural

### 1. Her belge bir sonrakini besler
Gereksinim olmadan yol haritası çıkmaz.
Plan olmadan kod düzgün gelmez.

### 2. Çekirdek önce
- **Çekirdek** = araç onsuz işe yaramaz; en küçük çalışan hâli
- **Ekstra** = sonradan eklenen güzellikler

> Önce çekirdeği kur, sonra katman katman ekle

-----

## Benzetme: Film

Bir film **kamera açılmadan** önce:

- Senaryo yazılır
- Storyboard çizilir
- Çekim planı yapılır

**Kamera en son açılır.**

Aşama 1–4 = plan. Aşama 5 = çekim.

-----

## Örnek Proje

# 🎨 Renk Paleti Üreteci

Butona bas → 5 renk + hex kodları çıksın.

Bu örneği birlikte yapacağız.
Aynı 5 aşamayı **kendi projenize** de uygulayacaksınız.

-----

## Aşama 1 — Fikir

Koda atlamadan önce **ne yaptığımızı** anlarız.

```
Tasarımcılar için bir renk paleti üreteci web aracı
yapmak istiyorum. Henüz kod yazma. Önce kısaca yanıtla:
- Bu araç kimin işine yarar?
- Hangi problemi çözer?
- Olmazsa olmaz 3-4 temel özelliği ne?
Maddeler halinde, sade Türkçe.
```

> Dikkat: kod gelmedi. Önce **düşündük**.

-----

## Aşama 2 — Gereksinim

Kullanıcı tam olarak **ne yapabilmeli**?

```
Bu araç için gereksinim listesi çıkar.
Her madde "Kullanıcı ... yapabilmeli" biçiminde olsun.
Sonra ikiye ayır:
- ÇEKİRDEK: araç bunlar olmadan işe yaramaz
- EKSTRA: sonradan eklenebilir güzellikler
```

-----

## Aşama 2 — Örnek Çıktı

**Çekirdek**
- Butona basınca 5 renk üretebilmeli
- Renkleri görebilmeli
- Hex kodlarını görebilmeli

**Ekstra**
- Hex'i kopyalayabilmeli
- Bir rengi kilitleyebilmeli
- Renk sayısını değiştirebilmeli
- PNG indirebilmeli

> Projeyi parçalamak = çekirdek ve ekstrayı ayırmak

-----

## Aşama 3 — Tasarım

**Önce defterde** 1 ekranlık kroki çiz:
üstte başlık + buton, ortada renk blokları, altta hex.

```
Bu aracın tek ekranlık görsel düzenini tarif et.
Üstte ne olsun, ortada ne, altta ne?
Renk blokları nasıl dizilsin?
Henüz kod yazma, sadece yerleşimi anlat.
```

> Burası sizin eviniz — siz tasarımcısınız.
> Ajanın tarifi krokinizle aynı mı?

-----

## Aşama 4 — Yol Haritası

Hangi sırayla yapacağız?

```
Bir yol haritası çıkar. Bu aracı hangi sırayla yapmalıyım?
Önce sadece ÇEKİRDEK (en basit çalışan hâli),
sonra EKSTRALAR tek tek.
Numaralı adımlar. Her adım TEK bir özellik olsun.
```

-----

## Aşama 4 — Örnek Çıktı

1. Boş sayfa + başlık + "Üret" butonu
2. Butona basınca 5 rastgele renk bloğu
3. Her bloğun altına hex kodu
4. Hex'in yanına "kopyala" butonu
5. Bir rengi kilitleme
6. PNG indir

> Adım 1–2–3 = çekirdek · gerisi = ekstra

-----

## Aşama 5 — Kodlat

Artık planımız var. **Tek tek** kodlatırız.

```
Yol haritasının 1. adımını uygula.
Tek HTML dosyası; CSS ve JavaScript gömülü;
Türkçe karakterler doğru çıksın.
SADECE 1. adımı yap, fazlasını ekleme.
```

Çalıştır → gör → sonra:

```
Şimdi 2. adımı ekle.
```

-----

## Tek Adım Kuralı

```
1. adımı yap → çalıştır → gör
2. adımı ekle → çalıştır → gör
3. adımı ekle → çalıştır → gör
```

**Hepsini birden isterseniz yarısı eksik gelir.**

Her adımda çalışan halini görerek ilerleyin.

-----

## Defter Alıştırması

Kendi küçük proje fikrini seç. Defterine yaz:

1. **Proje adı** + 1 cümle: ne yapar
2. **Çekirdek:** 1-2 madde
3. **Ekstra:** 3 madde
4. **Kaba ekran krokisi**

Bitince **kameraya göster.**

### Takıldıysan fikir
söz/alıntı kartı · emoji ruh hali panosu · kişisel link sayfası · geri sayım · "bugünün rengi" · su içme sayacı

-----

## Takıldığında Ne De?

| Belirti | Ne dersin |
|---------|-----------|
| Ajan hemen kod yazdı | "Henüz kod yazma, önce soruma cevap ver." |
| Tek seferde her şeyi yaptı | "Sadece 1. adımı yap, gerisini durdur." |
| Sayfa boş / eksik | "[BÖLÜM] görünmüyor." (ne gördüğünü tarif et) |
| Türkçe bozuk | "Türkçe karakterler bozuk, düzelt." |

> Ajan ne gördüğünü bilmez — **tarif et**, "çalışmıyor" deme

-----

## Atölye

5 aşamayı **kendi projene** uygula.

- Takılırsan paleti **birebir** tekrarla — o da geçerli
- Önce çekirdek → sonra katman katman
- Her katmandan sonra çalıştır, gör

> Hedef: dersten **çalışan bir araçla** çıkmak

-----

## Canlıya Al — surge.sh

Araç bilgisayarında kaldıkça **kimse göremez.**

**surge.sh** = ücretsiz; statik siteni saniyeler içinde
internete koyar ve **paylaşılabilir bir link** verir.

> Portfolyona, CV'ne, Instagram bio'na koyabilirsin

-----

## surge.sh — Adımlar

Antigravity'de **terminali** aç, projenin klasöründe yaz:

```
npx surge
```

1. İlk seferde **e-posta + şifre** sorar → ücretsiz hesap oluşur
2. **Klasör** sorar → `Enter` (mevcut klasör)
3. **Domain** sorar → `adin-projen.surge.sh` yaz → `Enter`
4. Bitti 🎉 → linkin hazır

> `index.html` klasörün içinde olmalı

-----

## Güncelleme & Paylaşım

**Değişiklik yaptın mı?**
Tekrar `npx surge` çalıştır — aynı linke yeni hâli yüklenir.

**Linkini paylaş:**
`https://adin-projen.surge.sh`

> Artık elinde gerçek, paylaşılabilir bir **eser** var

-----

## Bugün Ne Yapacağız?

| Süre | Adım |
|------|------|
| 10 dk | Giriş — bugün ne farklı |
| 15 dk | 5 Aşama yöntemi |
| 35 dk | Hoca canlı: paleti 5 aşamayla |
| 15 dk | Defterde kendi projeni parçala |
| 10 dk | Mola |
| 50 dk | Kendi aracını yap |
| 15 dk | Paylaşım + canlıya alma (surge) + ödev |

-----

## Sık Hatalar

**Aşama 5'e atlamak**
Önce 1–4'ü yap. Plansız kod jeneriktir.

**Her şeyi tek adımda istemek**
Yol haritasını adım adım kodlat.

**Çekirdek/ekstrayı ayırmamak**
Önce onsuz olmaz olanı kur.

**"Çalışmıyor" demek**
Ne gördüğünü tarif et.

-----

## Ödev

Kendi projeni **5 aşamadan** baştan sona geçir.

### Teslim
- `fikir.md`, `gereksinim.md`, `tasarim.md`, `yol-haritasi.md`
- `index.html` — çalışan aracın
- `notlar.txt` — her aşamada ne istedin, ne değişti
- **Bonus:** aracını `surge.sh` ile canlıya al → linkini `notlar.txt`'e ekle

### Değerlendirme
Kod kalitesi değil →
5 aşamayı uyguladın mı · çekirdek/ekstra net mi · kaç katman ekledin

> En az **çekirdek + 2 ekstra katman** çalışsın

-----

## Bir Sonraki Adım

Bu hafta: planladınız → kodlattınız → **canlıya aldınız.**

Önümüzdeki hafta (son hafta):

- Tüm araçlarınızı **bir portfolyoda** toplama
- Cilalama + sunum

> "Artık paylaşılabilir eserleriniz var. Son hafta hepsini bir vitrine koyacağız."

-----

## 20 Proje Fikri

### GİTA Öğrencileri İçin

Hepsi **tam frontend** — aynı 5 aşamayla yapılabilir.
Seviyene göre seç.

-----

## Kolay — Küçük Çekirdek

1. **Kişisel link sayfası** — tüm hesapların tek sayfada (Linktree gibi)
2. **Dijital kartvizit** — ad, unvan, iletişim; paylaşılabilir
3. **Alıntı/söz kartı üreteci** — güzel tipografiyle rastgele söz
4. **Geri sayım sayfası** — sergi açılışı / teslim tarihi
5. **Emoji ruh hali panosu** — günün hâlini seç
6. **"Bugünün rengi"** — her açılışta renk + hex + isim

-----

## Orta

7. **Renk paleti üreteci** — (bugünkü örnek)
8. **Gradyan üreteci** — 2 renk → degrade + CSS kodu
9. **Tipografi eşleştirici** — başlık + gövde font çiftleri
10. **Mood board** — görsel + renk ızgarası
11. **Sosyal medya şablonu** — kare gönderi önizleyici
12. **CSS filtre oyun alanı** — fotoğrafa filtre uygula, kodu al
13. **Before/After kaydırıcı** — iki görseli karşılaştır
14. **Etkinlik/sergi davetiyesi** — tek sayfa, şık

-----

## İleri

15. **Kişisel portfolyo** — projeler + hakkımda + iletişim
16. **Poster/afiş jeneratörü** — rastgele geometrik kompozisyon
17. **Renk kontrast denetleyici** — iki renk okunur mu? (erişilebilirlik)
18. **Desen (pattern) üreteci** — tekrar eden desen → indir
19. **Logo/monogram denemesi** — baş harfler + font + renk
20. **Renk teorisi quiz'i** — eğlenceli mini test

-----

## Unutma

> Hangi projeyi seçersen seç:
>
> **Fikir → Gereksinim → Tasarım → Yol Haritası → Kodlat**
>
> Önce çekirdek, sonra katman katman, en son **canlıya al**.
