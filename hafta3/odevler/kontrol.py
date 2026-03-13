# =============================================================
# Odev Kontrol Araci
# =============================================================
# Bu programi calistirarak odevlerindeki hatalari
# gonderim oncesinde gorebilirsin.
#
# Kullanim:
#   python3 kontrol.py                  (tum odevleri kontrol et)
#   python3 kontrol.py odev01_liste_temel.py   (tek dosya kontrol et)
# =============================================================

import ast
import sys
import os
import tokenize
import io


def satirlari_oku(dosya_adi):
    """Dosyayi okur, satirlari ve tam icerigi dondurur."""
    with open(dosya_adi, "r", encoding="utf-8") as f:
        icerik = f.read()
    return icerik, icerik.splitlines()


def sozdizimi_kontrol(dosya_adi, icerik):
    """ast.parse ile sozdizimi hatalarini yakalar."""
    try:
        tree = ast.parse(icerik, filename=dosya_adi)
        return tree, []
    except SyntaxError as e:
        satir = e.lineno if e.lineno else "?"
        mesaj = e.msg if e.msg else "Bilinmeyen sozdizimi hatasi"
        return None, [
            (satir, "HATA", f"Sozdizimi hatasi (SyntaxError): {mesaj}")
        ]


def ellipsis_kontrol(tree, satirlar):
    """AST uzerinde ... (Ellipsis) yer tutucularini arar."""
    sorunlar = []
    if tree is None:
        # AST yoksa ham metinde ara
        for i, satir in enumerate(satirlar, 1):
            temiz = satir.split("#")[0].strip()  # yorumlari cikar
            if temiz == "..." or temiz == "...,":
                sorunlar.append(
                    (i, "EKSIK", "Bu satirdaki ... yer tutucusu doldurulmamis")
                )
        return sorunlar

    for node in ast.walk(tree):
        # ... tek basina bir ifade olarak (ornegin satirda sadece ... var)
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
            if node.value.value is ...:
                sorunlar.append(
                    (node.lineno, "EKSIK",
                     "Bu satirdaki ... yer tutucusu doldurulmamis")
                )

        # ... bir fonksiyon argumani olarak (ornegin print(...), range(...))
        if isinstance(node, ast.Call):
            for arg in node.args:
                if isinstance(arg, ast.Constant) and arg.value is ...:
                    sorunlar.append(
                        (arg.lineno, "EKSIK",
                         "Fonksiyon icindeki ... yer tutucusu doldurulmamis "
                         "(degisken veya ifade yaz)")
                    )
            for kw in node.keywords:
                if isinstance(kw.value, ast.Constant) and kw.value.value is ...:
                    sorunlar.append(
                        (kw.value.lineno, "EKSIK",
                         "Fonksiyon icindeki ... yer tutucusu doldurulmamis")
                    )

        # ... bir atamada (ornegin degisken = ...)
        if isinstance(node, ast.Assign):
            if isinstance(node.value, ast.Constant) and node.value.value is ...:
                hedefler = []
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        hedefler.append(t.id)
                isim = ", ".join(hedefler) if hedefler else "degisken"
                sorunlar.append(
                    (node.lineno, "EKSIK",
                     f"'{isim}' degiskenine deger atanmamis (... yerine ifade yaz)")
                )

    return sorunlar


def string_placeholder_kontrol(tree):
    """'...' string yer tutucularini arar."""
    sorunlar = []
    if tree is None:
        return sorunlar

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and node.value == "...":
            sorunlar.append(
                (node.lineno, "UYARI",
                 '"..." metni bulundu — yer tutucu olarak kalmis olabilir')
            )

    return sorunlar


def tip_kontrol(tree):
    """Degisken tiplerinde yaygin hatalari arar."""
    sorunlar = []
    if tree is None:
        return sorunlar

    # Yorumlardaki tip ipuclarini kullanamayiz, ama yaygin degisken isimlerini kontrol edebiliriz
    sayi_olmasi_gereken = {"yas", "puan", "not_ortalamasi", "poster_genisligi",
                          "maksimum_genislik", "proje_sayisi", "deneme",
                          "toplam", "ortalama", "genislik", "sayac"}

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for hedef in node.targets:
                if isinstance(hedef, ast.Name) and hedef.id in sayi_olmasi_gereken:
                    if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                        sorunlar.append(
                            (node.lineno, "UYARI",
                             f"'{hedef.id}' degiskeni sayi (int/float) olmali, "
                             f"ama metin (string) olarak tanimlanmis: \"{node.value.value}\"")
                        )

    return sorunlar


def degisken_kullanim_kontrol(tree, satirlar):
    """Tanimlanmamis degisken kullanimini tespit etmeye calisir."""
    sorunlar = []
    if tree is None:
        return sorunlar

    # Basit kontrol: atanan degisken isimleri ile kullanilan isimleri karsilastir
    # (Python built-in ve import'lari haric)
    builtin_isimler = {
        "print", "input", "int", "float", "str", "len", "range", "enumerate",
        "True", "False", "None", "list", "dict", "tuple", "set", "type",
        "abs", "max", "min", "sum", "round", "sorted", "reversed", "zip",
        "map", "filter", "bool", "open", "super", "isinstance", "hasattr",
    }

    tanimli = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    tanimli.add(t.id)
        elif isinstance(node, ast.For):
            if isinstance(node.target, ast.Name):
                tanimli.add(node.target.id)
            elif isinstance(node.target, ast.Tuple):
                for elt in node.target.elts:
                    if isinstance(elt, ast.Name):
                        tanimli.add(elt.id)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                tanimli.add(alias.asname or alias.name)
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                tanimli.add(alias.asname or alias.name)

    # Fonksiyon argumanlari ve call icindeki Name'leri kontrol et
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            for arg in node.args:
                if isinstance(arg, ast.Name):
                    if arg.id not in tanimli and arg.id not in builtin_isimler:
                        # Satin icerigin kontrol et — yorum satiri mi?
                        satir_no = arg.lineno
                        if satir_no <= len(satirlar):
                            satir = satirlar[satir_no - 1]
                            kod_kismi = satir.split("#")[0]
                            if arg.id in kod_kismi:
                                sorunlar.append(
                                    (satir_no, "UYARI",
                                     f"'{arg.id}' tanimlanmamis bir isim — "
                                     f"degisken adi mi yoksa deger mi yazmak istedin? "
                                     f"Eger metin ise tirnak icine al: \"{arg.id}\"")
                                )

    return sorunlar


def dosya_kontrol(dosya_adi):
    """Tek bir dosyayi tum kontrollerden gecirir."""
    print(f"\n{'=' * 50}")
    print(f"  {dosya_adi}")
    print(f"{'=' * 50}")

    if not os.path.exists(dosya_adi):
        print("  HATA: Dosya bulunamadi!")
        return False

    icerik, satirlar = satirlari_oku(dosya_adi)

    # Bos dosya kontrolu
    if not icerik.strip():
        print("  HATA: Dosya bos!")
        return False

    tum_sorunlar = []

    # 1. Sozdizimi kontrolu
    tree, syntax_sorunlar = sozdizimi_kontrol(dosya_adi, icerik)
    tum_sorunlar.extend(syntax_sorunlar)

    # 2. Ellipsis (...) kontrolu
    tum_sorunlar.extend(ellipsis_kontrol(tree, satirlar))

    # 3. "..." string placeholder kontrolu
    tum_sorunlar.extend(string_placeholder_kontrol(tree))

    # 4. Degisken tipi kontrolu
    tum_sorunlar.extend(tip_kontrol(tree))

    # 5. Tanimlanmamis degisken kontrolu
    tum_sorunlar.extend(degisken_kullanim_kontrol(tree, satirlar))

    # Sonuclari yazdir
    if not tum_sorunlar:
        print("  TAMAM: Belirgin bir sorun bulunamadi!")
        print()
        print("  Simdi kodunu calistirip ciktisini kontrol et:")
        print(f"    python3 {dosya_adi}")
        print("  Ciktiyi dosyanin sonundaki 'Beklenen Cikti' ile karsilastir.")
        return True

    # Satirlara gore sirala
    tum_sorunlar.sort(key=lambda x: (x[0] if isinstance(x[0], int) else 0))

    hata_sayisi = sum(1 for s in tum_sorunlar if s[1] == "HATA")
    eksik_sayisi = sum(1 for s in tum_sorunlar if s[1] == "EKSIK")
    uyari_sayisi = sum(1 for s in tum_sorunlar if s[1] == "UYARI")

    for satir, tur, mesaj in tum_sorunlar:
        if tur == "HATA":
            isaret = "[X]"
        elif tur == "EKSIK":
            isaret = "[?]"
        else:
            isaret = "[!]"

        print(f"  {isaret} Satir {satir}: {mesaj}")

        # Ilgili satiri goster
        if isinstance(satir, int) and 1 <= satir <= len(satirlar):
            print(f"       | {satirlar[satir - 1]}")
        print()

    # Ozet
    print(f"  --- Ozet ---")
    if hata_sayisi:
        print(f"  [X] {hata_sayisi} hata (kod calisMAZ, duzeltmen gerekiyor)")
    if eksik_sayisi:
        print(f"  [?] {eksik_sayisi} eksik (... yer tutucusu doldurulmamis)")
    if uyari_sayisi:
        print(f"  [!] {uyari_sayisi} uyari (olasi sorun, kontrol et)")

    return False


def main():
    print()
    print("  ODEV KONTROL ARACI")
    print("  Gonderim oncesi hata tarayicisi")
    print()

    # Kontrol edilecek dosyalari belirle
    if len(sys.argv) > 1:
        # Kullanici belirli dosyalar verdi
        dosyalar = sys.argv[1:]
    else:
        # Ayni dizindeki odev dosyalarini bul
        dizin = os.path.dirname(os.path.abspath(__file__))
        dosyalar = sorted([
            f for f in os.listdir(dizin)
            if f.startswith("odev") and f.endswith(".py")
        ])
        if not dosyalar:
            print("  Odev dosyasi bulunamadi!")
            print("  Bu dosyayi odev dosyalariyla ayni klasore koy.")
            sys.exit(1)

        # Dosya yollarini duzelt
        dosyalar = [os.path.join(dizin, f) for f in dosyalar]

    print(f"  {len(dosyalar)} dosya kontrol edilecek...")

    basarili = 0
    toplam = len(dosyalar)

    for dosya in dosyalar:
        if dosya_kontrol(dosya):
            basarili += 1

    # Genel sonuc
    print()
    print("=" * 50)
    print(f"  SONUC: {basarili}/{toplam} dosya sorunsuz")
    print("=" * 50)

    if basarili == toplam:
        print()
        print("  Harika! Tum dosyalar temel kontrollerden gecti.")
        print("  Simdi her dosyayi tek tek calistir ve ciktilari kontrol et.")
        print()
    else:
        print()
        print("  Bazi dosyalarda sorunlar var.")
        print("  Yukardaki mesajlari okuyarak duzeltmeleri yap,")
        print("  sonra bu programi tekrar calistir.")
        print()

    sys.exit(0 if basarili == toplam else 1)


if __name__ == "__main__":
    main()
