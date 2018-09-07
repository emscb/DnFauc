from set_spe import auc
import time

try:
    w = open('jonadan.txt', 'r')
except:
    print("목록파일이 없습니다.")

itemList = []


for i in w.readlines():
    x,y = i.split('-')[0], i.split('-')[1]
    y = int(y)
    itemList.append((x,y))

for i in itemList:
    a = auc(i[0])
    a.crawl()
    priceList = a.process()
    price = 0
    num = i[1]
    for j in priceList:
        if j[1] <= num:
            num-=j[1]
            price+=j[0]*j[1]
        else:
            price+=j[0]*num
            break
    # 정테를 살 경우 101380
    # 캔 정테로 살 경우 81110
    if price > 101380:
        print(i[0] + "는 테라를 사서라도 정테로 사세요.")
    elif price > 81110:
        print(i[0] + "는 테라를 캐서 테라로 사세요.")
    else:
        print(i[0] + "는 경매장에서 사세요.")
time.sleep(20)