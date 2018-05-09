import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,

#add a pop up window with images of how to do the decrypting
class Instruct(QtWidget):
    def __init__(self):
        super().__init__()
    def buildPopUp(self,item):
        name = item.text()
        self.exPopup = exa
