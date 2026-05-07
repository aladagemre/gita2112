# Slaytlar — Blok 3: Parsons Puzzle

> Karışık kod satırları. Doğru sıraya koyun.
> Her puzzle 3 bölüm: (1) görev, (2) karışık satırlar (harflerle), (3) doğru sıra + neden + tuzak notları.

---

## PUZZLE 1 — Kolay

### Hoca demosu için. Birlikte çözülür. 5 satır, tuzak yok.

### Görev

> **"Bir puanlar listesinin toplamını hesaplayıp yazdır."**

Beklenen çıktı:
```
Toplam: 340
```

### Karışık Satırlar

```
A.   toplam = toplam + puan
B.   puanlar = [85, 90, 78, 87]
C.   print(f"Toplam: {toplam}")
D.   for puan in puanlar:
E.   toplam = 0
```

### Tahmin Et (30 sn — sıralamadan ÖNCE)

> "Hiç sırayı bulmadan: bu 5 satır doğru sırada olsa ekrana ne yazardı? Chat'e **tek sayı** gönderin."

Amaç: öğrenci satırları hızlıca okuyup mantığı zihninde çalıştırsın. Beklenen cevap: `340`. Yanlış cevap gelirse demesi "hangi iki sayıyı topladın?" diye tek tek yürütme.

### Doğru Sıra

```
B → E → D → A → C
```

### Neden Bu Sıra (öğretici not)

- **B (`puanlar = [...]`)** — Veriyi önce tanımlamalıyız. Elinde liste olmadan liste üstünde iş yapamazsın.
- **E (`toplam = 0`)** — Sayaç/toplam başlangıcı **döngüden ÖNCE** gelir. Aksi halde her turda sıfırlanır.
- **D (`for puan in puanlar:`)** — Döngü açılışı.
- **A (`toplam = toplam + puan`)** — Döngünün **içinde**, her turda toplamı artır. Girintilidir.
- **C (`print(...)`)** — Döngü **bittikten sonra**. İçeride olsaydı her turda yazılırdı.

> **Dikkat noktası:** A satırı girintili, E ve C satırları değil. Girintiler öğrencilerin en sık yanılgısıdır.

### Hocanın Soracağı Soru

> "E niye D'den önce? Diğer bir deyişle, toplamı 0'a neden döngüden ÖNCE atıyoruz?"

Cevap: Döngünün içinde olsaydı her turda 0'a sıfırlanırdı — önceki birikim kaybolur.

### Çalışır Haldeki Python

```python
puanlar = [85, 90, 78, 87]
toplam = 0
for puan in puanlar:
    toplam = toplam + puan
print(f"Toplam: {toplam}")
```

---

## PUZZLE 2 — Orta

### 7 satır, içinde 1 tuzak. Bireysel çalışma.

### Görev

> **"Renk listesindeki 'mavi'nin kaç kez geçtiğini bul ve yazdır."**

Beklenen çıktı:
```
mavi sayısı: 3
```

### Karışık Satırlar

```
A.   print(f"mavi sayısı: {sayac}")
B.   renkler = ["mavi", "kırmızı", "mavi", "sarı", "mavi", "yeşil"]
C.   if renk == "mavi":
D.   sayac = 0
E.   for renk in renkler:
F.   sayac = sayac + 1
G.   sayac = sayac - 1   ← TUZAK
```

### Tahmin Et (30 sn)

> "Doğru sırada bu kod kaç yazar? Chat'e tek sayı."

Beklenen: `3` (listedeki mavi sayısı). Yanlış cevap veren öğrenciye "listede kaç mavi var? sayar mısın?" diye dön.

### Doğru Sıra

```
B → D → E → C → F → A
```

(G satırı kullanılmaz.)

### Neden Bu Sıra

- **B** — Veri tanımlama (liste).
- **D** — Sayaç başlangıcı (döngüden önce, 0).
- **E** — Döngü aç.
- **C** — Koşul: bu renk mavi mi? (döngünün içinde)
- **F** — Mavi ise sayacı artır. (if'in içinde, iki kat girintili)
- **A** — Döngü bitince sonucu yazdır.

### Tuzak: G (`sayac = sayac - 1`)

G satırı sayacı azaltıyor. Amacımız **saymak** — azaltmak değil. Her satırı kullanmak zorunda değilsiniz. Tuzak satırları dahil etmeyin.

> **Hocanın sorusu:** "G satırını koymuş olsaydınız ne olurdu? Zihinde yürütün — mavi gördüğümüzde bir artırıyoruz, bir azaltıyoruz. Sonuç hep 0."

### Tuzak Mikrosu (1 cümle, 30 sn) — 3.1 provası

> "G satırı neden **mantık hatası**? Tek cümleyle chat'e yazın — neden yanlış?"

Bekle 30 sn, 2-3 cevabı oku. Kabul edilen cevaplar: "artırıp azaltıyor, sıfır eder", "her mavi için +1 ve -1 birbirini götürür", "sayma mantığına aykırı". "G yanlış" gibi yetersiz cevaba "neden?" diye dön — vize 1.2/3.1 için tam bu tip açıklama istenecek.

### Hocanın Dikkat Ettirmesi Gereken Noktalar

- **İki kat girinti:** F satırı hem for'un hem if'in içinde. Yani 8 boşluk (2 girinti).
  ```python
  for renk in renkler:
      if renk == "mavi":
          sayac = sayac + 1
  ```
- **C satırı:** `if renk == "mavi":` — tek `=` değil, çift `==`. Eşittir karşılaştırması.

### Çalışır Haldeki Python

```python
renkler = ["mavi", "kırmızı", "mavi", "sarı", "mavi", "yeşil"]
sayac = 0
for renk in renkler:
    if renk == "mavi":
        sayac = sayac + 1
print(f"mavi sayısı: {sayac}")
```

---

## PUZZLE 3 — Zor

### 10 satır, 1 tuzak, fonksiyon + döngü + koşul. Breakout ikili çalışma.

### Görev

> **"`en_yuksek_puan` adlı bir fonksiyon yaz. Bir projeler listesi alsın, en yüksek puanlı projenin puanını döndürsün. Sonra bu fonksiyonu çağırıp sonucu yazdır."**

Veri:
```python
projeler = [
    {"ad": "Logo",   "puan": 88},
    {"ad": "Afiş",   "puan": 95},
    {"ad": "Ambalaj","puan": 72},
]
```

Beklenen çıktı:
```
En yüksek puan: 95
```

### Karışık Satırlar

```
A.   def en_yuksek_puan(projeler):
B.   for proje in projeler:
C.       if proje["puan"] > en_yuksek:
D.           en_yuksek = proje["puan"]
E.       return en_yuksek
F.   en_yuksek = 0
G.   sonuc = en_yuksek_puan(projeler)
H.   print(f"En yüksek puan: {sonuc}")
I.   projeler = [{"ad": "Logo", "puan": 88}, {"ad": "Afiş", "puan": 95}, {"ad": "Ambalaj", "puan": 72}]
J.   en_yuksek = 100   ← TUZAK
```

### Tahmin Et (30 sn — breakout'a ÖNCE)

> "Bu fonksiyon doğru kurulursa `sonuc` ne olur? Chat'e tek sayı."

Beklenen: `95`. Yanlış cevap: `88` (ilk projenin puanı — return'un yerini yanlış okuyanlar) veya `100` (J tuzağına kanan). Tahmin hatalıysa "hangi projenin puanı en yüksek? liste 3 tane, biri 95" diye yönlendir.

### Doğru Sıra

```
A → F → B → C → D → E → I → G → H
```

(J satırı kullanılmaz.)

> **Not:** E satırı (`return en_yuksek`) fonksiyonun sonunda ve for döngüsünün **dışında** olmalı. Slayt notlarında E'nin girintisi 4 boşluk (fonksiyonun içi ama döngünün dışı). C ve D ise 8 boşluk (döngü + if).

### Girintilerin Haritası

```python
def en_yuksek_puan(projeler):      # A — 0 boşluk
    en_yuksek = 0                  # F — 4 boşluk
    for proje in projeler:         # B — 4 boşluk
        if proje["puan"] > en_yuksek:  # C — 8 boşluk
            en_yuksek = proje["puan"]   # D — 12 boşluk
    return en_yuksek               # E — 4 boşluk (döngü dışı)

projeler = [...]                   # I — 0 boşluk
sonuc = en_yuksek_puan(projeler)   # G — 0 boşluk
print(f"En yüksek puan: {sonuc}")  # H — 0 boşluk
```

### Neden Bu Sıra

- **A** — Fonksiyon tanımlama. Her şey bunun içinde.
- **F** — Fonksiyonun içindeki başlangıç değeri.
- **B** — Döngü.
- **C** — Koşul.
- **D** — Koşul sağlanırsa güncelle.
- **E** — Fonksiyon sonu — return. Döngünün **dışında**, yoksa ilk turda biter.
- **I** — Global veri. Fonksiyon tanımı zaten hazır, şimdi veriyi hazırla.
- **G** — Fonksiyonu çağır, sonucu sakla.
- **H** — Yazdır.

### Tuzak: J (`en_yuksek = 100`)

J satırı başlangıç değerini **100** yapıyor. F satırı (`en_yuksek = 0`) ile rekabet ediyor — sadece birini seçmelisiniz. Doğru olan **F**. Niye?

- F ile başlarsanız (`en_yuksek = 0`): Döngüde ilk projenin puanı (88) 0'dan büyük olduğu için `en_yuksek = 88`, sonra 95 > 88 olduğu için `en_yuksek = 95`. Doğru cevap.
- J ile başlarsanız (`en_yuksek = 100`): Tüm puanlar 100'den **küçük** olduğu için döngü `en_yuksek`'i hiç güncellemez. Fonksiyon 100 döner. Yanlış — bu projede 100 puan yok.

> **Hocanın sorusu:** "F ve J arasında neden F doğru? Başlangıç değerini ne yapmalıyız: çok **küçük** mü, çok **büyük** mü? Sebebi ne?"

Cevap: "En yüksek"i ararken başlangıç **çok küçük** olmalı — ki ilk gerçek değer onu yenip güncellemeyi başlatsın. Çok büyük başlangıç hiçbir gerçek değer tarafından geçilemez, döngü boşa döner.

### Tuzak Mikrosu (1 cümle, 30 sn) — 3.1 provası

> "J satırı konulursa fonksiyon ne döndürür ve **neden**? Chat'e tek cümle."

Beklenen cevap: "`100` döner çünkü hiçbir gerçek puan 100'den büyük değil, döngü güncelleme yapmaz." "100 döner" yeterli değil — **neden'i** iste. Bu tam olarak vize 1.2 / 3.1 tarzı açıklamadır.

### Kritik Hata Noktaları

- **return'u döngünün içine koymak:** Bu kodun en sık hatası. E satırı for döngüsünün içine düşerse, ilk turda fonksiyon biter ve sadece ilk projeyi görürüz.
  ```python
  # YANLIŞ:
  for proje in projeler:
      if proje["puan"] > en_yuksek:
          en_yuksek = proje["puan"]
          return en_yuksek   # İlk turda biter, 88 döner!
  ```
- **projeler'i fonksiyonun içinde tanımlamak:** I satırı fonksiyonun **dışında** olmalı. Fonksiyonun içine koyarsa parametre almanın anlamı kalmaz.

### Çalışır Haldeki Python

```python
def en_yuksek_puan(projeler):
    en_yuksek = 0
    for proje in projeler:
        if proje["puan"] > en_yuksek:
            en_yuksek = proje["puan"]
    return en_yuksek

projeler = [
    {"ad": "Logo",   "puan": 88},
    {"ad": "Afiş",   "puan": 95},
    {"ad": "Ambalaj","puan": 72},
]
sonuc = en_yuksek_puan(projeler)
print(f"En yüksek puan: {sonuc}")
```

### Breakout Talimatı (chat'e yapıştır)

```
2 kişilik breakout. 8 dakika.
Görev: satırları sırala, chat'e dönüp cevabı yazın.
Format: "A-F-B-C-D-E-I-G-H" (tire ile ayırın)
Girintilere dikkat — bir satır döngünün içinde mi dışında mı?
```

---

## Blok 3 Sonu

Ana odaya dönünce:

1. Cevapları topla.
2. Doğru cevabı ekranda göster, satır satır geç.
3. Tuzak satırını neden elediklerini sor.

> "5 dakika ara. Son blokta niyet kartları — vize provası."
