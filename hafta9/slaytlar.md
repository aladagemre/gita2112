# GİTA 2112 — Hafta 9

## Vibecoding: Antigravity ile Web Sayfası

-----

## Bu Hafta Farklı

- Bugün Python **yazmıyoruz**
- Gemini bizim için yazacak
- Biz çalıştıracak, yönetecek, değiştirteceğiz
- Çıktı: tarayıcıda açılan kendi sayfanız

> "Kod yazmak değil — kod yönetmek"

-----

## Vibecoding Nedir?

- Yapay zekaya ne istediğini **tarif et**
- Model kodu üretir
- Sen çalıştırır, değerlendirirsin
- Beğenmezsen → tekrar söyle → tekrar üretir

### Bu Hafta Araç

- **Antigravity** — Google'ın yapay zekâ destekli kod editörü (IDE)
- İçinde **ajan** (kodu yazar) ve **önizleme** (sayfayı anında gösterir) hazır gelir

-----

## Programcı Değil, Yönetmen

### 7 Hafta Boyunca
Programcı gibi düşündünüz — satır satır kod yazdınız

### Bugünden İtibaren
Yönetmen gibi düşünüyorsunuz

- Yönetmen kamerayı kullanmaz
- Ne istediğini bilir, **doğru kelimelerle anlatır**
- Çekim olur, beğenmezse "tekrar" der

-----

## Art Director / Asistan

Bir tasarım ajansında:

- **Art director** → ne istediğini söyler
- **Asistan/uygulamacı** → üretir

> "Posterin alt kısmına 3 sütunlu grid. Solda fotoğraf, ortada başlık. Arka plan #0F0F0F, yazılar krem."

Asistan açar, yapar. Art director "başlığı büyüt" der. Asistan yapar.

**Siz art director'sınız. Gemini asistanınız.**

-----

## İyi Prompt: 3 Parça

```
[Ne istiyorum] + [Kısıtlar] + [Format]
```

### Ne istiyorum
"Portfolyo sayfası", "renk paleti galerisi" — belirsiz değil, belirli

### Kısıtlar
İsimler, hex kodlar, kullanılacak/kullanılmayacak şeyler

### Format
"Tek HTML dosyası, CSS gömülü" — nasıl gelmeli?

-----

## Kötü Prompt vs İyi Prompt

| Kötü | İyi |
|------|-----|
| "güzel bir sayfa yap" | "kişisel portfolyo, siyah arka plan, vurgu #FF6B6B, 3 proje kartı, tek HTML" |
| "renkli bir şey yap" | "4 renk paleti gösteren galeri, beyaz arka plan, her palette renk blokları + hex kod altında" |
| "biraz değiştir" | "vurgu rengini #FFE66D yerine #FF6B6B yap" |

> Tarif edilmemiş şey **jenerik** döner

-----

## Kurulum — Antigravity

**Antigravity'yi indir ve kur**

1. `antigravity.google` adresine git
2. İşletim sistemine uygun sürümü indir → kur
3. Aç → **Sign in with Google** ile giriş yap
4. Yeni bir klasör (workspace) aç
5. Yan tarafta **ajan paneli** görünüyorsa hazır

### Ne İşe Yarar?
Ajana ne istediğinizi yazarsınız.
Ajan dosyayı kendisi oluşturur ve kodu yazar.

-----

## Önizleme — Hazır Gelir

Antigravity'de ayrı bir eklenti kurmaya gerek yok.

- `index.html` oluşunca **içinde tarayıcı/önizleme** açabilirsiniz
- Değişiklik yaptıkça sayfayı **anında** görürsünüz

### Ne İşe Yarar?
Kod ve sonuç yan yana — yazdığınızı hemen görür,
beğenmezseniz tekrar söylersiniz.

-----

## İlk Sayfayı Yapma (Antigravity Akışı)

1. Antigravity'de bir **workspace (klasör)** aç
2. **Ajan paneline** promptunu yaz → gönder
3. Ajan `index.html` dosyasını **kendisi oluşturur** ve kodu yazar
4. **Önizlemeyi** aç → sayfanı gör
5. Beğenmezsen ajana ne değişsin söyle → tekrar yazar

> Dosya adı `.html` ile bitmeli — yoksa tarayıcıda açılmaz

-----

## İterasyon Döngüsü

```
Aldım → Çalıştırdım → Beğenmedim → Söyledim → Tekrar aldım
```

Bu döngüyü **3-5 kere** yapacaksınız.

### Antigravity ile

Ajan paneline sadece değişikliği yazın:

> "Vurgu rengini sarıdan kırmızıya çevir"
> "Projelerin üstüne Hakkımda bölümü ekle"

Ajan dosyayı düzenler → önizleme yenilenir

-----

## İterasyon Örneği (4 Tur)

**1. Tur — İlk sayfa:**
> "Kişisel portfolyo yap. İsim: Defne Aksu. Siyah arka plan, vurgu #FFE66D. 3 proje. Tek HTML."

**2. Tur — Renk:**
> "Vurgu rengini #FFE66D yerine #FF6B6B yap."

**3. Tur — İçerik:**
> "Projelerin üstüne kısa bir Hakkımda bölümü ekle."

**4. Tur — Efekt:**
> "Proje kartlarına hover efekti ekle — hafifçe büyüsün, gölge gelsin."

-----

## Hata Aldığında

HTML'de Python gibi kırmızı traceback çıkmaz — sayfa eksik görünür.

| Belirti | Ne yapacaksın |
|---------|---------------|
| Sayfa tamamen boş | "Sayfa boş açılıyor, neden?" de |
| Stiller yok, her şey beyaz | "CSS uygulanmıyor, düzelt" de |
| Türkçe karakterler bozuk | "Türkçe karakterler bozuk, düzelt" de |
| Bir bölüm görünmüyor | "[BÖLÜM] görünmüyor, diğerleri çalışıyor" de |

> Gemini ne gördüğünü bilmez — **tarif edin**, "çalışmıyor" demeyin

-----

## Üç Sayfa Şablonu — Birini Seçin

### A — Kişisel Portfolyo
İsim, kısa bio, 3-5 proje kartı, iletişim

### B — Renk Paleti Galerisi
4-6 palet, her renk için blok + hex kodu — tasarım esin panosu

### C — Proje Brifleri Sayfası
Müşteri, tarih, renkler, açıklama — kişisel proje panosu

> Şablon başlangıç noktası — iterasyonla istediğiniz yere götürün

-----

## Şablon A — Kişisel Portfolyo

```
Benim için kişisel bir portfolyo web sayfası oluştur.
İsim: [ADINIZ]
Unvan: [VCD öğrencisi / illüstratör / tasarımcı]
Renk paleti: [2-3 HEX KOD]
Projeler: [PROJE 1], [PROJE 2], [PROJE 3]
Stil: [minimalist / renkli / karanlık tema]
Gereksinimler: Tek HTML dosyası, CSS gömülü,
masaüstü yeterli, Türkçe karakterler doğru çıksın.
Sadece HTML kodunu ver.
```

-----

## Şablon B — Renk Paleti Galerisi

```
Renk paletlerini gösteren bir HTML galeri sayfası oluştur.
Paletler:
- [PALET ADI 1]: [HEX1], [HEX2], [HEX3], [HEX4]
- [PALET ADI 2]: [HEX1], [HEX2], [HEX3], [HEX4]
Her palet için renk bloğu + altında hex kodu.
Arka plan beyaz, sistem fontu.
Tek HTML+CSS dosyası. Sadece HTML kodunu ver.
```

-----

## Şablon C — Proje Brifleri

```
Tasarım proje briflerini listeleyen bir web sayfası oluştur.
Her brif kartında: proje adı, müşteri,
teslim tarihi, kullanılan renkler (hex bloklar), kısa açıklama.
Projeler:
1. [PROJE] — Müşteri: [X], Tarih: [T], Renkler: [HEX]
2. [PROJE] — ...
Koyu arka plan, açık kart rengi. Tek HTML. Sadece kodu ver.
```

-----

## Bugün Ne Yapacağız?

| Süre | Adım |
|------|------|
| 15 dk | Vibecoding nedir — kurallar + mini demo |
| 20 dk | Prompt yazma atölyesi |
| 30 dk | Hoca canlı demo — bir sayfa baştan sona |
| 10 dk | Mola |
| 50 dk | Kendi sayfanızı yapın |
| 25 dk | İterasyon — 2-3 değişiklik yapın |
| 15 dk | Paylaşım |

-----

## Sık Hatalar

**Belirsiz prompt → jenerik çıktı**
Her promptta isim, renk, içerik, kısıt belirtin

**Çok şey tek promptta → yarısı yapılmaz**
Önce sayfa, sonra renk, sonra bölüm — tek tek ekleyin

**Konuşmayı kapatmak → ajan sıfırlanır**
Aynı sohbeti/oturumu kapatmayın

**`.txt` olarak kaydetmek → tarayıcı açmaz**
Uzantı mutlaka `.html` olmalı

-----

## Ödev

Sınıfta yaptığınız sayfayı evde **2 iterasyon daha** geliştirin.

### Teslim
- `sayfam.html` — son haliniz
- `notlar.txt` — her turda ne istediniz, ne değişti

### Değerlendirme
Kod kalitesi değil → **kaç iterasyon**, değişiklikler görünür mü

> Detay: `odevler/odev01_sayfani_gelistir.md`

-----

## Bir Sonraki Adım

Bu hafta yönetmen oldunuz.

Önümüzdeki haftalar:
- Sayfayı daha akıllı hale getirmek
- Renk paletini bir dosyadan okutmak
- Küçük etkileşimler eklemek

> "Kod yazmadınız — ama yazılmış kodu **yönettiniz**. Bu da bir beceri."
