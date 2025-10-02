from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, \
QLineEdit, QPushButton, QMessageBox
from fruit_db_helper import DB, DB_CONFIG

class editing(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("수정 신청")
        self.db = DB(**DB_CONFIG)

        self.name = QLineEdit()
        self.phone = QLineEdit()
        self.product_name = QLineEdit()
        self.edit_qty = QLineEdit()

        form = QFormLayout()
        form.addRow("이름", self.name)
        form.addRow("전화번호", self.phone)
        form.addRow("상품명", self.product_name)
        form.addRow("수정량", self.edit_qty)


        self.btn_edit = QPushButton("수정 신청")
        self.btn_edit.clicked.connect(self.try_edit)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_edit)
        self.setLayout(layout)
        
    def try_edit(self):
        name = self.name.text().strip()
        phone = self.phone.text().strip()
        product_name = self.product_name.text().strip()
        edit_qty_text = self.edit_qty.text().strip()

    # 입력값 검증
        if not (name and phone and product_name and edit_qty_text):
            QMessageBox.warning(self, "입력 오류", "모든 정보를 입력하세요.")
            return

        try:
            edit_qty = int(edit_qty_text)
            if edit_qty <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "입력 오류", "수정량은 1 이상의 숫자여야 합니다.")
            return

    # DB edits() 호출
        success = self.db.edits(name, phone, product_name, edit_qty)

        if success:
            self.edit_qty.setText("0")
            QMessageBox.information(self, "성공", "수정이 완료되었습니다.")
            self.accept()
        else:
            QMessageBox.warning(self, "실패", "수정에 실패했습니다. 정보 또는 수량을 확인하세요.")
            self.reject()