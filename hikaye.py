"""
dai.4546b
Copyright (c) 2025 Burak Demiröz

This source code is licensed under the MIT License.
See the LICENSE file for details.
"""

def oyun_baslangici():
    print("=== DAI.4546B ===")
    print("Yıl 2102. DAI şirketinde çalışan bir mürettebatsınız.")
    print("Uzay geminiz, gezegene yaklaşırken saldırıya uğruyor!")
    print("Gemi vuruluyor ve hızla düşüyor...")
    print("Hayatta kalmak için kaçış kapsülüne atlıyorsunuz.")
    print("Kapsül gezegene çarpıyor ve bilinmeyen bir yerde açılıyor.")
    print()

    print("Ne yapmak istersiniz?")
    print("1) Etrafı keşfetmek")
    print("2) Kapsülün içini incelemek")
    print("3) Bağlantı cihazınızı kontrol etmek")

    secim = input("Seçiminiz (1/2/3): ")

    if secim == "1":
        print("\nDışarı çıkıp etrafı keşfetmeye karar verdiniz.")
        print("Ucsuz Bucaksız Bir Okyonusun Ortasındasın, ancak bir DAI ait Keşif Gemisini görülebiliyor uzakta.")
    elif secim == "2":
        print("\nKapsülün içini incelediniz ve bazı yararlı ekipmanlar buldunuz.")
        print("Biraz yemek ve su var. Birde Bilgisayarın var.")
    elif secim == "3":
        print("\nBağlantı cihazınızı açtınız ancak sinyal zyok ve bozulmuş galiba.")
        print("Kendi başınıza hareket etmeniz gerekiyor.")
    else:
        print("\nGeçersiz seçim. Lütfen 1, 2 ya da 3 yazınız.")
        oyun_baslangici()

if __name__ == "__main__":
    oyun_baslangici()
