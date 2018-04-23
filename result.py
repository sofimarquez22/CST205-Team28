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
        self.openFileNameDialog()
        # im = Image.open(fileName)
        self.show()



    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.new_win = QWidget()
            newLabel = QLabel(self.new_win)
            pixmap = QPixmap(fileName)
            newLabel.setPixmap(pixmap)
            self.new_win.resize(pixmap.width(),pixmap.height())
            self.new_win.show()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Results()
    sys.exit(app.exec_())

# def decode_image(img):
#     """
#     check the red portion of an image (r, g, b) tuple for
#     hidden message characters (ASCII values)
#     """
#     width, height = img.size
#     msg = ""
#     index = 0
#     for row in range(height):
#         for col in range(width):
#             try:
#                 r, g, b = img.getpixel((col, row))
#             except ValueError:
#                 # need to add transparency a for some .png files
#                 r, g, b, a = img.getpixel((col, row))
#             # first pixel r value is length of message
#             if row == 0 and col == 0:
#                 length = r
#             elif index <= length:
#                 msg += chr(r)
#             index += 1
#     return msg
# # pick a .png or .bmp file you have in the working directory
# # or give full path name
# original_image_file = "Beach7.png"
# #original_image_file = "Beach7.bmp"
# img = Image.open(original_image_file)
# # image mode needs to be 'RGB'
# print(img, img.mode)  # test
# # create a new filename for the modified/encoded image
# encoded_image_file = "enc_" + original_image_file
# # don't exceed 255 characters in the message
# secret_msg = "this is a secret message added to the image"
# print(len(secret_msg))  # test
# img_encoded = encode_image(img, secret_msg)
# if img_encoded:
#     # save the image with the hidden text
#     img_encoded.save(encoded_image_file)
#     print("{} saved!".format(encoded_image_file))
#     # view the saved file, works with Windows only
#     # behaves like double-clicking on the saved file
#     import os
#     os.startfile(encoded_image_file)
#     '''
#     # or activate the default viewer associated with the image
#     # works on more platforms like Windows and Linux
#     import webbrowser
#     webbrowser.open(encoded_image_file)
#     '''
#     # get the hidden text back ...
#     img2 = Image.open(encoded_image_file)
#     hidden_text = decode_image(img2)
#     print("Hidden text:\n{}".format(hidden_tex))



# class result(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.search = QLineEdit()
#         self.button = QPushButton("Test", self)
#         self.button.clicked.connect(self.click)
#
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.search)
#         vbox.addWidget(self.button)
#         self.setLayout(vbox)
#         self.show()
#
#
#     @pyqtSlot()
#
#     def click(self):
#         openItem = self.getOpenFileNameDialog()
