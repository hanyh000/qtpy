from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, \
    QLabel, QLineEdit, QPushButton, QMessageBox
from fruit_db_helper import DB, DB_CONFIG

class MainWindow(QMainWindow):
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
        self.btn_add = QPushButton("입고")
        self.btn_add = QPushButton("수정")
        self.btn_add = QPushButton("취소")
        self.btn_add = QPushButton("구매")
        self.btn_add.clicked.connect(self.add_member)
        self.btn_add.clicked.connect(self.add_member)
        self.btn_add.clicked.connect(self.add_member)
        self.btn_add.clicked.connect(self.add_member)
        
        # 중앙: 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["상품ID", "상품명", "보유량", "가격"])
        self.table.setEditTriggers(self.table.NoEditTriggers)  # 표준 예시: 목록은 읽기 전용
        self.table.verticalHeader().setVisible(False)

        # 배치
        vbox.addLayout(form_box)
        vbox.addWidget(self.table)

        # 초기 데이터 로드
        self.load_buyers()

    def load_product(self):
        rows = self.db.fetch_buyers()
        self.table.setRowCount(len(rows))
        for r, (product_id, product_name, hold_qty, price) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(product_id)))
            self.table.setItem(r, 1, QTableWidgetItem(product_name))
            self.table.setItem(r, 2, QTableWidgetItem(hold_qty))
            self.table.setItem(r, 3, QTableWidgetItem(price))
        #self.table.resizeColumnsToContents()

    def add_member(self):
        name = self.input_name.text().strip()
        email = self.input_email.text().strip()
        if not name or not email:
            QMessageBox.warning(self, "오류", "이름과 이메일을 모두 입력하세요.")
            return
        ok = self.db.insert_member(name, email)
        if ok:
            QMessageBox.information(self, "완료", "추가되었습니다.")
            self.input_name.clear()
            self.input_email.clear()
            self.load_members()
        else:
            QMessageBox.critical(self, "실패", "추가 중 오류가 발생했습니다.")