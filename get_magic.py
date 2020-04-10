from src.Special import *
from tele_api import *

material = ['생명의 숨결', '용의 심장', '황금 가루', '하급 원소결정', '두툼한 고기']
matPrice = {}
matPrice2 = {}
# 각각의 매입가 작성 (matPrice 작성)
for m in material:
    a = AucInfo(m)
    a.crawl()

    # 현재 1000개 매입가로 계산
    priceList = a.process()
    c = Calculate()
    cost = c.avr(priceList)
    matPrice[m] = cost

    # 어제의 평균가로 계산
    matPrice2[m] = a.aucList[0]['averagePrice']

print(matPrice)
print(matPrice2)

# 기준 계산
strd = (matPrice['생명의 숨결'] * 28 + matPrice['용의 심장'] * 9 + matPrice['황금 가루'] * 9 + matPrice['하급 원소결정'] * 9
        + matPrice['두툼한 고기'] * 9) / 4.0
strd2 = (matPrice2['생명의 숨결'] * 28 + matPrice2['용의 심장'] * 9 + matPrice2['황금 가루'] * 9 + matPrice2['하급 원소결정'] * 9
         + matPrice2['두툼한 고기'] * 9) / 4.0

print('현재 매입가 기준 : ' + str(strd * 97 / 100))
print('어제 평균가 기준 : ' + str(strd2 * 97 / 100))

T = Telegram('@dnfdodododo')
T.send('현재 매입가 기준 : ' + str(int(strd * 97 / 100)) + '\n어제 평균가 기준 : ' + str(int(strd2 * 97 / 100)))
