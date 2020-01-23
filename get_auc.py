# 각 항목에 대해 경매장 평균가를 저장
from set_auc import Auc
import time
import sqlite3

db_path = "auction.db"
itemList = []
itemObj = []
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c2 = c.execute("SELECT itemName FROM item")
except:
    print('DB가 경로상에 없습니다.')

for i in c2:
    i = list(i)[0]
    itemList.append(i)

for k in itemList:
    itemObj.append(Auc(k))

for j in itemObj:
    price = j.get_avgPrice()
    sq = '''INSERT INTO aucInfo VALUES(?,?,?,?)'''
    try:
        value = tuple(price[0])
    except:
        print("%s의 가격 정보가 이상해서 넘어갑니다." % j.itemname); continue
    rm = c.execute(sq, value)
    conn.commit()
    print(time.ctime(), j.itemname, '\b의 가격이 입력되었습니다.')

conn.close()

mm = 3
while mm > 0:
    time.sleep(1)
    mm -= 1
