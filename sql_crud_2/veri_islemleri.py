from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

class VeriIslemleri:


    def tabloya_ekle(self, id, name, surname):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        self.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(id)))
        self.tableWidget.setItem(row_count, 1, QTableWidgetItem(name))
        self.tableWidget.setItem(row_count, 2, QTableWidgetItem(surname))
        self.tableWidget.setRowCount(row_count + 1)

    def tablodan_cikar(self, id):
        rows = self.tableWidget.rowCount()
        for row in range(rows):
            item = self.tableWidget.item(row, 0)
            if item and item.text() == id:
                self.tableWidget.removeRow(row)
                break

    def hata_mesaji_goster(self, mesaj):
        QMessageBox.warning(self, "Hata", mesaj)

    def bilgi_mesaji_goster(self, mesaj):
        QMessageBox.information(self, "Başarılı", mesaj)