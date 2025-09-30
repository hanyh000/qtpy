import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        window = QWidget()
        layout = QVBoxLayout()
        
        # 테이블 생성
        table_view = QTableView()

        # 모델 생성 (행, 열)
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["이름", "나이", "번호"])
        
        # 행, 열 너비를 창 너비에 맞게 늘리기
        table_view.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                
        # 리스트 데이터 출력
        data_list = [
            ["홍길동", 25, 1],
            ["김철수", 30, 2],
            ["이영희", 28, 3],
            ["ㅇㅇㅇ", 30, 4]
        ]
        #입력갯수에 따라 행열 변화
        # 모델에 데이터 추가
        for row in data_list:
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)

        # 모델을 뷰(QTableView)에 연결
        table_view.setModel(model)

        layout.addWidget(table_view)
        window.setLayout(layout)
        self.setCentralWidget(window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()
