import sys
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        window = QWidget()
        layout = QVBoxLayout()
        
        # QTableWidget 생성 (행 개수, 열 개수)
        table = QTableWidget(3, 2)  # 3행 2열
        table.setHorizontalHeaderLabels(["이름", "나이", "번호"])

        # 행, 열 너비를 창 너비에 맞게 늘리기
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # 리스트 데이터 출력
        data_list = [
            ["홍길동", 25, 1],
            ["김철수", 30, 2],
            ["이영희", 28, 3],
            ["ㅇㅇㅇ", 30, 4]
        ]
        #행열 초과시 초과 부분 출력 안함
        # 리스트 요소를 테이블에 하나씩 넣는 작업 
        for row, (name, age, num) in enumerate(data_list):
            # 행, 열, 그리고 데이터 
            table.setItem(row, 0, QTableWidgetItem(name))
            table.setItem(row, 1, QTableWidgetItem(str(age)))
            table.setItem(row, 2, QTableWidgetItem(str(num)))

        layout.addWidget(table)
        window.setLayout(layout)
        self.setCentralWidget(window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()