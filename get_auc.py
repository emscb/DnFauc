from set_auc import Auc
import time

itemList = []
itemObj = []
try:
    w = open('auction.txt', 'r')
except:
    print('목록파일이 없습니다.')

for i in w.readlines():
    itemList.append(i.strip())
    # j = i.strip().split('-')

for k in itemList:
    itemObj.append(Auc(k))

for j in itemObj:
    price = j.get_avgPrice()
    j.save_in_csv(price, 'auction.csv')
    print(time.ctime(), j.itemname, '\b의 가격이 입력되었습니다.')

mm = 5
while mm > 0:
    print(mm, '초 후 창이 닫힙니다.')
    time.sleep(1)
    mm -= 1
