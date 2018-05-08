import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit,QPushButton,QVBoxLayout, QFileDialog,QComboBox,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PIL import Image

class Results(QWidget):
    def __init__(self):
        super().__init__()
        self.search = QLineEdit()
        self.button = QPushButton("Test", self)
        self.button.clicked.connect(self.click)


        vbox = QVBoxLayout()
        vbox.addWidget(self.search)
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        self.show()

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
        # limit length of message to 255
        if length > 255:
            print("text too long! (don't exeed 255 characters)")
            return False
        if img.mode != 'RGB':
            print("image mode needs to be RGB")
            return False
        # use a copy of image to hide the text in
        encoded = img.copy()
        width, height = img.size
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                # first value is length of msg
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index -1]
                    asc = ord(c)
                else:
                    asc = r
                encoded.putpixel((col, row), (asc, g , b))
                index += 1
        encoded = encoded.save(fileName)
        return encoded

    def openImage(self, encoded):
        self.new_win = QWidget()
        newLabel = QLabel(self.new_win)
        pixmap = QPixmap(encoded)
        newLabel.setPixmap(pixmap)
        self.new_win.resize(pixmap.width(),pixmap.height())
        self.new_win.show()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Results()
    sys.exit(app.exec_())

# def encode_image(img, msg):
#     """
#     use the red portion of an image (r, g, b) tuple to
#     hide the msg string characters as ASCII values
#     red value of the first pixel is used for length of string
#     """
#     length = len(msg)
#     # limit length of message to 255
#     if length > 255:
#         print("text too long! (don't exeed 255 characters)")
#         return False
#     if img.mode != 'RGB':
#         print("image mode needs to be RGB")
#         return False
#     # use a copy of image to hide the text in
#     encoded = img.copy()
#     width, height = img.size
#     index = 0
#     for row in range(height):
#         for col in range(width):
#             r, g, b = img.getpixel((col, row))
#             # first value is length of msg
#             if row == 0 and col == 0 and index < length:
#                 asc = length
#             elif index <= length:
#                 c = msg[index -1]
#                 asc = ord(c)
#             else:
#                 asc = r
#             encoded.putpixel((col, row), (asc, g , b))
#             index += 1
#     return encoded
