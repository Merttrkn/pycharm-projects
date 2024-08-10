import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
# from PyQt5.QtCore import pyqtSignal
import sqlite3
from veri_islemleri import VeriIslemleri

db_file = "database.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS person_crud(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL
                    )""")
conn.commit()

class MainWindow(QMainWindow,VeriIslemleri):

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
            try:
                id = int(id)
                cursor.execute("SELECT * FROM person_crud WHERE id = ?", (id,))
                existing_person = cursor.fetchone()
                if existing_person:
                    QMessageBox.warning(self, "Hata", "Bu id numarası zaten var")
                else:
                    cursor.execute("INSERT INTO person_crud (id, name, surname) VALUES (?, ?, ?)", (id, name, surname))
                    conn.commit()
                    # QMessageBox.information(self, "Başarılı", "Yeni kişi başarıyla eklendi.")

                    row_count = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_count)
                    self.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(id)))
                    self.tableWidget.setItem(row_count, 1, QTableWidgetItem(name))
                    self.tableWidget.setItem(row_count, 2, QTableWidgetItem(surname))
                    self.tableWidget.setRowCount(row_count + 1)


            except ValueError:
                QMessageBox.warning(self, "Hata", "ID alanına geçerli bir sayı girin.")
        elif id:
            QMessageBox.warning(self, "Hata", "Ad ve Soyad alanları boş bırakılamaz.")
        elif name:
            QMessageBox.warning(self, "Hata", "ID ve Soyad alanları boş bırakılamaz.")
        else:
            QMessageBox.warning(self, "Hata", "ID, Ad ve Soyad alanları boş bırakılamaz.")

    def update_data(self):
        id = self.lineEdit_ID.text()
        name = self.lineEdit_name.text()
        surname = self.lineEdit_surname.text()

        if id and name and surname:
            try:
                id = int(id)
                cursor.execute("UPDATE person_crud SET name=?, surname=? WHERE id=?", (name, surname, id))
                conn.commit()
                QMessageBox.information(self, "Başarılı", "Kişi başarıyla güncellendi.")
                rows = self.tableWidget.rowCount()
                for row in range(rows):
                    item = self.tableWidget.item(row, 0)
                    if item and item.text() == str(id):
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(name))
                        self.tableWidget.setItem(row, 2, QTableWidgetItem(surname))
                        break
            except ValueError:
                QMessageBox.warning(self, "Hata", "id alanına geçerli bir sayı girin.")
        else:
            QMessageBox.warning(self, "Hata", "id, Ad ve Soyad alanları boş bırakılamaz.")


    def delete_data(self):
        id = self.lineEdit_ID.text()
        cursor.execute("DELETE FROM person_crud WHERE id=?", (id,))
        conn.commit()
        QMessageBox.information(self, "Başarılı", "Kişi başarıyla silindi.")
        rows = self.tableWidget.rowCount()
        for row in range(rows):
            item = self.tableWidget.item(row, 0)
            if item and item.text() == id:
                self.tableWidget.removeRow(row)
                break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())