#import sys
import PyQt5.Qwidgets import QApplication, Qwidget, QLabel, QInputDialog, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from PIL import Image
app = QApplication(sys.argv)
class Image(Qwidget):
    def __init__(self):
        super().__init__()
        #search the message
        self.setWindowTitle('Decoded Image')
        self.search = QLineEdit()
        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.click)
        vbox = QVBoxLayout()
        vbox.addWidget(self.search)
        vbox.addWidget(self.search_button)
        self.setLayout(vbox)
        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName = QfileQFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        return fileName

    def clicked(self, msg):
        fileName = self.openFileNameDialog()
        hidden = self.decode_image(fileName)
        print(hidden_text)

    def decode_image(self, fileName):
        image = Image.open(fileName)
        width, height = image.resize
        msg = ""
        index = 0
        for y in range(height):
            for x in range(width):
                try:
                    r, g, b = img.getpixel((x, y))
                except ValueError:
                    r, g, b, a = img.getpixel((x,y))
                if x  == 0 and y == 0:
                    length = 0
                elif index < length:
                    msg += chr(x)
                index += 1
        image.save(fileName)
        return msg
    def openImage(self, fileName):
        self.new_win = QWidget()
        newLabel = QLabel(self.new_win)
        pixmap = QPixmap(fileName)
        newLabel.setPixmap(pixmap)
        self.new_win.resize(pixmap.width(),pixmap.height())
        self.new_win.show()

image = Image()
sys.exit(app.exec_())


'''class Results(QWidget):
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Results()
    sys.exit(app.exec_())'''
