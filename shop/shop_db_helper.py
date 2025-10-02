import pymysql

DB_CONFIG = dict(
    host="localhost",
    user="root",
    password="as6106",
    database="shop",
    charset="utf8"
)

class DB:
    def __init__(self, **config):
        self.config = config

    def connect(self):
        return pymysql.connect(**self.config)
    
    def fetch_products(self):
        sql = "SELECT * FROM products ORDER BY product_id"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
            
    def stock_products(self, product_name, price, stock_qty):
        sql = "insert into products (product_name, price, stock_qty) values(%s, %s, %s)"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql,(product_name, price, stock_qty))
                conn.commit()
                return True
            
            except Exception as e:
                print(e)
                conn.rollback()
                return False
    
    def shipment_products(self, product_id, stock_qty):
        try:
            with self.connect() as conn:
                with conn.cursor() as cur:

                    check_sql = "SELECT stock_qty FROM products WHERE product_id = %s"
                    cur.execute(check_sql, (product_id,))
                    row = cur.fetchone()

                    if not row:
                        print("수정 실패: 해당 입고 기록 없음")
                        return False

                    current_stcok_qty = row[0]

                    if stock_qty > current_stcok_qty:
                        print("입고 실패: 출고량이 입고량보다 많음")
                        return False

                    new_stcok_qty = current_stcok_qty - stock_qty

                    update_products_sql = "UPDATE products SET stock_qty = %s WHERE product_id = %s"
                    cur.execute(update_products_sql, (new_stcok_qty, product_id))
                conn.commit()
            return True

        except Exception as e:
            print(f"edits error: {e}")
            conn.rollback()
            return False
    
    def delete_products(self, product_id) :
        sql = "DELETE FROM products WHERE product_id=%s"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (product_id,))
                conn.commit()
                return True
            
            except Exception as e:
                print(e)
                conn.rollback()
                return False