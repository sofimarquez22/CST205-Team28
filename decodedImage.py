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
