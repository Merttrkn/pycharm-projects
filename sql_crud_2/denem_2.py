# import sys
# from PyQt5.QtWidgets import QMessageBox
# import sqlite3
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
# from PyQt5 import uic
#
#
#
# db_file = "database.db"
# conn = sqlite3.connect(db_file)
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS person_crud(
#                     id INTEGER PRIMARY KEY,
#                     name TEXT NOT NULL,
#                     surname TEXT NOT NULL
#                     )""")
# conn.commit()
#
# class DataHandler:
#     def create_data(self, id, name, surname):
#         if id and name and surname:
#             try:
#                 id = int(id)
#                 cursor.execute("SELECT * FROM person_crud WHERE id = ?", (id,))
#                 existing_person = cursor.fetchone()
#                 if existing_person:
#                     QMessageBox.warning(None, "Hata", "Bu id numarası zaten var")
#                 else:
#                     cursor.execute("INSERT INTO person_crud (id, name, surname) VALUES (?, ?, ?)", (id, name, surname))
#                     conn.commit()
#                     return True
#             except ValueError:
#                 QMessageBox.warning(None, "Hata", "ID alanına geçerli bir sayı girin.")
#         elif id:
#             QMessageBox.warning(None, "Hata", "Ad ve Soyad alanları boş bırakılamaz.")
#         elif name:
#             QMessageBox.warning(None, "Hata", "ID ve Soyad alanları boş bırakılamaz.")
#         else:
#             QMessageBox.warning(None, "Hata", "ID, Ad ve Soyad alanları boş bırakılamaz.")
#         return False
#
#     def update_data(self, id, name, surname):
#         if id and name and surname:
#             try:
#                 id = int(id)
#                 cursor.execute("UPDATE person_crud SET name=?, surname=? WHERE id=?", (name, surname, id))
#                 conn.commit()
#                 return True
#             except ValueError:
#                 QMessageBox.warning(None, "Hata", "id alanına geçerli bir sayı girin.")
#         else:
#             QMessageBox.warning(None, "Hata", "id, Ad ve Soyad alanları boş bırakılamaz.")
#         return False
#
#     def delete_data(self, id):
#         cursor.execute("DELETE FROM person_crud WHERE id=?", (id,))
#         conn.commit()
#         return True
#
# class MainWindow(DataHandler):
#     def __init__(self, parent=None):
#         super().__init__(parent=parent)
#
#         uic.loadUi("crud.ui", self)
#
#         self.pushButton_create.clicked.connect(self.create_and_display)
#         self.pushButton_update.clicked.connect(self.update_and_display)
#         self.pushButton_delete.clicked.connect(self.delete_and_display)
#         self.tableWidget.setColumnCount(3)
#
#     def create_and_display(self):
#         id = self.lineEdit_ID.text()
#         name = self.lineEdit_name.text()
#         surname = self.lineEdit_surname.text()
#
#         if self.create_data(id, name, surname):
#             row_count = self.tableWidget.rowCount()
#             self.tableWidget.insertRow(row_count)
#             self.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(id)))
#             self.tableWidget.setItem(row_count, 1, QTableWidgetItem(name))
#             self.tableWidget.setItem(row_count, 2, QTableWidgetItem(surname))
#             self.tableWidget.setRowCount(row_count + 1)
#
#     def update_and_display(self):
#         id = self.lineEdit_ID.text()
#         name = self.lineEdit_name.text()
#         surname = self.lineEdit_surname.text()
#
#         if self.update_data(id, name, surname):
#             rows = self.tableWidget.rowCount()
#             for row in range(rows):
#                 item = self.tableWidget.item(row, 0)
#                 if item and item.text() == str(id):
#                     self.tableWidget.setItem(row, 1, QTableWidgetItem(name))
#                     self.tableWidget.setItem(row, 2, QTableWidgetItem(surname))
#                     break
#
#     def delete_and_display(self):
#         id = self.lineEdit_ID.text()
#         if self.delete_data(id):
#             rows = self.tableWidget.rowCount()
#             for row in range(rows):
#                 item = self.tableWidget.item(row, 0)
#                 if item and item.text() == id:
#                     self.tableWidget.removeRow(row)
#                     break
#
# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec_()