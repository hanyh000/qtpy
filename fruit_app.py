import sys
from PyQt5.QtWidgets import QApplication
from fruit_buy import buying
from fruit_cancel import canceling
from fruit_delivery import deliverying
from fruit_main import fruitWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = fruitWindow()
    w.show()
    sys.exit(app.exec_())