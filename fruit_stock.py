from PyQt5.QtWidgets import *
from fruit_db_helper import DB, DB_CONFIG

class stocking(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("입고")
        self.db = DB(**DB_CONFIG)

        self.product_id = QLineEdit()
        self.product_name = QLineEdit()
        self.stock_qty = QLineEdit()
        self.price = QLineEdit()

        form = QFormLayout()
        form.addRow("상품ID", self.product_id)
        form.addRow("상품명", self.product_name)
        form.addRow("입고량", self.stock_qty)
        form.addRow("가격", self.price)

        self.btn_stock = QPushButton("상품 입고")
        self.btn_stock.clicked.connect(self.try_stock)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_stock)
        self.setLayout(layout)

    def try_stock(self):
        pi = self.product_id.text()
        pn = self.product_name.text()
        sq = self.stock_qty.text()
        price = self.price.text()

        if not (pi and pn and sq and price):
            QMessageBox.warning(self, "입력 오류", "입고량은 숫자여야 합니다.")
            return
        
        try:
            stock_qty = int(sq)
            if stock_qty <= 0:
                raise ValueError
            
        except ValueError:
            QMessageBox.warning(self, "입력 오류", "입고량은 1 이상의 숫자여야 합니다.")
            return
        
        success = self.db.stocks(pi, pn, price, stock_qty)

        if success:
            self.stock_qty.setText("0")
            QMessageBox.information(self, "성공", "입고가 완료되었습니다.")
            self.accept()

        else:
            QMessageBox.warning(self, "실패", "입고에 실패했습니다. 정보를 확인하세요.")
            self.reject()