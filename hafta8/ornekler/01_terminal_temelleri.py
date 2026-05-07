# =============================================================
# DERS 1: Terminal Temelleri (Rehber)
# =============================================================
# Bu dosya çalıştırmak için DEĞİL, okumak için yazılmıştır.
# İçindeki komutları SİZİN terminalde denemeniz gereklidir.
#
# Bu derste öğreneceğiz:
#   - Terminal nedir, nasıl açılır
#   - pwd, ls, cd komutları (Mac/Linux ve Windows)
#   - Bir Python dosyasını terminalden çalıştırma
#   - Göreli ve mutlak yol
# =============================================================


# --- Sorun: Dosyalar Nerede? ---
# Bir tasarım dosyasını "Documents/Projeler/Logo" klasöründe
# tuttuğunuzu düşünün. Hangi klasörde olduğunuzu, dosyaların
# orada olup olmadığını bilmek istersiniz.
#
# Terminal de aynı şeyi yazıyla yapar:
#   - Şu an hangi klasördeyim? (pwd)
#   - Bu klasörde ne var? (ls)
#   - Başka bir klasöre git (cd)


# --- Terminal Nasıl Açılır? ---
#
# YÖNTEM 1 — VS Code içinden:
#   Üst menü → Terminal → New Terminal
#
# YÖNTEM 2 — Bilgisayarınızdan:
#   macOS:    Spotlight'a "Terminal" yazın
#   Windows:  Başlat'a "PowerShell" yazın
#   Linux:    Ctrl+Alt+T


# --- Üç Komut: pwd, ls, cd ---
#
# pwd: print working directory (bulunduğun klasörü yazdır)
#
#   Mac / Linux:
#     $ pwd
#     /Users/defne/Documents/gita2112
#
#   Windows (PowerShell):
#     PS> pwd
#     C:\Users\Defne\Documents\gita2112
#
#   Windows (cmd):
#     > cd
#     C:\Users\Defne\Documents\gita2112
#
# ----------------------------------------
#
# ls: list (klasördeki dosyaları listele)
#
#   Mac / Linux:
#     $ ls
#     hafta1  hafta2  hafta3  ...
#
#   Windows:
#     > dir
#     hafta1  hafta2  hafta3  ...
#
# ----------------------------------------
#
# cd: change directory (klasör değiştir)
#
#   $ cd hafta8           # hafta8 klasörüne gir
#   $ cd ornekler         # bir alt klasör daha
#   $ cd ..               # bir üst klasöre çık
#   $ cd                  # ev klasörüne git (Mac/Linux)
#   $ cd ~/Documents      # ev klasörü altındaki Documents'e


# --- Bir Python Dosyası Çalıştırma ---
#
# 1. Dosyanın bulunduğu klasöre gidin (cd)
# 2. python3 dosya_adi.py yazın
#
# Örnek (Mac/Linux):
#   $ cd ~/Documents/gita2112/hafta8/ornekler
#   $ python3 03_dosya_okuma.py
#
# Örnek (Windows):
#   > cd C:\Users\Defne\Documents\gita2112\hafta8\ornekler
#   > python 03_dosya_okuma.py
#
# Mac/Linux'ta python3, Windows'ta genelde python yazılır.
# Sisteminizde hangisi çalışıyorsa onu kullanın.


# --- Göreli ve Mutlak Yol ---
#
# Bir dosyaya iki türlü işaret edebilirsiniz:
#
# MUTLAK YOL — bilgisayarın en üstünden başlar:
#   /Users/defne/Documents/gita2112/hafta8/renkler.txt
#   C:\Users\Defne\Documents\gita2112\hafta8\renkler.txt
#
# GÖRELİ YOL — şu an bulunduğunuz yere göre:
#   renkler.txt              (aynı klasörde)
#   veri/renkler.txt         (alt klasörde)
#   ../renkler.txt           (bir üst klasörde)
#
# Python kodlarımızda göreli yolu sıkça kullanacağız.
# AMA: Terminalin nerede açıldığı önemlidir.
# pwd komutuyla her zaman kontrol edebilirsiniz.


# --- Sık Yapılan Hatalar ---
#
# 1. Dosya bulunamadı?
#    pwd ile bulunduğunuz klasörü kontrol edin.
#    ls / dir ile dosyanın orada olup olmadığını görün.
#
# 2. cd komutu çalışmadı?
#    Yazdığınız klasör adı doğru mu? Büyük/küçük harf önemlidir
#    (özellikle Mac/Linux'ta).
#
# 3. python3: command not found?
#    Mac'te python3 olmalı. Windows'ta python yazın.
#    Hala olmuyorsa Python sisteme kurulmamış olabilir.


# --- Mini Alıştırma (kendi terminalinizde) ---
#
# Şu komutları sırayla çalıştırın:
#
#   pwd                         # nerede olduğumu göster
#   ls                          # klasörde ne var
#   cd Documents                # Documents'e gir
#   pwd                         # tekrar nerede olduğumu göster
#   cd ..                       # bir üst klasöre dön
#   pwd                         # son durumum
#
# Bu sırayı 2-3 kez deneyin, refleks olsun.


# --- Bu Dosyayı Çalıştırırsanız ---
print("Bu dosya bir rehberdir, gerçek kod içermez.")
print("Yorum satırlarındaki komutları kendi terminalinizde deneyin.")
print()
print("Sıradaki dosya: 02_uv_kullanimi.py")
