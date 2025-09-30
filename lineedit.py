import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

form_class = uic.loadUiType("lineedit.ui")[0]

class Window(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.lineEdit.setPlaceholderText("여기에 입력하세요")
        self.lineEdit.returnPressed.connect(self.clearText)

    def clearText(self):
        self.lineEdit.clear()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()