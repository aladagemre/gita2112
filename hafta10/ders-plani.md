# GİTA 2112 — Hafta 10 Ders Planı

## Bir Projeyi Sıfırdan Geliştirmek: 5 Aşamalı Belge Akışı

**Süre:** 2,5 saat (09:00–11:30) · **Format:** Online · **Araç:** Antigravity IDE (kurulu)
**Canlı örnek:** Renk Paleti Üreteci (tam frontend — sunucu/API yok)

---

## Kazanımlar

Ders sonunda öğrenci:

1. Bir proje fikrini **5 aşamaya** bölebilir: Fikir → Gereksinim → Tasarım → Yol Haritası → Kodlat
2. Her aşamada doğru prompt yazıp **bir belge** üretebilir; belgenin bir sonrakini beslediğini görür
3. Projeyi **çekirdek + ekstra** olarak ayırabilir
4. Antigravity'de bir aracı **adım adım** (tek seferde değil) kurabilir
5. Yöntemi **kendi projesine** uygulayabilir

> Asıl ders palet değil — **yöntem**. Palet sadece yöntemi gösteren canlı örnek.

---

## Ders Öncesi Kontrol Listesi (hoca)

- [ ] Antigravity açık, giriş yapılmış, boş bir workspace hazır
- [ ] 5 aşamanın **örnek belgeleri** elinde (aşağıda) — slayta/ekrana yansıtılacak
- [ ] Öğrencilere hatırlat: Antigravity kurulu olsun, defter + kalem hazır
- [ ] Ekran paylaşımı + öğrenci kamerası test edildi

---

## Akış Özeti

| Süre | Dakika | Bölüm |
|------|--------|-------|
| 09:00–09:10 | 10 | Giriş: bugün ne farklı |
| 09:10–09:25 | 15 | 5 Aşama yöntemi (kavram) |
| 09:25–10:00 | 35 | Hoca canlı demo: paleti 5 aşamayla kur |
| 10:00–10:15 | 15 | Defter alıştırması: kendi projeni parçala + kameraya göster |
| 10:15–10:25 | 10 | Mola |
| 10:25–11:15 | 50 | Atölye: herkes kendi aracını yapar |
| 11:15–11:30 | 15 | Paylaşım + transfer + ödev |

---

## 1) Giriş — Bugün Ne Farklı (10 dk)

**Söyle:**
> "Geçen hafta tek bir sayfa yaptık. Bugün bir **sayfa** değil, bir **yöntem** öğreneceğiz. Ben gerçek projelerimi yaparken tek prompt yazmıyorum — önce ne yapacağımı belge belge planlıyorum, sonra kodlatıyorum. Bugün bunun küçük halini yapacağız. Bunu öğrenirseniz, sadece paleti değil, **aklınıza gelen her projeyi** yapabilirsiniz."

**Tahtada/slaytta tek cümle:**
> "Büyük şeyler tek promptla olmaz — aşama aşama, belge belge ilerler."

**Geçen haftayla köprü:** "Geçen hafta art director gibi tarif ettiniz. Bugün art director **projeyi planlıyor**: önce brief, sonra üretim."

---

## 2) 5 Aşama Yöntemi (15 dk)

Slaytta göster, her birini bir cümleyle açıkla. **Henüz Antigravity açma.**

| # | Aşama | Soru | Çıktı (belge) |
|---|-------|------|---------------|
| 1 | **Fikir** | Ne yapıyoruz, kime, neden? | Problem tanımı |
| 2 | **Gereksinim** | Kullanıcı ne yapabilmeli? | Özellik listesi (çekirdek + ekstra) |
| 3 | **Tasarım** | Nasıl görünecek, ne nerede? | Ekran krokisi/tarifi |
| 4 | **Yol Haritası** | Hangi sırayla yapacağız? | Numaralı adımlar |
| 5 | **Kodlat** | Hadi yapalım | Çalışan araç |

**İki kuralı vurgula:**
- **Her belge bir sonrakini besler.** Gereksinim olmadan yol haritası çıkmaz.
- **Çekirdek önce.** Çekirdek = araç onsuz işe yaramaz, en küçük çalışan hâli. Ekstra = sonradan eklenen güzellikler.

> Benzetme: "Bir film çekmeden önce senaryo, storyboard, çekim planı yapılır. Kamera en son açılır. Aşama 5'ten önceki her şey **plan**."

---

## 3) Hoca Canlı Demo — Paleti 5 Aşamayla (35 dk)

Antigravity'yi aç, ekranı paylaş. Her aşamanın prompt'unu **yazarken sesli düşün**. Öğrenci sadece izler (henüz yapmaz).

### Aşama 1 — Fikir (5 dk)

**Prompt (ajana yaz):**
```
Tasarımcılar için bir renk paleti üreteci web aracı yapmak istiyorum.
Henüz kod yazma. Önce şunları kısaca yanıtla:
- Bu araç kimin işine yarar?
- Hangi problemi çözer?
- Olmazsa olmaz 3-4 temel özelliği ne?
Maddeler halinde, sade Türkçe.
```

**Beklenen çıktı (örnek):**
> Kime: grafik/web tasarımcıları, öğrenciler. Problem: uyumlu renk seçmek zor, ilham gerek. Temel özellikler: rastgele palet üret, renkleri göster, hex kodlarını göster, kopyala.

**Söyle:** "Dikkat — kod gelmedi. Önce **ne yaptığımızı anladık.** En sık hata buraya atlamamak."

### Aşama 2 — Gereksinim (7 dk)

**Prompt:**
```
Bu araç için gereksinim listesi çıkar. Kullanıcı tam olarak ne yapabilmeli?
Her madde "Kullanıcı ... yapabilmeli" biçiminde olsun.
Sonra maddeleri ikiye ayır:
- ÇEKİRDEK: araç bunlar olmadan işe yaramaz
- EKSTRA: sonradan eklenebilir güzellikler
```

**Beklenen çıktı (örnek):**
> **Çekirdek:** butona basınca 5 renk üretebilmeli · renkleri görebilmeli · hex kodlarını görebilmeli
> **Ekstra:** hex'i kopyalayabilmeli · bir rengi kilitleyip tekrar üretebilmeli · renk sayısını değiştirebilmeli · paleti PNG indirebilmeli

**Söyle:** "İşte projeyi parçalamak bu. Çekirdek küçük — 3 madde. Asıl beceri burada: neyin şart, neyin süs olduğunu ayırmak."

### Aşama 3 — Tasarım (8 dk)

**Önce defterde (hoca da kameraya çizer):** 1 ekranlık kaba kroki — üstte başlık + buton, ortada 5 renk bloğu yan yana, her bloğun altında hex kodu.

**Sonra prompt:**
```
Bu aracın tek ekranlık görsel düzenini tarif et.
Üstte ne olsun, ortada ne, altta ne? Renk blokları nasıl dizilsin?
Henüz kod yazma, sadece yerleşimi anlat.
```

**Söyle:** "Burası sizin eviniz — tasarımcısınız. Ajanın tarifi sizin krokinizle aynı mı? Farklıysa **siz haklısınız**, ajana kendi düzeninizi söyleyin."

### Aşama 4 — Yol Haritası (5 dk)

**Prompt:**
```
Şimdi bir yol haritası çıkar. Bu aracı hangi sırayla yapmalıyım?
Önce sadece ÇEKİRDEK (en basit çalışan hâli), sonra EKSTRALAR tek tek.
Numaralı adımlar halinde. Her adım TEK bir özellik olsun.
```

**Beklenen çıktı (örnek):**
> 1. Boş sayfa + başlık + "Üret" butonu
> 2. Butona basınca 5 rastgele renk bloğu çıksın
> 3. Her bloğun altına hex kodu yaz
> 4. Hex'in yanına "kopyala" butonu
> 5. Bir rengi kilitleme özelliği
> 6. PNG indir

### Aşama 5 — Kodlat (10 dk)

**İlk prompt:**
```
Yol haritasının 1. adımını uygula. Tek HTML dosyası; CSS ve JavaScript gömülü;
Türkçe karakterler doğru çıksın. SADECE 1. adımı yap, fazlasını ekleme.
```
Önizlemede aç, göster. Sonra:
```
Şimdi 2. adımı ekle.
```
Çalıştır → gör → "3. adımı ekle" ... 3-4 adım canlı yap.

**Söyle:** "Gördünüz mü — her seferinde **tek adım**. Hepsini birden isteseydim yarısı eksik gelirdi. Çalışır halini gördükçe ilerliyoruz."

---

## 4) Defter Alıştırması — Kendi Projeni Parçala (15 dk)

**Yönerge (slaytta):**
> Kendi küçük proje fikrini seç. Defterine yaz:
> 1. **Proje adı** + 1 cümle: ne yapar
> 2. **ÇEKİRDEK:** 1-2 madde (onsuz olmaz)
> 3. **EKSTRA:** 3 madde
> 4. **Kaba ekran krokisi**
> Bitince kameraya göster.

**Fikir havuzu (takılan için):** alıntı/söz kartı üreteci · emoji ruh hali panosu · kişisel link sayfası · basit geri sayım · "bugünün rengi" · spor/su içme sayacı.

**Hoca:** 2-3 öğrenciyi seç, krokisini kameraya gösterttir, **30 sn** geri bildirim ver — özellikle çekirdek/ekstra ayrımına bak. ("Bu çekirdek mi gerçekten? Onsuz araç çalışır mı?")

---

## 5) Mola (10 dk)

---

## 6) Atölye — Herkes Kendi Aracını Yapar (50 dk)

**Yönerge:**
> Antigravity'de 5 aşamayı **kendi projene** uygula. Takılırsan paleti birebir tekrarla — o da geçerli teslim.

**Üç hız (kimseye söylenmez, hoca böyle yönetir):**
- **Güvenli (zayıf):** Paleti birebir, slayttaki promptlarla yap. Sonunda çalışan bir araç = başarı.
- **Orta:** Paleti yap + 1-2 ekstra katman ekle.
- **İleri (güçlü):** Kendi projeni 5 aşamadan baştan geçir.

**Hoca dolaşır (breakout room / ekran isteyerek):** Önce takılanlara git. En sık 2 sorun + cevabı:

| Belirti | Öğrenciye söylet |
|---------|------------------|
| Ajan hemen kod yazmaya başladı | "Henüz kod yazma, önce soruma cevap ver." |
| Tek seferde her şeyi yaptı | "Sadece 1. adımı yap, gerisini durdur." |
| Sayfa boş / eksik açıldı | Ne gördüğünü tarif et: "X bölümü görünmüyor." |
| Türkçe karakter bozuk | "Türkçe karakterler bozuk, düzelt." |

> Kural (geçen haftadan): "Ajan ne gördüğünü bilmez — **tarif et**, 'çalışmıyor' deme."

---

## 7) Paylaşım + Transfer + Ödev (15 dk)

**Paylaşım (8 dk):** 2-3 öğrenci ekranını paylaşsın — aracını + en az bir aşama belgesini göstersin. "Çekirdeğin neydi? Kaç katman ekledin?"

**Transfer (4 dk):**
> "Bugün paleti yaptık ama asıl öğrendiğiniz **5 aşama**. Aynı aşamalar bir poster jeneratörüne, kişisel sitenize, bir quize de uyar. Önce planla, sonra kodlat."

**Ödev (3 dk):** Aşağıdaki bölümü göster.

---

## Ödev

Kendi projeni **5 aşamadan** baştan sona geçir.

### Teslim
- `fikir.md`, `gereksinim.md`, `tasarim.md`, `yol-haritasi.md` — 4 aşama belgesi (Antigravity üretecek, kaydet)
- `index.html` — çalışan aracın
- `notlar.txt` — her aşamada ne istedin, ne değişti

### Değerlendirme
Kod kalitesi **değil** →
- 5 aşamayı uyguladın mı?
- Çekirdek / ekstra ayrımı net mi?
- Çekirdekten sonra kaç katman ekledin?

> En az **çekirdek + 2 ekstra katman** çalışır halde olsun.

---

## Notlar (hoca için)

- **Skills / agents.md / Workflows öğrenciye AÇILMAZ** — ileri özellik, karma sınıfı boğar. En fazla güçlü 2 öğrenciye "isterseniz bu akışı bir Workflow'a kaydedin" bonusu.
- Antigravity ajan belgeleri kendi dosyalara yazar; öğrenci dosya yönetmez, **planlamayı** öğrenir.
- H11 (son hafta) köprüsü: bu araçları **canlıya alma** + portföye koyma. Bugün çıkan araç oraya taşınacak.
