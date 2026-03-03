# GITA2112 — Bilgisayar Programlamaya Giriş

Işık Üniversitesi GITA2112 dersi için oluşturulmuş kaynak deposu. Bu repoda haftalık ders örnekleri ve ödevler bulunmaktadır.

## Klasör Yapısı

```
gita2112/
└── hafta2/
    ├── ornekler/   # Ders örnekleri
    └── odevler/    # Ödev dosyaları
```

İlerleyen haftalar eklendikçe yeni klasörler burada görünecektir.

---

## Dosyaları İndirme

### Yöntem 1: ZIP İndir (Önerilen)

1. Sayfanın sağ üstündeki yeşil **Code** butonuna tıkla
2. **Download ZIP** seç
3. ZIP dosyasını aç ve istediğin klasöre taşı
4. Her hafta yeni dosyalar eklendiğinde bu adımları tekrarla

### Yöntem 2: Git ile Clone & Pull (Uzun vadeli çözüm)

ZIP yönteminde her hafta dosyaları tekrar indirip açman gerekir. Git kullanırsan yalnızca tek bir komutla (`git pull`) o haftaya eklenen tüm yeni dosyalar bilgisayarına gelir — ZIP indirmene gerek kalmaz.

#### Git Kurulumu

Öncelikle sisteminizde git kurulu olup olmadığını kontrol edin. Terminal veya WSL üzerinde git komutunu verdiğinizde komutu bulamıyorsa kurmanız gereklidir. [git-scm.com/download/](http://git-scm.com/download/) adresinden işletim sisteminizi seçerek belirtilen yolla kurulumu gerçekleştirin.


---

**İlk kez indirmek için** (Git kurulduktan sonra bir kez yapılır):

```bash
git clone https://github.com/aladagemre/gita2112.git
```

**Yeni hafta dosyalarını almak için** (her hafta bu komutu çalıştır):

```bash
cd gita2112
git pull
```

---

## Gereksinimler

- **Python 3** — [python.org](https://www.python.org/downloads/) adresinden indirilebilir
- **VS Code** — Önerilen kod editörü ([code.visualstudio.com](https://code.visualstudio.com))
