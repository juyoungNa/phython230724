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

#검색구문
cur.execute("""
SELECT *
  FROM PhoneBook;
""")
for row in cur:
    print(row)