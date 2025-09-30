import sys
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        window = QWidget()
        
        layout = QGridLayout()
        layout.addWidget(QPushButton("(0,0)"), 0, 0)
        layout.addWidget(QPushButton("(0,1)"), 0, 1)
        layout.addWidget(QPushButton("(1,0)"), 1, 0)
        layout.addWidget(QPushButton("(1,1)"), 1, 1)

        window.setLayout(layout)
        self.setCentralWidget(window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()