import sys
from PIL import Image
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle("DIY!")
        btn = QPushButton("Show the steps", self)
        btn.clicked.connect(self.clicked)
        self.show()

    def clicked(self):
        QMessageBox.about(self, "Title", label)

app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
