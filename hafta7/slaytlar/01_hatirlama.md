# Slaytlar — Blok 1: Hatırlama Haritası

> Ekran paylaşımı için. Her slayt ayrı sayfa gibi düşünülebilir — dersi verirken bir sayfa üstünde dur, sonra aşağı kaydır.
> Her slaytın sonunda "Soru" kısmı, öğrencilere sorulacak soruyu içerir.

---

## Slayt 0 — Açılış

### Python'u Ne Kadar Biliyoruz?

6 hafta, 6 konu grubu. Hepsi şu an elinizin altında.

```
Hafta 2 → Değişken, print, input, if
Hafta 3 → for döngüsü, liste
Hafta 4 → Sözlük, break/continue
Hafta 5 → f-string, matematik, tip dönüşümü
Hafta 6 → Fonksiyonlar
Hafta 7 → Bildiklerimizi birleştirmek (BUGÜN)
```

**Soru:** Aklınıza ilk gelen Python kavramı ne? Chat'e tek kelime yazın.

---

## Slayt 1 — Hafta 2: Temeller

### Değişken, print, input, if/elif/else

Python bize hafıza verdi (değişken), konuşma verdi (print), dinleme verdi (input), karar verdi (if).

```python
isim = input("Adınız? ")
yas = int(input("Yaşınız? "))

if yas >= 18:
    print(f"Merhaba {isim}, hoş geldin.")
else:
    print(f"{isim}, henüz 18 yaşından küçüksün.")
```

**Tasarım bağlantısı:** Bir formu tasarlıyorsunuz. Kullanıcı bilgilerini girer (input), sistem karar verir (if), sonuç gösterilir (print). Tüm etkileşimli arayüzlerin iskeleti bu.

**Tahmin Et (chat):** Yukarıdaki kod çalıştırıldı, kullanıcı adını "Defne" yazdı, yaşını "17" yazdı. Ekrana ne yazar? Tek satır halinde chat'e yazın.

> *Cevap: `Defne, henüz 18 yaşından küçüksün.`* — öğrenci 17 olduğu için else dalı çalışır.

---

## Slayt 2 — Hafta 3: Listeler ve Döngüler

### Liste, for, while, demet

Artık tek bir şey yerine **birden fazla** şey tutabiliyoruz. Ve hepsiyle tek tek ilgilenebiliyoruz.

```python
renkler = ["kırmızı", "mavi", "sarı", "yeşil"]

for renk in renkler:
    print(f"Palette var: {renk}")
```

**Tasarım bağlantısı:** Bir moodboard veya renk paleti bir listedir. Bir grid'deki tüm kareler bir listedir. Bir görseller serisine tek tek filtre uygulamak — for döngüsü.

**range() hatırlatması:**
```python
for i in range(5):   # 0, 1, 2, 3, 4
    print(f"Kare {i+1}")
```

**Tahmin Et (chat):** `for i in range(3): print(i * 2)` satırını çalıştırırsak ekrana ne yazar? (3 satır)

> *Cevap: `0`, `2`, `4` — range(3) 0'dan başlar, 3 dahil değil.*

---

## Slayt 3 — Hafta 4: Sözlük ve Döngü Kontrolü

### Sözlük, break, continue, sözlük listesi

Liste "aynı türden şeyleri" tutar (renkler, puanlar). Sözlük bir **şeyin özelliklerini** tutar (bir projenin adı, puanı, kategorisi).

```python
proje = {
    "ad": "Logo Tasarımı",
    "puan": 88,
    "kategori": "Kurumsal"
}

print(proje["ad"])     # Logo Tasarımı
print(proje["puan"])   # 88
```

**Sözlük listesi** — birden fazla projeyi tutarız:

```python
projeler = [
    {"ad": "Logo", "puan": 88},
    {"ad": "Afiş", "puan": 95},
]

for p in projeler:
    print(f"{p['ad']}: {p['puan']}")
```

**Tasarım bağlantısı:** Her proje bir InDesign sayfası gibi — aynı şablonun farklı içeriklerle doldurulmuş hali. Sözlük şablon, liste sayfaların bütünü.

**Tahmin Et (chat):** Yukarıdaki `projeler` için `print(projeler[1]["ad"])` çalıştırılsa ne yazar?

> *Cevap: `Afiş` — index 1 ikinci sözlüktür, onun "ad" anahtarı "Afiş".*

---

## Slayt 4 — Hafta 5: f-string, Matematik, Tip

### String formatlama, int/float, kısayol operatörler

Ekrana güzel metin yazmayı ve sayılarla işlem yapmayı öğrendik.

```python
isim = "Defne"
puan = 87.345

print(f"{isim}: {puan:.1f} puan")
# Defne: 87.3 puan
```

Matematik operatörleri:
```python
a = 17
print(a / 5)    # 3.4  (bölme)
print(a // 5)   # 3    (tam bölme)
print(a % 5)    # 2    (mod)
```

Tip dönüşümü — `input()` hep string döner:
```python
yas = int(input("Yaş: "))  # string -> int
```

**Tasarım bağlantısı:** Grid hesapları (`genislik // 3`), oran-orantı hesapları (`alan * 2.5`), veri görselleştirme için sayıyı formatlama (`:.1f`) — hepsi bu hafta.

**Soru:** `print("5" + 3)` ne verir? Tahmin edin.

---

## Slayt 5 — Hafta 6: Fonksiyonlar

### def, parametre, return, varsayılan değerler

Kodun sembolü. Bir kez tanımla, istediğin kadar kullan.

```python
def ortalama(sayilar):
    toplam = 0
    for s in sayilar:
        toplam += s
    return toplam / len(sayilar)

print(ortalama([85, 90, 78]))   # 84.3...
print(ortalama([75, 88, 92]))   # 85.0
```

**İki önemli şey:**

1. **Tanımlamak ≠ çalıştırmak.** `def` yazınca fonksiyon oluşur ama çalışmaz. `ortalama(...)` yazınca çalışır.
2. **print vs return.** print ekrana yazar. return değeri geri verir (sonra kullanabilirsiniz).

```python
def topla(a, b):
    return a + b

sonuc = topla(3, 5) * 2   # 16
```

**Tasarım bağlantısı:** Illustrator sembolü. Bir kez tasarlarsın, her yerde kullanırsın. Sembolu değiştirdiğinde tüm kopyaları güncellenir.

**Tahmin Et (chat):** `topla(2, 3) + topla(4, 1)` satırının sonucu nedir? `def topla(a, b): return a + b` fonksiyonuyla.

> *Cevap: `10` — iki çağrı ayrı ayrı çalışır (5 + 5).*

---

## Slayt 6 — Bu Hafta (7): Kod Yazmadan Önce Düşünmek

### Yeni Python konusu yok. Yeni **süreç** var.

Şimdiye kadar hoca tahtada yazdı, siz aynısını yazdınız. Ama beyaz ekran karşınıza gelince — kimse nasıl başlayacağını bilmiyor.

Bu hafta öğreneceğimiz:

```
NİYET → STORYBOARD → PSEUDOCODE → PYTHON
 (Türkçe) (Çizim)    (Yarı kod)    (Gerçek kod)
```

Bir afiş brifinden Photoshop'a nasıl geçiyorsanız, niyetten koda da aynı şekilde geçeceksiniz.

**Bu hafta biriktireceklerimiz:**
- Storyboard çizme tekniği
- Pseudocode yazma
- Parsons puzzle ile kod okuma
- Niyet kartlarıyla kod yazma

Defter + kalem yanınızda dursun.

---

## Zihin Haritası (Son 5 dakika)

### PYTHON [merkez daire]

6 dal çiz, her dalda hafta numarası ve anahtar kelimeler:

```
               ┌─ Hafta 2 ──── değişken, print, input, if
               │
               ├─ Hafta 3 ──── liste, for, while
               │
    PYTHON ────┼─ Hafta 4 ──── sözlük, break/continue
               │
               ├─ Hafta 5 ──── f-string, matematik, tip
               │
               ├─ Hafta 6 ──── fonksiyon (def, return)
               │
               └─ Hafta 7 ──── süreç: niyet → kod
```

### Nasıl yapılır (hoca için yönerge)

- Zoom whiteboard veya boş A4 paylaş.
- Ortaya PYTHON yaz.
- **Her öğrenciden tek tek iste** (11 kişi, 30 saniye/kişi):
  - "Hafta X'ten aklında kalan bir şey?"
  - Söylediğini ilgili dala yaz.
- Bitince hepsini beraber bir kez daha oku.

### Görsel tavsiye

Öğrenci de defterine böyle bir harita çizsin:
- Ortaya PYTHON
- 6 dal
- Her dala 2-3 anahtar kelime
- Her hafta farklı renk (isteyenler için)

Bu harita vize boyunca nereye bakacaklarını söyler.

---

## Blok 1 Sonu

Ara zamanı.

> "5 dakika ara. 9:25'te Storyboard atölyesine geçeceğiz. Defter-kalem hazırlayın."
