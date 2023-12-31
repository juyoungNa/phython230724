# db1.py

import sqlite3

#연결객체 생성(일단은 메모리에서 연습)
con = sqlite3.connect(":memory:")
#커서객체
cur = con.cursor()
#테이블 구조 생성
cur.execute("""
CREATE TABLE IF NOT EXISTS PhoneBook 
(id integer primary key autoincrement,
name text, phoneNum text);
""" )

#1건입력
cur.execute("""
INSERT INTO PhoneBook
 (name, phoneNum)
VALUES
 ('홍길동','010-111');
 """)

#입력 파라메터 처리
name = "전우치"
phoneNumber = "010-222"
cur.execute("""
INSERT INTO PhoneBook
 (name, phoneNum)
VALUES
 (?,?);
""", (name, phoneNumber))

#다중의 행을 입력
datalist = (("이순신", "010-333"),("박문수", "010-123"))
cur.executemany("""
INSERT INTO PhoneBook
 (name, phoneNum)
VALUES
 (?,?);
""", datalist)

#검색구문
cur.execute("""
SELECT *
  FROM PhoneBook
-- WHERE id = 3
;
""")
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))

cur.execute("""
SELECT id
     , name
     , phoneNum
  FROM PhoneBook
;
""")
print("---fetchall()---")
print(cur.fetchall())


# for row in cur:
#     print(row)
