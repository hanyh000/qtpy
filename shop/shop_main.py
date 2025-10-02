from PyQt5.QtWidgets import *
from shop_db_helper import DB, DB_CONFIG
from shop_stock import stock_dialog
from shop_shipment import shipment_dialog
from shop_remove import remove_dialog

class shopwindow(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("상점 재고 관리")
        self.resize(600,400)

        self.db = DB(**DB_CONFIG)

        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        form_box = QHBoxLayout()
        self.btn_sk = QPushButton("입고")
        self.btn_st = QPushButton("출고")
        self.btn_re = QPushButton("삭제")

        self.btn_sk.clicked.connect(self.stock)
        self.btn_st.clicked.connect(self.shipment)
        self.btn_re.clicked.connect(self.remove)

        form_box.addWidget(self.btn_sk)
        form_box.addWidget(self.btn_st)
        form_box.addWidget(self.btn_re)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["제품ID","제품명","가격","보유량"])
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)

        vbox.addLayout(form_box)
        vbox.addWidget(self.table)

        self.load_products()

    def load_products(self):
        rows = self.db.fetch_products()
        self.table.setRowCount(len(rows))
        for r, (product_id, product_name, price, stock_qty) in enumerate(rows):
            self.table.setItem(r,0,QTableWidgetItem(str(product_id)))
            self.table.setItem(r,1,QTableWidgetItem(product_name))
            self.table.setItem(r,2,QTableWidgetItem(str(price)))
            self.table.setItem(r,3,QTableWidgetItem(str(stock_qty)))

        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def stock(self):
        dlg = stock_dialog()
        if dlg.exec_( ) == stock_dialog.Accepted:
            self.load_products()
        self.show()
    def shipment(self):
        dlg = shipment_dialog()
        if dlg.exec_( ) == shipment_dialog.Accepted:
            self.load_products()
        self.show()
    def remove(self):
        dlg = remove_dialog()
        if dlg.exec_( ) == remove_dialog.Accepted:
            self.load_products()
        self.show()