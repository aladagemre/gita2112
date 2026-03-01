# =============================================================
# ÖDEV 5: Boolean Değişkenler, and ve İç İçe if
# =============================================================
# Bu ödevde yapacakların:
#   - Kullanıcıdan yaş ve portfolyo proje sayısını al
#   - Karşılaştırma sonuçlarını boolean değişkenlerde sakla
#   - İç içe if (nested if) ile başvuruyu değerlendir
#
# Konu: Boolean değişkenler, iç içe if, and operatörü
# Kazanım: Birden fazla koşulu katmanlı biçimde kontrol edebilmek
# =============================================================


print("=== Portfolyo Başvuru Sistemi ===")
print("Başvurunun kabul edilip edilmeyeceğini öğrenmek için bilgilerini gir.")
print()


# --- Başvuru Kuralları ---
# Kural 1: Başvuran en az 18 yaşında olmalı.
# Kural 2: Portfolyoda en az 5 proje bulunmalı.
# Her iki koşul sağlanırsa → kabul.
# Sadece yaş uygunsa ama proje yetmiyorsa → proje eklemesi istenir.
# Yaş uygun değilse → direkt reddedilir (proje sayısına bakılmaz).


# --- Kullanıcıdan Bilgi Al ---
yas = int(input("Yaşın kaç? "))
proje_sayisi = int(input("Portfolyonda kaç proje var? "))


# --- Boolean Değişkenleri Tanımla ---
# Karşılaştırma işlemleri True veya False üretir.
# Bu sonuçları değişkende saklarsak kod daha okunabilir olur.

resit_mi = yas >= 18             # 18 veya üzeriyse True, değilse False

# Buraya kodunu yaz ↓
# proje_sayisi 5 veya üzerinde mi kontrol et ve sonucu yeterli_proje_mi değişkenine kaydet
yeterli_proje_mi = ...           # Bu satırı tamamla!


# --- İç İçe if Yapısını Tamamla ---
# Dış if: yaş kontrolü — önce reşit mi?
# İç if: yaş uygunsa proje sayısını kontrol et.
#
# Yapı şöyle görünmeli:
#
#   if resit_mi:
#       if yeterli_proje_mi:
#           → "Başvurun kabul edildi!"
#       else:
#           → kaç proje eksik olduğunu hesapla ve söyle
#   else:
#       → kaç yıl daha beklemesi gerektiğini hesapla ve söyle

if resit_mi:
    if yeterli_proje_mi:
        print("...")  # ← kabul mesajını buraya yaz
    else:
        print("...")  # ← "Yaşın uygun, ama portfolyon henüz hazır değil." mesajı
        print("...")  # ← kaç proje eksik olduğunu hesaplayıp yazdır (İpucu: 5 - proje_sayisi)
else:
    print("...")  # ← "Üzgünüz, yaş koşulunu sağlamıyorsun." mesajı
    print("...")  # ← kaç yıl beklenmesi gerektiğini hesaplayıp yazdır (İpucu: 18 - yas)


# =============================================================
# Beklenen Çıktı — 3 Farklı Örnek:
# =============================================================
#
# Örnek 1 — Her iki koşul da sağlanıyor:
#   Yaşın kaç? 22
#   Portfolyonda kaç proje var? 7
#   Tebrikler! Başvurun kabul edildi. Harika işler bekliyoruz.
#
# ---
#
# Örnek 2 — Yaş uygun ama proje yetmiyor:
#   Yaşın kaç? 19
#   Portfolyonda kaç proje var? 3
#   Yaşın uygun, ama portfolyon henüz hazır değil.
#   Başvurabilmek için 2 proje daha eklemelisin.
#
# ---
#
# Örnek 3 — Yaş koşulu sağlanmıyor:
#   Yaşın kaç? 16
#   Portfolyonda kaç proje var? 10
#   Üzgünüz, yaş koşulunu sağlamıyorsun.
#   2 yıl sonra tekrar başvurabilirsin. O zamana kadar tasarlamaya devam et!
