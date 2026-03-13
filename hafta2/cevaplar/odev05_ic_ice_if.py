# =============================================================
# ÖDEV 5: Boolean Değişkenler, and ve İç İçe if — CEVAP ANAHTARI
# =============================================================


print("=== Portfolyo Başvuru Sistemi ===")
print("Başvurunun kabul edilip edilmeyeceğini öğrenmek için bilgilerini gir.")
print()


# --- Kullanıcıdan Bilgi Al ---

yas = int(input("Yaşın kaç? "))
proje_sayisi = int(input("Portfolyonda kaç proje var? "))


# --- Boolean Değişkenleri Tanımla ---

resit_mi = yas >= 18
yeterli_proje_mi = proje_sayisi >= 5


# --- İç İçe if Yapısı ---

if resit_mi:
    if yeterli_proje_mi:
        print("Tebrikler! Başvurun kabul edildi. Harika işler bekliyoruz.")
    else:
        print("Yaşın uygun, ama portfolyon henüz hazır değil.")
        print("Başvurabilmek için", 5 - proje_sayisi, "proje daha eklemelisin.")
else:
    print("Üzgünüz, yaş koşulunu sağlamıyorsun.")
    print(str(18 - yas) + " yıl sonra tekrar başvurabilirsin. O zamana kadar tasarlamaya devam et!")


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
