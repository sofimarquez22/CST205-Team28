'''
CST205-01_SP18:Multimedia Design & Progmng
CST205-Team28 Final Project
Eduardo Soto Rodriguez, Francisco Herrera, Blanca Marquez
5/13/2018

Purpose of this program is to allow the user to hide a message in a RGB image
and then also allow them to decode the image.
Everyone in the team worked on different files to avoid merge conflicts and the
result of the work is this final file in which was pieced together.
'''
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QComboBox, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QTextBrowser, QGroupBox, QInputDialog, QFileDialog)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PIL import Image


globalsave = ""

'''
This window is the second window of the program which will pop-up when the how-to
button is clicked. This will show a four step guide as to how to use the program.
Resposible for this was Blanca and Eduardo.
'''

class NewWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.step1_label = QLabel("Step 1: Enter anything in textbox and then click the search button.")
        self.picLabel = QLabel(self)
        self.instruc_img = QPixmap('Steps/StepOne.PNG')
        self.picLabel.setPixmap(self.instruc_img)
        self.resize(self.instruc_img.width(),self.instruc_img.height())

        verBox1 = QVBoxLayout()
        verBox1.addWidget(self.step1_label)
        verBox1.addWidget(self.picLabel)

        groupbox1 = QGroupBox()
        groupbox1.setLayout(verBox1)

        self.step2_label = QLabel("Step 2: Click on the images folder, pick an image provided or any image you have.")
        self.picLabel2 = QLabel(self)
        self.instruc_img2 = QPixmap('Steps/StepTwo.PNG')
        self.picLabel2.setPixmap(self.instruc_img2)
        self.resize(self.instruc_img2.width(),self.instruc_img2.height())

        verBox2 = QVBoxLayout()
        verBox2.addWidget(self.step2_label)
        verBox2.addWidget(self.picLabel2)

        groupbox2 = QGroupBox()
        groupbox2.setLayout(verBox2)

        self.step3_label = QLabel("Step 3: Orginal image will show and then click on decode.")
        self.picLabel3 = QLabel(self)
        self.instruc_img3 = QPixmap('Steps/StepThree.PNG')
        self.picLabel3.setPixmap(self.instruc_img3)
        self.resize(self.instruc_img3.width(),self.instruc_img3.height())

        verBox3 = QVBoxLayout()
        verBox3.addWidget(self.step3_label)
        verBox3.addWidget(self.picLabel3)

        groupbox3 = QGroupBox()
        groupbox3.setLayout(verBox3)

        self.step4_label = QLabel("Step 4: Click on the secret_image file and open to show the final results.")
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
        self.setWindowTitle('How-To Guide')
        self.show()


'''
For this window, it is the main window in which organizes the display for it to
show two group boxes. The first group box consists of a line stating that the button
demonstrates and explains of how to use this program. The second group box consists
of the texbox for the message and a button for the selection of an image that the user
wants for their encoding. Also, there is the the decoding button which will also open
for the selection of the encoded image and will display the message at the botton as
well as the encoded image itself.
Resposible for this was Eduardo.
'''

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

        self.choose_label = QLabel("Choose an RGB image from your files! And put your message! 200 character limit!")
        self.search = QLineEdit()
        self.file_button = QPushButton("Search and Encode", self)
        self.file_button.clicked.connect(self.click)
        self.dec_label = QLabel("Push this to Decode")
        self.dec_button = QPushButton("Decode", self)
        self.dec_button.clicked.connect(self.click_dec)
        self.after_label = QLabel("")
        self.message_label = QLabel("")

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
        vbox2.addWidget(self.after_label)
        vbox2.addWidget(self.message_label)

        gbox2 = QGroupBox()
        gbox2.setLayout(vbox2)

        masterbox = QVBoxLayout()
        masterbox.addWidget(gbox1)
        masterbox.addWidget(gbox2)

        self.setGeometry(500, 500, 500, 500)
        self.setLayout(masterbox)
        self.setWindowTitle('Hide those Letters!')

    '''
    As for the slots that were created, the open_win is connected to a second window
    that will pop-up when the how-to button is clicked. The click function is for the search
    and encode button which will show the original image chosen and give conformation in the
    the terminal of whether the user did it correctly. The click_dec function will be connected to the
    decoding part of the program and will show you the message that was hidden in the image.
    The openFileNameDialog function is the one that leads the program to open your files for
    choosing the image that the user desires and will be used among the program.
    Resposible for this was Francisco.
    '''

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
        self.after_label.setText("Zoom on the top left corner either here or at the image file!")
        self.message_label.setText("Hidden text:\n{}".format(hidden_text))
        self.show()
        print("Hidden text:\n{}".format(hidden_text))


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        return fileName

    '''
    Title: Hide Private Message in an Image (Python)
    Author: vegaseat
    Link: https://www.daniweb.com/programming/software-development/code/485063/hide-private-message-in-an-image-python
    For the encoding and decoding part of the project, we used both of these pieces of
    code. For the encoding code, it opens the image that was selected/passed in as
    the globalsave. Then it checks some requirements of what message was inputted by
    the user and if it fails, you can try again. After passing, it creates a new file
    were the encoded image will be. Then through a nested for loop, it will take every
    character and hide it in the red tuple. Then it returns the new image file.
    '''

    def encode_image(self, globalsave):
        message = self.search.text()
        image = Image.open(globalsave)

        length = len(message)
        if length > 200:
            print("Please enter a shorter message.")
            return False
        if length == 0:
            print("You must enter a message.")
            return False
        if image.mode != 'RGB':
            print("Image mode needs to be RGB. Try a .jpg image file instead!")
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

    '''
    Title: Hide Private Message in an Image (Python)
    Author: vegaseat
    Link: https://www.daniweb.com/programming/software-development/code/485063/hide-private-message-in-an-image-python
    For the encoding and decoding part of the project, we used both of these pieces of
    code. For the decoding code, the encoded image will be opened and through the use
    of a nested for loop, it will gather the red tuples that were changed. It then
    returns the message back.
    '''

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
