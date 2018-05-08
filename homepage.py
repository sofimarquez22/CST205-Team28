import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QComboBox, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QTextBrowser, QGroupBox, QInputDialog, QFileDialog)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PIL import Image


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.setWindowTitle('Manipulating')

        self.combo_box_images = QComboBox()
        self.combo_box_images.addItems(image_list)
        self.box_label = QLabel("")
        self.first_title = QLabel('Choose an image')
=======
>>>>>>> cb86217b423a951766bb12cb98f35ac66ae2379d

        self.int_label = QLabel("How to use")
        self.int_button = QPushButton("Click Here!", self)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.int_label)
        hbox1.addWidget(self.int_button)

        gbox1 = QGroupBox()
        gbox1.setLayout(hbox1)

        self.choose_label = QLabel("Choose image from your files! And put your message!")
        self.search = QLineEdit()
        self.file_button = QPushButton("Search", self)
        self.file_button.clicked.connect(self.click)
        self.dec_label = QLabel("Push this to Deconde")
        self.dec_button = QPushButton("Decode", self)
        self.dec_button.clicked.connect(self.click_dec)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.choose_label)
        vbox2.addWidget(self.search)
        vbox2.addWidget(self.file_button)
        vbox2.addWidget(self.dec_label)
        vbox2.addWidget(self.dec_button)

        gbox2 = QGroupBox()
        gbox2.setLayout(vbox2)

        masterbox = QVBoxLayout()
        masterbox.addWidget(gbox1)
        masterbox.addWidget(gbox2)

        self.setGeometry(500, 500, 500, 500)
        self.setLayout(masterbox)
        self.setWindowTitle('Manipulaing')


    @pyqtSlot()
    def click(self):
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        fileName = self.openFileNameDialog()
        encoded = self.encode_image(fileName)
        self.openSecretImage(encoded)
        self.show()


    def click_dec(self,secret):
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        fileName = self.openFileNameDialog()
        hidden_text = self.decode_image(fileName)
        print("Hidden text:\n{}".format(hidden_text))


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        return fileName


    def encode_image(self, fileName):
        message = self.search.text()
        image = Image.open(fileName)

        length = len(message)
        if length > 200:
            print("Please enter a shorter message.")
            return False
        if image.mode != 'RGB':
            print("image mode needs to be RGB")
            return False
        encoded = image.copy()
        width, height = image.size
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = image.getpixel((col, row))
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = message[index -1]
                    asc = ord(c)
                else:
                    asc = r
                encoded.putpixel((col, row), (asc, g , b))
                index += 1
        encoded = encoded.save('secret_image.png')
        return encoded


    def decode_image(self,fileName):
        chosen_image = Image.open(fileName)
        width, height = chosen_image.size
        secret = ""
        index = 0
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = chosen_image.getpixel((col, row))
                except ValueError:
                    r, g, b, a = chosen_image.getpixel((col, row))
                if row == 0 and col == 0:
                    length = r
                elif index <= length:
                    secret += chr(r)
                index += 1
        chosen_image.save('decode_image.jpg')
        return secret


    def openSecretImage(self, encoded):
        self.new_win = QWidget()
        newLabel = QLabel(self.new_win)
        pixmap = QPixmap(encoded)
        newLabel.setPixmap(pixmap)
        self.new_win.resize(pixmap.width(),pixmap.height())
        self.new_win.show()


# class InstructionWindow(QDialog):
#     def __init__(self):
#         super().__init__()

app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
