# 각 항목에 대해 경매장 평균가를 저장
from src.Auc import Auc
import time
import requests
import sqlite3
import json
from Config import KOA_URL

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
    price = j.get_avg_price()
    if price == -1:
        continue
    sq = '''INSERT INTO aucInfo VALUES(?,?,?,?,?)'''
    value = tuple(price[0])
    rm = c.execute(sq, value)
    conn.commit()
    print(time.ctime(), j.item_name, '\b의 가격이 입력되었습니다.')

add_list = []
sync_date = ""
t = time.localtime(time.time())
now = '%04d-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday)
try:
    sync_date = requests.get("{url}/config".format(url=KOA_URL))
    sync_date = sync_date.json()["dbsync"]
except requests.exceptions.ConnectionError:
    print("Koa와 연결하는 데 실패했습니다.")
except KeyError:
    print("DB 동기화 정보가 없습니다.")
else:
    if sync_date == now:
        print("DB 동기화가 이미 이뤄졌습니다.")
    else:
        add_list_table = c.execute(
            '''SELECT aucdate, itemName, itemId, avgPrice FROM aucInfo WHERE aucdate >= "{date}"'''
            .format(date=sync_date))

        for a in add_list_table:
            add_list.append(json.dumps({"date": a[0], "itemName": a[1], "itemId": a[2], "avgPrice": a[3]}))

        add_dict = {"list": add_list}

        try:
            r = requests.put("{url}/auc/{date}".format(url=KOA_URL, date=now), add_dict)
            if r.status_code == 413:
                print("동기화해야 할 데이터가 너무 많습니다.")
        except requests.exceptions.ConnectionError:
            print("Koa와 연결하는 데 실패했습니다.")

conn.close()

mm = 3
while mm > 0:
    time.sleep(1)
    mm -= 1
