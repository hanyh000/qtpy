#과일 상점
#과일 종류 : 사과, 레몬, 포도, 자몽, 귤 등등
#테이블 구성 : buyer 와 product로 구분후 product_name으로 연동하여 구매하고자 하는 양과 제품 보유량을 계산
#구매자와 구매하고자 하는 과일 구매량 보유량을 표형태로 출력
#모든 종류의 과일 보유량을 출력한 후 구매자와 전화번호, 과일이름, 구매량을 입력하고 추가 보유량을 추가한 구매량으로 줄인후 전종목 과일 보유량을 재표시
#buyers 컬럼은 name, phone, product_name, buy_qty
#products 컬럼은 product_id, product_name, hold_qty, price
#수정 버튼을 누르면 사용자의 이름과 전화번호를 입력받고 과일이름과 구매량을 재입력 후 보유량에 수정전 구매량을 더하여 보유량 복구
#취소 버튼을 누르면 사용자의 이름과 전화번호를 입력받고  보유량에 취소전 구매량을 더하여 보유량 복구
#배송 버튼을 누르면 사용자 정보를 체크박스 형식으로 출력하고 사용자 체크후 배송시작 버튼을 누르면 데이터 베이스에서 사용자 정보를 지움
#관리자용 입고버튼을 누르면 과일 이름과 입고량을 입력받고 보유량에 입고량을 더하여 전체 과일 갯수 목록 출력
#메인.py를 기반으로 버튼을 누르면 buy.py, delivery.py, cancel.py, edit.py, stock.py 해당하는 버튼에 파일 창이 실행되고 완료하면 다시 메인.py로 돌아오게끔 할것인데 너가 코드를 짜지 않고 도움만 주는 형식으로 도와주면 좋겠어
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

    #구매자 정보 넘기기
    def verify_buyers(self,name, phone):
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
    def fetch_buyers(self):
        sql = "SELECT name, phone, product_name, buy_qty FROM buyers ORDER BY name"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()


    # 구매자 정보
    def insert_or_update_buyer(self, name, phone, product_name, buy_qty):
        try:
            with self.connect() as conn:
                with conn.cursor() as cur:
                # 이미 구매 기록이 있는지 확인
                    sql_check = "SELECT buy_qty FROM buyers WHERE phone = %s AND product_name = %s"
                    cur.execute(sql_check, (phone, product_name))
                    result = cur.fetchone()

                    if result:
                    # 기존 구매량 업데이트
                        new_qty = result[0] + buy_qty
                        sql_update = "UPDATE buyers SET buy_qty = %s WHERE phone = %s AND product_name = %s"
                        cur.execute(sql_update, (new_qty, phone, product_name))
                    else:
                    # 신규 구매 기록 삽입
                        sql_insert = "INSERT INTO buyers (name, phone, product_name, buy_qty) VALUES (%s, %s, %s, %s)"
                        cur.execute(sql_insert, (name, phone, product_name, buy_qty))
                conn.commit()
            return True
        except Exception as e:
            print(f"insert_or_update_buyer error: {e}")
            return False
        
    def delete_buyers(self, name, phone, product_name, buy_qty):
        check_sql = "SELECT COUNT(*) FROM buyers WHERE name=%s AND phone=%s AND product_name=%s"
        delete_sql = "DELETE FROM buyers WHERE VALUES (%s, %s, %s, %s)"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(check_sql, (name, phone, product_name))
                count, = cur.fetchone()
                if count > 0:
                    print("이미 구매 기록이 존재합니다.")
                    return False
                else:
                    try:
                        cur.execute(delete_sql, (name, phone, product_name, buy_qty))
                        conn.commit()
                        return True
                    except Exception as e:
                        print(f"insert_buyers error: {e}")
                        conn.rollback()
                        return False

        
    #구매 신청시 보유량 계산
    def buying(self):
        try:
            with self.connect() as conn:
                with conn.cursor() as cur:
                    # 예: products 테이블 보유량 업데이트 쿼리 실행
                    update_sql = "UPDATE products p JOIN buyers b ON p.product_name = b.product_name SET p.hold_qty = p.hold_qty - b.buy_qty" 
                    cur.execute(update_sql)
                conn.commit()
        except Exception as e:
            print(f"buying error: {e}")
            raise


    def cancel(self, phone):
        try:
            with self.connect() as conn:
                with conn.cursor() as cur:
                # 보유량 증가 처리 (기존 구매량 products에 반영)
                    cur.execute("SELECT product_name, buy_qty FROM buyers WHERE phone = %s", (phone,))
                    buys = cur.fetchall()

                    for product_name, buy_qty in buys:
                        update_sql = "UPDATE products SET hold_qty = hold_qty + %s WHERE product_name = %s"
                        cur.execute(update_sql, (buy_qty, product_name))

                # 구매 기록 삭제
                    delete_sql = "DELETE FROM buyers WHERE phone = %s"
                    cur.execute(delete_sql, (phone,))

                conn.commit()
                return True
        except Exception as e:
            print(f"cancel error: {e}")
            return False
            
        except Exception as e:
            print(f"buying Error: {e}")
            raise
    
    def edits(self, name, phone, product_name, edit_qty):
        try:
            with self.connect() as conn:
                with conn.cursor() as cur:
                    # 1. 기존 구매량 조회
                    check_sql = "SELECT buy_qty FROM buyers WHERE name = %s AND phone = %s AND product_name = %s"
                    cur.execute(check_sql, (name, phone, product_name))
                    row = cur.fetchone()

                    if not row:
                        print("수정 실패: 해당 구매 기록 없음")
                        return False

                    current_buy_qty = row[0]

                # 2. 수정량 > 구매량 → 오류
                    if edit_qty > current_buy_qty:
                        print("수정 실패: 수정량이 구매량보다 많음")
                        return False

                    new_buy_qty = current_buy_qty - edit_qty

                # 3. buyers 테이블 업데이트
                    update_buyers_sql = " UPDATE buyers SET buy_qty = %s WHERE name = %s AND phone = %s AND product_name = %s"
                    cur.execute(update_buyers_sql, (new_buy_qty, name, phone, product_name))

                # 4. products 테이블 보유량 증가
                    update_products_sql = "UPDATE products SET hold_qty = hold_qty + %s WHERE product_name = %s"
                    cur.execute(update_products_sql, (edit_qty, product_name))

                conn.commit()
            return True

        except Exception as e:
            print(f"edits error: {e}")
            return False

    def verify_buyer (self,name,phone):
        sql = "SELECT COUNT(*) FROM buyers WHERE name=%s AND phone=%s"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))
                count, = cur.fetchone()
                return count == 1
            
    def delivery(self,phone):
        sql = "DELETE FROM buyers WHERE phone = %s"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (phone,))
            conn.commit()
            
    def stocks(self, product_id, product_name, price, stock_qty):
            with self.connect() as conn:
                with conn.cursor() as cur:
                    check_sql = "SELECT hold_qty FROM products WHERE product_id = %s AND product_name = %s AND price = %s"
                    cur.execute(check_sql, (product_id,product_name,price))
                    row = cur.fetchone()
                    if row:
                        new_qty = row[0]+ stock_qty
                        update_sql = "UPDATE products SET hold_qty = %s WHERE product_id = %s AND product_name = %s AND price =%s"
                        cur.execute(update_sql, (new_qty, product_id, product_name, price))
                    else:
                        sql_insert = "INSERT INTO products (product_id, product_name, hold_qty, price) VALUES (%s, %s, %s, %s)"
                        cur.execute(sql_insert, (product_id, product_name, stock_qty, price ))
                conn.commit()
            return True
                    