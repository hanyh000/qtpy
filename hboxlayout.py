import sys
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        window = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("버튼 1"))
        layout.addWidget(QPushButton("버튼 2"))
        layout.addWidget(QPushButton("버튼 3"))

        window.setLayout(layout)
        self.setCentralWidget(window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()

