import sys
import PyQt5.Qwidgets import QApplication, Qwidget, QLabel
from PyQt5.QtGui import QPixmap
#import PIL from Image
app = QApplication(sys.argv)
class Image(Qwidget):
    def __init__(self):
        self.setWindowTitle('Decoded Image')
        self.my_image = QPixmap(#need a way to get the image from the previous page)
        self.show()

image = Image()
sys.exit(app.exec_())



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
    def click(self,msg):
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        # self.openFileNameDialog()
        fileName = self.openFileNameDialog()
        # self.openImage(fileName)
        # msgEncriptedImg = self.decode_image(fileName)
        hidden_text = self.decode_image(fileName)
        print("Hidden text:\n{}".format(hidden_text))
        print(hidden_text)
        # self.openImage(fileName)
        # self.decode_image(fileName)
        # self.show()
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        return fileName
    def decode_image(self,fileName):
        img = Image.open(fileName)
        width, height = img.size
        msg = ""
        index = 0
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = img.getpixel((col, row))
                except ValueError:
                    # need to add transparency a for some .png files
                    r, g, b, a = img.getpixel((col, row))
                # first pixel r value is length of message
                if row == 0 and col == 0:
                    length = r
                elif index <= length:
                    msg += chr(r)
                index += 1
        img.save(fileName)
        return msg
    def openImage(self, fileName):
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
