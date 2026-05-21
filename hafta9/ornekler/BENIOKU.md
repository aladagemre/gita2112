# Hafta 9 — Örnekler

Bu klasörde Gemini'den gelmiş gibi hazırlanmış iki tam HTML/CSS örneği var.
Derste **Plan B** olarak (Gemini erişimi yoksa) gösterilebilir.
Aynı zamanda öğrenciye "Gemini bana ne verebilir?" sorusunun cevabıdır.

---

## Dosyalar

| Dosya | Ne içerir |
|---|---|
| `ornek_portfolyo.html` | Tek sayfalık siyah-beyaz minimalist kişisel portfolyo. İsim, hakkımda, 3 proje, footer. |
| `ornek_palet_galerisi.html` | 4 renk paletinin yan yana gösterildiği beyaz sayfa. Her palette 4 renk bloğu + hex kodu. |

---

## Nasıl Açılır

### Yöntem 1 — Çift Tıkla

Dosyaya çift tıklayın. Varsayılan tarayıcınız (Chrome, Safari, Firefox) açılır.

### Yöntem 2 — VS Code + Live Server (Önerilen)

1. VS Code'a "Live Server" eklentisini kurun (Ritwick Dey).
2. Dosyayı VS Code'da açın.
3. Sağ alt köşedeki **"Go Live"** butonuna tıklayın veya dosyaya sağ tıklayıp **"Open with Live Server"** seçin.
4. Tarayıcı otomatik açılır. Dosyayı düzenleyip kaydettikçe sayfa kendi yenilenir.

---

## Bu Dosyalardan Ne Öğrenebilirsiniz?

Sadece tarayıcıda açıp bakmayın — VS Code'da **kodu da okuyun**:

### `ornek_portfolyo.html` İçinde Aranacaklar

- `<style>` bloğu nerede başlıyor, nerede bitiyor?
- `:root { --bg: ... }` ne işe yarar? (CSS değişkenleri — yukarıda bir kere tanımlanıp aşağıda `var(--bg)` ile kullanılıyor)
- `.projeler { display: grid; ... }` — grid düzen ne demek?
- `aspect-ratio: 1 / 1;` (palet dosyasında) — kare bloklar için kullanılmış

### `ornek_palet_galerisi.html` İçinde Aranacaklar

- `style="background:#FF6B6B"` — inline style kullanımı. Neden burada öyle yapılmış? (Her renk farklı olduğu için class yazmaktansa kolay yol seçilmiş)
- `repeat(4, 1fr)` — grid'de 4 eşit kolon
- `monospace` font ne işe yarar? (Hex kodları için sabit genişlikli font)

---

## Bu Örnekleri Kendi Sayfanız İçin Kullanma

İki yol:

**Yol A — Sıfırdan Gemini'den isteyin.** Önerilir. `prompt_sablonlari.md` dosyasındaki şablonu doldurup gönderin. Gemini'nin çıktısı bu örneklere benzeyecek (ama bire bir aynı olmayacak — çeşitliliği için bu iyi).

**Yol B — Bu örneği kendinize uyarlayın.** Dosyayı kopyalayın, isminizi/renklerinizi değiştirin. Bu **vibecoding değil**, sadece kopyalama olur. Sınıf egzersizinde yöntem A tercih edilsin.

---

## Türkçe Karakter Uyarısı

Her iki dosyada `<meta charset="utf-8">` etiketi var. Bu sayede "ş, ğ, ü, ç, ı, ö" gibi karakterler doğru görünür. Gemini bazen bunu unutur — sizin yaptığınız sayfada Türkçe karakterler bozuksa bu etiketi kontrol edin.
