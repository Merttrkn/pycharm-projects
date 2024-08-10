import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from mert import DatabaseManager


class Person:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname


class MyMainWindow(QMainWindow, DatabaseManager):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi("crud.ui", self)

        self.pushButton_create.clicked.connect(self.create_data)
        self.pushButton_update.clicked.connect(self.update_data)
        self.pushButton_delete.clicked.connect(self.delete_data)
        self.tableWidget.setColumnCount(3)

    def create_data(self):
        id = self.lineEdit_ID.text()
        name = self.lineEdit_name.text()
        surname = self.lineEdit_surname.text()

        if id and name and surname:
            person = Person(int(id), name, surname)
            if self.insert_person(person):
                # QMessageBox.information(self, "Başarılı", "Yeni kişi başarıyla eklendi.")

                row_count = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_count)
                self.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(id)))
                self.tableWidget.setItem(row_count, 1, QTableWidgetItem(name))
                self.tableWidget.setItem(row_count, 2, QTableWidgetItem(surname))
                self.tableWidget.setRowCount(row_count + 1)
        else:
            QMessageBox.warning(self, "Hata", "ID, Ad ve Soyad alanları boş bırakılamaz.")

    def update_data(self):
        id = self.lineEdit_ID.text()
        name = self.lineEdit_name.text()
        surname = self.lineEdit_surname.text()

        if id and name and surname:
            person = Person(int(id), name, surname)
            if self.update_person(person):
                QMessageBox.information(self, "Başarılı", "Kişi başarıyla güncellendi.")
                rows = self.tableWidget.rowCount()
                for row in range(rows):
                    item = self.tableWidget.item(row, 0)
                    if item and item.text() == str(id):
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(name))
                        self.tableWidget.setItem(row, 2, QTableWidgetItem(surname))
                        break
        else:
            QMessageBox.warning(self, "Hata", "ID, Ad ve Soyad alanları boş bırakılamaz.")

    def delete_data(self):
        id = self.lineEdit_ID.text()
        self.delete_person(id)
        QMessageBox.information(self, "Başarılı", "Kişi başarıyla silindi.")
        rows = self.tableWidget.rowCount()
        for row in range(rows):
            item = self.tableWidget.item(row, 0)
            if item and item.text() == id:
                self.tableWidget.removeRow(row)
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
