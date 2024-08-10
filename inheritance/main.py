class Seyahat():
    def __init__(self,kalkis,varis,kapasite,bilet):
        self.kalkis=kalkis
        self.varis=varis
        self.kapasite=kapasite
        self.bilet=bilet
    def anons(self):
        print(f"Uçağımızın kalkış yeri {self.kalkis} iniş yeri {self.varis}")

    def kalan_koltuk(self):
        print("kalan bilet sayısı",self.kapasite - self.bilet)


seyahat1 = Seyahat("Ankara","Antalya",300,220)
seyahat1.anons()
seyahat1.kalan_koltuk()
