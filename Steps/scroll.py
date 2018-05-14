from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QComboBox, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QTextBrowser, QGroupBox, QInputDialog, QFileDialog, QScrollArea)
def setupUi(self, Interface):
    Interface.setObjectName("Interface")
    Interface.resize(1152, 1009)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(Interface.sizePolicy().hasHeightForWidth())
    Interface.setSizePolicy(sizePolicy)
    Interface.setMouseTracking(False)
    icon = QtGui.QIcon()

    self.horizontalLayout = QtWidgets.QHBoxLayout()
    self.horizontalLayout.setObjectName("horizontalLayout")

    self.scrollArea = QtWidgets.QScrollArea()
    self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1131, 951))
    self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
    self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
    self.scrollArea.setWidgetResizable(True)
    self.scrollArea.setObjectName("scrollArea")
    self.scrollArea.setEnabled(True)

    self.horizontalLayout.addWidget(self.scrollArea)

    centralWidget = QWidgets.QWidget()
    centralWidget.setObjectName("centralWidget")
    centralWidget.setLayout(self.horizontalLayout)

    self.setCentralWidget(centralWidget)
