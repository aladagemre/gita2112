# GİTA 2112 — Hafta 9: Vibecoding (Gemini ile Web Sayfası Üretmek)

> Bu hafta Python yazmıyoruz — **kod okuyoruz ve yönetiyoruz**.
> Gemini bizim için kod yazacak, biz onu çalıştıracak, beğenmeyince değiştirteceğiz.
> Bu belge, derste yapacaklarımızın yazılı özetidir.

---

## Hafta 8'den Bu Yana

Geçen hafta `import`, dosya okuma/yazma, `try/except` ve `class` gibi yapıları gördük. Hatta `09_kod_okuma.py` ve `15_yabanci_kod_atolye.py` dosyalarında **başkasının yazdığı kodu satır satır okumayı** denedik. Bu haftanın temeli oydu.

Bugün artık şunu söyleyebiliriz:

> Python'un içini öğrenmiş bulunuyoruz. Bundan sonra **dile yön vermeyi** öğreneceğiz.

---

## 1. Vibecoding Nedir?

Vibecoding, kodu **kendi elinizle yazmadan** bir yapay zekaya yazdırma pratiğidir. Siz ne istediğinizi tarif edersiniz, model üretir. Sonra çıktıyı değerlendirir, eksiklerini söyler, yeniden ürettirirsiniz.

### Programcı Değil, Yönetmen

Yedi hafta boyunca bir **programcı** gibi düşündünüz: satır satır kod yazdınız. Bugünden itibaren modunuzu değiştirin. Artık bir **yönetmen** gibi düşünüyorsunuz:

- Yönetmen kameranın arkasında durmaz, kamerayı kullanmaz.
- Yönetmen ne istediğini bilir, **doğru kelimelerle anlatır**.
- Çekim olur, beğenmezse "tekrar" der.
- Bir iş bitince diğer setine geçer.

Vibecoder de böyledir. Tek farkı — ekibi yapay zeka.

### Tasarım Dünyasından Bir Benzetme: Art Director ve Asistan

Bir tasarım ajansında **art director** ne istediğini söyler, **asistan/uygulamacı** üretir. Art director şöyle der:

> "Posterin alt kısmına 3 sütunlu bir grid yerleştir. Solda fotoğraf, ortada başlık, sağda metin. Başlık 60pt, font Garamond. Arka plan #0F0F0F, yazılar krem."

Asistan açar Illustrator'ı, yapar. Art director bakar, "başlığı 80pt yap, fotoğrafı sağa al" der. Asistan yapar.

**Siz art director'sınız. Gemini asistanınız.** Bu hafta ondan size HTML/CSS web sayfaları üretmesini isteyeceksiniz.

> ↪ **Vibecoding Kuralı 1:** Kod yazma kasını dinlendir. **Tarif etme** kasını çalıştır.

---

## 2. İyi Prompt Anatomisi

Gemini'ye "bir web sayfası yap" derseniz size jenerik, sıradan bir şey verir. Çünkü ne istediğinizi bilmiyor. **İyi bir prompt** üç şeyi söyler:

> **[Ne istiyorum] + [Kısıtlar] + [Format]**

### Kötü Prompt vs İyi Prompt

| Kötü | İyi |
|------|-----|
| "bir web sayfası yap" | "Kişisel portfolyo sayfası yap. İsim: Elif Yılmaz. Siyah arka plan, beyaz yazı, vurgu rengi #FF6B6B. 3 proje kartı: 'Caz Festivali Afişi', 'Doğa Derneği Kimliği', 'Kitap Kapağı'. Tek HTML dosyası, harici CSS framework kullanma." |
| "renkli bir sayfa lazım" | "4 renk paleti gösteren HTML galeri sayfası yap. Paletler: Yaz Sıcağı (#FF6B6B, #FFD93D, #FF8C42), Kış Tonları (#1E3A8A, #3B82F6, #93C5FD), Pastel Bahçe (#FFB5A7, #FCD5CE, #F8EDEB), Gece Mavi (#22223B, #4A4E69, #9A8C98). Her palette renk bloğu + altında hex kodu. Beyaz arka plan, sistem fontu. Tek HTML dosyası." |
| "fonksiyon ekle" (mevcut koda) | "Bu HTML kodunu düzenle: [KOD]. Her proje kartına hover efekti ekle — fareyle üstüne gelinince kart hafifçe büyüsün ve gölge alsın. Kodun gerisini değiştirme." |

### Üç Parçayı Açıklayalım

**[Ne istiyorum]** — Çıktının cinsi ne? "Portfolyo sayfası", "renk paleti galerisi", "fotoğrafçı sitesi". Belirsiz değil, **belirli bir tür** söyleyin.

**[Kısıtlar]** — Sınırlar, kurallar, içerik. İsimler, hex kodları, kullanılacak/kullanılmayacak şeyler. Bir tasarım brifi yazar gibi yazın.

**[Format]** — Çıktı nasıl gelmeli? "Tek HTML dosyası, CSS gömülü", "İki ayrı dosya: index.html ve style.css", "Sadece HTML kodunu ver, açıklama yapma".

> ↪ **Vibecoding Kuralı 2:** **Tarif edilmemiş şey jenerik döner.** Renk yoksa Gemini Material varsayılanını verir. İçerik yoksa "Lorem ipsum" alırsınız.

---

## 3. Kurulum: Gemini Code Assist + Live Server

Bu iki eklentiyi ders öncesi kurmanız gerekiyor. Bir kere yapılır, sonra hep kullanılır.

### Gemini Code Assist — VS Code'a Kurun

VS Code'un sol kenarında blok gibi bir ikon var: **Extensions** (`Ctrl+Shift+X` / `Cmd+Shift+X`). Oraya tıklayın, arama kutusuna yazın:

```
Gemini Code Assist
```

Google'ın eklentisi çıkacak (yayıncı: Google). **Install** deyin. Kurulduktan sonra VS Code sol kenarında **Gemini ikonu** belirir.

İkona tıklayın → **Sign in with Google** → Google hesabınızla giriş yapın. Giriş başarılıysa sol altta "Gemini Code Assist" yazar.

Artık tarayıcıya geçmeden, **doğrudan VS Code içinde** Gemini'ye soru sorabilirsiniz.

### Live Server — Otomatik Yenileme İçin Kurun

Yine Extensions'a girin, yazın:

```
Live Server
```

Ritwick Dey'in eklentisi. **Install** deyin. Kurulunca hazır — ek giriş gerekmez.

---

## 4. İlk Sayfayı Yapma Akışı

Gemini Code Assist kuruluysa iki farklı yol var. **Yol B daha pratik**, özellikle değişiklik yaparken.

### Yol A — gemini.google.com üzerinden

1. Tarayıcıda gemini.google.com'u açın.
2. Promptu yazın, **Enter**.
3. Gelen kod bloğunun sağ üstündeki **"Copy"** butonuna tıklayın.
4. VS Code'a geçin → **File → New File → Save As → `index.html`** olarak kaydedin.
5. Yapıştırın (`Ctrl+V`) ve kaydedin (`Ctrl+S`).

### Yol B — VS Code içinde Gemini ile (Önerilen)

1. VS Code'da `index.html` adında boş bir dosya oluşturun (File → New File → Save As).
2. Sol kenardaki **Gemini ikonuna** tıklayın → chat paneli açılır.
3. Promptunuzu yazın, **Enter**.
4. Gemini kod bloğu verir. Bloğun üstünde **"Insert into file"** veya **"Apply"** butonu çıkar → tıklayın.
5. Kod doğrudan `index.html`'e girer. Kaydedin.
6. **`index.html`'e sağ tıklayın → "Open with Live Server"** — tarayıcı açılır ve her kaydettiğinizde otomatik yenilenir.

> Dosya adının sonu **`.html`** olmak zorunda. Yoksa tarayıcı açmaz.

> ↪ **Vibecoding Kuralı 3:** Çalıştırmadan beğenip beğenmediğine karar verme. Önce **tarayıcıda gör**.

---

## 5. İterasyon Döngüsü

Bir prompttan mükemmel çıktı almak nadir bir hadisedir. Asıl iş **iterasyondadır**:

```
Aldım → Çalıştırdım → Beğenmedim → Söyledim → Tekrar aldım
```

Bu döngüyü 3-5 kere yapacaksınız. Her döngüde sayfa biraz daha sizinkine benzeyecek.

### VS Code içinde Gemini ile İterasyon (Önerilen)

VS Code'da Gemini Code Assist chat paneli zaten açıkken şunu yapın:

1. `index.html` dosyasını açık bırakın.
2. Chat paneline sadece **ne değiştirmek istediğinizi** yazın — HTML bilmenize gerek yok, Türkçe tarif edin:
   > "Vurgu rengini sarıdan kırmızıya çevir"
   > "Projelerin üstüne kısa bir 'Hakkımda' bölümü ekle"
   > "Kart arka planları biraz daha açık olsun"
3. Gemini mevcut dosyayı görüyor ve değişikliği uyguluyor.
4. Live Server sayfa yenileniyor — tarayıcıda sonucu görüyorsunuz.

### gemini.google.com'da İterasyon

Tarayıcı üzerinden gidiyorsanız **aynı konuşma sekmesini kapatmayın**. Gemini o konuşmada az önce ne verdiğini biliyor. Sadece ne değiştirmek istediğinizi yazın:

> "Vurgu rengini #FFE66D yerine #FF6B6B yap."
> "Projelerin üstüne kısa bir 'Hakkımda' bölümü ekle."
> "Kartların üzerine gelinince hafifçe büyüsün."

Yeni kodu kopyalayıp `index.html`'in **tamamının üstüne yapıştırın** (eski kodu silin, yenisini koyun).

> ↪ **Vibecoding Kuralı 4:** Konuşmayı kapatırsanız Gemini sıfırlanır. **Aynı sekmede devam edin** — ya da yeni sekme açtıysanız sayfanızın son halini "Bu sayfam var, şunu değiştir" diye yapıştırın.

### Örnek İterasyon Zinciri

**1. Tur — İlk sayfa:**
> "Kişisel portfolyo sayfası yap. İsim: Defne Aksu. Renkler: siyah arka plan, beyaz yazı, vurgu #FFE66D. 3 proje. Tek HTML."

**2. Tur — Renk değiştir:**
> "Vurgu rengini #FFE66D yerine #FF6B6B yap."

**3. Tur — İçerik ekle:**
> "Projelerin üstüne kısa bir 'Hakkımda' bölümü ekle. 3-4 cümlelik boş alan olsun."

**4. Tur — Etkileşim ekle:**
> "Proje kartlarının üzerine gelinince kart hafifçe büyüsün ve gölge alsın."

---

## 5. Hata Aldığında Ne Yaparsın?

HTML'de geleneksel anlamda **traceback yoktur**. Tarayıcı genelde hataları görmezden gelir — sayfa eksik veya kırık görünür ama "kırmızı yazı" çıkmaz. Bu kafa karıştırıcı olabilir.

### Olası Belirtiler ve Refleksler

| Belirti | Olası sebep | Ne yapacaksın |
|---|---|---|
| Tarayıcıda boş beyaz sayfa | Dosya hiç yüklenmedi, `.html` uzantısı eksik | Dosya adını kontrol et |
| Sayfa açılıyor ama stilsiz görünüyor | `<style>` etiketi eksik veya bozuk | Gemini'ye "stiller uygulanmıyor" de + kodu yapıştır |
| Bazı içerik görünmüyor | Bir HTML etiketi kapanmamış | Gemini'ye "şu bölüm görünmüyor" de + kodu yapıştır |
| Türkçe karakterler bozuk | `<meta charset="utf-8">` eksik | Gemini'ye "Türkçe karakterler bozuk geliyor" de |
| Kod uzun ve karmaşık | Kasten karmaşıklaştırılmış | Gemini'ye "Bunu sadeleştir, gereksiz CSS'i sil" de |

### Hata Bildirme Promptu

VS Code içinde Gemini ile çalışıyorsanız dosyayı açıkken chat'e yazın:
> "Sayfa tarayıcıda açılıyor ama stiller uygulanmıyor. Neden olabilir, düzelt."

gemini.google.com'daysanız ve **aynı konuşmadaysanız:**
> "Az önce verdiğin sayfayı tarayıcıda açtım, stiller uygulanmıyor. Düzelt."

**Konuşmayı kapatıp yeniden başlattıysanız:** Gemini sıfırlandı. `index.html` dosyasını VS Code'da açın, tüm içeriği kopyalayın (`Ctrl+A` → `Ctrl+C`), yeni Gemini konuşmasına yapıştırın ve sorunuzu ekleyin:
> "[YAPIŞTIRILMIŞ KOD] — Bu sayfayı tarayıcıda açtığımda stiller gelmiyor. Düzelt."

> ↪ **Vibecoding Kuralı 5:** Gemini ne gördüğünü tahmin edemez. **Ekranda ne gördüğünüzü tarif edin**, "çalışmıyor" demeyin.

---

## 6. Üç Sayfa Şablonu

Bu hafta üç farklı sayfa türünden birini seçeceksiniz. Hangisi hoşunuza giderse onu yapın.

### Şablon A — Kişisel Portfolyo

Adınız, kısa biyografi, 3-5 proje kartı, iletişim bilgisi. Tasarımcının "vitrini".

**Starter prompt:**
```
Benim için kişisel bir portfolyo web sayfası oluştur.
İsim: [ADINIZ]
Unvan: [VCD öğrencisi / illüstratör / tasarımcı]
Renk paleti: [2-3 HEX KOD]
Projeler: [PROJE 1 ADI], [PROJE 2 ADI], [PROJE 3 ADI]
Stil: [minimalist / renkli / karanlık tema]
Gereksinimler: Tek HTML dosyası, harici CSS framework kullanma,
masaüstü görünümü yeterli.
```

### Şablon B — Renk Paleti Galerisi

Sevdiğiniz 4-6 paletin tek sayfada gösterimi. Her palette renk bloğu ve altında hex kodu. Tasarım esinleri için tutulan bir "kart deste"si gibi.

**Starter prompt:**
```
Renk paletlerini gösteren bir HTML galerisi oluştur.
Paletler:
- [PALET ADI 1]: [HEX1], [HEX2], [HEX3]
- [PALET ADI 2]: [HEX1], [HEX2], [HEX3]
Her palet için renk bloğu ve hex kodu göster.
Arka plan beyaz, font Inter veya system-font.
Tek HTML+CSS dosyası.
```

### Şablon C — Proje Brifleri Sayfası

Şu an üzerinde çalıştığınız tasarım projelerinin briflerini bir arada gösteren bir sayfa. Müşteri adı, teslim tarihi, renkler, açıklama. Kişisel proje yönetim panosu gibi.

**Starter prompt:**
```
Tasarım proje briflerini listeleyen bir web sayfası oluştur.
Sayfada her brif şunları içersin: proje adı, müşteri, teslim tarihi,
kullanılan renkler.
Projeler:
1. [PROJE ADI] — Müşteri: [MÜŞTERİ], Tarih: [TARİH], Renkler: [HEX]
2. [PROJE ADI] — Müşteri: [MÜŞTERİ], Tarih: [TARİH], Renkler: [HEX]
Kart düzeni kullan. Koyu arka plan, açık kart rengi.
Tek HTML dosyası.
```

> ↪ **Vibecoding Kuralı 6:** Şablonlar başlangıç noktasıdır, son söz değil. İlk çıktıyı aldıktan sonra **iterasyona** girişin.

---

## 7. Bu Hafta Beklenen Akış (Sınıfta)

| Adım | Süre | Ne yapacaksınız |
|---|---|---|
| 1 | 15 dk | Vibecoding nedir, kurallar, mini demo (hoca anlatır) |
| 2 | 20 dk | Prompt yazma atölyesi — iyi/kötü örnek karşılaştırma |
| 3 | 30 dk | Hocanın canlı demosu — bir sayfa baştan sona |
| — | 10 dk | Mola |
| 4 | 50 dk | Kendi sayfanızı yapın (şablonlardan birini seçin) |
| 5 | 25 dk | İterasyon turu — sayfanızı 2-3 kez değiştirtin |
| 6 | 15 dk | Paylaşım — birkaç kişi ekran göstersin |

---

## 8. Sık Yapılan Hatalar

### 1. Belirsiz prompt yazmak  ↪ Jenerik çıktı

> "Güzel bir sayfa yap" → Material varsayılanları gelir, sizinle ilgisi yok.

Her promptta **isim, renk, içerik, kısıt** belirtin. Bir tasarım brifi yazar gibi yazın.

### 2. Çoklu istek tek prompta sıkıştırmak  ↪ Yarısı yapılmaz

> "Portfolyo yap, içine renk paleti ekle, alta iletişim formu koy, header'ı sticky yap, dark/light mode toggle ekle, animasyonlar olsun"

Çok şey istediğinizde Gemini bir-iki tanesini atlar. **Tek tek ekleyin, iterasyon yapın.** Önce sayfa, sonra renk paleti, sonra form...

### 3. Eski sürümle yeni değişiklik karıştırmak  ↪ Geriye dönüş

Yeni iterasyonda eski kodu yapıştırmazsanız Gemini en baştan başlar veya yanlış sürümle çalışır. Her seferinde **mevcut kodu yapıştırın**.

### 4. Kodun ne yaptığını anlamadan kaydetmek  ↪ Bakım imkansızlaşır

Gemini size 200 satırlık bir kod verirse en azından bölümlerine bakın: `<head>` ne içeriyor, kaç `<div>` var, CSS bölümünde neler tanımlı. Anlamadan kaydedersen sonra "şu kısmı değiştir" diyemezsin.

### 5. Live Server kurmamak  ↪ Her seferinde tarayıcıyı manuel yenilemek

Live Server'ı kurun. Kaydedince otomatik yenilenir, çok hızlı iterasyon yaparsınız.

### 6. Dosyayı `.txt` olarak kaydetmek  ↪ Tarayıcı açmaz

VS Code'da "Save As" yaparken **uzantıyı `.html` yazmayı unutmayın**. Yoksa tarayıcı dosyayı kod olarak değil metin olarak gösterir.

### 7. CSS'i ayrı dosya istediğinizi söylemeyip karışıklığa düşmek

Sade başlamak için **CSS'i HTML içine `<style>` olarak gömün**. Gemini'ye "tek dosya" deyin. Sonra istediğiniz zaman "CSS'i ayır" diye iterasyon yapabilirsiniz.

---

## 9. Bu Haftanın Ödevi

`odevler/odev01_sayfani_gelistir.md` dosyasında detaylı talimat var. Kısaca:

- Bu hafta sınıfta yaptığınız sayfayı evde **2 iterasyon daha geliştirin**.
- Her iterasyonda Gemini'ye **ne sordunuz** ve **ne değişti**, kısaca not tutun (`notlar.txt`).
- Teslim: `sayfam.html` + `notlar.txt` (zip veya klasör halinde).

**Değerlendirme kriteri:** Kaç iterasyon yaptığınız, değişikliklerin görünür olup olmaması. Kod kalitesi değil, **süreç** ölçülecek.

---

## 10. Bir Sonraki Adım

Önümüzdeki haftalarda bu sayfayı daha akıllı hale getirmeyi konuşacağız:

- Renk paletini bir Python dosyasından okuyup HTML'e yerleştirmek
- JSON'dan proje verilerini HTML'e basmak
- Bir form, bir buton, bir küçük etkileşim eklemek

Bu hafta öğrendiklerinizden ikisi orada kritik:

1. **İyi prompt yazma** — Hangi konuda olursa olsun, Gemini ile iş gördüğünüzde işin yarısı budur.
2. **Kodu yapıştırıp ne yaptığını okumak** — Hafta 8'de başlamıştık, bu hafta daha çok pratik yaptık. Gelecek hafta daha da fazla.

> Bu hafta kod yazmadınız. Ama yazılmış kodu **yönettiniz**. İkisi farklı beceriler — ve ikincisi günümüzde en az ilki kadar değerli.
