from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, \
QLineEdit, QPushButton, QMessageBox
from fruit_db_helper import DB, DB_CONFIG

class canceling(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("취소 신청")
        self.db = DB(**DB_CONFIG)

        self.phone = QLineEdit()

        form = QFormLayout()
        form.addRow("전화번호", self.phone)

        self.btn_buy = QPushButton("취소 신청")
        self.btn_buy.clicked.connect(self.try_cancel)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_buy)
        self.setLayout(layout)
        
    def try_cancel(self, phone):
        phone = self.phone.text()

        if not phone:
            QMessageBox.warning(self, "입력 오류", "전화번호를 입력하세요.")
            return

    # 구매 기록 존재 여부 확인
        try:
            with self.db.connect() as conn:
                with conn.cursor() as cur:
                    check_sql = "SELECT COUNT(*) FROM buyers WHERE phone = %s"
                    cur.execute(check_sql, (phone,))
                    count = cur.fetchone()[0]

                if count == 0:
                    QMessageBox.warning(self, "취소 실패", "해당 전화번호의 구매 기록이 없습니다.")
                    return
        except Exception as e:
            QMessageBox.critical(self, "오류", f"작업 중 오류 발생: {e}")
            return

    # cancel 메서드 호출
        if self.db.cancel(phone):
            QMessageBox.information(self, "성공", "구매 기록 취소 및 보유량 업데이트 완료")
            self.accept()
        else:
            QMessageBox.critical(self, "오류", "취소 처리 중 오류 발생")
            self.reject()
