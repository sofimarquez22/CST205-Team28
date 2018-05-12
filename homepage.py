import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QComboBox, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QTextBrowser, QGroupBox, QInputDialog, QFileDialog)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PIL import Image


globalsave = ""


class NewWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.step1_label = QLabel("Enter anything in textbox and then click the search button.")
        self.picLabel = QLabel(self)
        self.instruc_img = QPixmap('Steps/StepOne.PNG')
        self.picLabel.setPixmap(self.instruc_img)
        self.resize(self.instruc_img.width(),self.instruc_img.height())

        verBox1 = QVBoxLayout()
        verBox1.addWidget(self.step1_label)
        verBox1.addWidget(self.picLabel)

        groupbox1 = QGroupBox()
        groupbox1.setLayout(verBox1)

        self.step2_label = QLabel("Click on the images folder, pick an image provided or any image you have.")
        self.picLabel2 = QLabel(self)
        self.instruc_img2 = QPixmap('Steps/StepTwo.PNG')
        self.picLabel2.setPixmap(self.instruc_img2)
        self.resize(self.instruc_img2.width(),self.instruc_img2.height())

        verBox2 = QVBoxLayout()
        verBox2.addWidget(self.step2_label)
        verBox2.addWidget(self.picLabel2)

        groupbox2 = QGroupBox()
        groupbox2.setLayout(verBox2)

        self.step3_label = QLabel("Orginal image will show and then click on decode.")
        self.picLabel3 = QLabel(self)
        self.instruc_img3 = QPixmap('Steps/StepThree.PNG')
        self.picLabel3.setPixmap(self.instruc_img3)
        self.resize(self.instruc_img3.width(),self.instruc_img3.height())

        verBox3 = QVBoxLayout()
        verBox3.addWidget(self.step3_label)
        verBox3.addWidget(self.picLabel3)

        groupbox3 = QGroupBox()
        groupbox3.setLayout(verBox3)

        self.step4_label = QLabel("Click on the secret_image file and open to show the final results.")
        self.picLabel4 = QLabel(self)
        self.instruc_img4 = QPixmap('Steps/StepFour.PNG')
        self.picLabel4.setPixmap(self.instruc_img4)
        self.resize(self.instruc_img4.width(),self.instruc_img4.height())

        verBox4 = QVBoxLayout()
        verBox4.addWidget(self.step4_label)
        verBox4.addWidget(self.picLabel4)

        groupbox4 = QGroupBox()
        groupbox4.setLayout(verBox4)

        Final_masterbox = QHBoxLayout()
        Final_masterbox.addWidget(groupbox1)
        Final_masterbox.addWidget(groupbox2)
        Final_masterbox.addWidget(groupbox3)
        Final_masterbox.addWidget(groupbox4)

        self.setLayout(Final_masterbox)
        self.show()


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.int_label = QLabel("How to use")
        self.int_button = QPushButton("Click Here!", self)
        self.int_button.clicked.connect(self.open_win)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.int_label)
        hbox1.addWidget(self.int_button)

        gbox1 = QGroupBox()
        gbox1.setLayout(hbox1)

        self.choose_label = QLabel("Choose image from your files! And put your message!")
        self.search = QLineEdit()
        self.file_button = QPushButton("Search", self)
        self.file_button.clicked.connect(self.click)
        self.dec_label = QLabel("Push this to Decode")
        self.dec_button = QPushButton("Decode", self)
        self.dec_button.clicked.connect(self.click_dec)

        global globalsave
        self.picLabel = QLabel(self)
        self.labelImg = QPixmap(globalsave)
        self.picLabel.setPixmap(self.labelImg)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.choose_label)
        vbox2.addWidget(self.search)
        vbox2.addWidget(self.file_button)
        vbox2.addWidget(self.dec_label)
        vbox2.addWidget(self.dec_button)
        vbox2.addWidget(self.picLabel)

        gbox2 = QGroupBox()
        gbox2.setLayout(vbox2)

        masterbox = QVBoxLayout()
        masterbox.addWidget(gbox1)
        masterbox.addWidget(gbox2)

        self.setGeometry(500, 500, 500, 500)
        self.setLayout(masterbox)
        self.setWindowTitle('Hide those Letters!')


    @pyqtSlot()
    def open_win(self):
        self.new_win = NewWindow()


    def click(self):
        globalsave = self.openFileNameDialog()
        encoded_mes = self.encode_image(globalsave)
        self.labelImg = QPixmap(globalsave)
        self.picLabel.setPixmap(self.labelImg)
        self.show()


    def click_dec(self,secret):
        fileName = self.openFileNameDialog()
        hidden_text = self.decode_image(fileName)
        self.labelImg = QPixmap(fileName)
        self.picLabel.setPixmap(self.labelImg)
        self.show()
        print("Hidden text:\n{}".format(hidden_text))


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        return fileName


    def encode_image(self, globalsave):
        message = self.search.text()
        image = Image.open(globalsave)

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


    def decode_image(self,encoded):
        chosen_image = Image.open(encoded)
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


app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
