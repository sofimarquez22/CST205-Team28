import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QDialog,
                                QTextBrowser, QComboBox, QGroupBox)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot


class NewWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.picLabel = QLabel(self)
        self.instruc_img = QPixmap('images/stars.jpg')
        self.picLabel.setPixmap(self.instruc_img)
        self.resize(self.instruc_img.width(),self.instruc_img.height())


        self.picLabel2 = QLabel(self)
        self.instruc_img2 = QPixmap('images/clouds.jpg')
        self.picLabel2.setPixmap(self.instruc_img2)
        self.resize(self.instruc_img2.width(),self.instruc_img2.height())

        self.picLabel3 = QLabel(self)
        self.instruc_img3 = QPixmap('images/forestroad.jpg')
        self.picLabel3.setPixmap(self.instruc_img3)
        self.resize(self.instruc_img3.width(),self.instruc_img3.height())


        vbox = QVBoxLayout()
        vbox.addWidget(self.picLabel)
        vbox.addWidget(self.picLabel2)
        vbox.addWidget(self.picLabel3)
        self.setLayout(vbox)
        self.show()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton('CLICK ME')

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

        self.int.clicked.connect(self.open_win)


    @pyqtSlot()
    def open_win(self):
        self.new_win = NewWindow()

app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
