from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, \
QLineEdit, QPushButton, QMessageBox
from db_helper import DB, DB_CONFIG

class inputinfo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("구매 신청")
        self.db = DB(**DB_CONFIG)

        self.name = QLineEdit()
        self.phone = QLineEdit()
        self.product_name = QLineEdit()
        self.buy_qty = QLineEdit()

        form = QFormLayout()
        form.addRow("이름", self.name)
        form.addRow("전화번호", self.phone)
        form.addRow("상품명", self.product_name)
        form.addRow("구매량", self.buy_qty)

        self.btn_buy = QPushButton("구매 신청")
        self.btn_buy.clicked.connect(self.try_buy)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_buy)
        self.setLayout(layout)

    def try_buy(self):
        pn = self.product_name.text().strip()
        if not pn:
            QMessageBox.warning(self, "")
            return

        ok = self.db.verify_user(pn)
        if ok:
            self.accept()
        else:
            QMessageBox.critical(self, "")