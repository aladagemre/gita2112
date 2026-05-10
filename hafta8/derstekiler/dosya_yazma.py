# Konu: Metin dosyasına yazma
# ----------------------------
# Bu örnek bir liste içeriğini bir metin dosyasına satır satır yazar.
# - "w" modu: dosya yoksa oluşturur, varsa içeriğini SİLER ve baştan yazar.
#   (Eklemek için "a" modu kullanılır.)
# - dosya.write() satır sonunu otomatik eklemez; bu yüzden manuel olarak "\n" ekledik.
# - with bloğu sayesinde yazma bitince dosya otomatik kapanır ve disk'e flush edilir.

renkler = ["kırmızı", "mavi", "turuncu"]
with open("yeni_palet.txt", "w", encoding="utf-8") as dosya:
    for renk in renkler:
        dosya.write(renk + "\n")