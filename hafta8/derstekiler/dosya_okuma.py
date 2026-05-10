# Konu: Metin dosyası okuma (dosya işlemleri - temel)
# ----------------------------------------------------
# Bu örnek bir metin dosyasının (renkler.txt) içeriğini iki farklı yöntemle okur:
#   1) "with open(...) as dosya:" — bağlam yöneticisi (context manager) kullanır.
#      Bu yöntem dosyayı otomatik olarak kapatır; tercih edilen yoldur.
#   2) "open(...)" — dosyayı manuel açar, fakat close() çağrılmadığı için
#      dosya sızıntısına (file leak) yol açar. Karşılaştırma amaçlıdır, kullanılmamalıdır.
# encoding="utf-8" parametresi Türkçe karakterlerin doğru okunmasını sağlar.

with open("renkler.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)

dosya = open("renkler.txt")
icerik = dosya.read()
print(icerik)