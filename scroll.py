from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class SurfViewer(QMainWindow):
    def __init__(self, parent=None):
        super(SurfViewer, self).__init__()
        self.parent = parent

        self.centralTabs= QTabWidget()
        self.setCentralWidget(self.centralTabs)
        self.setFixedWidth(200)
        self.setFixedHeight(200)

        #tab Model selection
        self.tab_ModelSelect = QWidget()
        self.centralTabs.addTab(self.tab_ModelSelect,"Label")


        self.groupscrolllayouttest2 = QVBoxLayout() ####
        self.groupscrollbartest2 = QGroupBox() ####

        self.groupscrolllayouttest = QHBoxLayout() ####
        self.groupscrollbartest = QGroupBox() ####


        self.mainHBOX_param_scene = QVBoxLayout()
        for i in range(10):
            Label = QLabel('BlaBlaBlaBlaBlaBlaBlaBlaBlaBlaBlaBlaBlaBlaBlaBlaBlaBla')
            Label.setFixedWidth(200)
            self.mainHBOX_param_scene.addWidget(Label)


        #
        scroll = QScrollArea()
        scroll.setWidget(self.groupscrollbartest)
        scroll.setWidgetResizable(True)
        scroll.setFixedWidth(20)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # self.mainHBOX_param_scene.addWidget(scroll)
        self.groupscrollbartest.setLayout(self.mainHBOX_param_scene)
        self.groupscrolllayouttest.addWidget(self.groupscrollbartest)
        self.groupscrolllayouttest.addWidget(scroll)

        scroll2 = QScrollArea()
        scroll2.setWidget(self.groupscrollbartest2)
        scroll2.setWidgetResizable(True)
        scroll2.setFixedWidth(20)
        scroll2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.groupscrollbartest2.setLayout(self.groupscrolllayouttest)
        self.groupscrolllayouttest2.addWidget(self.groupscrollbartest2)
        self.groupscrolllayouttest2.addWidget(scroll2)


        self.tab_ModelSelect.setLayout(self.groupscrolllayouttest2)

def main():
    app = QApplication(sys.argv)
    ex = SurfViewer(app)
    ex.setWindowTitle('window')
    # ex.showMaximized()
    ex.show()
    sys.exit(app.exec_( ))


if __name__ == '__main__':
    main()
