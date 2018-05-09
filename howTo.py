import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5 import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("DIY!")
        btn = QPushButton("Show the steps", self)
        btn.clicked.connect(self.clickMethod)
        self.show()

    def clicked(self):
        QMessageBox.about(self, "Title", "Message")

app = QtGWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
