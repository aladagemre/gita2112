# Hafta 7 — Defter Sayfası

> Bu tek sayfayı yazdır. Defterinin ilk sayfasına yapıştır. Vize sırasında da yanında dursun.

---

## STORYBOARD TEMPLATE

Bir görevi kodlamadan önce buraya doldur:

**Niyet (tek cümle):**
```
_____________________________________________________
_____________________________________________________
```

**Veri (elinde ne var?):**
```
_____________________________________________________
```

**Beklenen çıktı:**
```
_____________________________________________________
```

---

```
┌───────────────────────┐  ┌───────────────────────┐  ┌───────────────────────┐  ┌───────────────────────┐
│                       │  │                       │  │                       │  │                       │
│        KARE 1         │  │        KARE 2         │  │        KARE 3         │  │        KARE 4         │
│                       │  │                       │  │                       │  │                       │
│     Başlangıç         │  │       Döngü           │  │   Koşul / Eylem       │  │      Sonuç            │
│                       │  │                       │  │                       │  │                       │
│                       │  │                       │  │                       │  │                       │
│                       │  │                       │  │                       │  │                       │
│                       │  │                       │  │                       │  │                       │
│                       │  │                       │  │                       │  │                       │
└───────────────────────┘  └───────────────────────┘  └───────────────────────┘  └───────────────────────┘
```

> **İpucu:** 4 kare yetmezse alta 2 kare daha çiz. Kareleri basit tut — kutu + iki-üç kelime. Çizim değil, **düşünce haritası**.

---

## PSEUDOCODE YAZARKEN SOR

Pseudocode'u yazmadan önce bu 6 soruyu geç:

- [ ] **Veri ne türde?**  (liste? sözlük? sözlük listesi? sayı?)
- [ ] **Kaç tane?**  (tek şey mi, birden fazla mı?)
- [ ] **Döngü var mı?**  (birden fazla şey üstünde iş yapıyorsam evet)
- [ ] **Koşul var mı?**  (filtreleme? karar? evet → if)
- [ ] **Takip edecek değişken var mı?**  (sayaç, toplam, en yüksek...)
- [ ] **Sonuç ne olacak?**  (yazdıracak mı? döndürecek mi? liste mi?)

Bu altı soruya cevap vermeden pseudocode yazmaya başlama.

---

## TÜRKÇE → PYTHON ÇEVİRİ SÖZLÜĞÜ

| Türkçe (pseudocode'da)                      | Python karşılığı                         |
|----------------------------------------------|------------------------------------------|
| ... diye bir değişken aç, başlangıçta 0      | `sayac = 0`                              |
| ... diye bir liste aç, boş                   | `liste = []`                             |
| ... diye bir sözlük aç, boş                  | `sozluk = {}`                            |
| Hepsi için / Her ... için                    | `for ... in ...:`                        |
| Sayısını say                                 | `len(liste)`                             |
| Eğer ...                                     | `if ...:`                                |
| Değilse / aksi halde                         | `else:`                                  |
| Ya da / başka bir şeyse                      | `elif ...:`                              |
| ... eşit mi?                                 | `==`   (tek `=` değil!)                  |
| ... büyük mü?                                | `>`                                      |
| ... büyük ya da eşit mi?                     | `>=`                                     |
| Yaz / ekrana bas                             | `print(...)`                             |
| Döndür / sonuç olarak ver                    | `return ...`                             |
| Sayacı 1 artır / say                         | `sayac += 1`                             |
| Toplama ekle                                 | `toplam += x`                            |
| Listeye ekle                                 | `liste.append(x)`                        |
| Sözlüğe ekle                                 | `sozluk[anahtar] = deger`                |
| Listede var mı                               | `x in liste`                             |
| Sözlükte var mı                              | `anahtar in sozluk`                      |
| Fonksiyon yaz / tanımla                      | `def ad(parametre):`                     |
| Fonksiyonu çalıştır / çağır                  | `ad(argüman)`                            |

---

## VCD'NİN PYTHON ALFABESİ (hafıza haritası)

```
        Hafta 2 ─── değişken, print, input, if
              │
        Hafta 3 ─── liste, for, while, range
              │
PYTHON ───────┼─── Hafta 4 ─── sözlük, break, continue
              │
        Hafta 5 ─── f-string, int/float, //, %, **
              │
        Hafta 6 ─── fonksiyon (def, return, varsayılan)
              │
        Hafta 7 ─── süreç: niyet → storyboard → pseudocode → python
```

---

## KOD YAZARKEN KENDİNE SOR

Her yeni kod parçasında:

1. **Niyet ne?** (tek cümleyle yazabiliyor muyum?)
2. **İlk kare ne?** (başlangıç değerleri neler?)
3. **Döngü gerekli mi?** (tek bir şey mi, çok mu?)
4. **Koşul gerekli mi?** (filtre / karar?)
5. **Sonucu nerede saklıyorum?** (sayaç, toplam, liste, en yüksek...)
6. **Çıktı ne?** (print mi return mı?)

---

## SIK KARIŞAN 5 NOKTA

1. **`=` vs `==`** — ilki atama ("bu değeri koy"), ikincisi karşılaştırma ("eşit mi?").
2. **Girinti** — döngünün veya if'in içindeki satırlar **dört boşluk** girintili olmalı.
3. **Başlangıç değeri** — sayaç, toplam, liste her zaman döngüden **önce** tanımlı olmalı.
4. **`print` vs `return`** — print ekrana yazar, return değeri geri verir. Fonksiyonun sonucunu kullanacaksan `return`.
5. **Sözlükte erişim** — `proje["ad"]` (nokta değil, köşeli parantez).

---

*Hoca: Emre Aladağ — Işık Üniversitesi GITA 2112 — 2026 Bahar*
