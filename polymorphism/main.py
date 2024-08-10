class Personel:
    def __init__(kisi, ad, soyad, gorev, calismaSuresi):
        kisi.ad = ad
        kisi.soyad = soyad
        kisi.gorev = gorev
        kisi.calismaSuresi = calismaSuresi

    def maasHesapla(kisi):
        asgariUcret = 2324
        kidemKatsayisi = kisi.calismaSuresi * 0.01
        maas = asgariUcret + (asgariUcret * kidemKatsayisi)
        return maas

    def veriYazdir(kisi):
        print("Personelin Adı-Soyadı: ", kisi.ad, kisi.soyad)
        print("Görevi: ", kisi.gorev)
        print("Kurumda Çalışma Süresi: ", kisi.calismaSuresi)
        print("Aldığı Ücret: ")


class Calisan(Personel):
    pass


class Yonetici(Personel):
    def maasHesapla(kisi):
        asgariUcret = 2324
        kidemKatsayisi = kisi.calismaSuresi * 0.01
        if kisi.gorev == "Mühendis":
            unvanKatsayisi = 0.25
        elif kisi.gorev == "Üretim Müdürü":
            unvanKatsayisi = 1.25
        maas = (3 * asgariUcret) + (asgariUcret * kidemKatsayisi) + (asgariUcret * unvanKatsayisi)
        return maas


personel1 = Calisan("Ahmet", "Yılmaz", "İşçi", 4)
personel2 = Calisan("Veli", "Kocaman", "İşçi", 9)
personel3 = Calisan("Hasan", "Karadağ", "Ustabaşı", 13)
personel4 = Yonetici("Tamer", "Doğrusöz", "Mühendis", 8)
personel5 = Yonetici("Serdar", "Deveci", "Üretim Müdürü", 5)

personel1.veriYazdir()
print(personel1.maasHesapla())
print()
print()
personel2.veriYazdir()
print(personel2.maasHesapla())
print()
print()
personel3.veriYazdir()
print(personel3.maasHesapla())
print()
print()
personel4.veriYazdir()
print(personel4.maasHesapla())
print()
print()
personel5.veriYazdir()
print(personel5.maasHesapla())