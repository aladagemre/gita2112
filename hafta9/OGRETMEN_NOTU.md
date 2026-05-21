# Hafta 9 — Öğretmen Notu (Vibecoding)

> Bu hafta öğrenci Python yazmıyor. Hoca da yazmıyor. **Gemini** yazıyor.
> Sizin işiniz: prompt yazmayı, kodu yönetmeyi ve iterasyonu **modellemek**.

---

## Zaman Bütçesi

| Adım | Min | İdeal | Lüks |
|---|---|---|---|
| 0. Açılış + vibecoding nedir | 10 | 15 | 20 |
| 1. Prompt yazma atölyesi (birlikte) | 15 | 20 | 25 |
| 2. Hoca canlı demosu — bir sayfa | 25 | 30 | 40 |
| Mola | 10 | 10 | 10 |
| 3. Öğrenciler kendi sayfası | 40 | 50 | 60 |
| 4. İterasyon turu | 20 | 25 | 30 |
| 5. Paylaşım + retrospektif | 10 | 15 | 20 |
| **Toplam** | **130 dk** | **165 dk** | **205 dk** |

İdeal sürüm 2 saat 45 dakika — bir oturumda biter. Eğer 2 saatlik bir sınıf yapıyorsanız "Min" satırını takip edin: paylaşımı atlayabilir, demoyu kısaltabilirsiniz.

---

## Ders Öncesi Hazırlık

### Ders Başlamadan 30 Dakika Önce

- [ ] gemini.google.com'da oturumun açık olduğundan emin olun. Hesaba giriş gerekiyorsa şimdi yapın, ders sırasında yapmayın.
- [ ] VS Code açık, projeksiyon ekranı yansıtılmış.
- [ ] **Live Server eklentisi yüklü mü?** Yüklü değilse hemen kurun: `Extensions` → "Live Server" (Ritwick Dey).
- [ ] Hazırlık klasörü oluşturun: `Desktop/hafta9_demo/`. İçi boş olsun, demo sırasında siz dolduracaksınız.
- [ ] `ornekler/ornek_portfolyo.html` ve `ornekler/ornek_palet_galerisi.html` dosyalarını **bir kere** tarayıcıda açıp çalıştığını doğrulayın. (Plan B için lazım.)

### Hazırda Bekleyecek İki Prompt

Demo sırasında **canlı yazacağınız** ana prompt budur — kafanızdan değil, hazır okuyun:

```
Benim için kişisel bir portfolyo web sayfası oluştur.
İsim: Elif Yılmaz
Unvan: VCD öğrencisi
Renk paleti: arka plan #0F0F0F (siyah), yazılar #F5F5F5 (krem),
vurgu rengi #FF6B6B (mercan).
Projeler:
1. Caz Festivali Afişi
2. Doğa Derneği Görsel Kimliği
3. Kitap Kapağı Serisi
Stil: minimalist, küçük başlık + büyük proje kartları.
Gereksinimler: Tek HTML dosyası, harici CSS framework kullanma,
masaüstü görünümü yeterli, kartlar ızgara (grid) düzeninde.
```

**İterasyon prompt'u** (demoda 2. tur):

```
Yukarıdaki HTML kodunu düzenle. Şu değişiklikleri yap:
1. Proje kartlarına hover efekti ekle — üzerine gelinince scale 1.03,
   altında hafif gölge.
2. Sayfanın üstüne 3-4 cümlelik "Hakkımda" bölümü ekle.
Mevcut kodu olduğu gibi koru, sadece bu değişiklikleri uygula.
```

> Bu iki promptu **kendi notepad'inizde** açık tutun, demoda Gemini'ye yapıştırın. Canlı yazarken yazım hatası yapıp sınıfı bekletmemek için.

---

## Anlatım Akışı (Detaylı)

### Açılış (15 dk)

**Söyleyiniz:**
> "Bu hafta Python yazmıyoruz. Bu hafta Python **yazdırıyoruz**. Daha doğrusu HTML yazdıracağız. Ama mantık aynı — biz tarif edeceğiz, model üretecek, biz değerlendireceğiz."

Tahtaya iki kelime yazın: **PROGRAMCI** vs **YÖNETMEN**. Aralarına çizgi çekin. Bugünden itibaren öğrencinin sağ tarafa geçtiğini söyleyin.

**Sormayın:** "Daha önce Gemini kullandınız mı?" — eğer hayır derlerse sınıf demoralize olur. Bunun yerine: "Bu araçları kullandığınız her durumda işe yarayacak bir disiplin öğrenmeye geldik."

### Prompt Atölyesi (20 dk)

Tahtaya **3 kötü prompt** yazın, sınıfa "Bunda ne eksik?" diye sorun:

1. "bir web sayfası yap"
2. "renkli ve havalı bir tasarım"
3. "fonksiyon ekle" (önceki kod yokken)

Sınıftan cevap alın. Sonra **3 iyi prompt** yazın, ders notundaki tablodaki örnekleri kullanın.

**Anahtar mesaj:** "[Ne istiyorum] + [Kısıtlar] + [Format]". Bu üç parçayı tahtaya yazın ve dersin sonuna kadar silmeyin.

### Hoca Canlı Demosu (30 dk)

**Adımlar — projeksiyonda:**

1. gemini.google.com'a girin.
2. Hazırladığınız uzun promptu yapıştırın. (Canlı yazmayın — sınıf sıkılır.)
3. Gönderin. "Şimdi bekliyoruz" deyin, çıktıyı sınıfla birlikte okuyun.
4. Kod kutusunun "Copy" butonuna basın.
5. VS Code → `Desktop/hafta9_demo/index.html` yarat. **Uzantı `.html`!**
6. Yapıştır + Kaydet.
7. Sağ tık → "Open with Live Server".
8. Tarayıcı açılır. **Sınıfa "Beğendiniz mi?" diye sorun.** Genelde "evet ama..." diye başlar.
9. İterasyon promptunu kopyalayıp Gemini'ye yapıştırın. (Hazırda bekleyen 2. prompt.)
10. Yeni kodu yapıştır → kaydet → Live Server kendi kendine yeniler. **Sınıf "vay" der.** Bu önemli, bu duyguyu yaşatın.

**Demoda mutlaka söyleyin:**
- "Gördüğünüz gibi her seferinde **tüm kodu yapıştırıyorum**. Gemini'ye 'önceki kod' diyerek çalışmıyorum."
- "Her iterasyondan sonra mutlaka **tarayıcıda kontrol** ediyorum. Görmeden geçmiyorum."
- "Beğenmediğim bir şey olursa cümleyle tarif ediyorum: 'kartlar çok küçük', 'renk soluk', 'spacing dar'."

### Öğrenci Egzersizi (50 dk)

Sınıfa şu talimatı verin:
1. Üç şablondan birini seçin (portfolyo, palet, brif).
2. `prompt_sablonlari.md` dosyasını açın, kendinize göre doldurun.
3. Gemini'ye gönderin, kodu alın, `Desktop/hafta9_calismam/index.html` olarak kaydedin.
4. Tarayıcıda açın.
5. **Hocaya gelmeden önce** en az bir iterasyon yapın.

**Hoca rolü bu evrede:** Sınıfta gezin. Tek tek bakın. Takılan öğrenciye **kodu siz yazmayın** — onun promptunu **birlikte düzeltin**. "Şuraya hex kodunu ekle, bak gör nasıl değişecek" deyin.

### İterasyon Turu (25 dk)

Sınıfa: "Şimdi en az 2 iterasyon yapın. Şu şeyleri deneyin:"
- Bir renk değiştirin
- Bir bölüm ekleyin (Hakkımda, İletişim)
- Hover efekti ekleyin
- Font boyutunu büyütün
- Kart düzenini grid'den listeye veya tersi

`prompt_sablonlari.md` dosyasının iterasyon bölümünden hazır cümleler verin.

### Paylaşım (15 dk)

3-4 gönüllüden ekranını paylaşmasını isteyin. Her biri:
- Sayfasını gösterir
- En son hangi iterasyonu yaptığını anlatır
- Hangi prompt işe yaradı, hangi işlemedi

**Hoca kapanış mesajı:**
> "Bu sayfayı dakikalar içinde yaptınız. Geçen yıl bu kadar sayfayı yapmak günler sürerdi. Mesele kod değildi — mesele **iyi tarif etmek**. Önümüzdeki hafta bu sayfayı Python ile de besleyeceğiz. Şimdilik evde 2 iterasyon daha geliştirin, hazır gelin."

---

## Plan B — Gemini Erişimi Yoksa

İnternet kopar, Gemini quota dolar, oturum kapanır — bu olabilir. Plan B:

### B1 — Hazır HTML'leri Göster

`ornekler/ornek_portfolyo.html` ve `ornekler/ornek_palet_galerisi.html` dosyalarını tarayıcıda açın. Sınıfa şöyle deyin:

> "Gemini bize ne verirdi? Bu verirdi. Şimdi koda bakalım — sözlerimle kod arasında köprü kuralım."

VS Code'da HTML dosyasını açın, satır satır gezin:
- `<head>` ne içeriyor?
- CSS bloğunda hangi renk değişkenleri var?
- `<body>` içinde kaç bölüm var?

### B2 — Promptu Yazıp Sonucu Hayal Edin

Sınıfla birlikte bir prompt yazın. Tahtaya/ekrana yapıştırın. Sonra "Gemini bu prompta şunu üretirdi" diyerek hazır HTML'i gösterin. **Prompt → çıktı eşlemesi** yapın.

### B3 — Evde Yapma Talimatı

Eğer Gemini hiç çalışmazsa, dersin ödevini "evde Gemini açıkken yapın" şeklinde uzatın. Ders notunu okuyup şablonlardan prompt yazıp evde denemelerini söyleyin.

---

## Risk Tablosu

| Risk | Olasılık | Çözüm |
|---|---|---|
| Gemini Türkçe istediğimizi anlamıyor / İngilizce dönüyor | Düşük | Promptu Türkçe yaz, "Türkçe cevap ver" diye ekle. Yine olmazsa İngilizce yaz, çıktıyı çevirme. |
| Gemini kod yerine açıklama veriyor | Orta | "Sadece HTML kodunu ver, açıklama yapma" diye ekleyin. |
| Sayfa açılıyor ama stiller boş | Orta | `<style>` bloğunun kopyalanmadığını kontrol et. Gemini'ye "stiller uygulanmıyor" deyip kodu yapıştır. |
| Live Server kurulu değil | Yüksek | Çift tıkla → tarayıcıda aç. Manuel yenile (Cmd+R / F5). |
| VS Code dosyayı `.txt` olarak kaydetti | Yüksek | "Save As" dialogunda dosya adı bölümüne `.html` uzantısı **yazılarak** verilmeli. Bilgisayara göre uzantı görünmüyor olabilir. |
| Öğrenci kodu nereye kaydedeceğini bilmiyor | Yüksek | Standart yol verin: `Desktop/hafta9_calismam/index.html`. Herkes aynı yere. |
| Gemini bağlamı kaybetti, eski sayfayı geri verdi | Orta | Yeni iterasyonda **mevcut tüm kodu** yapıştırma alışkanlığı, ders notunda kural #4. |
| Bir öğrencinin sayfası feci hızla bitti, sıkıldı | Düşük | İterasyon önerilerinden zorunu verin: "Sayfaya bir form ekle ve buton tıklanınca alert çıksın". |

---

## H10 Köprüsü

H10'da bu sayfaya **Python ile veri besleyeceğiz** — JSON dosyasından okuyup HTML'e basacağız (yine Gemini ile). Bugünün sayfası H10'a temel olacak.

Ders sonu mesajınız: "Sayfanızı kaybetmeyin. Önümüzdeki hafta üzerine ekleyeceğiz."

---

## Vibecoding Disiplin Notu (Önemli)

Bu ders, "Gemini her şeyi halleder" mesajı **vermemek** zorunda. Çünkü:

1. Gemini hatalı kod yazar — H8'de bunu okumayı öğrettiğimiz için bu hafta da öğrenci kodu okumalı.
2. Gemini kötü tasarım kararları verir — öğrenci bunları **eleştirmeli**, kabul etmemeli.
3. Gemini bağlamı kaybeder — öğrenci kodu yönetebilmeli.

Bu üç noktayı ders boyunca **örnekle** geçirin. "Bakın, burada Gemini şunu yapmış ama bence bu kart çok büyük. Söyleyelim küçültsün." gibi.

> Vibecoding **araç kullanmak** demektir, **teslim olmak** değil.
