from PyQt5.QtWidgets import *
from shop_db_helper import DB, DB_CONFIG

class stock_dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("입고")
        self.db= DB(**DB_CONFIG)

        self.pn = QLineEdit()
        self.pe = QLineEdit()
        self.sq = QSpinBox()

        form  = QFormLayout()
        form.addRow("상품명", self.pn)
        form.addRow("가격", self.pe)
        form.addRow("입고량", self.sq)

        buttonBOx = QHBoxLayout() 

        self.btn_sk = QPushButton("입고")
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
        pn = self.pn.text().strip()
        pe = self.pe.text().strip()
        sq = self.sq.value()

        if not pn or not pe or not sq:
            QMessageBox.warning(self, "오류", "모든 정보를 기입하시오")
            return
        
        ok = self.db.stock_products(pn,pe,sq)
        if ok:
            QMessageBox.information(self,"완료", "입고되었습니다")
            self.accept()

        else:
            QMessageBox.critical(self,"실패","입고 도중 문제 발생")
            self.reject()