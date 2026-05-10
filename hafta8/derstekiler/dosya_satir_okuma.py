# Konu: Dosyayı satır satır okuma + enumerate
# --------------------------------------------
# Bu örnek bir metin dosyasını döngü ile satır satır gezer.
# - Dosya nesnesi (dosya) doğrudan iter edilebilir; her döngü adımında bir satır gelir.
# - enumerate() satırları sıraya koyar ve (indeks, satır) tuple'ı döndürür.
#   i+1 yazmamızın nedeni indekslerin 0'dan başlamasıdır; biz 1'den göstermek istiyoruz.
# - satir.strip() satır sonundaki "\n" karakterini ve boşlukları temizler.
# - f-string içinde <...> kullanmak satır kenarlarındaki gizli boşlukları görmeyi sağlar.

with open("renkler.txt", "r", encoding="utf-8") as dosya:
    for i, satir in enumerate(dosya):
        print(f"{i+1}: <{satir.strip()}>")