from PyQt5.QtWidgets import *
from fruit_db_helper import DB, DB_CONFIG

class buying(QDialog):
    def __init__(self):
        super().__init__()
        
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

        name = self.name.text()
        phone = self.phone.text()
        product_name = self.product_name.text()
        buy_qty_text = self.buy_qty.text()

        try:
            buy_qty = int(buy_qty_text)
        except ValueError:
            QMessageBox.warning(self, "입력 오류", "구매량은 숫자여야 합니다.")
            return
    
        success = self.db.insert_or_update_buyer(name, phone, product_name, buy_qty)
        if not success:
            QMessageBox.warning(self, "구매 실패", "구매 신청에 실패했습니다.")
            return
        
        try:
            self.db.buying(name, phone)
            QMessageBox.information(self, "성공", "구매 및 보유량 업데이트 성공")
            self.accept()  

        except Exception as e:
            QMessageBox.critical(self, "오류", f"보유량 업데이트 실패: {e}")
            self.reject()