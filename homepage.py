import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QComboBox, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QTextBrowser, QGroupBox)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from image_information import image_info
from PIL import Image

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
