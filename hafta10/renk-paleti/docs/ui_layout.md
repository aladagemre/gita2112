# UI Tasarım Yerleşim Planı (UI Layout Design)

Bu doküman, tek ekranlık (Single-Page) Renk Paleti Üreteci web uygulamasının arayüz yerleşimini, görsel hiyerarşisini ve kullanıcı etkileşimlerini (UX) tanımlar.

---

## 1. Genel Tasarım Dili ve Estetik (Design System)

* **Düzen:** Ekranın dikey kaydırma çubuğu (scrollbar) olmadan, tarayıcı penceresinin yüksekliğini tam kapladığı (%100 viewport height) tek ekranlı modern bir yerleşim.
* **Renk Paleti & Arka Plan:** Nötr koyu gri/siyah tonlarında (`#0A0A0C` veya `#0F0F12`) minimalist bir arayüz. Bu sayede üretilen renk blokları ekranda patlayarak ön plana çıkar.
* **Yazı Tipi (Typography):** Modern, geometrik ve okunaklı bir sans-serif yazı tipi olan **Inter** veya **Outfit** (Google Fonts).
* **Görsel Efektler:** Kontrollerde cam efekti (Glassmorphism - `backdrop-filter: blur`), renk kartı geçişlerinde yumuşak animasyonlar (`transition: all 0.5s ease`).

---

## 2. Ekran Yerleşim Planı (Wireframe)

Aşağıdaki şemada uygulamanın ekran yerleşimi gösterilmiştir:

```
+-------------------------------------------------------------------------+
| [Logo]          [ Rastgele Üret (Space) ] [Görsel Yükle]        [Ayarlar] | -> ÜST BÖLÜM (Header)
+-------------------------------------------------------------------------+
|        |        |        |        |        |                            |
|        |        |        |        |        |                            |
| R1     | R2     | R3     | R4     | R5     |                            |
| #HEX1  | #HEX2  | #HEX3  | #HEX4  | #HEX5  |                            | -> ORTA BÖLÜM (Kanvas)
| [Kilit]| [Kilit]| [Kilit]| [Kilit]| [Kilit]|                            | (5 Eşit Dikey Sütun)
|        |        |        |        |        |                            |
|        |        |        |        |        |                            |
+-------------------------------------------------------------------------+
| [Klavye Kısayol İpucu]                      [Erişilebilirlik: AA Uygun] | -> ALT BÖLÜM (Footer)
+-------------------------------------------------------------------------+
```

---

## 3. Ekran Bölümleri Detayları

### A. Üst Bölüm (Header - Kontrol Paneli)
Tüm kontrol araçlarının yer aldığı, ekranın en üstünde sabit duran, yarı saydam koyu bir şerit.
* **Sol Taraf:** Minimalist bir logo ve uygulama ismi (`Antigravity Colors` 🌟).
* **Orta Taraf (Ana Butonlar):**
  * **"Yeni Palet Üret" Butonu:** Dikkat çeken, neon geçişli (gradient) ve üzerinde klavye kısayolu simgesi (`Space` veya `⌨️ Space`) bulunan buton.
  * **"Görselden Renk Çıkar" Butonu:** Yanında fotoğraf ikonu olan, minimalist ikincil buton.
* **Sağ Taraf:**
  * **"CSS / Kodu Kopyala" Butonu:** Tek tıkla tüm paleti panoya kopyalayan buton.
  * **"Kontrast Panelini Aç" Butonu:** Erişilebilirlik test ekranını tetikleyen buton.

### B. Orta Bölüm (Main Canvas - Renk Blokları)
Ekranın en büyük kısmını (%80-85) kaplayan, palet renklerini sergileyen ana alan.
* **Masaüstü Düzeni:** Yan yana dizilmiş 5 eşit dikey sütun (CSS Grid veya Flexbox kullanılarak).
* **Mobil Düzeni:** Üst üste dizilmiş 5 yatay satır (mobil ekran dikey olduğu için renklerin daha iyi algılanmasını sağlar).
* **Renk Kartının İç Yapısı (Her Bir Blok İçin):**
  * Arka plan rengi, o bloğun atanan rengidir.
  * **Hover (Üzerine Gelindiğinde) Durumu:** Kartın üzerinde kontrol ikonları yumuşakça belirir:
    * **Kilit Butonu (Lock):** Rengi sabitlemek için. Kilitlendiğinde ikon sürekli görünür olur ve kilit simgesi "kapalı kilide" dönüşür.
    * **Renk Seçici İkonu:** Kullanıcının rengi manuel ayarlayabilmesi için entegre HTML5 Color Picker'ı tetikler.
    * **Kontrast Skor Etiketi:** Kartın üzerindeki metnin arka plan rengiyle uyum skorunu (Ör: `AA` veya `AAA`) gösteren dinamik kontrast uyarı rozeti.
  * **Kartın Alt Kısmı:**
    * **HEX Kodu Metni (Ör: `#E2F1AF`):** Büyük, okunaklı, kalın yazı tipi. Rengin koyuluğuna/açıklığına göre yazı rengi otomatik olarak siyah veya beyaza döner.
    * Kodun üzerine tıklandığında anlık olarak `"Kopyalandı!"` toast uyarısı belirir.

### C. Alt Bölüm (Footer - Bilgi Çubuğu)
Ekranın en altında yer alan, dikkat dağıtmayan çok ince şerit.
* **Sol Kısım:** Kullanıcıyı yönlendiren ipucu metni: *"Yeni renkler için Boşluk (Space) tuşuna basın, sabitlemek için kilide tıklayın."*
* **Sağ Kısım:** Proje durumu ve küçük bir geliştirici imzası.

---

## 4. Etkileşim ve Animasyon Senaryoları (Micro-UX)
1. **Palet Değişimi:** Yeni palet üretildiğinde, kilitli olmayan sütunların renkleri sert bir şekilde değil, `0.2` saniyelik çok hafif bir renk geçişi (transition) efektiyle değişir.
2. **Kopyalama Bildirimi:** HEX koduna tıklandığında, kodun hemen üzerinde baloncuk şeklinde beliren ve 1 saniye sonra sönerek kaybolan bir "Kopyalandı!" efekti uygulanır.
3. **Responsive Değişim:** Ekran genişliği 768px'in altına indiğinde sütunlar dikeyden yatay dizilime yumuşak bir kırılmayla geçer.
