import time
from set_auc import Auc

matList = {"전사의 함성 포션": 1, "무색 큐브 조각": 60, "생명의 숨결": 10, "청색 마력의 산물": 10}
priceList = {}
for m in matList.keys():
    a = Auc(m)
    l = a.crawl()
    for l1 in l:
        print(l1['count'])
        print(l1['unitPrice'])
