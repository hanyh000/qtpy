import sys
from PyQt5.QtWidgets import QApplication
from fruit_input_info import inputinfo
from fruit_pd_output import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = inputinfo()
    if login.exec_() == inputinfo.Accepted:
        w = MainWindow()
        w.show()
        sys.exit(app.exec_())
    else:
        sys.exit(0)