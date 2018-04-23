import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QComboBox, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QTextBrowser, QGroupBox)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PIL import Image

image_list = ['driveforest', 'icemountains', 'nightcity']

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CST 205 Main Window')

        self.combo_box_images = QComboBox()
        self.combo_box_images.addItems(image_list)
        self.box_label = QLabel("")

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.combo_box_images)
        vbox1.addWidget(self.box_label)

        self.setLayout(vbox1)
        self.combo_box_images.currentIndexChanged.connect(self.update_ui)
        self.setWindowTitle("Window layout")

    @pyqtSlot()
    def update_ui(self):
        my_text = self.combo_box_images.currentText()
        my_index = self.combo_box_images.currentIndex()
        self.box_label.setText(f'You chose {my_list[my_index]}.')


app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
