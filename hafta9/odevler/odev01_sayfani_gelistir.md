# Ödev 1 — Sayfanı Geliştir

> Zorluk: Kolay-Orta · Süre: 1-2 saat · Teslim: `sayfam.html` + `notlar.txt`

---

## Amaç

Derste başladığınız HTML sayfasını evde **en az 2 iterasyon daha** geliştirerek tamamlamak.

Sınıfta sayfayı oluşturdunuz (ya da en azından bir başlangıç versiyonu aldınız). Bu ödevde:

1. Sayfayı evde iki kez daha **anlamlı şekilde** değiştirteceksiniz.
2. Her seferinde Gemini'ye ne sorduğunuzu ve ne değiştiğini not edeceksiniz.

---

## Adım Adım Talimat

### Adım 1 — Sınıftaki Dosyayı Hazırla

Sınıftaki bilgisayardan kendi bilgisayarınıza `index.html` dosyasını taşıyın. (E-posta, Drive, USB — fark etmez.)

Bilgisayarınızda yeni bir klasör yaratın: `hafta9_odev_[ADINIZ]/`. Dosyayı bu klasöre koyun ve adını **`sayfam.html`** olarak değiştirin.

> Eğer sınıfta sayfa bitmediyse veya kaybettiyseniz, `prompt_sablonlari.md` dosyasındaki şablonlardan birini kullanarak **baştan** bir sayfa oluşturun. Bu, "0. iterasyon" sayılır.

### Adım 2 — Bir notlar.txt Dosyası Oluştur

Aynı klasörde **`notlar.txt`** adında bir metin dosyası açın. İçine şu şablonu yapıştırın:

```
ADIM: [Adınız Soyadınız]
TARIH: [bugünün tarihi]

=== İTERASYON 1 ===
Tarih: ____
Geminì'ye ne sordum:
[promptu buraya yapıştır]

Ne değişti (gözle gördüğüm):
- ____
- ____

=== İTERASYON 2 ===
Tarih: ____
Geminì'ye ne sordum:
[promptu buraya yapıştır]

Ne değişti (gözle gördüğüm):
- ____
- ____

=== (İSTEĞE BAĞLI) İTERASYON 3 ===
Tarih: ____
...
```

### Adım 3 — İlk İterasyonu Yap

Geminì'yi (gemini.google.com) açın. Mevcut HTML kodunuzu yapıştırarak bir değişiklik isteyin. Örneğin:

- "Bu HTML'e bir 'İletişim' bölümü ekle. E-posta, Instagram, Behance linkleri olsun. Mevcut kod: [KOD]"
- "Bu HTML'in renklerini değiştir: arka plan #1a1a2e, yazılar #eee, vurgu #e94560. Mevcut kod: [KOD]"
- "Bu HTML'deki kartlara hover efekti ekle — üzerine gelince hafif büyüsün. Mevcut kod: [KOD]"

`prompt_sablonlari.md` dosyasında hazır şablonlar var.

Gemini yeni kodu verince:
1. Kopyalayın.
2. `sayfam.html` dosyasını VS Code'da açın, içeriğini silip yenisini yapıştırın, kaydedin.
3. Tarayıcıda yenileyin.
4. **Görsel değişikliği gördüğünüzden emin olun.**

Sonra `notlar.txt`'deki "İTERASYON 1" bölümünü doldurun.

### Adım 4 — İkinci İterasyonu Yap

Aynı şeyi tekrar yapın — ama **farklı bir şey** değiştirin. Eğer ilk iterasyonda renk değiştirdiyseniz, bu sefer bir bölüm ekleyin. Eğer bölüm eklediyseniz, bu sefer hover/animasyon ekleyin.

### Adım 5 — (İsteğe Bağlı) Üçüncü İterasyon

Daha ileri gitmek istiyorsanız bir iterasyon daha yapın. Ekstra puan olarak değerlendirilir.

### Adım 6 — Teslim

Klasörünüzde şu iki dosya olmalı:

```
hafta9_odev_[ADINIZ]/
  sayfam.html
  notlar.txt
```

Klasörü zip yapın (sağ tık → "Compress" / "Sıkıştır"). Hocanın söylediği yere (e-posta, Drive klasörü vb.) yükleyin.

---

## Değerlendirme Rubriği

| Kriter | Puan |
|---|---|
| `sayfam.html` tarayıcıda açılıyor ve görüntüleniyor | 20 |
| En az 2 iterasyon yapılmış (her biri gözle görünür değişiklik içeriyor) | 30 |
| `notlar.txt` istenilen formatta dolu, promptlar yapıştırılmış | 20 |
| Promptlar **spesifik** ve **kısıtlı** — "güzel yap" gibi muğlak değil | 20 |
| Sayfa kişiselleştirilmiş (gerçek isim, gerçek proje veya gerçek renk paleti) | 10 |
| **Toplam** | **100** |

### Ekstra Puanlar (Maksimum +15)

- 3. iterasyon yapılmış (+5)
- İterasyonlardan biri bir **sorunu çözmek için** yapılmış (örn. "şu görünmüyordu, düzelttirdim") ve notlarda anlatılmış (+5)
- Sayfada CSS dışında bir küçük etkileşim var (hover, transition, basit JS alert) (+5)

---

## Sık Sorulan Sorular

### "Gemini bana çok karmaşık kod verdi. Anlamıyorum."

Sorun değil. **Anlamak zorunda değilsiniz**. Yapmanız gereken:
1. Kodu kaydedin, tarayıcıda açın, gözle bakın.
2. Beğenmediğiniz bir şey varsa Gemini'ye "şunu sadeleştir" deyin.

Eğer kod kafanızı çok karıştırıyorsa, Gemini'ye şunu söyleyin:
> "Bu kodu daha sade yap. Gereksiz CSS'i sil. Aynı görünsün ama kısa olsun."

### "Promptum çalışmıyor, Gemini istediğimi yapmıyor."

İki sebep olabilir:
1. **Prompt çok muğlak.** "Daha güzel yap" yerine "başlığı 48px yap, rengini #FF6B6B yap" deyin.
2. **Çok şey istiyorsunuz.** Tek prompta 5 değişiklik sığdırmayın. Tek tek yapın.

### "Live Server yok, sayfa açılmıyor."

Live Server zorunlu değil. Dosyaya çift tıklayın, tarayıcı açılır. Her kaydetten sonra tarayıcıyı manuel yenileyin (Cmd+R / F5).

### "Türkçe karakterler bozuk."

`<head>` bölümüne şu satırın var olduğundan emin olun:
```html
<meta charset="utf-8">
```
Yoksa Gemini'ye "Türkçe karakterler bozuk, düzelt" deyip kodu yapıştırın.

### "Bir hata vermek istemiyorum. Sayfa çok temel, üzerinden geçemedim."

İterasyon önerileri (zor değil, gözle görülür):
- Tüm renkleri tek tek değiştir
- Bir "Hakkımda" paragrafı ekle
- Tüm fontları büyüt
- Kart düzenini grid'den listeye çevir
- Kartlara çerçeve veya gölge ekle

Bunlardan ikisi yeterli.

---

## Hatırlatma

Bu ödevin **kod yazma** ile ilgisi yok. Ödev, "iyi tarif edebiliyor musun ve ne aldığını yönetebiliyor musun" sorusunu ölçüyor. İki iterasyonu çekinmeden yapın — yanlış cevap diye bir şey yok.
