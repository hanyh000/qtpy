from PyQt5.QtWidgets import *
from fruit_db_helper import DB, DB_CONFIG
from fruit_buy import buying
from fruit_cancel import canceling
from fruit_delivery import deliverying
from fruit_edit import editing
from fruit_stock import stocking

class fruitWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("회원 관리")
        self.db = DB(**DB_CONFIG)

        # 중앙 위젯 및 레이아웃
        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

         # 상단: 입력 폼 + 추가 버튼
        form_box = QHBoxLayout()
        self.btn_stock = QPushButton("입고")
        self.btn_dvery = QPushButton("배송")
        self.btn_edit = QPushButton("수정")
        self.btn_ccl = QPushButton("취소")
        self.btn_buy = QPushButton("구매")
        self.btn_stock.clicked.connect(self.exam1)
        self.btn_dvery.clicked.connect(self.exam2)
        self.btn_edit.clicked.connect(self.exam3)
        self.btn_ccl.clicked.connect(self.exam4)
        self.btn_buy.clicked.connect(self.exam5)
        form_box.addWidget(self.btn_stock)
        form_box.addWidget(self.btn_dvery)
        form_box.addWidget(self.btn_edit)
        form_box.addWidget(self.btn_ccl)
        form_box.addWidget(self.btn_buy)
        
        
        # 중앙: 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["상품ID", "상품명", "보유량(box)", "가격"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)

        # 배치
        vbox.addLayout(form_box)
        vbox.addWidget(self.table)

        # 초기 데이터 로드
        self.load_product()

    def load_product(self):
        rows = self.db.fetch_products()
        self.table.setRowCount(len(rows))
        for r, (product_id, product_name, hold_qty, price) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(product_id)))
            self.table.setItem(r, 1, QTableWidgetItem(product_name))
            self.table.setItem(r, 2, QTableWidgetItem(str(hold_qty)))
            self.table.setItem(r, 3, QTableWidgetItem(str(price)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def exam1(self):  # 입고
        dlg = stocking()
        if dlg.exec_() == QDialog.Accepted:
            self.load_product()
        self.show()

    def exam2(self):  # 배송
        dlg = deliverying()
        if dlg.exec_() == QDialog.Accepted:
            self.load_product()
        self.show()

    def exam3(self):  # 수정
        dlg = editing()
        if dlg.exec_() == QDialog.Accepted:
            self.load_product()
        self.show()

    def exam4(self):  # 취소
        dlg = canceling()
        if dlg.exec_() == QDialog.Accepted:
            self.load_product()
        self.show()

    def exam5(self):  # 구매
        dlg = buying()
        if dlg.exec_() == QDialog.Accepted:
            self.load_product()
        self.show()