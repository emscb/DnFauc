# 각 항목에 대해 경매장 평균가를 저장
from src.set_auc import Auc
import time
import sqlite3

db_path = "auction.db"
itemList = []
itemObj = []
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    itemList_table = c.execute("SELECT itemName FROM item")

    for i in itemList_table:
        i = list(i)[0]
        itemList.append(i)

    print("경매장 정보 수집 중...\n")
    for k in itemList:
        obj = Auc(k)
        if obj.status:
            itemObj.append(obj)
        else:
            time.sleep(3)
            exit(-1)
    print("수집 완료\n")
except sqlite3.OperationalError:  # 테이블 없음
    print('DB가 경로상에 없습니다.')

for j in itemObj:
    price = j.get_avgPrice()
    if price == -1:
        continue
    sq = '''INSERT INTO aucInfo VALUES(?,?,?,?)'''
    value = tuple(price[0])
    rm = c.execute(sq, value)
    conn.commit()
    print(time.ctime(), j.itemname, '\b의 가격이 입력되었습니다.')

conn.close()

mm = 3
while mm > 0:
    time.sleep(1)
    mm -= 1
