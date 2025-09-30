#과일 상점
#과일 종류 : 사과, 레몬, 포도, 자몽, 귤 등등
#테이블 구성 : buyer 와 product로 구분후 product_name으로 연동하여 구매하고자 하는 양과 제품 보유량을 계산
#구매자와 구매하고자 하는 과일 구매량 보유량을 표형태로 출력
#모든 종류의 과일 보유량을 출력한 후 구매자와 전화번호, 과일이름, 구매량을 입력하고 추가 보유량을 추가한 구매량으로 줄인후 전종목 과일 보유량을 재표시
#buyers 컬럼은 name, phone, product_name, buy_qty
#products 컬럼은 product_id, product_name, hold_qty, price
#수정 버튼을 누르면 사용자의 이름과 전화번호를 입력받고 과일이름과 구매량을 재입력 후 보유량에 수정전 구매량을 더하여 보유량 복구
#취소 버튼을 누르면 사용자의 이름과 전화번호를 입력받고  보유량에 취소전 구매량을 더하여 보유량 복구
#관리자용 입고버튼을 누르면 과일 이름과 입고량을 입력받고 보유량에 입고량을 더하여 전체 과일 갯수 목록 출력
# db_helper.py
import pymysql

DB_CONFIG = dict(
    host="localhost",
    user="root",
    password="as6106",
    database="fruitdb",
    charset="utf8"
)

class DB:
    def __init__(self, **config):
        self.config = config

    def connect(self):
        return pymysql.connect(**self.config)

    #구매자 정보 입력
    def verify_user(self, name, phone):
        sql = "SELECT COUNT(*) FROM buyers WHERE name=%s AND phone=%s"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))
                count, = cur.fetchone()
                return count == 1

    # 과일 전체 조회
    def fetch_products(self):
        sql = "SELECT product_id, product_name, hold_qty, price FROM products ORDER BY product_name"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()

    # 구매자 정보
    def insert_buyers(self, name, phone, product_name,buy_qty):
        sql = "INSERT INTO buyers (name, phone, product_name,buy_qty) VALUES (%s, %s, %s,%s)"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (name, phone, product_name,buy_qty))
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False
    #