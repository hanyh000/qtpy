import pymysql

DB_CONFIG = dict(
    host="localhost",
    user = "root",
    password = "as6106",
    database = "sampledb",
    charset = "utf8"
)

class DB:
    def __init__(self, **config):
        self.config = config
    def connect(self):
        return pymysql.connect(**self.config)
    
    def verify_user(self, username, password):
        sql = "SELECT COUNT(*) FROM users WHERE username = %s AND password = %s"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(username,password))
                count, = cur.fetchone()
                return count == 1
    def fetch_members(self):
        sql = "SELECT id, name, email FROM members ORDER BY id"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
    def insert_member(self, name, email):
        sql = "INSERT INTO members (name, email) VALUES (%s,%s)"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (name,email))
                    conn.commit()
                    return True
            except Exception:
                conn.rollback()
                return False