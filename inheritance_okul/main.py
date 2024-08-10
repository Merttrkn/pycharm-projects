class School():
    def __init__(self,kidem,ad,soyad):
        self.kidem=kidem
        self.ad=ad
        self.soyad=soyad

class Student(School):
    def __init__(self,kidem,ad,soyad,sube):
        super().__init__(kidem,ad,soyad)
        self.sube = sube
    def ogr_bilgi(self):
        print(f"Yeni kaydın adı: {self.ad} soyad: {self.soyad} ve mesleği {self.kidem} şubesi {self.sube}")
class Teacher(School):
    def __init__(self,kidem,ad,soyad,maas):
        super().__init__(kidem,ad,soyad)
        self.maas = maas
    def teach_info(self):
        print(f"Yeni öğretmenin adı: {self.ad} soyad: {self.soyad} ve mesleği {self.kidem} maaşı {self.maas}")

ogr1 = Student("öğrenci","mert","türkan","C Şubesi")
teach1 = Teacher("öğretmen","ayhan" ,"sarıkaya", 10000)
Student.ogr_bilgi(ogr1)
Teacher.teach_info(teach1)

