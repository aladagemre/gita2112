# Renk Paleti Üreteci Gereksinim Listesi (Requirements)

Bu belge, tasarımcılar için geliştirilecek olan renk paleti üreteci web aracının iş gereksinimlerini tanımlar. Gereksinimler öncelik sırasına göre **Çekirdek** (MVP - Minimum Viable Product) ve **Ekstra** (Gelecek Özellikler) olarak iki gruba ayrılmıştır.

---

## 1. ÇEKİRDEK GEREKSİNİMLER (Olmazsa Olmazlar)

Araç, bu özellikler olmadan temel işlevini yerine getiremez.

### Palet Üretimi ve Manipülasyonu
* **G01 (Yapıldı):** Kullanıcı, klavyedeki boşluk (Space) tuşuna basarak veya ekrandaki "Palet Üret" butonuna tıklayarak rastgele uyumlu 5 renkten oluşan bir palet üretebilmeli.
* **G02 (Yapıldı):** Kullanıcı, paletteki beğendiği belirli renkleri kilitleyebilmeli; böylece yeni bir palet üretildiğinde kilitli renkler değişmeden sabit kalmalı.
* **G03 (Yapıldı):** Kullanıcı, renklerin HEX kodlarını renk kartlarının üzerinde net bir şekilde görebilmeli.
* **G04 (Yapıldı):** Kullanıcı, kilitlenmemiş herhangi bir rengin üzerine tıklayarak açılan renk seçici (color picker) ile rengi manuel olarak değiştirebilmeli.

### Kopyalama ve Temel Dışa Aktarma
* **G05 (Yapıldı):** Kullanıcı, herhangi bir renk kartının üzerindeki HEX koduna tıkladığında o kod otomatik olarak panoya (clipboard) kopyalanabilmeli.
* **G06 (Yapıldı):** Kullanıcı, tüm paleti tek tıkla CSS Değişkenleri (CSS Variables) formatında kopyalayabilmeli.

### Arayüz ve Kullanılabilirlik
* **G07 (Yapıldı):** Kullanıcı, aracı hem geniş ekranlı masaüstü cihazlardan hem de mobil cihazlardan (responsive tasarım ile) sorunsuzca kullanabilmeli.

---

## 2. EKSTRA GEREKSİNİMLER (Sonradan Eklenebilir Güzellikler)

Bu özellikler kullanıcı deneyimini zenginleştirmek ve profesyonel ihtiyaçlara cevap vermek için sonradan eklenecektir.

### Görselden Renk Analizi (Color Extractor)
* **G08 (Yapıldı):** Kullanıcı, sürükle-bırak yöntemiyle veya dosya seçerek sisteme bir görsel yükleyebilmeli.
* **G09 (Yapıldı):** Kullanıcı, yüklediği görseldeki en baskın 5 rengin otomatik olarak çıkarılarak palete dönüştürüldüğünü görebilmeli.

### Erişilebilirlik ve Kontrast Analizi (A11y)
* **G10 (Yapıldı):** Kullanıcı, seçtiği iki rengin (örneğin metin ve arka plan) kontrast oranını WCAG 2.1 (AA ve AAA standartlarına göre) uygunluk durumunu anlık olarak test edebilmeli.
* **G11 (Yapıldı):** Kullanıcı, oluşturduğu paletin farklı renk körlüğü türlerine (Protanopi, Döteranopi, Tritanopi vb.) göre nasıl göründüğünü simüle edebilmeli.

### Gelişmiş Dışa Aktarma ve Kaydetme
* **G12 (Yapıldı):** Kullanıcı, paleti Tailwind CSS config dosyası (JSON), SCSS, SVG veya PDF formatlarında indirebilmeli veya kopyalayabilmeli.
* **G13 (Yapıldı):** Kullanıcı, ürettiği paletleri tarayıcı hafızasına (Local Storage) kaydedip daha sonra tekrar erişebilmeli ve beğendiği paletlerden bir kütüphane oluşturabilmeli.

### Gelişmiş Üretim Kuralları
* **G14 (Yapıldı):** Kullanıcı, rastgele üretim yerine belirli renk teorisi şemalarına göre (Monokromatik, Analog, Tamamlayıcı/Complementary, Üçlü/Triadic) palet üretebilmesi.
* **G15 (Yapıldı):** Kullanıcı, o oturumda ürettiği paletler arasında geri (Undo) ve ileri (Redo) gidebilmeli.
* **G16 (Yapıldı):** Kullanıcı, palet boyutunu dinamik olarak 2 ile 10 kart arasında ayarlayabilmeli (renk ekleme ve silme butonları ile).
* **G17 (Yapıldı):** Kullanıcı, renk kartlarını sürükleyip bırakarak palet içindeki sıralarını değiştirebilmeli.
* **G18 (Yapıldı):** Kullanıcı, her rengin Ton (H), Doygunluk (S) ve Işık (L) değerlerini slider (sürgü) kontrolleriyle doğrudan ve hassas bir şekilde ayarlayabilmeli.
* **G19 (Yapıldı):** Kullanıcı, kaydettiği paletlere etiket (tag) ekleyebilmeli ve kütüphanede arama/filtreleme yaparak paletleri bulabilmeli.
* **G20 (Yapıldı):** Kullanıcı, uygulamayı çevrimdışı (offline) kullanabilmeli ve PWA destekli tarayıcılarda cihazına yükleyebilmeli.
