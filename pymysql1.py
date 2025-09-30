import pymysql

# 데이터베이스 연결
conn = pymysql.connect(
    host="localhost" ,
    user="root",
    password="as6106",
    database="sample",
    charset="utf8"
)

# 커서 생성
cur = conn.cursor()

# SQL 실행
cur.execute("SELECT VERSION()")
# cur.execute("create table users(ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, email VARCHAR(100))")
# SELECT * FROM users
# 결과 가져오기
result = cur.fetchone()
print("Database version:", result)

# 연결 종료
cur.close()
conn.close()