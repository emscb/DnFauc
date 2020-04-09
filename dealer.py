import time
from src.Auc import Auc

matList = {"전사의 함성 포션": 1, "무색 큐브 조각": 60, "생명의 숨결": 10, "청색 마력의 산물": 10}
priceList = {}
for m in matList.keys():
    a = Auc(m)
    l = a.crawl()
    count = 500
    amount = 0
    # 500개 사면 개당 얼만지 priceList에 추가
    for l1 in l:
        if l1['count'] >= count:
            amount += (l1['unitPrice'] * count)
            count = 0
        else:
            amount += l1['unitPrice'] * l1['count']
            count -= l1['count']
            continue
        priceList[m] = amount / 500
        print(m + "의 값이 저장되었습니다.")
        break
    if count > 0:
        priceList[m] = amount / count
        print(m + "의 값이 저장되었습니다.")
thp = Auc("투신의 함성 포션").crawl()[0]['unitPrice']
jjg = Auc("정신 자극의 비약").crawl()[0]['unitPrice']

print()

if thp >= priceList["전사의 함성 포션"] + priceList["무색 큐브 조각"] * 60:
    print("투함포는 만드세요.")
else:
    print("투함포는 경매장에서 사세요.")

if jjg >= priceList["생명의 숨결"]*10 + priceList["청색 마력의 산물"]*10:
    print("정자극은 만드세요.")
else:
    print("정자극은 경매장에서 사세요.")
time.sleep(10)
