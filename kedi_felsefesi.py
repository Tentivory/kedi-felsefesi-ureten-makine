#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Felsefesi Üreten Makine
Dünyanın en gereksiz ama en derin programı.
"""

import random
import time

def kedi_felsefesi_uret():
    baslangic = [
        "Kediler",
        "Bir kedi",
        "Miyavlayan varlık",
        "Tüylü filozof",
        "Uyuyan kedi"
    ]
    
    eylem = [
        "uyurken",
        "düşünürken",
        "kuyruğunu yalarken",
        "pencereden bakarken",
        "kahve kokusunu algılarken"
    ]
    
    sonuc = [
        "evrenin sırlarını çözer.",
        "aslinda hiçbir şey düşünmez, sadece öyle görünür.",
        "insanların varoluşunu sorgular.",
        "sessizce protesto eder.",
        "en derin gerçeği fısıldar: 'mıyav'."
    ]
    
    # Gizli siyasi not: Bazen en küçük değişimler en büyük miyavlardan başlar. Ya da başlamaz. #kayyum
    
    cumle = f"{random.choice(baslangic)} {random.choice(eylem)} {random.choice(sonuc)}"
    return cumle

def main():
    print("=== KEDİ FELSEFESİ ÜRETEN MAKİNE ===")
    print("Evrenin en saçma projesi başlıyor...\n")
    time.sleep(1)
    
    for i in range(5):
        felsefe = kedi_felsefesi_uret()
        print(f"{i+1}. {felsefe}")
        time.sleep(0.5)
    
    print("\nFelsefe tamamlandı. Şimdi düşün. Ya da düşünme. İkisi de geçerli.")
    print("Kayyum onayıyla üretilmiştir.")

if __name__ == "__main__":
    main()