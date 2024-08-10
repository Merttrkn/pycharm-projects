"""to_do_list = []


def add_task(to_do_list):
    task = input("Eklenecek görevi giriniz")
    to_do_list.append(task)
    print("Görev başarıyla eklendi")


def show_task(to_do_list):
    print("yapılacak görevler:")
    for task in to_do_list:
        print("-", task)


def delete_task(to_do_list):
    task = input("Silmek istediğin görevi gir:")
    if task not in to_do_list:
        print("Görev bulunamadı")
    else:
        to_do_list.remove(task)
        print("Değer silindi")


while True:
    print("/n To-do list uygulaması")
    print("1.Görev ekle")
    print("2.Görevleri göster")
    print("3.Görev sil")
    print("4.çıkış")
    choice = input("Seçiminiz(1/2/3/4):")

    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        show_task(to_do_list)
    elif choice == "3":
        delete_task(to_do_list)
    elif choice == "4":
        print("uygulamadan çıkılıyor")
        break
    else:
        print("geçersiz görev")"""

