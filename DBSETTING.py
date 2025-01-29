import sqlite3


print("1. Main Table을 삭제, INIT의 LastSongID를 0으로 설정")
print("2. 나가기")
selectNum = int(input("원하는 번호를 입력하십시오: "))
# 데이터베이스에 연결
conn = sqlite3.connect(r"databases\\songData.db")
cur = conn.cursor()


# 1. delete Main (***주의***)
if (selectNum ==1):
    print("실행합니까? 삭제한 파일은 되돌릴 수 없습니다.")
    YorN = input("(y/n): ")
    if (YorN =="y" or YorN =="Y"):
        cur.execute("DELETE FROM main")
        cur.execute("UPDATE INIT SET LastSongID = 0")
        conn.commit()
        print("DELETE COMPLETE!")
    else:
        pass
# 2. 나가기
elif (selectNum ==2):
    pass
conn.close()

