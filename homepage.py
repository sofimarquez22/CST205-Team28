import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QComboBox, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QTextBrowser, QGroupBox)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PIL import Image

image_list = ['driveforest', 'icemountains', 'nightcity']

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Manipulaing')

        self.combo_box_images = QComboBox()
        self.combo_box_images.addItems(image_list)
        self.box_label = QLabel("")
        self.first_title = QLabel('Choose an image')


        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.first_title)
        hbox1.addWidget(self.combo_box_images)
        hbox1.addWidget(self.box_label)

        gbox1 = QGroupBox()
        gbox1.setLayout(hbox1)

        self.choose_label = QLabel("Choose image from your files!")
        self.file_button = QPushButton("Search")
        # self.file_button.clicked.connect(self.click)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.choose_label)
        hbox2.addWidget(self.file_button)

        gbox2 = QGroupBox()
        gbox2.setLayout(hbox2)

        self.int_label = QLabel("How to use")
        self.int_button = QPushButton("Click Here!")

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.int_label)
        vbox1.addWidget(self.int_button)

        masterbox = QVBoxLayout()
        masterbox.addWidget(gbox1)
        masterbox.addWidget(gbox2)
        masterbox.addWidget(vbox1)

        self.setLayout(masterbox)
        self.combo_box_images.currentIndexChanged.connect(self.update_ui)
        self.setWindowTitle("Window layout")

    @pyqtSlot()
    def update_ui(self):
        my_text = self.combo_box_images.currentText()
        my_index = self.combo_box_images.currentIndex()
        self.box_label.setText(f'You chose {my_list[my_index]}.')

class InstructionWindow(QDialog):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
