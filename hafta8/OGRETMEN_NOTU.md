# Hafta 8 — Öğretmen Notu

> Bu belge yalnızca öğretmen içindir. Öğrencilere paylaşılmaz.

Bu hafta **stratejik olarak yoğun** — 7 konu, 3 saatlik ders. Buradaki notlar zaman bütçeni, demo kararlarını ve plan B senaryolarını netleştirmek için.

---

## Stratejik Çerçeve

Hafta 8'in tek hedefi: H10 vibecoding seansında öğrencinin "Gemini bana bu kodu verdi, nereye koyacağımı, nasıl çalıştıracağımı, hata alırsam ne yapacağımı bilmiyorum" demesini önlemek.

**Filtre soru:** Bu blok, öğrencinin Gemini çıktısıyla bir başına kalınca işine yarayacak mı? Yararlanmıyorsa kes.

---

## Zaman Bütçesi (180 dk net ders, +15 dk mola)

| Blok | Konu | Min | İdeal | Lüks | Notlar |
|---|---|---|---|---|---|
| 0 | Hata refleksi (ısınma) | 5 | 7 | 10 | Sadece ad ve "son satıra bak" — derinleşme yok |
| 1 | Terminal | 15 | 20 | 25 | 3 komut + göreli/mutlak yol |
| 2 | uv + bağımlılık | 30 | 40 | 50 | **Plan B kritik** (aşağıda) |
| — | Mola | 10 | 10 | 15 | İlk 1.5 saatten sonra |
| 3 | Dosya I/O (txt) | 25 | 30 | 35 | encoding demosu canlı |
| 4 | import + modül | 15 | 20 | 25 | math/random/datetime turu |
| 5 | CSV | 10 | 15 | 20 | Bölüm 4'ün uzantısı gibi |
| 6 | JSON | 20 | 25 | 30 | indent=2 görsel kontrast |
| 7 | Traceback derinleşme | 15 | 20 | 25 | Sondaki yer — 5 hata tipini canlı çalıştır |
| 8 | Yabancı kod okuma | 20 | 25 | 30 | **Kesilemez** — vibecoding'in özü |
| | **Toplam** | **165** | **210** | **265** | İdeal hedef: 195-210 dk |

> ⚠️ **Bütçe uyarısı:** 180 dk net ders + 15 dk mola = **195 dk efektif**. **Minimum sütununa yakın koşmaya niyet edin** — ideal sütun başarılırsa lüks. Lüks sütun (265 dk) sadece 4 saatlik bir ders senaryosunda anlamlı; 3 saatlik tek seansta asla. Bölüm 1 ve Bölüm 8'in min süreleri özellikle dar — pratikte sırasıyla 18-20 ve 25-30 dk hedefleyin.

**Yetişmezse kesim sırası:** 1) Bölüm 5 (CSV) en aza in — sadece dosyayı göster, açıklamayı evdeki örneklere bırak. 2) Bölüm 4 (import) ders notuna ev ödevi olarak yönlendir. 3) Bölüm 6 JSON'u 15 dk'ya sıkıştır. **Hiçbir koşulda** Bölüm 0 (hata refleksi) ve Bölüm 8 (kod okuma) kesilmez.

### Bölüm 8 (09_kod_okuma) için Stratejik Karar

09_kod_okuma.py 5 fonksiyon içeriyor (~130 satır). 25 dk içinde **hepsini** sınıfta yorumlamaya çalışmayın — yetişmez. Önerilen plan:

- **Sınıfta birlikte (15 dk):** İlk 2 fonksiyonu satır satır yorumlayın (`csv_oku` ve `sicak_renkleri_bul` gibi). Bu, list comprehension + try/except + tip ipucu okuma refleksini açar.
- **Sınıfta hızlı geçiş (5 dk):** Kalan 3 fonksiyonun yapısını (imza + ne yaptığı) gösterin, satır satır yorum yapmayın.
- **Ev ödevi (5 dk söz vermek yeterli):** "Ev için: kalan 3 fonksiyonun `# SİZİN YORUMUNUZ` satırlarını siz doldurun. Hafta 9'da kontrol edeceğiz."

Böylece Bölüm 8 25 dk'da bitse bile içerik kalitesi düşmez.

### Ödev 5 ↔ 09_kod_okuma Benzerliği — Kasıtlı

Ödev 5 (CSV→JSON) ile 09_kod_okuma.py akış olarak çok benziyor. Bu **kasıtlıdır**: öğrenci 09'u ders sonunda görüp ev ödevinde uyarlayacak. "Yabancı kodu oku, kendi probleme uyarla" — vibecoding'in özü. Öğrenci "Ödev 5'i yaparken 09'a bakayım mı?" diye sorarsa: **evet, mutlaka**.

---

## Bölüm 2 (uv) İçin Kritik Karar: Demo mu, Slayt mı?

### Önerilen: Canlı demo
- Hocanın ekranında `uv init`, `uv add requests`, `uv run` komutları gerçek zamanlı çalışsın.
- Öğrenciler izlesin, kendi makinelerinde **denemek için Ödev 1**'e bıraksın.
- **Avantaj:** "Bu komutlar çalışıyor, gerçek" hissi. Soyut kalmıyor.

### Plan B: Bir öğrencinin makinesi sorun çıkarırsa
1. Eğer öğrenci uv kuramıyor (PATH, network, izin) — o öğrenci için canlı çözüm aramayın, ders bekler.
2. "Bugün izle, akşam birlikte hallederiz" deyip dersi devam ettirin.
3. Sınıfta 3+ kişi takılıyorsa — derste konuyu kavramsal seviyede bırakın, `uv` kurulumunu **bir sonraki dersin başına** alın (10 dk).

### Plan C: Hiç kimse uv kuramazsa
- Çok düşük ihtimal. Eğer böyle bir senaryo olursa: ders notunda anlatın, demoda "şu komut şunu yapar" diye gösterin (kuramayan da kavrar), kurulumu **tamamen Ödev 1'e** itin. Bir sonraki dersin başında 15 dk hızlı çek.

---

## Bölüm 0 (Hata Refleksi Isınma) Senaryosu

Dersin **ilk 5-7 dakikası**. Slayt veya tahta yeter. Söylenecekler:

> Bugün hata göreceksiniz. Çoook hata. Komut yanlış yazılır, dosya bulunmaz, modül kurulu değildir. **Panik yok.** Python bize her zaman bir şey söyler — buna **traceback** denir, son satırı bizi yönlendirir. 5 sık tip var:
>
> - `NameError` — yazım yanlış (yas vs yass)
> - `TypeError` — yanlış tip işlemi (str + int)
> - `IndentationError` — girinti hatası
> - `FileNotFoundError` — yanlış klasördesin veya dosya yok
> - `ModuleNotFoundError` — `pip install` veya `uv add` yapmadın
>
> Refleks: **HATA → en alt satıra bak → tipi gör → tanıdık mı?**
>
> Bugün dersin sonunda detaya gireceğiz, ama şu refleksi şimdiden alın.

Sonra ders boyunca her hata çıktığında: "Tanıdık geldi mi? Hangi tip?"

---

## Demo Hazırlığı (Ders Öncesi)

- [ ] Kendi makinende `uv` çalışıyor mu? Versiyonu güncel mi?
- [ ] `hafta8/ornekler/` klasöründe bir kez tüm örnekleri çalıştırdın mı? `python3 03_dosya_okuma.py` … `09_kod_okuma.py`
- [ ] **Encoding demosu için** `encoding="utf-8"` parametresi olmadan dosya okuduğunda ne olduğu hazırlandı mı? (Mac'te göstermek zor — slaytta Windows ekran görüntüsü daha güçlü)
- [ ] **JSON `indent=2` görsel kontrast** için iki ekran görüntüsü: tek satır jumbo JSON vs. indent'li güzel JSON
- [ ] `08_traceback_okuma.py` — Hata 3 (IndentationError) için ayrı `deneme_indent.py` dosyası hazır mı? (Aynı dosyada uncomment edilirse her şeyi bozar)

---

## Ödev Akışı

| Ödev | Zorluk | Süre tahmini | Ön koşul | Yapılacak |
|---|---|---|---|---|
| 1 | Kurulum | 30-45 dk | uv kurulu | Terminal + uv akışını belgelemek |
| 2 | Kolay-Orta | 30-40 dk | Bölüm 3 | input + f-string + dosya yazma/okuma |
| 3 | Orta | 30-45 dk | Bölüm 3 + H4 sözlük | Dosya okuma + filtre + sayma |
| 4 | Orta | 40-50 dk | Bölüm 4-5 (JSON) | Sözlük + JSON yazma/okuma + güncelleme |
| 5 | Zor | 60-80 dk | Tümü + H6 fonksiyon | CSV → JSON dönüşüm, **fonksiyon iskeletinde** |

**Ödev 5'in özelliği:** H6 fonksiyonlarını H8'de yazma seviyesinde kullanan tek ödev. Öğrenci `def` iskeletini görüp içini doldurur. Bu, vibecoding'de Gemini'nin üreteceği fonksiyon-yapılı kodu okuma+değiştirme prova eder.

---

## Risk Tablosu

| Risk | Olasılık | Etki | Müdahale |
|---|---|---|---|
| uv kurulum sorunu (1 öğrenci) | Yüksek | Düşük | "İzle, akşam halledelim" |
| uv kurulum sorunu (3+ öğrenci) | Orta | Yüksek | Demo'yu kavramsal seviyeye düşür, kurulumu sonraya bırak |
| `encoding="utf-8"` ezbere yazılır | Yüksek | Orta | Canlı demoda bozuk açılışı **göster** — tılsım olmaktan çıkar |
| 09_kod_okuma kesilir | Orta | Çok yüksek | Diğer blokları sıkı tut, 9'u kesinlikle kesme |
| Öğrenci ödev 5'te çıkmaza girer | Yüksek | Düşük | Fonksiyon iskeleti var — 4 küçük problem, hep birden değil |
| Ders 30+ dk geride kalır | Orta | Yüksek | Bölüm 5 (CSV) ile başlayarak kes |

---

## Hafta 9 İçin Köprü

H8'in son cümlesi: "Önümüzdeki hafta bu konuları pekiştireceğiz, sonra Hafta 10'da Gemini ile vibecoding yapacağız." Öğrenci bu mesajı **dersin son 2 dakikasında** netçe duymalı.

H9 planı: try/except ayrıntı + traceback pratik atölyesi + Gemini'den geliyor gibi yabancı kod okuma alıştırmaları + opsiyonel `requests` + JSON API mini demo. Bu pakete H8 sonunda hangi konularda ek pratik gerektiği görülerek karar verilir.
