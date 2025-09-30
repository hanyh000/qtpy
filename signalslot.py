import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("lineedit.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit.setPlaceholderText("여기에 입력하세요")
        self.lineEdit.returnPressed.connect(self.changeBackgroundColor)

    def changeBackgroundColor(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.lineEdit.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()