# Ödevler — Nasıl Yapılır?

Bu hafta 5 ödev var. Her ödev dosyasını bir kod editöründe aç, `...` ile işaretli yerleri doldur, sonra çalıştır.

**Ödev 1 farklıdır:** Kod yazmazsınız, terminalde komutlar çalıştırıp sonucu bir metin dosyasında belgelersiniz. Ayrıntı `odev01_terminal_uv.md` dosyasındadır.

---

## Programları Nasıl Çalıştırırsınız?

### Yöntem 1 — VS Code ile (Önerilen)

1. Ödev dosyasını VS Code'da açın (örnek: `odev02_brifi_yazma.py`)
2. Sağ üstteki **Run** düğmesine tıklayın
3. Çıktı altta **Terminal** panelinde görünür

### Yöntem 2 — Terminal ile

VS Code'da **Terminal → New Terminal** menüsünü açın, ardından şu komutu yazın:

```
cd hafta8/odevler
python3 odev02_brifi_yazma.py
```

Diğer ödevler için dosya adını değiştirin:

```
python3 odev03_renk_paleti.py
python3 odev04_proje_kunyesi.py
python3 odev05_csv_to_json.py
```

> **Windows için:** `python3` yerine `python` yazın.

---

## Çalışma Akışı

1. Dosyayı aç
2. `...` yerlerini doldur
3. Çalıştır — çıktıyı dosya sonundaki **Beklenen Çıktı** yorumuyla karşılaştır
4. Çıktılar eşleşene kadar düzenle

---

## Ödev 1 — Terminal & uv Kurulumu (`odev01_terminal_uv.md`)

Bu ödev kod değil, **kurulum** ödevidir. `uv`'yi sisteminize kuracak, küçük bir proje oluşturacak ve adımlarınızı bir metin dosyasında belgeleyeceksiniz.

- **Görev 1:** `uv` kurulumu (Mac / Windows)
- **Görev 2:** `uv init odev1_proje` ile yeni proje
- **Görev 3:** `uv add requests` paket ekleme
- **Görev 4:** `pyproject.toml` içeriğini kopyalama
- **Görev 5:** Tüm adımları `kurulum_notlari.txt` adlı bir dosyada belgeleme

Detaylı talimatlar `odev01_terminal_uv.md` dosyasındadır.

---

## Ödev 2 — Tasarım Brifi Yazma (`odev02_brifi_yazma.py`)

Kullanıcıdan proje bilgilerini alıp `.txt` dosyasına yazan bir program. Konu: input + dosya yazma + f-string. En basit "input al → dosyaya yaz → geri oku" döngüsü.

- **Görev 1:** Kullanıcıdan proje adı, müşteri adı, tarih ve renkler al
- **Görev 2:** Bir brif metni oluştur (f-string)
- **Görev 3:** `proje_brifi.txt` dosyasına yaz
- **Görev 4:** Yazdığını geri okuyup ekrana basarak doğrula

---

## Ödev 3 — Renk Paleti Okuma (`odev03_renk_paleti.py`)

Bir müşteri size 14 renk içeren bir liste yolladı. `veri/musteri_renkleri.txt` dosyasını okuyup analiz edeceksiniz. Konu: dosya okuma + filtreleme + sözlükle sayma.

- **Görev 1:** Dosyayı `with open()` ile aç ve satır satır oku
- **Görev 2:** Toplam renk sayısını yazdır
- **Görev 3:** "M" harfiyle başlayan renkleri listele
- **Görev 4:** Her rengin kaç defa geçtiğini say (sözlük ile)

---

## Ödev 4 — Proje Künyesi (JSON) (`odev04_proje_kunyesi.py`)

Bir proje sözlüğünü JSON dosyasına kaydetmek ve geri okumak.

- **Görev 1:** Proje sözlüğü oluştur (ad, tarih, renkler, fontlar, durum)
- **Görev 2:** `proje_kunyesi.json` dosyasına yaz
- **Görev 3:** Aynı dosyayı geri oku
- **Görev 4:** Sözlük üzerinde değişiklik yap (yeni renk ekle, durum güncelle)
- **Görev 5:** Güncel sözlüğü tekrar dosyaya yaz

---

## Ödev 5 — CSV'den JSON'a Köprü (`odev05_csv_to_json.py`) — Zor

Hafta 8'in tüm konularını + Hafta 6 fonksiyonlarını birleştirir. Program **dört küçük fonksiyon** etrafında kuruludur — her birini tek başına yazıp test edebilirsiniz.

- **Fonksiyon 1:** `csv_oku()` — CSV dosyasını sözlük listesi olarak döndür
- **Fonksiyon 2:** `filtrele()` — bütçesi belirli bir eşiğin üstünde olanları ayır
- **Fonksiyon 3:** `toplam_butce()` — toplam bütçeyi hesapla
- **Fonksiyon 4:** `json_yaz()` — özet sözlüğü oluştur ve JSON'a yaz

Fonksiyon imzaları (`def ...` ve `return` satırları) hazır verilmiştir. Sizin işiniz **gövdelerini doldurmak**. İpucu: bir fonksiyonu doldurun, çalıştırın, sonra diğerine geçin.

---

## Genel İpuçları

| Durum | Ne yapmalısın? |
|---|---|
| `FileNotFoundError` | Dosya yolunu kontrol et. Terminalde `pwd` ile şu an neredesin bak. |
| Türkçe karakterler bozuk | `encoding="utf-8"` parametresini ekledin mi? |
| `KeyError: '...'` | Sözlükte o anahtar var mı? Yazım kontrol et. |
| `IndexError: list index out of range` | Liste/satır kaç eleman var? `0`'dan başlar. |
| Sonuç boş çıktı | `print` yerine `return` mi kullandın? Ya da tersi? |
| Çıktı `Ellipsis` çıktı | `...` yerine doğru kodu yazmayı unuttun |
| `ModuleNotFoundError` | `import` satırını yazdın mı? Modül adını doğru mu yazdın? |

---

## Çalıştığınız Klasör Önemli!

Ödev dosyaları `veri/musteri_renkleri.txt` ve `veri/projeler.csv` gibi göreli yollar kullanır. Bu yüzden **terminalin `odevler/` klasöründe açık olması** gerekir.

Eğer `FileNotFoundError` alırsanız:

```
cd hafta8/odevler
ls veri/         # dosyaları görüyor musunuz?
python3 odev03_renk_paleti.py
```

VS Code'da Run düğmesi kullanırsanız çoğu zaman doğru klasörden çalışır.
