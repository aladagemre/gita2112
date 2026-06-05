# Proje Geliştirme Yol Haritası (Roadmap)

Bu doküman, Renk Paleti Üreteci projesinin sıfırdan başlayarak adım adım nasıl kodlanacağını gösteren yol haritasıdır. Geliştirme süreci önce **Çekirdek (MVP)** özellikleri hayata geçirecek, ardından **Ekstra** özellikleri tek tek ekleyecek şekilde planlanmıştır.

---

## AŞAMA 1: ÇEKİRDEK (MVP) ÖZELLİKLER
*Bu aşama tamamlandığında, araç temel işlevini tamamen yerine getirebilir durumda olacaktır.*

1. **[Yapıldı] Adım 1: Temel Arayüz Şablonunun Kurulması (HTML & CSS)**
   * Ekranı dikey kaydırma olmadan tam kaplayan dikey 5 sütunlu ana düzenin (masaüstü için yanyana, mobil için üst üste) ve üst/alt barların HTML/CSS iskeletinin kodlanması.
2. **[Yapıldı] Adım 2: Rastgele Renk Üretim Fonksiyonunun Yazılması (JS)**
   * JavaScript ile rastgele 5 adet uyumlu HEX renk kodu üreten ve bunları ekran kartlarının arka planına ve HEX yazılarına dinamik olarak atayan motorun yazılması.
3. **[Yapıldı] Adım 3: Tetikleyicilerin Eklenmesi (Space Bar ve Buton)**
   * Klavyede `Space` (Boşluk) tuşuna basıldığında veya üst menüdeki "Yeni Palet Üret" butonuna tıklandığında renk üretim fonksiyonunun çalıştırılması.
4. **[Yapıldı] Adım 4: Renk Kilitleme (Lock) Fonksiyonunun Eklenmesi**
   * Her kartın üzerine kilit ikonu eklenmesi, kilit durumunun JavaScript state'inde tutulması ve yeni üretim tetiklendiğinde kilitli renklerin korunmasının sağlanması.
5. **[Yapıldı] Adım 5: Tek Tıkla HEX Kodunu Kopyalama ve Bildirim (Toast)**
   * Kart üzerindeki HEX koduna tıklandığında değerin panoya kopyalanması ve kopyalandığına dair kartın üzerinde 1 saniye görünüp kaybolan bir "Kopyalandı!" uyarısının gösterilmesi.
6. **[Yapıldı] Adım 6: Manuel Renk Seçici (Color Picker) Entegrasyonu**
   * Her kartın üzerinde bir renk seçici butonu konumlandırılması, bu buton tetiklendiğinde tarayıcı renk seçicisinin açılması ve seçilen yeni değerin karta atanması.
7. **[Yapıldı] Adım 7: Paleti CSS Değişkeni Olarak Kopyalama**
   * Üst menüdeki "CSS Kopyala" butonuna basıldığında paletteki tüm renklerin tek seferde `--color-1: #hex1;` formatında toplu olarak panoya kopyalanması.

---

## AŞAMA 2: EKSTRA ÖZELLİKLER (Adım Adım Geliştirme)
*Çekirdek özellikler bittikten sonra, kullanıcı deneyimini zenginleştirmek için sırasıyla eklenecektir.*

8. **[Yapıldı] Adım 8: Gerçek Zamanlı Kontrast ve Erişilebilirlik (WCAG) Analizi**
   * Her renk kartının kendi arka planı ile üzerindeki metin rengi arasındaki kontrast oranını hesaplayan algoritmanın yazılması ve WCAG standardına göre uygunluk etiketinin (`AA` / `AAA` / `Geçersiz`) dinamik gösterilmesi.
9. **[Yapıldı] Adım 9: Görselden Renk Çıkarma (Color Extractor)**
   * Üst menüye görsel sürükleme alanı eklenmesi, yüklenen görseli bir HTML Canvas yardımıyla analiz edip en baskın 5 rengi otomatik olarak palete aktaran sistemin kurulması.
10. **[Yapıldı] Adım 10: Palet Geçmişi (Undo / Redo) Mekanizması**
    * Kullanıcının ürettiği paletleri bir dizi (array) içinde hafızada tutarak sol/sağ ok tuşlarıyla veya butonlarla geçmiş paletler arasında ileri/geri gitmesini sağlayan mantığın kurulması.
11. **[Yapıldı] Adım 11: Palet Kaydetme ve Yerel Kütüphane (Local Storage)**
    * Kullanıcının beğendiği paletleri isimlendirerek tarayıcı yerel hafızasına kaydetmesini, kayıtlı paletleri listeleyebilmesini ve istediğinde kütüphaneden geri yükleyebilmesini sağlayan panelin yapılması.
12. **[Yapıldı] Adım 12: Renk Körlüğü Simülasyon Filtreleri**
    * Arayüze eklenecek bir seçim kutusuyla, renk bloklarına CSS/SVG filtreleri uygulayarak farklı renk körlüğü tiplerinde (Protanopi, Döteranopi, Tritanopi vb.) renklerin nasıl göründüğünü simüle etme.
13. **[Yapıldı] Adım 13: Çoklu Dışa Aktarma Formatları (Tailwind, JSON, SVG)**
    * Dışa aktarma paneline Tailwind config JSON, SCSS değişkenleri veya paletin renk bloklarını içeren bir SVG görsel dosyası indirme butonlarının eklenmesi.
14. **[Yapıldı] Adım 14: Gelişmiş Üretim Kuralları (Renk Teorisi Şemaları)**
    * Kullanıcının rastgele üretim yerine belirli renk teorisi şemalarına göre (Monokromatik, Analog, Tamamlayıcı, Üçlü) palet üretebilmesi ve kilitli renklere göre şemanın dinamik şekillenmesi.
15. **[Yapıldı] Adım 15: Dinamik Palet Boyutu Yönetimi**
    * Paletteki renk kartı sayısının dinamik olarak ayarlanması (2 ila 10 renk arası). Üst menüye "Renk Ekle" butonu ve her renk kartı üzerine silme (kaldırma) butonu eklenmesi.
16. **[Yapıldı] Adım 16: Kartların Sürükle-Bırak ile Yeniden Sıralanması (Drag & Drop)**
    * Kartların HTML5 Drag and Drop API kullanılarak sürüklenip bırakılmasıyla palet içindeki sırasının değiştirilmesi ve renk düzeninin anlık güncellenmesi.
17. **[Yapıldı] Adım 17: Doğrudan HSL İnce Ayar Sürgüleri (Range Sliders)**
    * Her kartın içinde açılıp kapanabilen, rengin Ton (H), Doygunluk (S) ve Işık (L) değerlerini gerçek zamanlı olarak hassas bir şekilde ayarlamaya yarayan sürgülü kontrol paneli entegrasyonu.
18. **[Yapıldı] Adım 18: Kütüphane Etiketleme (Tagging) ve Arama/Filtreleme**
    * Kaydedilen paletlere virgülle ayrılmış etiketler eklenebilmesi, kütüphane çekmecesindeki paletlerin isim veya etiketlerine göre dinamik olarak filtrelenip aranabilmesi.
19. **[Yapıldı] Adım 19: PWA Çevrimdışı ve Kurulum Desteği (Progressive Web App)**
    * Uygulamanın bir PWA olarak yüklenebilmesi için `manifest.json` ve çevrimdışı önbellekleme desteği sunan bir `sw.js` (Service Worker) dosyasının oluşturulması ve entegre edilmesi.

