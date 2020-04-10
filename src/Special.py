from src.Auc import Auc
import time
from tele_api import *


class AucInfo:
    def __init__(self, name):
        self.itemName = name
        self.aucList = self.priceList = []

    def crawl(self):  # 경매장 정보 받아오기
        a = Auc(self.itemName)
        a.limit = 100
        self.aucList = a.crawl()

        if len(self.aucList) == 0:
            print('등록된 아이템이 없습니다.\n잠시 후 창이 닫힙니다.')
            time.sleep(5)
            exit()

    def process(self):  # (개당가, 개수) list of tuple 생성/반환
        for k in self.aucList:
            if k['unitPrice'] != 0:
                self.priceList.append((k['unitPrice'], k['count']))
        return self.priceList


class Calculate:
    def __init__(self):
        self.priceList = self.avrList = []
        self.recipeDict = self.manuPrice = {}

    def avr(self, price_list):  # (개당가, 개수) list에서 하나씩 500개 살 경우 개당 가격 계산
        self.priceList = price_list
        sum = 0
        div = 0
        sum2 = 0
        for i in self.priceList:
            if sum2 + i[1] > 500:
                sum += i[0] * (500 - sum2) ** 2
                div += (500 - sum2) ** 2
                break
            else:
                sum += i[0] * i[1] ** 2
                div += i[1] ** 2
                sum2 += i[1]
        avg = sum / div
        return avg

    def spend(self, price_list, recipe_dict):
        self.avrList = price_list
        self.recipeDict = recipe_dict
        self.manuPrice = {}
        for i in self.recipeDict.keys():
            price = 0
            try:
                for j in self.recipeDict[i].keys():
                    price += self.avrList[j] * int(self.recipeDict[i][j])
                # 이득을 못보는 아이템은 애초에 추가하지 않음
                if price < self.avrList[i]:
                    self.manuPrice[i] = price
            except Exception as a:
                print(a, end='')
                print('의 가격정보가 저장되어있지 않습니다.')
                try:
                    w = open('material.txt', 'a')
                except FileNotFoundError:
                    print('아이템 목록파일이 없습니다.')
                w.write(str(a)[1:-1] + '\n')
                print('아이템 목록에 추가합니다.')
                w.close()
                return -1
        return self.manuPrice

    def saving(self, recipe_dict, thing):
        self.recipeDict = recipe_dict
        a = thing
        if a == '':
            return self.recipeDict
        for i in self.recipeDict.keys():
            for j in self.recipeDict[i].keys():
                if j == a:
                    self.recipeDict[i][j] = 0
        return self.recipeDict

    def benefit(self, price_list, manu_list):
        self.sellingPrice = price_list
        self.madePrice = manu_list
        self.benePrice = []
        if self.madePrice == -1:
            return
        for i in self.madePrice.keys():
            self.benePrice.append([i, int((self.sellingPrice[i] - self.madePrice[i]) * 97)])

        # 이익이 큰 순으로 정렬
        self.benePrice = sorted(self.benePrice, key=lambda x: x[1], reverse=True)

        message = ''
        for j in self.benePrice:
            print('%-14s\t100개당 %6d만큼의 이득입니다.' % (j[0], j[1]))
            message += '%-14s\t100개당 %6d만큼의 이득입니다.\n' % (j[0], j[1])

        T = Telegram('@dnfdodododo')
        T.send(message)
        time.sleep(30)
