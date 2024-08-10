from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)


app = QApplication([])
window = MainPage()
window.show()
sys.exit(app.exec_())
