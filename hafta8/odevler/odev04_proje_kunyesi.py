# =============================================================
# ÖDEV 4: Proje Künyesi (JSON)  [Orta]
# =============================================================
# Bu ödevde yapacakların:
#   - Bir Python sözlüğü oluştur
#   - JSON dosyasına yaz (json.dump)
#   - Dosyayı geri oku (json.load)
#   - Sözlüğü güncelle ve tekrar kaydet
#
# Konu: Sözlük + json.dump + json.load + ensure_ascii + indent
# Kazanım: Sözlük verisini diske kalıcı yazıp geri okuyabilmek
# =============================================================


import json


print("=== Proje Künyesi Oluşturucu ===")
print()


# --- Görev 1: Proje Sözlüğü Oluştur ---
# Aşağıdaki sözlüğü doldur. Kendi tasarım projeniz olabilir.

proje = {
    "ad": "...",                                    # ← örn: "Sergi Kataloğu"
    "tarih": "...",                                 # ← örn: "2026-09-15"
    "tasarimci": "...",                             # ← kendi adınız
    "renkler": [..., ..., ...],                     # ← 3 renk hex kodu, örn: "#FF6B6B"
    "fontlar": [..., ...],                          # ← 2 font adı, örn: "Inter"
    "tamamlandi": False,                            # ← bunu olduğu gibi bırakın
}

print("Sözlük hazırlandı:")
print(proje)
print()


# --- Görev 2: JSON Dosyasına Yaz ---
# proje_kunyesi.json dosyasına kaydet.
# ensure_ascii=False ve indent=2 parametrelerini eklemeyi unutma.

with open("proje_kunyesi.json", "w", encoding="utf-8") as dosya:
    json.dump(proje, ..., ensure_ascii=False, indent=2)   # ← ikinci argüman: dosya değişkeni

print("proje_kunyesi.json dosyasına yazıldı.")
print()


# --- Görev 3: Dosyayı Geri Oku ---

with open("proje_kunyesi.json", "r", encoding="utf-8") as dosya:
    okunan = json.load(...)                         # ← argüman: dosya değişkeni

print("Geri okunan sözlük:")
print(okunan)
print()
print(f"Tipi: {type(okunan).__name__}")             # dict olmalı
print()


# --- Görev 4: Sözlüğü Güncelle ---
# Üç şey yap:
#   1. renkler listesine yeni bir hex ekle
#   2. tamamlandi alanını True yap
#   3. yeni bir alan ekle: "yayinlandi_sayfa", string bir URL

okunan["renkler"].append(...)                       # ← yeni bir hex kodu, örn: "#FFD93D"
okunan["tamamlandi"] = ...                          # ← True
okunan[...] = "https://defne-aydin.com/projeler"    # ← yeni anahtar adı: "yayinlandi_sayfa"

print("Güncellenmiş sözlük:")
print(okunan)
print()


# --- Görev 5: Güncel Sözlüğü Tekrar Yaz ---
# proje_kunyesi.json dosyasını "w" modu ile aç ve okunan sözlüğünü kaydet.

with open(..., "w", encoding="utf-8") as dosya:    # ← "proje_kunyesi.json"
    json.dump(..., dosya, ensure_ascii=False, indent=2)   # ← okunan sözlüğünü ver

print("Güncel veri proje_kunyesi.json dosyasına tekrar yazıldı.")


# =============================================================
# Beklenen Çıktı (örnek değerlerle):
# =============================================================
#
# === Proje Künyesi Oluşturucu ===
#
# Sözlük hazırlandı:
# {'ad': 'Sergi Kataloğu', 'tarih': '2026-09-15', 'tasarimci': 'Defne Aydın', 'renkler': ['#FF6B6B', '#1E3A8A', '#2B2D42'], 'fontlar': ['Inter', 'Playfair Display'], 'tamamlandi': False}
#
# proje_kunyesi.json dosyasına yazıldı.
#
# Geri okunan sözlük:
# {'ad': 'Sergi Kataloğu', 'tarih': '2026-09-15', 'tasarimci': 'Defne Aydın', 'renkler': ['#FF6B6B', '#1E3A8A', '#2B2D42'], 'fontlar': ['Inter', 'Playfair Display'], 'tamamlandi': False}
#
# Tipi: dict
#
# Güncellenmiş sözlük:
# {'ad': 'Sergi Kataloğu', 'tarih': '2026-09-15', 'tasarimci': 'Defne Aydın', 'renkler': ['#FF6B6B', '#1E3A8A', '#2B2D42', '#FFD93D'], 'fontlar': ['Inter', 'Playfair Display'], 'tamamlandi': True, 'yayinlandi_sayfa': 'https://defne-aydin.com/projeler'}
#
# Güncel veri proje_kunyesi.json dosyasına tekrar yazıldı.
#
# Ayrıca: proje_kunyesi.json dosyasını VS Code'da açtığınızda,
# Türkçe karakterler düzgün görünmeli (Defne Aydın), 2 boşluk
# girintili ve insan tarafından okunabilir olmalı.
