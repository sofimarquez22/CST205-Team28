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


import sys
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QApplication


class exampleWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        listWidget = QListWidget(self)
        listWidget.itemDoubleClicked.connect(self.buildExamplePopup)

        names = ["Jack", "Chris", "Joey", "Kim", "Duncan"]

        for n in names:
            QListWidgetItem(n, listWidget)

        self.setGeometry(100, 100, 100, 100)
        self.show()

    @staticmethod
    def buildExamplePopup(item):
        name = item.text()
        exPopup = examplePopup(name)
        exPopup.setGeometry(100, 200, 100, 100)
        exPopup.show()


class examplePopup(QWidget):
    def __init__(self, name):
        super().__init__()

        self.name = name

        self.initUI()

    def initUI(self):
        lblName = QLabel(self.name, self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = exampleWidget()
    sys.exit(app.exec_())
