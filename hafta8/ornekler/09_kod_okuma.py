# =============================================================
# DERS 9: Yabancı Bir Kodu Okuma Alıştırması
# =============================================================
# Bu dosya, bir yapay zeka aracının (örneğin Gemini) size
# verebileceği TİPİK bir kod parçasıdır. İçinde henüz YAZMAYI
# öğrenmediğimiz ama OKUMAYI öğrenmemiz gereken birkaç yapı var:
#
#   - List comprehension  ([... for ... in ... if ...])
#   - try / except         (hatayı yakalama)
#   - Tip ipuçları         (parametre: float, -> str)
#
# Görev: Bu dosyayı satır satır okuyun. Her bölümün üstündeki
# yorum bloğu, ne yaptığını "Türkçe pseudocode" gibi açıklar.
# Aşağıda boş yorum satırları var; bunları siz doldurun.
#
# Bu kod ÇALIŞIR. Çalıştırıp çıktısına bakın, sonra okuyun.
# =============================================================


import csv
import json
from datetime import date


# --- Kısım 1: Renkleri Dosyadan Okuma ---
#
# Bu fonksiyon bir CSV dosyasından renk paleti okur ve
# liste olarak döndürür. Her renk bir sözlük olur:
#   {"isim": "Mercan", "hex": "#FF6B6B", "grup": "sıcak"}
#
# Yeni yapı: try / except — dosya bulunamazsa boş liste döndürür.

def renkleri_oku(dosya_yolu: str) -> list:
    # SİZİN YORUMUNUZ:
    # ...
    try:
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            okuyucu = csv.reader(dosya)
            next(okuyucu)  # ilk satır başlık — atla
            renkler = []
            for satir in okuyucu:
                renk = {
                    "isim": satir[0],
                    "hex": satir[1],
                    "grup": satir[2],
                }
                renkler.append(renk)
            return renkler
    except FileNotFoundError:
        # SİZİN YORUMUNUZ:
        # ...
        print(f"Uyarı: {dosya_yolu} bulunamadı, boş liste döndürülüyor.")
        return []


# --- Kısım 2: Sıcak Renkleri Filtreleme ---
#
# Yeni yapı: list comprehension — tek satırda
# döngü + if + listeye ekleme yapar.

def sicak_renkleri_bul(renkler: list) -> list:
    # SİZİN YORUMUNUZ:
    # ...
    return [r for r in renkler if r["grup"] == "sıcak"]


# --- Kısım 3: Sadece HEX Kodlarını Çıkar ---
#
# Yine list comprehension, ama bu sefer sözlüklerden
# sadece "hex" alanını alıyoruz.

def hex_listesi(renkler: list) -> list:
    # SİZİN YORUMUNUZ:
    # ...
    return [r["hex"] for r in renkler]


# --- Kısım 4: Bir Palet Künyesi Üret ---
#
# Bir sözlük üretiyor: paletin adı, kaç renk olduğu,
# tarih, hex listesi.

def palet_kunyesi(palet_adi: str, renkler: list) -> dict:
    # SİZİN YORUMUNUZ:
    # ...
    return {
        "ad": palet_adi,
        "olusturma_tarihi": str(date.today()),
        "renk_sayisi": len(renkler),
        "renkler_hex": hex_listesi(renkler),
    }


# --- Kısım 5: Künyeyi JSON Dosyasına Kaydet ---

def kunye_kaydet(kunye: dict, dosya_yolu: str) -> None:
    # SİZİN YORUMUNUZ:
    # ...
    with open(dosya_yolu, "w", encoding="utf-8") as dosya:
        json.dump(kunye, dosya, ensure_ascii=False, indent=2)


# --- Ana Akış ---
#
# Yukarıdaki fonksiyonları sırayla çağıran bölüm.

def main() -> None:
    print("=== Sıcak Renk Paleti Hazırlanıyor ===")
    print()

    # 1. Renkleri oku
    tum_renkler = renkleri_oku("veri/renkler.csv")
    print(f"Toplam {len(tum_renkler)} renk okundu.")

    # 2. Sıcak olanları ayır
    sicak = sicak_renkleri_bul(tum_renkler)
    print(f"Sıcak renkler: {len(sicak)} adet")

    for renk in sicak:
        print(f"  - {renk['isim']} ({renk['hex']})")

    # 3. Künye oluştur
    kunye = palet_kunyesi("Sıcak Palet 2026", sicak)

    # 4. JSON olarak kaydet
    kunye_kaydet(kunye, "sicak_palet_kunyesi.json")
    print()
    print("sicak_palet_kunyesi.json dosyasına kaydedildi.")


# Bu satır "bu dosya doğrudan çalıştırılırsa main() fonksiyonunu çağır"
# demek. Şimdilik sadece "main'i çağırıyor" diye okuyun.
if __name__ == "__main__":
    main()


# =============================================================
# OKUMA ALIŞTIRMASI — Derste Birlikte Yapılacak
# =============================================================
#
# Yukarıda her fonksiyonun başında "SİZİN YORUMUNUZ" diyen
# boş yorum satırları var. Şu soruyla doldurun:
#
#   "Bu fonksiyon ne yapıyor? Hangi girdiyi alıp ne döndürüyor?"
#
# Cevabı 1-2 cümleyle Türkçe olarak yazın.
# Örnek:
#
#   def renkleri_oku(dosya_yolu: str) -> list:
#       # SİZİN YORUMUNUZ:
#       # Verilen CSV dosyasını okur, her satırı sözlüğe çevirir
#       # ve sözlüklerden oluşan bir liste döndürür.
#       # Dosya yoksa hata vermek yerine boş liste döner.
#
#
# YENİ KARŞILAŞTIĞINIZ ÜÇ YAPI:
#
#   1. Tip ipuçları — def f(x: str) -> list:
#      "x str türünde olmalı, fonksiyon list döndürür" anlamı.
#      Yazmanız gerekmiyor. Görünce paniklemeyin.
#
#   2. List comprehension — [r for r in renkler if r["grup"] == "sıcak"]
#      Tek satırda döngü + filtre + listeye ekleme.
#      Sıraya göre okuyun: for ... → if ... → her bir r.
#
#   3. try / except — try bloğunda hata olursa except çalışır.
#      Programın çökmesini engeller.
#      "Bu satır kırılabilir, kırılırsa şunu yap" mantığı.
#
# Bu yapıları YAZMANIZ beklenmiyor. Sadece OKUYUNCA "ha bu şu
# demek" diyebilmeniz yeterli.
