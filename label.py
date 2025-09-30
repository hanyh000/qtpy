import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

form_class = uic.loadUiType("label.ui")[0]

class Window(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.is_label.setText("Hello World!")
        self.is_label.setAlignment(Qt.AlignCenter)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()