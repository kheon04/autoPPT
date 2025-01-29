import sqlite3


# DB 작업시, 반드시 try, finally문을 활용할것: 리소스 누수, 커밋 유지를 위해
try:
    # 데이터베이스에 연결
    conn = sqlite3.connect(r"databases\\songData.db")

    # 커서 생성
    cur = conn.cursor()

    # PRAGMA를 사용하여 테이블 정보 추출
    cur.execute(f"PRAGMA table_info(Main)")
    columns_info = cur.fetchall()

    # 열 이름 추출 및 출력
    column_names = [column[1] for column in columns_info]  # 1번 인덱스가 열 이름
    print("Column Names:", column_names)

    # 데이터 삽입 SQL 문
    insert_sql = "INSERT INTO Main (ID, SongID, SlideNum, Signs, Line) VALUES (?, ?, ?, ?, ?);"

    artistNames =[]
    artistName = input("아티스트 이름을 입력하십시오 (0 to exit): ")
    while (artistName != "0"):
      artistNames.append(artistName)
      print(artistNames)
      artistName = input("아티스트 이름을 입력하십시오 (0 to exit): ")

    # artistNames = ['마커스', '아이자야 씩스티원', '어노인팅', '예람워십', '예수전도단', 'WELOVE', '제이어스', '팀룩워십', '피아워십', '히즈윌']
    for name in artistNames:
      insert_sql = "INSERT INTO Artist (Name) VALUES (?)"
      cur.execute(insert_sql, (name,))
    
    # conn의 현재 작업 내용을 저장
    conn.commit()

finally:
    # 연결 종료 (예외가 발생해도 실행됨)
    conn.close()


# 한 묶음. 이대로 사용하기
try:
    # 데이터베이스에 연결
    conn = sqlite3.connect(r"databases\\songData.db")

    # 커서 생성
    cur = conn.cursor()
    # 다중의 행을 삽입
    userlist = (("이순신","30"), ("박문수","27"))
    cur.executemany(insert_sql, userlist)

finally:
    # 연결 종료 (예외가 발생해도 실행됨)
    conn.close()