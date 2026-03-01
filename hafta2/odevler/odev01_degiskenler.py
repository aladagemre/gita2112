# =============================================================
# ÖDEV 1: print() ve Değişkenler
# =============================================================
# Bu ödevde yapacakların:
#   - Kendine ait bilgileri değişkenlere kaydet
#   - Bu bilgileri print() ile ekrana yazdır
#   - Sayıyı metinle birleştirmek için str() kullan
#
# Konu: print(), str, int, float, str() dönüşümü
# Kazanım: Değişken tanımlayabilmek ve ekrana anlamlı çıktı verebilmek
# =============================================================


print("=== Tasarımcı Kartım ===")
print()  # Boş satır — görsel düzen için


# --- Görev 1: Değişkenleri Doldur ---
# Aşağıdaki değişkenlere kendi bilgilerini yaz.
# Tırnak içindekiler metin (str), tırnaksızlar sayı (int veya float).

isim = "..."           # str  → kendi adın, örnek: "Defne"
sehir = "..."          # str  → yaşadığın şehir, örnek: "İzmir"
yas = 0                # int  → kaç yaşındasın, örnek: 20
sevdigi_renk = "..."   # str  → en sevdiğin renk, örnek: "turkuaz"
not_ortalamasi = 0.0   # float → not ortalaması, örnek: 3.25


# --- Görev 2: Bilgileri Ekrana Yazdır ---
# print() içinde virgül kullanarak değişkenleri yan yana yazdırabilirsin.

# Örnek (bu satır sana gösterim için yazıldı, silme):
print("Şehir:", sehir)

# Aşağıdaki print() satırlarını tamamla — "..." yerine doğru değişkeni yaz:
print("Ad:", ...)
print("En sevdiğim renk:", ...)


# --- Görev 3: Sayıyı Metne Katarak Yazdır ---
# "+" ile birleştirme yaparken sayıyı str() ile metne çevirmemiz gerekir.

# Örnek (bu satır sana gösterim için yazıldı, silme):
print("Yaşım: " + str(yas))

# Aşağıdaki print() satırlarını tamamla — "..." yerine doğru ifadeyi yaz:
print("Not ortalamam: " + str(...))


print()
print("=== Kart sonu ===")


# =============================================================
# Beklenen Çıktı (değişkenler dolu hâliyle örnek):
# =============================================================
#
# === Tasarımcı Kartım ===
#
# Şehir: İzmir
# Ad: Defne
# En sevdiğim renk: turkuaz
# Yaşım: 20
# Not ortalamam: 3.25
#
# === Kart sonu ===
