# =============================================================
# DERS 6: Çoklu Koşul Dalları — if / elif / else Zinciri
# =============================================================
# Bu derste öğreneceğiz:
#   - elif (else if) ile birden fazla koşul kontrol etme
#   - Zincir mantığı: ilk doğru koşul çalışır, diğerleri atlanır
#   - >= (büyük eşit) karşılaştırma operatörü


# --- Kullanıcıdan Puan Alma ---
puan = int(input("Aldığın puan: "))  # input her zaman string, int() ile sayıya çeviriyoruz

# --- if / elif / else Zinciri ---
# Python koşulları yukarıdan aşağıya sırayla kontrol eder.
# İlk True olan bloğu çalıştırır ve zincirden çıkar.
# Hiçbiri sağlanmazsa else bloğu çalışır.

if puan >= 90:       # 90 ve üzeri → AA
    print("AA")
elif puan >= 80:     # 80-89 arası → BA  (90'dan küçük olduğunu zaten biliyoruz)
    print("BA")
elif puan >= 70:     # 70-79 arası → BB
    print("BB")
elif puan >= 60:     # 60-69 arası → CB
    print("CB")
elif puan >= 50:     # 50-59 arası → DC
    print("DC")
elif puan >= 40:     # 40-49 arası → DD
    print("DD")
else:                # 40'tan küçük → F
    print("F")

# Bu satır koşuldan bağımsız, her durumda çalışır.
print("Başarılar!")
