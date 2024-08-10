import PyQt5
import numpy


def my_function():
  print("Hello from a function")

my_function()"""

"""def Ulke(fname):
    print(fname + " " + "Türkiye")
Ulke("Ankara")
Ulke("İstanbul")
Ulke ("İzmir")

def children(child1,child2,child3):
    print("En büyük çocuk"+" " + child1)
children(child1="Ahmet",child2="Mehmet",child3="Mert")

def ornek(*k):
    print("Bugünün hava durumu" +" "+ k[1])
ornek("yağmurlu" ,"karlı" ,"güneşli")


def my_function(country="Türkiye"):
    print("I am from " + country)
my_function("Amerika")
my_function("Hindistan")
my_function("Rusya")
my_function()

def ıslem(x):
    return 7 * x
print(ıslem(1))
print(ıslem(13))
print(ıslem(5))
print(ıslem(9))

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
print("---------------------------------------------------")

x= lambda a,b,c:3*6*9
print(x(3,6,9))

sayilar = [*range(1,6)]
list(map(lambda sayi:sayi**2,sayilar))
print("--------------------------------------------------------------")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print("----------------------------------------------------")

"""birinci_sayi = int(input("birinci sayıyı giriniz:"))
ikinci_sayi = int (input("ikinci sayıyı giriniz:"))
print(f"iki sayının toplamı {birinci_sayi + ikinci_sayi} eder")
print(f"iki sayının çarpımı {birinci_sayi * ikinci_sayi} eder")
print(f"iki sayının farkı {birinci_sayi - ikinci_sayi} eder")
print(f"iki sayının bölümü {birinci_sayi / ikinci_sayi} eder")"""
print("------------------------------------")

"""class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def __str__(self):
    return f"{self.name},{self.age}"
p1=Person("Mert",21)
p2=Person("Nazım",34)
print(p1.name)
print(p2.age)
print(p1,p2)"""

class Best:
  def __init__(self,boy,kilo):
    self.boy = boy
    self.kilo = kilo
  def bilgi(self):
    print("bu adamın boyu" ,self.boy ,"cm ve kilosu" ,self.kilo ,"kg")
p1=Best(176,80)
p1.bilgi()

print("------------------------------------------")

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("MERT", 36)
p1.myfunc()
print("-------------------------------------")

class Person():
  def __init__(self,fname,lname):
    self.firstname=fname
    self.lastname=lname
  def printname(self):
    print(self.fname , self.lname)
class Student(Person):
  def __init__(self,fname,lname,age):
    super().__init__(fname,lname)
    self.year=age
  def tanitim(self):
    print("kaydı yapılacak kişinin adı ",self.firstname,"soyadı",self.lastname,"yaşı da",self.year)
kisi=Student("mert","türkan",90)
kisi.tanitim()

print("----------------------------------------")
def tanimlama():
  global x
  x=300
tanimlama()
print(x)
print("---------------------------------")

import datetime
x=datetime.datetime.now()
print(x)



"""try:
  username = int(input("kullanıcı adını giriniz:"))

  print("kullanıcı adı:" + username)
except Exception as e:
  print(e)
  print("geçersiz kullanıcı")
sifre = input("şifreyi giriniz:")

print("şifre:"+sifre)
print("giriş başarılı")"""
print("-----------------------------------------")

age = 36
name = "John"
print("His name is {1}. {1} is {0} years old.".format(age, name))