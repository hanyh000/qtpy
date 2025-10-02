from PyQt5.QtWidgets import *
from shop_db_helper import DB, DB_CONFIG

class shipment_dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("출고")
        self.db= DB(**DB_CONFIG)

        self.pi = QLineEdit()
        self.sq = QSpinBox()

        form  = QFormLayout()
        form.addRow("상품id", self.pi)
        form.addRow("출고량", self.sq)

        buttonBOx = QHBoxLayout() 

        self.btn_sk = QPushButton("출고")
        self.btn_sk.clicked.connect(self.stocks)
        self.btn_cc = QPushButton("취소")
        self.btn_cc.clicked.connect(self.reject)

        buttonBOx.addWidget(self.btn_sk)
        buttonBOx.addWidget(self.btn_cc)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(buttonBOx)
        self.setLayout(layout)

    def stocks(self):
        id = self.pi.text().strip()
        sq = self.sq.value()

        if not (id and sq):
            QMessageBox.warning(self, "입력 오류", "모든 정보를 입력하시오.")
            return
        
        try:
            stock_qty = int(sq)
            if stock_qty <= 0:
                raise ValueError
            
        except ValueError:
            QMessageBox.warning(self, "입력 오류", "출고량은 1 이상의 숫자여야 합니다.")
            return
        
        success = self.db.shipment_products(id, stock_qty)

        if success:
            self.sq.setValue(0)
            QMessageBox.information(self, "성공", "출고가 완료되었습니다.")
            self.accept()
        else:
            QMessageBox.warning(self, "실패", "출고에 실패했습니다.")
            self.reject()
        