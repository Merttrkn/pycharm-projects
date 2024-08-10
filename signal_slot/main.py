import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from PyQt5 import uic
import sqlite3
from mert import Mert

db_file = "database.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS person_crud(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL
                    )""")
conn.commit()


class MainWindow(Mert):
    def __init__(self, *args):
        super().__init__()

        uic.loadUi("crud.ui", self)

        self.pushButton_create.clicked.connect(self.on_create_clicked)
        self.pushButton_update.clicked.connect(self.on_update_clicked)
        self.pushButton_delete.clicked.connect(self.on_delete_clicked)
        self.tableWidget.setColumnCount(3)

        self.signal_create_data.connect(self.create_data)
        self.signal_update_data.connect(self.update_data)
        self.signal_delete_data.connect(self.delete_data)

    @pyqtSlot()
    def on_create_clicked(self):
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
                    self.create_data(id, name, surname)
            except ValueError:
                QMessageBox.warning(self, "Hata", "ID alanına geçerli bir sayı girin.")
        else:
            QMessageBox.warning(self, "Hata", "ID, Ad ve Soyad alanları boş bırakılamaz.")

    @pyqtSlot(str, str, str)
    def create_data(self, id, name, surname):
        cursor.execute("INSERT INTO person_crud (id, name, surname) VALUES (?, ?, ?)", (id, name, surname))
        conn.commit()
        # QMessageBox.information(self, "Başarılı", "Yeni kişi başarıyla eklendi.")

        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        self.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(id)))
        self.tableWidget.setItem(row_count, 1, QTableWidgetItem(name))
        self.tableWidget.setItem(row_count, 2, QTableWidgetItem(surname))
        self.tableWidget.setRowCount(row_count + 1)

    @pyqtSlot()
    def on_update_clicked(self):
        id = self.lineEdit_ID.text()
        name = self.lineEdit_name.text()
        surname = self.lineEdit_surname.text()

        if id and name and surname:
            try:
                id = int(id)
                cursor.execute("SELECT * FROM person_crud WHERE id = ?", (id,))
                existing_person = cursor.fetchone()
                if not existing_person:
                    QMessageBox.warning(self, "Hata", "Bu id numarasına sahip kişi bulunamadı.")
                else:
                    self.update_data(id, name, surname)
            except ValueError:
                QMessageBox.warning(self, "Hata", "ID alanına geçerli bir sayı girin.")
        else:
            QMessageBox.warning(self, "Hata", "ID, Ad ve Soyad alanları boş bırakılamaz.")

    @pyqtSlot(str, str, str)
    def update_data(self, id, name, surname):
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

    @pyqtSlot()
    def on_delete_clicked(self):
        id = self.lineEdit_ID.text()
        if id:
            try:
                id = int(id)
                cursor.execute("SELECT * FROM person_crud WHERE id = ?", (id,))
                existing_person = cursor.fetchone()
                if not existing_person:
                    QMessageBox.warning(self, "Hata", "Bu id numarasına sahip kişi bulunamadı.")
                else:
                    self.delete_data(id)
            except ValueError:
                QMessageBox.warning(self, "Hata", "ID alanına geçerli bir sayı girin.")
        else:
            QMessageBox.warning(self, "Hata", "ID alanı boş bırakılamaz.")

    @pyqtSlot(str)
    def delete_data(self, id):
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
