import sqlite3
conn = sqlite3.connect('test.db')

c = conn.cursor()
c.execute("CREATE TABLE test (id integer PRIMARY KEY, subject text, content text, date text)")
c.execute("INSERT INTO test VALUES (1, 'test1', 'test1 datas', '20250105')")
c.execute("INSERT INTO test VALUES (2, '두 번째 블로그', '두 번째 블로그입니다.', '20190827')")

_id = 3
subject = "세 번째 블로그"
content = "세 번째 블로그입니다."
date = "20190827"

c.execute("INSERT INTO test VALUES (:id,:subject,:content,:date)", {"id":_id,"subject": subject,"content": content, "date":date})
