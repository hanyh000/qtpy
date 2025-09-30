from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
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
        form.addRow("전화번호", self.product_name)
        form.addRow("전화번호", self.buy_qty)

        self.btn_buy = QPushButton("구매 신청")
        self.btn_buy.clicked.connect(self.try_buy)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_buy)
        self.setLayout(layout)

    def try_buy(self):
        pn = self.product_name.text().strip()
        if not pn:
            QMessageBox.warning(self, "오류", "아이디와 비밀번호를 모두 입력하세요.")
            return

        ok = self.db.verify_user(pn)
        if ok:
            self.accept()
        else:
            QMessageBox.critical(self, "실패", "아이디 또는 비밀번호가 올바르지 않습니다.")