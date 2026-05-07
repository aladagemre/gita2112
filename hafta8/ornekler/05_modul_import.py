# =============================================================
# DERS 5: import ve Modül Kavramı
# =============================================================
# Bu derste öğreneceğiz:
#   - import nedir, ne yapar
#   - Standart kütüphane modülleri turu
#   - math, random, datetime, os ile küçük örnekler
#   - import'un üç yazılış şekli
# =============================================================


# --- Sorun: Python Tek Başına Yetmez ---
#
# Python'un yerleşik dünyasında print, for, if, len, range
# gibi temel yapılar var. Ama:
#
#   - Karekök hesaplamak istiyorsanız?
#   - Rastgele bir renk seçmek istiyorsanız?
#   - Bugünün tarihini almak istiyorsanız?
#   - Bir klasördeki dosyaları listelemek istiyorsanız?
#
# Bunlar için MODÜL denilen ek paketler vardır.
# Hepsi Python ile birlikte ücretsiz gelir, sadece import'la
# etkinleştirmeniz gerekir.


# --- Modül = Photoshop'a Plugin Yüklemek ---
#
# Photoshop ilk kurulduğunda temel araçları getirir.
# Bir plugin kurarsanız ek özellikler açılır.
# Modüller de aynen öyledir: import yazınca ek yetenek açılır.


# --- import'un Üç Yazılış Şekli ---

# 1. En temiz — modül adıyla erişim:
import math

# 2. Sadece bir parçayı al:
from random import choice, randint

# 3. Kısa ad ver (çok kullanılan modüllerde):
import datetime as dt


print("=== Modül Kullanım Örnekleri ===")
print()


# --- math Modülü ---
#
# Matematik fonksiyonları: karekök, pi, yuvarlama, vb.

print("--- 1. math modülü ---")

print(f"math.pi = {math.pi}")
print(f"math.sqrt(64) = {math.sqrt(64)}")
print(f"math.ceil(4.2) = {math.ceil(4.2)}")     # yukarı yuvarla
print(f"math.floor(4.8) = {math.floor(4.8)}")    # aşağı yuvarla
print()

# Tasarım örneği: bir dairesel logonun çevresi
yaricap = 25  # cm
cevre = 2 * math.pi * yaricap
print(f"25 cm yarıçaplı dairenin çevresi: {cevre:.2f} cm")
print()


# --- random Modülü ---
#
# Rastgelelik üretmek. Kreatif kodlamada çok kullanışlı.

print("--- 2. random modülü ---")

renkler = ["Mercan", "Lacivert", "Sarı", "Turuncu", "Mor"]

# Listeden rastgele bir tane seç:
secilen = choice(renkler)
print(f"Bugünün rengi: {secilen}")

# Belirli bir aralıkta rastgele tam sayı:
sayi = randint(1, 100)
print(f"Rastgele sayı (1-100): {sayi}")

# Rastgele HEX renk üretelim — randint'i yine kullanıyoruz:
hex_renk = "#{:06X}".format(randint(0, 0xFFFFFF))
print(f"Rastgele HEX: {hex_renk}")
print()


# --- datetime Modülü ---
#
# Tarih ve zaman işlemleri.

print("--- 3. datetime modülü ---")

bugun = dt.date.today()
print(f"Bugün: {bugun}")

simdi = dt.datetime.now()
print(f"Şu anki zaman: {simdi}")

# Daha okunaklı format:
print(f"Tarih: {bugun.strftime('%d %B %Y')}")
print()

# Tasarım örneği: bir poster dosyası adı oluştur
proje_adi = "caz_festivali"
dosya_adi = f"{proje_adi}_{bugun}.psd"
print(f"Önerilen dosya adı: {dosya_adi}")
print()


# --- os Modülü ---
#
# İşletim sistemi işlemleri: klasör listeleme, yol birleştirme.

import os

print("--- 4. os modülü ---")

# Şu anki klasör:
print(f"Şu anki klasör: {os.getcwd()}")

# veri/ klasöründeki dosyalar:
veri_dosyalari = os.listdir("veri")
print(f"veri/ klasöründekiler: {veri_dosyalari}")
print()


# --- import'u Nereye Koymalı? ---
#
# Tüm import ifadeleri DOSYANIN EN BAŞINDA olmalıdır.
# Yukarıda biz öğretici amaçla yer yer middle'a koyduk
# ama gerçek projelerde her zaman en başta olur.
#
# DOĞRU:
# ──────────────
# import math
# import random
# import json
#
# def hesapla():
#     ...
#
# YANLIŞ ALIŞKANLIK (çalışır ama dağınık):
# ──────────────
# def hesapla():
#     import math
#     ...


# --- import vs from ... import Farkı ---
#
# import math:
#   math.sqrt(64)        ← her zaman "math." önekiyle
#   math.pi              ← nereden geldiği belli
#
# from math import sqrt, pi:
#   sqrt(64)             ← önek yok, kısa ama
#   pi                   ← bu "pi" math'ten mi geldi anlaşılmaz
#
# Önerimiz: ŞİMDİLİK her zaman birinci yöntemi kullanın.
# Kodunuz daha okunabilir olur.


# --- Sık Karşılaşılan Hatalar ---
#
# 1. ModuleNotFoundError: No module named 'pillow'
#    → Standart kütüphane DEĞİL. uv add pillow ile kurun.
#
# 2. AttributeError: module 'random' has no attribute 'piick'
#    → Yazım hatası. random.pick yok, random.choice var.
#
# 3. NameError: name 'sqrt' is not defined
#    → from math import sqrt yapmadınız ya da import math ile
#      math.sqrt(...) yazmanız gerekiyor.


# --- Bu Hafta Sıkça Kullanacaklarımız ---
print("--- Sık kullanacağımız modüller ---")
print("import csv     → CSV dosyaları")
print("import json    → JSON dosyaları")
print("import math    → matematik fonksiyonları")
print("import random  → rastgelelik")
print("import os      → klasör/dosya işlemleri")
