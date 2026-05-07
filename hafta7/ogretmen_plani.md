# Hafta 7 — Öğretmen Planı

> 18 Nisan Cuma, 09:00-11:30. ONLINE ders. 11 öğrenci. Vize dağıtıldıktan 1 gün sonra.
> Ana amaç: Öğrencilerin **kod yazmadan önce düşünme** alışkanlığı kazanmasını sağlamak. Vize Bölüm 3.3 için prova.
> Bu hafta yeni konu yok — **süreç** öğretiyoruz. Yeni syntax girmeyin.

---

## Hazırlık (dersten 15 dk önce)

- [ ] Zoom / Meet açık, ekran paylaşımı test edildi
- [ ] `slaytlar/01_hatirlama.md` ekranda sekme olarak açık
- [ ] Breakout room özelliği açık, manuel atama modu
- [ ] Chat üstünden dosya/link paylaşımına izin verildi
- [ ] Öğrencilere 1 gün önce e-posta: "Defter + kalem + kamera — bu hafta çizim yapacağız"
- [ ] Vize'yi açmış ama henüz 3.3'e geçmemiş öğrenciler için: bu ders direkt o göreve hazırlık, kaçırmak istemeyin

### Derse giriş mesajı (chat'e ilk 30 saniyede atılacak)

```
Günaydın. Bu hafta defterinizi yanınıza alın. Kamerayı açın, çünkü
çizdiğinizi göstereceksiniz. Yeni Python konusu yok — bildiklerimizi
VİZEDE nasıl kullanacağımızı konuşacağız.
```

---

## Genel Akış

| Blok | Süre   | Konu                                   | Ana etkinlik                 |
|------|--------|----------------------------------------|------------------------------|
| 1    | 20 dk  | Hatırlama Haritası (6 haftanın özeti)  | Hoca slayt + chat etkileşimi |
| Ara  | 5 dk   |                                        |                              |
| 2    | 35 dk  | Storyboard Atölyesi                    | Defterde çizim + breakout    |
| Ara  | 10 dk  |                                        |                              |
| 3    | 35 dk  | Parsons Puzzle                         | Chat'te sıra gönderimi       |
| Ara  | 5 dk   |                                        |                              |
| 4    | 40 dk  | Niyet → Pseudocode → Kod               | Bireysel + birlikte          |

---

## BLOK 1 — Hatırlama Haritası (09:00-09:20)

### Amaç

6 haftada öğrendikleri kavramları bir bütün olarak görmelerini sağlamak. Vizede "hepsini birlikte kullanman gerekiyor" — ama kafalarında henüz bir harita yok. Bu 20 dakika o haritayı kuruyor.

### Açılış Cümlesi

> "Şimdi size garip bir soru soracağım. Python'u öğrenmeye başlayalı 6 hafta oldu. Chat'e tek kelime yazın: **aklınıza ilk gelen Python kavramı nedir?**"

15 saniye sessizce bekle. Cevapları topla. Beklenen cevaplar: print, input, değişken, for, if, liste, sözlük, fonksiyon.

### Slayt Akışı

Slaytlar: `slaytlar/01_hatirlama.md`.

Her hafta için ~1.5 dakika ayır. Slayt başı yapılacaklar:

1. Slaytı göster.
2. Minik kod örneğini yüksek sesle oku.
3. VCD analojisini söyle.
4. **"Tahmin Et" sorusunu oku** (her slaytta hazır). 20-30 sn chat cevapları. 2-3 cevabı oku, doğruyu onayla. Bu **vize 1.1 (Kod Yorumlama) mikro provası**.
5. Sonraki slayta geç.

> **Önemli:** "Tahmin Et" sorularını atlama. Vize 1.1 tam olarak bu beceriyi ölçüyor (koda bakıp ne yapacağını söyleyebilmek). 6 slayt × 30 sn = 3 dk, bunu bölüşebilmek için **zihin haritası kısa kesildi** (aşağı bak).

### Zihin Haritası (Son 3 Dakika — kısaltıldı)

Slayt 6'dan sonra boş bir sayfa paylaş (veya Zoom whiteboard). Ortaya "PYTHON" yaz. 6 dal çiz (hafta 2-7).

3 dakikada hızlı sür: Hoca 6 dalı çizer, her dala 1-2 anahtar kelime atar (slaytlarda zaten gelmiş cevaplardan devşir). Tüm öğrencileri tek tek çağırmak için zaman yok — bunun yerine **chat'e hızlı katkı**: "Bir dala eklemek istediğiniz bir kavram var mı? Chat'e yazın, hangi haftaya ait?"

> **Not:** Eski plan zihin haritası için 5 dk + öğrenci başına 30 sn tek tek çağırma öngörüyordu. Bu versiyon kısaltıldı (3 dk, chat üstü) çünkü "Tahmin Et" mikrosu slaytlarda bireysel katılımı zaten sağlıyor.

### Eğer Takılırlarsa

- Öğrenci "bilmiyorum, hatırlamıyorum" derse: "O hafta ödevlerinden birini hatırlar mısın? Hangi örnek?" → dolaylı yoldan çek.
- Bir hafta birden fazla kez unutuluyorsa: O konuda zayıflar. Notu al, ileride aynı konuyu Niyet Kartlarına daha çok koy.
- Kimse cevap vermiyorsa: "Hafta 4'te sözlük yaptık — `{"ad": "Defne"}`. Bu ne işe yarıyordu?" (bilinçli açık uçlu hatırlatma).

---

## ARA (09:20-09:25)

> "5 dakika. Defter-kalem hazırlayın. 9:25'te buradayız."

---

## BLOK 2 — Storyboard Atölyesi (09:25-10:00)

### Amaç

Kağıt-kalemle algoritma çizmeyi öğretmek. Defterde düşünmenin kodda düşünmekten farklı olduğunu hissettirmek.

### Açılış (3 dk)

> "Şimdi biraz farklı bir şey yapacağız. Ekran kapalı, defter açık. Bir tasarım sürecinden başlayalım."

> "Bir afiş tasarlarken ne yaparsınız? Doğrudan InDesign açar mısınız? Yoksa önce eskiz mi çizersiniz?"

Chat cevaplarını bekle. Yanıtlar arasında "eskiz", "moodboard", "referans" geçecektir.

> "Kod yazmadan önce de aynısını yapacağız. Buna **storyboard** diyeceğiz. 3-5 kare. Her karede tek bir şey."

### Hoca Demosu (5 dk) — Slayt 1

Ekranda `slaytlar/02_storyboard_senaryolari.md` → **Senaryo 1** (kolay).

Hoca sesli düşünerek defterinde çiziyor, ekranda tablet/kamera ile gösteriyor (veya Zoom whiteboard):

> "Niyet: 'Renk listesindeki sıcak renkleri say.' Önce ne yaparım? 
> Kare 1 — başlangıç. Elimde boş bir sayaç var. Sıfırdan başlıyor.
> Kare 2 — her rengi teker teker ele alacağım. Bir döngü açıyorum.
> Kare 3 — her renkte kontrol ediyorum: sıcak mı? Sıcaksa sayacı artır.
> Kare 4 — döngü bitince sayacı yazdır.
>
> İşte. 4 kare. Şimdi bu kareler kod yazmayı önemsiz hale getirdi."

Sonra Python karşılığını göster.

### Öğrenci Pratiği 1 — Birlikte (7 dk)

Slayt → **Senaryo 2** (orta).

> "Şimdi sıra sizde. Bu sefer hep birlikte çizeceğiz. Defterinizi açın. Ben size niyeti söyleyeceğim — siz 4 kare çizin. 3 dakikanız var."

Niyet: *"Bir puanlar listesi al. 60'ın altında olanları say ve ortalamasını bul."*

3 dakika sessizce bekle (zor ama bekle). Sonra:

> "Kamera açık olanlar defterlerini tutsun. Gösterin bakalım."

3-4 öğrencinin defterini incele. Chat'ten yorum:

> "[Öğrenci adı], kare 1'ini göstersen? … Güzel, sayaç 0'dan başlamış. Kare 2'ni görelim…"

### Öğrenci Pratiği 2 — Breakout (15 dk)

Slayt → **Senaryo 3** (zor).

Niyet: *"Projeler listesinde ortalamanın üstündeki projelerin adlarını yazdır."*

> "Şimdi 2 kişilik breakout room'lara geçeceğiz. İkiliyle 10 dakika çalışacaksınız. Biriniz storyboard çiziyor, diğeriniz pseudocode yazıyor. Sonra değişin."

Breakout açılışı:
- 5 breakout (11 öğrenci → 5 ikili + 1 üçlü ya da hoca eşlik eden 1 tekli)
- Süre: 10 dk
- "Broadcast" mesajı 8. dakikada: "2 dakika kaldı, pseudocode'unuzu tamamlayın."

Ana odaya dönüldüğünde (5 dk):
- 2-3 ikiliden ekran paylaşımı / defter gösterimi iste
- Doğru cevabı göster (Senaryo 3'ün referans çözümü)

### Hocanın Hazır Repliği (Takılanlar İçin)

| Öğrenci durumu                         | Hocanın cevabı                                          |
|----------------------------------------|---------------------------------------------------------|
| "Kare 1'de ne olacak bilmiyorum"       | "Ne elinde var? Liste mi? Boş sayaç mı? 'Başlangıç durumun' ne?" |
| "Kare 2 ve 3 aynı şey gibi"            | "Kare 2'de ne yapıyorsun? Kare 3'te ne yapıyorsun? Farklı kelime kullan." |
| "Çizim yapamam, elim yatkın değil"     | "Çizim değil, kutu + iki kelime. Tek resim çizmiyoruz." |
| Baştan Python yazıyor                  | "Dur. Python kapalı. Sadece Türkçe cümle. Kare başına 1 cümle." |
| İkiliden biri suskun                   | Breakout'a gir, direkt suskuna sor: "Sen kare kaçtasın?" |

### Online Özel Notlar

- **Kamera açık olanlar** kamerayı defterine çevirsin, kendi yüzüne değil. "Kamera hedefi: defter" diye hatırlat.
- **Kamera kapalı olanlar** defter fotoğrafını chat'e upload edebilir. Vakti varsa teşvik et, yoksa gözardı et.
- Breakout'a geçerken öğrencinin "kamera aç ki partnerin görsün" hatırlatmasını yap.

---

## ARA (10:00-10:10)

> "10 dakika ara. Kahve, esneme, pencere aç. 10:10'da devam."

---

## BLOK 3 — Parsons Puzzle (10:10-10:45)

### Amaç

Karışık kod satırlarını doğru sıraya koyarak **bağımlılık sezgisi** geliştirmek. Bir satırı koyabilmek için ondan önceki satırda ne olması gerektiğini anlamak.

### Açılış (3 dk)

> "Şimdi ters bir oyun. Size karışık kod satırları vereceğim. Sizin işiniz satırları doğru sıraya koymak. Kimin önce geldiğini bulacaksınız."

> "İki taktik: önce **hangi değişken nereden geliyor** — yani tanımlamaların nerede olduğunu bulun. İkinci taktik: **girintilere dikkat**. Girintili satırlar bir başka satırın içindedir."

### Puzzle 1 — Kolay, Birlikte (8 dk)

Slayt: `slaytlar/03_parsons_puzzles.md` → Puzzle 1.

1. Ekrana karışık satırları göster. Harfleri oku. (30 sn)
2. **Tahmin Et mikrosu (30 sn):** "Hiç sıralamadan — bu 5 satır doğru sırada olsa ekrana ne yazardı? Chat'e tek sayı." → 1.1 provası. Beklenen: `340`.
3. "Şimdi sıraya koyun. Defterinize harfleri yazın." (3 dk)
4. Chat'ten cevap topla, doğru sırayı birlikte aç. (2 dk)
5. Neden-bu-sıra slaytını ekrana ver. (2 dk)

### Puzzle 2 — Orta, Bireysel (11 dk)

Slayt: Puzzle 2.

1. Karışık satırları göster. (30 sn)
2. **Tahmin Et (30 sn):** "Kod doğru sıradaysa ne yazar? Chat'e tek sayı." Beklenen: `3`.
3. "5 dakika. Sıraya koyun, chat'e yazın. Tuzak satır var — kullanmak zorunda değilsiniz." (5 dk)
4. Cevaplar gelsin. Tuzak kullanan öğrenciye "G'yi çıkarınca ne olur?" diye dön. (2 dk)
5. **Tuzak mikrosu (30 sn):** "G satırı neden mantık hatası? Tek cümleyle chat'e yazın." → 3.1 provası. 2-3 cevabı oku.
6. Doğru sırayı ekrana aç. (2 dk)

### Puzzle 3 — Zor, Breakout (10 dk)

Slayt: Puzzle 3. Fonksiyon + döngü + koşul içerir.

1. Karışık satırları göster. Harfleri oku. (30 sn)
2. **Tahmin Et (30 sn):** "Bu fonksiyon doğru kurulursa `sonuc` ne olur? Chat'e tek sayı." Beklenen: `95`.
3. "Yine 2 kişilik breakout. Birlikte çözüp chat'e tek cevap gönderin." (5 dk breakout — eskiden 8 idi, kısaldı)
4. Ana odaya dönüş, doğru sırayı aç, **girinti haritasını** göster. (2 dk)
5. **Tuzak mikrosu (30 sn):** "J satırı konulursa ne döndürür ve **neden**? Chat'e tek cümle." → 3.1 provası. 1-2 cevabı oku.
6. Kapanış: "Doğru sırada fonksiyon 95 döner. J ile 100 dönerdi — başlangıç çok büyük." (30 sn)

> **Süre kırpma notu:** Puzzle 3 breakout eskiden 8 dk idi, mikrolar için 5 dk'ya düştü. İkili zaten tahmin evresinde mantığı gördüğü için breakout daha verimli geçiyor.

### Hocanın Hazır Repliği

| Öğrenci durumu                             | Hocanın cevabı                                             |
|--------------------------------------------|------------------------------------------------------------|
| "Nereden başlayacağımı bilmiyorum"         | "Önce tanımlama satırını bul — hangi satır bir değişken yaratıyor?" |
| Girintisiz satırı döngünün içine koyuyor   | "Satırın başındaki boşlukları sayar mısın? Girintili mi değil mi?" |
| Tüm satırları kullanmaya zorlanıyor        | "Her satırı kullanmak zorunda değilsin. Bazısı tuzak."     |
| Cevap hemen yanlış veriyor                 | "Acele etme. Her satırı elinle 'yürüt' — bu satır çalıştığında ne olur?" |

### Online Özel Notlar

- Chat çok hızlı akacak. Cevapları aldıkça sayıyı vurgula: "8 cevap geldi, 3'ü doğru."
- Yanlış cevap verene dokunurken ismini söyle ama yargılama — "X çıkardığı için yanlış olmuş, doğal" tarzı.

---

## ARA (10:45-10:50)

> "5 dakika. Son bloğa hazırlan. Defter yanında olsun — son blokta en çok defteri kullanacağız."

---

## BLOK 4 — Niyet → Pseudocode → Kod (10:50-11:30)

### Amaç

Vize Bölüm 3.3'ün birebir provası. Niyetten kod üretmek. Her öğrenci **Kart 7'yi bireysel** yapsın.

**Ana akış:** Intro (5) → **Kart 1** (8, ısınma) → **Kart 4** (10, vize 3.3a) → **Kart 2** (2, kısa köprü) → **Kart 7** (12, vize 3.3b **bireysel**) → Kapanış (3). Toplam **40 dk**.

**Not:** Kart 3, 5, 6, 8, 9, 10 slaytta hazır ama derste kullanılmayacak — öğrenci PDF olarak alacağı için evde pratik eder. Plandan sapmanın bedeli yüksek: Kart 4 ve Kart 7 atlanırsa vize provası boşa düşer.

### Açılış (4 dk)

> "Vize paketinde Bölüm 3.3 var — Niyet → Kod. Bu son blok tam o görevin provası. Size niyet vereceğim, siz 4 aşamada geleceksiniz: storyboard, pseudocode, Python, test."

> "Açık olayım: bu blokta yapacağımız **iki kart vize 3.3'te, bir ek egzersiz de 3.2'de birebir prova**. Dikkatli olun."

Slayt: `slaytlar/04_niyet_kartlari.md` → Kart 1.

### Kart 1 — Birlikte, Tam Süreç (7 dk) — Isınma

Kart 1'in niyeti: *"Projeler listesini gez. Her projenin adını yazdır."*

**Süreç:**
1. "Önce defterinize storyboard çizin. 2 dakika." (2 dk)
2. "Chat'e pseudocode'unuzun ilk satırını yazın." (1 dk)
3. Gelen cevaplardan 2-3'ünü oku, karşılaştır.
4. Ekranda tam pseudocode'u birlikte yaz (kart 1'in örneği).
5. Python'a çevir, çalıştır, çıktıyı göster.

Amaç: süreç alışkanlığı. Kart kolay olsun ki herkes ritmi tutsun.

### Kart 4 — Birlikte, Vize 3.3(a) Provası (9 dk)

Kart 4'ün niyeti: *"Tüm projelerin puan ortalamasını hesapla ve yazdır."*

> "Bu kart vize'de ayniyle var. Adı `ortalama_puan`. Bugün birlikte çözeceğiz — evde bir kez daha bakmadan yazın."

**Süreç:**
1. "Storyboard — defterinize. 2 dk." (2 dk)
2. "Chat'e pseudocode'u 2-3 satır olarak yazın. Tam Türkçe." (2 dk)
3. 2-3 cevabı oku, doğruları onayla.
4. Python birlikte yazılır — hoca ekranda, bir öğrenci (adıyla çağır) satır söyler. (3 dk)
5. Fonksiyon versiyonuna çevir (`def ortalama_puan(projeler):`). Vize'de bu istenecek. (2 dk)
6. Çalıştır, çıktı: `Ortalama: 82.5`. (1 dk)

> "Bakın — bu fonksiyonu vize kağıdınızda da göreceksiniz. Defterinizde bu sayfa dursun."

### Kart 4.5 — "Değiştir" Mikrosu, Vize 3.2 Provası (3 dk)

> "Az önce Kart 4'ü çözdük. Şimdi o kodu **değiştiriyoruz** — yeniden yazmıyoruz. Vize'de Bölüm 3.2 böyle olacak."

**Süreç:**
1. "Yeni niyet: sadece 80+ puanlıların ortalaması. Kart 4'teki koda hangi 3 değişiklik gerekir?" (chat'e iste, 30 sn)
2. Beklenen cevaplar: "if ekle", "sayaç ekle", "len yerine sayaç ile böl". Gelen doğru cevapları ekranda Kart 4 kodunun üstüne **kalın** işaretle.
3. Ekranda birlikte değiştir, çalıştır, çıktı `89.75` çıkar. (2 dk)
4. Kapanış cümlesi: "Bölüm 3.2'de **asla** baştan yazmayın — verilen kodu tuşlayıp değiştirin. Yeni baştan yazmak sizi yavaşlatır."

### Kart 2 — Kısa Köprü (2 dk)

Kart 2'nin niyeti: *"Puanı 80'in üstünde olan projelerin adını yazdır."*

Bu kart tek başına zaman almıyor — sadece hatırlatma. Pseudocode'u ekranda göster, Python'u göster, "Bu yapıyı Kart 7'de kullanacağız" de. Geç.

### Kart 7 — BİREYSEL, Vize 3.3(b) Provası (12 dk)

Kart 7'nin niyeti: *"En yüksek puanlı projenin adını yazdır."*

> "Son kart tamamen size. 10 dakika tek başınıza çalışacaksınız. Storyboard → pseudocode → Python. Takılanlar bana DM atsın, chat'e yazmayın."

> "Bu kart vize'de ayniyle var. Adı `en_yuksek_puanli`. Kendiniz yapacaksınız — bakarak yapmadığınızı bilin."

10 dakika boyunca:
- Kamera kapalı olabilir (düşünme zamanı).
- Hoca sessiz kalır ama DM'leri takip eder.
- 5. dakikada chat'e broadcast: "İlk takip değişkeniniz ne? (en_iyi_puan)."
- 8. dakikada: "2 dakika kaldı. Python'unuzu çalıştırın."

10. dakikada (2 dk):
> "Bir öğrenci ekran paylaşımı açsın — kodunu göstersin."

1 öğrencinin çözümünü incele. Yanlışları tanısal dille ele al:

> "İki takip değişkeni kurmuş — `en_iyi_puan` ve `en_iyi_ad`. İkisini de aynı anda güncelliyor — güzel. Başlangıçta `0` vermiş, bu veride çalışır ama tüm puanlar negatif olsaydı yanılırdı. Mantık sağlam."

### Kapanış (3 dk)

Dersin bittiği anda öğrenci vize'ye dönecek — bu bloğun kapanışı "sayfa çevirme" ritüeli, dinlenme değil.

> "Bu hafta yeni Python öğrenmedik. Yeni bir **süreç** öğrendik: niyet → storyboard → pseudocode → Python. Artık ekrana bakıp donduğunuzda defteriniz kurtarıcı."

> "Dersten çıkar çıkmaz vize'ye döneceksiniz. Bölüm 3.3'e geldiğinizde bugünkü Kart 4 ve Kart 7'yi göreceksiniz — ayniyle. Bölüm 3.2'de ise Kart 4.5'teki 'değiştir' mantığını göreceksiniz. Defteriniz açık, ders notunuz açık — hepsi sizin yanınızda."

> "İki şey söyleyeceğim. Bir: 3.3'e geldiğinizde önce **defterinizi açın**. Storyboard çizin. Pseudocode yazın. Sonra Python'a geçin. Bugün yaptığımız süreç — aynı süreç. Kafanızı vermeden Python yazmak, bu hafta ezbere yazma kalıbının adıydı."

> "İki: takıldığınızda `hafta[2-6]/ornekler/` klasörüne bakın, sık kullanılan kalıplar orada. DM atabilirsiniz; pazartesi boyunca buralardayım."

> "24 Nisan Cuma'ya kadar 7 gün var. Acele etmeyin, bir oturuşta bitirmeyin. Son gece bırakmayın — mantığınız dağılır."

Chat'e son mesaj:
```
Vizede Bölüm 3.3 → Kart 4 + Kart 7 (bugünkü prova)
       Bölüm 3.2 → Kart 4.5 mantığı (değiştir)
Defter + ders notu + gita2112/ klasörü = elinizin altında.
LLM yasak. Başarılar.
```

### Hocanın Hazır Repliği — Kart 7 İçin

| Öğrenci durumu                                 | Hocanın cevabı                                     |
|------------------------------------------------|----------------------------------------------------|
| "Nereden başlayacağım bilmiyorum"              | "Niyet cümlesini tekrar oku. 'En yüksek' derken ne takip etmen gerekiyor? Bir değil iki şey." |
| Pseudocode yazmadan Python yazmaya başlıyor    | "Python kapat. Türkçe yaz önce. 3 satır pseudocode yeterli." |
| Başlangıç değeri yok (`en_iyi_puan` tanımsız)  | "İlk kare nerede? Karşılaştırma yapmadan önce neye karşı karşılaştırıyorsun?" |
| Sadece puanı güncelliyor, adı unutuyor         | "İki değişkeni birlikte güncelle — biri güncellenip diğeri güncellenmezse ad yanlış kişiye kalır." |
| Çıktı yanlış ama mantık doğru                  | "Tek bir yerde yanlışın var — hangi satır olduğunu bulabilir misin? Elinle yürüt." |

---

## Ders Sonrası (11:30-12:00)

- [ ] Kaydı (varsa) öğrencilere at
- [ ] Ders sırasında suskun kalan öğrencilere kısa DM: "Vize Bölüm 3'te takılırsan bana yaz, birlikte bakarız."
- [ ] Defterde güzel çalışan öğrencinin fotoğrafını (izinle) dersten sonra paylaş — model olur.

---

## Risk ve Önlemler

### Risk: Vize paniği, derse konsantre olamıyorlar

Açılışta vize hakkında 30 saniye tanımlayıcı konuşma yap:
> "Vize Bölüm 3'te panik yapanlar için söylüyorum — bu dersin amacı tam olarak 3.3'ü kolaylaştırmak. Bugünü atmayın."

### Risk: Storyboard çizimi ciddiye alınmıyor

> "Çizimlerinizi göstereceksiniz. 'Beceremem' olmaz — kutu + iki kelime. Tasarımcısınız, bu size kolay."

Tasarım kimliklerine dokunarak ciddiye aldırmak işe yarar.

### Risk: Chat'e cevap yazılmıyor, sessizlik

5 saniye bekle. Sonra ismen çağır: "[Öğrenci adı], senin fikrin ne?"
Çağrılmak istemeyen kamera kapatanları ismen çağırma — DM'den sor.

### Risk: 1-2 hızlı öğrenci tüm cevapları erken veriyor

Onlara DM at: "Sen hızlısın. Diğer arkadaşlar kavrayana kadar cevap vermeden bekle, sonra doğrulamak için yaz."

### Risk: Zamanlama kayar, son blok eksik kalır

Blok 1'i 15 dakikaya sıkıştırabilirsin (zihin haritası sondan kısaltılabilir). Blok 2 breakout 12 dakikaya düşer. Asla Blok 4'ten kesme — vize provası o.

---

## Dosya Referansları

- Ders notu (öğrenciye): `hafta7/ders_notu.md`
- Slaytlar (hoca, ekran paylaşımı):
  - `hafta7/slaytlar/01_hatirlama.md`
  - `hafta7/slaytlar/02_storyboard_senaryolari.md`
  - `hafta7/slaytlar/03_parsons_puzzles.md`
  - `hafta7/slaytlar/04_niyet_kartlari.md`
- Defter sayfası (öğrenciye, yazdırılacak): `hafta7/ogrenci_defter_sayfasi.md`
