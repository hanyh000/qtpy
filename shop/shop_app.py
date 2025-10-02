import sys
from PyQt5.QtWidgets import QApplication
from shop_main import shopwindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = shopwindow()
    w.show()
    sys.exit(app.exec_())