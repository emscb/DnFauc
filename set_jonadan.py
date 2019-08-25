from set_spe import auc
import time

try:
    w = open('jonadan.txt', 'r')
except:
    print("목록파일이 없습니다.")

itemList = []
priceList = []
itemLimitList = {}
calcList = []

for i in w.readlines():
    x, y = i.split('-')[0], i.split('-')[1]
    y = float(y)
    itemList.append((x,y))
    itemLimitList[x] = int(i.split('-')[2])

for i in itemList:
    a = auc(i[0])
    a.crawl()
    aucList = a.process()
    price = 0
    num = i[1]
    for j in aucList:
        if j[1] <= num:
            num -= j[1]
            price += j[0]*j[1]
        else:
            price += j[0]*num
            break
    # 정테를 살 경우 개당 101380
    # 캔 정테로 살 경우 개당 81110
    if price > 101380:
        print(i[0] + "는 테라를 사서라도 정테로 사세요."); priceList.append((i[0],price))
    elif price > 81110:
        print(i[0] + "는 테라를 캐서 테라로 사세요."); priceList.append((i[0],price))
    else:
        print(i[0] + "는 경매장에서 사세요.")
print()

if len(priceList) == 0:
    print(str(1013800) + "골드보다 비싼 카드를 드세요!")
    print(str(506900) + "골드보다 비싼 레어 카드를 드세요!"); time.sleep(5); exit()

priceList.sort(key=lambda x: x[1], reverse=True)
for i in priceList:
    for j in range(itemLimitList[i[0]]):
        calcList.append((i[0], i[1]))

r = 0
sum = 0
while(r<10):
    try:
        print(calcList[r][0] + " 사세요.")
        sum += calcList[r][1]
        r += 1
    except IndexError:
        print("경매장 정보가 없습니다."); exit()
sum = int(sum*100/97)
print('\n' + str(sum) + "골드보다 비싼 카드를 드세요!")
r = 0
sum = 0
while(r<6):
    sum += calcList[r][1]
    r += 1
    sum = int(sum)
print('\n' + str(sum) + "골드보다 비싼 레어 카드를 드세요!")
time.sleep(10)
