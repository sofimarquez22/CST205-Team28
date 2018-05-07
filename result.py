import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit,QPushButton,QVBoxLayout, QFileDialog,QComboBox,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PIL import Image


class Results(QWidget):
    def __init__(self):
        super().__init__()


        self.search = QLineEdit()
        self.button = QPushButton("Upload", self)
        self.buttonMsg = QPushButton("Encode", self)
        self.button.clicked.connect(self.click)
        self.buttonMsg.clicked.connect(self.msgClick)

        # img = Image.open(fileName)
        # imageDisplay = QLabel(self)
        # pixmap = QPixmap(img)
        #
        # label.setPixmap(pixmap)

        vbox = QVBoxLayout()
        vbox.addWidget(self.search)
        vbox.addWidget(self.button)
        vbox.addWidget(self.buttonMsg)
        self.setLayout(vbox)
        self.show()

    def click(self):
        # self.title = 'PyQt5 file dialogs - pythonspot.com'
        # self.openFileNameDialog()
        fileName = self.openFileNameDialog()
        # self.openImage(fileName)
        # msg = self.search.text()
        # msgEncriptedImg = self.encode_image(fileName, msg)
        return fileName
        # self.openImage(fileName)
        # self.decode_image(fileName)
        # self.show()

    def msgClick(self, fileName):
        msg = self.search.text()

        msgEncriptedImg = self.encode_image(fileName, msg)





    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        return fileName

    def encode_image(self, fileName, msg):
        # msg = self.search.text()
        testImg = Image.open(fileName)

        length = len(msg)

        if length > 255:
            print("Message must be under 255 characters")
            return False
        if testImg.mode != 'RGB':
            print("Works only with RGB images")
            return False

        msgEncriptedImg = testImg.copy()
        width, height = testImg.size
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = testImg.getpixel((col, row))

                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index -1]
                    asc = ord(c)
                else:
                    asc = r
                msgEncriptedImg.putpixel((col, row), (asc, g , b))
                index += 1
        print("{} saved!".format(msgEncriptedImg))
        msgEncriptedImg = msgEncriptedImg.save(fileName)
        return msgEncriptedImg

    def openImage(self, fileName):
        self.new_win = QWidget()
        newLabel = QLabel(self.new_win)
        pixmap = QPixmap(fileName)
        newLabel.setPixmap(pixmap)
        self.new_win.resize(pixmap.width(),pixmap.height())
        self.new_win.show()

    # def decode_image(self, fileName):
    #     img = Image.open(fileName)
    #     width, height = img.size
    #     msg = ""
    #     index = 0
    #     for row in range(height):
    #         for col in range(width):
    #             try:
    #                 r, g, b = img.getpixel((col, row))
    #             except ValueError:
    #             # need to add transparency a for some .png files
    #                 r, g, b, a = img.getpixel((col, row))
    #         # first pixel r value is length of message
    #             if row == 0 and col == 0:
    #                 length = r
    #             elif index <= length:
    #                 msg += chr(r)
    #                 index += 1
    #     return msg








if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Results()
    sys.exit(app.exec_())
