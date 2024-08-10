import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout ,QWidget, QMainWindow, QFileDialog
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("deneme.ui",self)
        self.init_ui()

    def init_ui(self):
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.label.setText("Hoşbulduk!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())