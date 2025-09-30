import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("sample.ui")[0]
class Window(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = Window()
    myWindow.show()
    app.exec_()