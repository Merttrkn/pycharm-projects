from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow


class Mert(QMainWindow):
    signal_create_data = pyqtSignal(str, str, str)
    signal_update_data = pyqtSignal(str, str, str)
    signal_delete_data = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def create_data(self, id, name, surname):
        self.signal_create_data.emit(id, name, surname)

    def update_data(self, id, name, surname):
        self.signal_update_data.emit(id, name, surname)

    def delete_data(self, id):
        self.signal_delete_data.emit(id)
