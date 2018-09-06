from set_spe import *
import csv
while(True):
    try:
        w = open('material.txt', 'r')
    except:
        print('아이템 목록파일이 없습니다.')

    # 현재 경매장 판매 가격 계산 (avrList 작성)
    avrList = {}
    for i in w.readlines():
        i = i.strip()
        k = auc(i)
        k.crawl()
        p = k.process()
        k2 = calculate()
        avrList[i] = k2.avr(p)
        print(i+'의 가격이 저장되었습니다.')
    w.close()
    # print(avrList)

    # 제작 방법, 재료 저장 (recipeDict 작성)
    try:
        u2 = open('recipe.csv', 'r')
    except:
        print('레시피 정보가 없습니다.')
    u = csv.reader(u2)
    recipeDict = {}
    for line in u:
        tempDict = {}
        num = 0
        while(True):
            try:
                if line[1:][num] != '':
                    tempDict[line[1:][num]] = line[1:][num+1]
                    num+=2
                else:
                    break
            except:
                break
        recipeDict[line[0]] = tempDict
    # print(recipeDict)

    # 제작 방법에 따른 제작 비용 계산을 위한 객체 생성
    c = calculate()
    print()
    # 경매장에서 구매하지 않을 재료 분석 (reciptDict 변경)
    while(True):
        a = input('구매하지 않을 재료가 있습니까? 없으시면 Enter를 입력하십시오 : ')
        if a == '':
            break
        else:
            recipeDict = c.saving(recipeDict, a)

    # 제작 비용 계산 (manuPrice 작성)
    manuPrice = c.spend(avrList, recipeDict)
    if manuPrice == -1:
        print('프로그램이 다시 실행됩니다.\n')
    # print(manuPrice)

    print()
    # 100개 판매당 이익 계산
    c.benefit(avrList, manuPrice)
    time.sleep(3)