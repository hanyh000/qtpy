import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("textedit.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plainTextEdit.setPlainText("여기에 글을 입력해 보세요!")
        self.btnClear.clicked.connect(self.clearText)

    def clearText(self):
        self.plainTextEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()