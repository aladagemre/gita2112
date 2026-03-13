# =============================================================
# ÖDEV 3: Koşullu İfade — if / else — CEVAP ANAHTARI
# =============================================================


print("=== Baskı Makinesi Kontrolü ===")
print("Bu program posterinin baskı makinesine sığıp sığmadığını kontrol eder.")
print()


# --- Sabit Bilgi ---

maksimum_genislik = 70


# --- Kullanıcıdan Girdi Al ---

poster_genisligi = int(input("Posterinin genişliği kaç cm? "))


# --- Koşul ---

if poster_genisligi <= maksimum_genislik:
    print("Harika!", str(poster_genisligi), "cm posterın makineye sığıyor. Baskıya hazır!")

else:
    print("Dikkat!", str(poster_genisligi), "cm makinemizin limitini (" + str(maksimum_genislik) + " cm) aşıyor. Boyutu küçültmen gerekiyor.")


# =============================================================
# Beklenen Çıktı — Örnek 1 (sığan poster):
# =============================================================
#
# Posterinin genişliği kaç cm? 50
# Harika! 50 cm posterın makineye sığıyor. Baskıya hazır!
#
# =============================================================
# Beklenen Çıktı — Örnek 2 (sığmayan poster):
# =============================================================
#
# Posterinin genişliği kaç cm? 90
# Dikkat! 90 cm makinemizin limitini (70 cm) aşıyor. Boyutu küçültmen gerekiyor.
