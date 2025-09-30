import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("textedit.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.plainTextEdit.setPlainText("여기에 글을 입력해 보세요!")
        self.plainTextEdit.textChanged.connect(self.changeBackgroundColor)

        self.btnClear.clicked.connect(self.clearText)

    def clearText(self):
        self.plainTextEdit.clear()

    def changeBackgroundColor(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.plainTextEdit.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()
