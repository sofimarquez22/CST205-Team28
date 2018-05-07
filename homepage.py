import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QComboBox, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QTextBrowser, QGroupBox, QInputDialog, QFileDialog)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PIL import Image

# image_list = ['driveforest', 'icemountains', 'nightcity']

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.int_label = QLabel("How to use")
        self.int_button = QPushButton("Click Here!", self)

        # self.combo_box_images = QComboBox()
        # self.combo_box_images.addItems(image_list)
        # self.box_label = QLabel("")
        # self.first_title = QLabel('Choose an image')
        # self.start_button = QPushButton("Start", self)
        # self.start_button.clicked.connect(self.chosen_image)


        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.int_label)
        hbox1.addWidget(self.int_button)
        # hbox1.addWidget(self.first_title)
        # hbox1.addWidget(self.combo_box_images)
        # hbox1.addWidget(self.box_label)

        gbox1 = QGroupBox()
        gbox1.setLayout(hbox1)

        self.choose_label = QLabel("Choose image from your files! And put your message!")
        self.search = QLineEdit()
        self.file_button = QPushButton("Search", self)
        self.file_button.clicked.connect(self.click)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.choose_label)
        vbox2.addWidget(self.search)
        vbox2.addWidget(self.file_button)


        gbox2 = QGroupBox()
        gbox2.setLayout(vbox2)


        masterbox = QVBoxLayout()
        masterbox.addWidget(gbox1)
        masterbox.addWidget(gbox2)



        self.setGeometry(500, 500, 500, 500)
        self.setLayout(masterbox)
        # self.combo_box_images.currentIndexChanged.connect(self.update_ui)
        self.setWindowTitle('Manipulaing')


    @pyqtSlot()
    def update_ui(self):
        my_text = self.combo_box_images.currentText()
        my_index = self.combo_box_images.currentIndex()
        self.box_label.setText(f'You chose {my_list[my_index]}.')

    # def chosen_image(self):
    #     encoded = self.encode_image(fileName)
    #     self.openImage(encoded)
    #     self.show()

    def click(self):
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        # self.openFileNameDialog()
        fileName = self.openFileNameDialog()
        # self.openImage(fileName)
        encoded = self.encode_image(fileName)
        self.openImage(encoded)
        self.show()


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        return fileName


    def encode_image(self, fileName):
        msg = self.search.text()
        img = Image.open(fileName)

        length = len(msg)
        if length > 255:
            print("text too long! (don't exeed 255 characters)")
            return False
        if img.mode != 'RGB':
            print("image mode needs to be RGB")
            return False
        encoded = img.copy()
        width, height = img.size
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index -1]
                    asc = ord(c)
                else:
                    asc = r
                encoded.putpixel((col, row), (asc, g , b))
                index += 1
        encoded = encoded.save('new_image.png')
        return encoded

    def openImage(self, encoded):
        self.new_win = QWidget()
        newLabel = QLabel(self.new_win)
        pixmap = QPixmap(encoded)
        newLabel.setPixmap(pixmap)
        self.new_win.resize(pixmap.width(),pixmap.height())
        self.new_win.show()

class InstructionWindow(QDialog):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
