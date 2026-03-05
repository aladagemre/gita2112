# =============================================================
# DERS 1: Listeler — Temel Kavramlar
# =============================================================
# Bu derste öğreneceğiz:
#   - Liste oluşturma []
#   - Elemanlara indeksle erişim [0], [-1]
#   - len() ile liste uzunluğu
#   - Liste içinde farklı veri tipleri


# --- Liste Oluşturma ---
# Liste, birden fazla değeri tek bir değişkende saklar.
# Köşeli parantez [] ile oluşturulur, elemanlar virgülle ayrılır.

renkler = ["kırmızı", "mavi", "yeşil", "sarı"]
print("Renk paletim:", renkler)


# --- İndeksle Erişim ---
# Her elemanın bir sıra numarası (indeks) vardır.
# İndeksler 0'dan başlar!
#
#   indeks:   0          1        2        3
#   renkler: ["kırmızı", "mavi", "yeşil", "sarı"]

print("İlk renk:", renkler[0])       # kırmızı
print("İkinci renk:", renkler[1])     # mavi
print("Üçüncü renk:", renkler[2])     # yeşil


# --- Negatif İndeks ---
# -1 son eleman, -2 sondan ikinci...
print("Son renk:", renkler[-1])       # sarı
print("Sondan ikinci:", renkler[-2])  # yeşil


# --- len() ile Uzunluk ---
# len() listenin kaç elemanlı olduğunu söyler.
print("Paletteki renk sayısı:", len(renkler))  # 4


# --- Farklı Veri Tipleri ---
# Bir liste farklı türde veriler içerebilir (ama genelde aynı türde tutarız).
# True → boolean (Hafta 2'de gördüğümüz True/False değerleri)
karisik = ["Logo Tasarımı", 2024, True, 4.5]
print("Karışık liste:", karisik)
print("Proje adı:", karisik[0])
print("Yıl:", karisik[1])
