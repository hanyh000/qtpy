from PyQt5.QtWidgets import *
from shop_db_helper import DB, DB_CONFIG

class remove_dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("삭제")
        self.db= DB(**DB_CONFIG)

        self.id = QLineEdit()

        form  = QFormLayout()
        form.addRow("상품id", self.id)

        buttonBOx = QHBoxLayout() 

        self.btn_re = QPushButton("삭제")
        self.btn_re.clicked.connect(self.removes)
        self.btn_cc = QPushButton("취소")
        self.btn_cc.clicked.connect(self.reject)

        buttonBOx.addWidget(self.btn_re)
        buttonBOx.addWidget(self.btn_cc)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(buttonBOx)
        self.setLayout(layout)

    def removes(self):
        id = self.id.text().strip()
        if not id:
            QMessageBox.warning(self, "오류", "id를 입력하시오.")
            return
        
        ok = self.db.delete_products(id)
        if ok:
            QMessageBox.information(self, "완료", "삭제되었습니다.")
            self.accept()

        else:
            QMessageBox.critical(self, "실패", "삭제 중 오류가 발생했습니다.")
            self.reject()