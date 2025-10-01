from PyQt5.QtWidgets import  QDialog, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, \
QTableWidgetItem,QLabel, QLineEdit, QPushButton, QMessageBox,QDialog, QVBoxLayout, QFormLayout, \
QLineEdit, QPushButton, QMessageBox
from fruit_db_helper import DB, DB_CONFIG

class deliverying(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("배송 관리")
        self.db = DB(**DB_CONFIG)

        # 중앙 위젯 및 레이아웃
        vbox = QVBoxLayout()

        # 상단: 입력 폼 + 추가 버튼
        form_box = QHBoxLayout()
        self.input_name = QLineEdit()
        self.input_phone = QLineEdit()
        self.btn_add = QPushButton("배송시작")
        self.btn_add.clicked.connect(self.try_delivery)

        form_box.addWidget(QLabel("이름"))
        form_box.addWidget(self.input_name)
        form_box.addWidget(QLabel("전화번호"))
        form_box.addWidget(self.input_phone)
        form_box.addWidget(self.btn_add)

        # 중앙: 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["이름", "전화번호", "상품명", "구매량"])
        self.table.setEditTriggers(self.table.NoEditTriggers)  # 표준 예시: 목록은 읽기 전용
        self.table.verticalHeader().setVisible(False)

        # 배치
        vbox.addWidget(self.table)
        vbox.addLayout(form_box)

        self.setLayout(vbox)
        # 초기 데이터 로드
        self.load_buyers()
    def load_buyers(self):
        rows = self.db.fetch_buyers()
        self.table.setRowCount(len(rows))
        for r, (name, phone, product_name, buy_qty) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(name))
            self.table.setItem(r, 1, QTableWidgetItem(phone))
            self.table.setItem(r, 2, QTableWidgetItem(product_name))
            self.table.setItem(r, 3, QTableWidgetItem(str(buy_qty)))
        self.table.resizeColumnsToContents()

    def try_delivery(self):
        nm = self.input_name.text().strip()
        pe = self.input_phone.text().strip()
        if not nm or not pe:
            QMessageBox.warning(self, "오류", "이름과 전화번호를 모두 입력하세요.")
            return

        if self.db.verify_buyer(nm, pe):
            self.db.delivery(pe)

            self.accept()
        else:
            QMessageBox.critical(self, "실패", "아이디 또는 비밀번호가 올바르지 않습니다.")