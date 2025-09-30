import sys
from PyQt5.QtWidgets import QApplication
from fruit_input_info import inputinfo
from fruit_pd_output import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()
    sys.exit(app.exec_())