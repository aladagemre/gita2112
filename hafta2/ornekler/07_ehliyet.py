# =============================================================
# DERS 7: Boolean Değişkenler ve İç İçe if Yapısı
# =============================================================
# Bu derste öğreneceğiz:
#   - Boolean (True/False) veri tipi
#   - Karşılaştırma sonucunu değişkende saklama
#   - and ile boolean değişkenleri birleştirme
#   - İç içe (nested) if yapısı


# =============================================================
# ÖRNEK 1: Basit Yaş Kontrolü
# =============================================================
# Tek bir koşul: yaş 18'den büyük mü?

yas = int(input("Kaç yaşındasın? "))

if yas >= 18:
    print("Ehliyet alabilirsiniz!")
    print("Haydi, ne bekliyorsun? Ehliyet sınavına çalışmaya başlayalım!")
else:
    # 18 - yas ifadesi kaç yıl kaldığını hesaplar
    print("Maalesef ehliyet alamazsınız. Daha", 18 - yas, "yıl beklemeniz gerekiyor.")
    print("İşin iş...")

print("iyi günler!")


# =============================================================
# ÖRNEK 2: Boolean Değişkenler
# =============================================================
# Karşılaştırma işlemleri (>=, ==, !=, <, >) sonuç olarak
# True veya False değeri üretir. Bu değerleri değişkende saklayabiliriz.
# Bu tür değişkenlere "boolean değişken" denir.

yas = int(input("Yaşınız:"))  # Örnek: 20
ehliyet = input("Ehliyetiniz var mı? e/h")  # Örnek: "e"

resit_mi = yas >= 18       # yas 18'den büyükse True, değilse False
ehliyet_var_mi = ehliyet == "e"  # kullanıcı "e" girdiyse True, değilse False

# Aşağıdaki iki satır tamamen aynı sonucu verir:
# if yas >= 18 and ehliyet == "e":   ← doğrudan karşılaştırma
# if resit_mi and ehliyet_var_mi:    ← boolean değişken kullanımı (daha okunabilir)

if resit_mi and ehliyet_var_mi:
    print("İşe alındınız!")
else:
    # Bu blok şu durumlarda çalışır:
    # - Yaş uygun ama ehliyet yok
    # - Ehliyet var ama yaş uygun değil
    # - Her ikisi de uygun değil
    print("Koşulları sağlamıyorsunuz")


# =============================================================
# ÖRNEK 3: İç İçe (Nested) if
# =============================================================
# Bir if bloğunun içine başka bir if yazılabilir.
# Dıştaki koşul sağlanırsa içteki koşul kontrol edilir.

yas = int(input("Yaşınız:"))

if yas >= 18:
    # Bu blok sadece yaş >= 18 olduğunda çalışır
    ehliyet = input("Ehliyetiniz var mı? e/h")

    if ehliyet == "e":      # iç if: ehliyet var mı?
        print("İşe alındın!")
    else:
        print("Ehliyet olmadan olmaz")
else:
    # yaş < 18 ise direkt buraya atlanır, ehliyet sorusu sorulmaz
    print("Yaşın çok küçük")
