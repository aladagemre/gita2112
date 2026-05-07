# =============================================================
# DERS 2: uv ile Bağımlılık Takibi (Rehber)
# =============================================================
# Bu dosya da çalıştırmak için DEĞİL, okumak için yazılmıştır.
# Komutları SİZİN terminalde çalıştırmanız gerekir.
#
# Bu derste öğreneceğiz:
#   - uv nedir, niye lazım
#   - Sanal ortam (virtual environment) kavramı
#   - uv init, uv add, uv run komutları
#   - pyproject.toml dosyasının yapısı
# =============================================================


# --- Sorun: Her Projenin Farklı İhtiyaçları Var ---
#
# Bir tasarım stüdyosu düşünün. Bir poster işi için Pantone
# renk kataloğu, bir kitap için belirli fontlar, bir mobil
# uygulama için farklı mockup'lar gerekiyor.
# Her proje için ayrı bir klasör, ayrı bir malzeme listesi.
#
# Python projeleri de aynı: bir projede Pillow 10, başkasında
# Pillow 11 isteyebilirsiniz. Birinin diğerini bozmaması için
# her projeye AYRI BİR ORTAM gerekir.
#
# uv bunu sizin yerinize halleder.


# --- uv Kurulumu ---
#
# Mac / Linux:
#   $ curl -LsSf https://astral.sh/uv/install.sh | sh
#
# Windows (PowerShell):
#   PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
#
# Kurulumdan sonra terminali kapatıp tekrar açın.
# Şu komutla doğrulayın:
#   $ uv --version
#   uv 0.5.x
#
# Sürüm görürseniz başarılı.


# --- Bir Proje Başlatma: uv init ---
#
# Documents klasörünüze gidin ve yeni bir proje başlatın:
#
#   $ cd Documents
#   $ uv init renk-paleti
#   $ cd renk-paleti
#
# Bu komut "renk-paleti" adlı bir klasör oluşturur.
# İçinde şu dosyalar olur:
#
#   renk-paleti/
#     ├── .python-version
#     ├── README.md
#     ├── main.py            ← örnek bir Python dosyası
#     ├── pyproject.toml     ← projenin künyesi (önemli!)
#     └── .gitignore


# --- Paket Ekleme: uv add ---
#
# Projeye Pillow paketini eklemek isteyelim:
#
#   $ uv add pillow
#
# uv şunu yapar:
#   1. pyproject.toml dosyasındaki dependencies listesine
#      "pillow" ekler
#   2. Sanal bir ortam oluşturur (.venv klasörü)
#   3. Pillow'u o ortama kurar
#
# Birden fazla paket ekleyebilirsiniz:
#
#   $ uv add requests beautifulsoup4
#
# Çıkarmak isterseniz:
#
#   $ uv remove pillow


# --- pyproject.toml Dosyasının Yapısı ---
#
# Yeni oluşturulan dosya şuna benzer:
#
# [project]
# name = "renk-paleti"
# version = "0.1.0"
# description = "Add your description here"
# readme = "README.md"
# requires-python = ">=3.11"
# dependencies = [
#     "pillow>=11.0.0",
# ]
#
# Üç kısım önemli:
#
# 1. name = projenizin adı
# 2. requires-python = en az hangi Python sürümü
# 3. dependencies = projenizin ihtiyaç duyduğu paketler
#
# uv add yapınca dependencies otomatik güncellenir.
# Manuel açmaya gerek yok.


# --- Programınızı Çalıştırma: uv run ---
#
# Normal Python dosyasını çalıştırırken "python3 main.py" yazardık.
# uv projelerinde "uv run main.py" yazıyoruz:
#
#   $ uv run main.py
#
# Niye fark var?
# Çünkü uv run, projenin sanal ortamını kullanır. Yani
# Pillow ya da hangi paketi eklediyseniz, onlar bulunur.
# Düz "python3 main.py" yazarsanız sanal ortamın dışındasınız —
# paketler bulunamaz.


# --- Tipik İş Akışı (Hatırlamanız Gereken Sıra) ---
#
# 1. Yeni proje başlat:
#    $ uv init proje-adi
#    $ cd proje-adi
#
# 2. Paket ekle (gerektiğinde):
#    $ uv add paket-adi
#
# 3. Kod yaz (main.py veya başka bir .py dosyası)
#
# 4. Çalıştır:
#    $ uv run main.py
#
# 5. Yeni paket ihtiyacı doğarsa adım 2'ye dön.


# --- Sık Karşılaşılan Hatalar ---
#
# 1. "uv: command not found"
#    uv kurulumundan sonra terminali yeniden açmadınız.
#    Yeni bir terminal penceresi açın.
#
# 2. "ModuleNotFoundError: No module named 'pillow'"
#    İki ihtimal:
#    a) uv add pillow yapmayı unuttunuz
#    b) "uv run" yerine "python3" yazdınız (sanal ortam dışında)
#
# 3. uv init dediniz, klasör zaten var hatası
#    Var olan klasörün içindeyken yapmak isterseniz:
#    $ uv init       (klasör adı vermeyin)


# --- Bu Dosyayı Çalıştırırsanız ---
print("Bu dosya bir uv kullanım rehberidir.")
print("Yorum satırlarındaki komutları SIRAYLA terminalde deneyin.")
print()
print("Bu hafta için uv kurulumunu MUTLAKA evde sakince yapın.")
print("Sıradaki dosya: 03_dosya_okuma.py")
