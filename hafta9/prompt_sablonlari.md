# Hafta 9 — Prompt Şablonları

> Bu sayfa kopyala-yapıştır içindir. Köşeli parantezleri (`[...]`) silip kendi içeriğinizi yazın.

---

## Bölüm 1 — Başlangıç (Yeni Sayfa Oluşturma)

### Şablon 1 — Kişisel Portfolyo

```
Benim için kişisel bir portfolyo web sayfası oluştur.
İsim: [ADINIZ]
Unvan: [VCD öğrencisi / illüstratör / motion designer]
Renk paleti: [2-3 HEX KOD — örn. arka plan #0F0F0F, yazı #F5F5F5, vurgu #FF6B6B]
Projeler:
1. [PROJE 1 ADI]
2. [PROJE 2 ADI]
3. [PROJE 3 ADI]
Stil: [minimalist / renkli / karanlık tema / brutalist]
Gereksinimler:
- Tek HTML dosyası, CSS gömülü <style> bloğunda.
- Harici CSS framework (Bootstrap, Tailwind) kullanma.
- Masaüstü görünümü yeterli, mobil olmasa da olur.
- Türkçe karakterleri doğru göstersin (meta charset utf-8).
- Sadece HTML kodunu ver, açıklama yapma.
```

### Şablon 2 — Renk Paleti Galerisi

```
Renk paletlerini gösteren bir HTML galeri sayfası oluştur.
Paletler:
- [PALET ADI 1]: [HEX1], [HEX2], [HEX3], [HEX4]
- [PALET ADI 2]: [HEX1], [HEX2], [HEX3], [HEX4]
- [PALET ADI 3]: [HEX1], [HEX2], [HEX3], [HEX4]
- [PALET ADI 4]: [HEX1], [HEX2], [HEX3], [HEX4]

Her palet için:
- Palet adı üstte, başlık olarak
- Her renk için kare blok, altında hex kodu yazılı
- Renkler yan yana hizalı

Genel stil:
- Arka plan beyaz
- Font sistem fontu (system-ui veya Inter)
- Grid layout, paletler alt alta veya 2'li
- Tek HTML+CSS dosyası
- Sadece HTML kodunu ver, açıklama yapma.
```

### Şablon 3 — Proje Brifleri Sayfası

```
Tasarım proje briflerini listeleyen bir web sayfası oluştur.
Her brif kart şeklinde olsun ve şunları içersin:
- Proje adı
- Müşteri
- Teslim tarihi
- Kullanılan renkler (hex kodlar, küçük renk blokları olarak)
- Kısa açıklama (1-2 cümle)

Projeler:
1. [PROJE ADI] — Müşteri: [MÜŞTERİ], Tarih: [TARİH], Renkler: [HEX1, HEX2, HEX3], Açıklama: [KISA METİN]
2. [PROJE ADI] — Müşteri: [MÜŞTERİ], Tarih: [TARİH], Renkler: [HEX1, HEX2, HEX3], Açıklama: [KISA METİN]
3. [PROJE ADI] — Müşteri: [MÜŞTERİ], Tarih: [TARİH], Renkler: [HEX1, HEX2, HEX3], Açıklama: [KISA METİN]

Stil:
- Koyu arka plan (#1a1a2e gibi), açık kart rengi (#16213e veya benzeri)
- Vurgu rengi olarak [HEX] kullan (başlıklar, çizgiler)
- Kart düzeni grid, masaüstünde 3'lü sıra
- Tek HTML dosyası, CSS gömülü
- Sadece HTML kodunu ver, açıklama yapma.
```

---

## Bölüm 2 — İterasyon (Mevcut Sayfayı Değiştirme)

> **VS Code + Gemini Code Assist kullanıyorsanız:** `index.html` açıkken chat'e sadece değişikliği yazın — Gemini dosyayı zaten görüyor, kod yapıştırmanıza gerek yok.
>
> **gemini.google.com'da aynı konuşmadaysanız:** Yine sadece değişikliği yazın — Gemini son verdiği kodu hatırlıyor.
>
> **Konuşmayı kapattıysanız veya yeni sekme açtıysanız:** `index.html`'i VS Code'da açın, `Ctrl+A` → `Ctrl+C` ile tüm içeriği kopyalayın, Gemini'ye yapıştırıp ardından değişikliği söyleyin.

### Renk Değiştirme

```
Sayfanın renklerini şu şekilde değiştir:
- Arka plan: [YENI HEX]
- Yazı rengi: [YENI HEX]
- Vurgu rengi: [YENI HEX]
```

### Bölüm Ekleme

```
Sayfaya "[BÖLÜM ADI]" bölümü ekle.
Bölüm [projelerin üstüne / altına / en sona] gelsin.
İçinde [3-4 cümlelik kısa metin / liste / boş yer tutucu] olsun.
Mevcut stilini koru, yeni bölümü ona uyarla.
```

### Hover Efekti Ekleme

```
Proje kartlarına hover efekti ekle.
Fareyle üstüne gelinince:
- Kart hafifçe büyüsün (scale 1.03)
- Altında yumuşak bir gölge belirsin
- Geçiş animasyonu 0.2 saniye
```

### Font Boyutu / Stil Değişikliği

```
Font ayarlarını şöyle değiştir:
- Ana başlık: [YENI BOYUT, örn. 64px]
- Gövde metni: [YENI BOYUT]
- Font ailesi: [YENI FONT — örn. Georgia, system-ui]
```

### Düzen Değiştirme (grid ↔ liste)

```
Proje kartlarının düzenini [grid'den listeye / listeden grid'e] çevir.
```

### Türkçe Karakter Düzeltme

```
Tarayıcıda açtığımda Türkçe karakterler (ş, ğ, ü, ç, ı) bozuk görünüyor.
Düzelt.
```

---

## Bölüm 3 — Sorun Bildirme

> Bir şey çalışmıyorsa **ne gördüğünüzü** anlatın, "çalışmıyor" demeyin.
> VS Code + Gemini Code Assist kullanıyorsanız `index.html` açıkken şu mesajları gönderin — kodu tekrar yapıştırmanıza gerek yok.

### Sayfa Boş Çıkıyor

```
Tarayıcıda açtığımda sayfa tamamen boş, beyaz görünüyor.
HTML doğru mu, eksik bir şey var mı?
```

### Stiller Uygulanmıyor

```
İçerik görünüyor ama hiçbir CSS uygulanmamış gibi — her şey beyaz,
fontlar varsayılan, hiçbir renk yok. Sebebi ne, düzelt.
```

### Belirli Bir Bölüm Görünmüyor

```
Tarayıcıda açtığımda [BÖLÜM ADI] görünmüyor, diğer bölümler çalışıyor.
Sorun ne, düzelt.
```

---

## Bölüm 4 — Daraltma ve Sadeleştirme

### Sade Hale Getirme

```
Bu HTML kodu fazla karmaşık. Aynı görüntüyü daha kısa kodla yap.
Gereksiz CSS sınıflarını sil, gereksiz div'leri birleştir.
Görüntü aynı kalsın.
```

### CSS'i Ayırma

```
HTML'in içindeki CSS'i ayrı bir dosyaya çıkar.
Bana iki dosya ver:
1. index.html (sadece HTML, link ile CSS'e bağlanır)
2. style.css (tüm CSS kuralları)
```

---

## Bölüm 5 — Kontrol Soruları (Kendinize)

Bir prompt göndermeden önce kontrol edin:

- [ ] İsim, renk, içerik **somut** mu? "Güzel bir şey" değil mi?
- [ ] Hex kodları belirtildi mi?
- [ ] Format söylendi mi? ("Tek HTML, CSS gömülü" gibi)
- [ ] İterasyon yapıyorsam mevcut kodu yapıştırdım mı?
- [ ] "Sadece kodu ver, açıklama yapma" eklendi mi?

Beşi de evetse gönderin.
