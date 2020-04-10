import requests
from src.Auc import Auc


class Item:
    def __init__(self, name):
        self.url = 'https://api.neople.co.kr/df/items?itemName=' + name + '&limit=20&wordType=match&apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'
        self.url2 = self.itemName = self.itemRarity = self.itemType = self.itemTypeDetail = self.itemAvailableLevel\
            = self.itemObtainInfo = self.itemExplainDetail = self.itemFlavorText = self.setItemName = self.itemName\
            = self.itemStatus = self.itemReinforceSkill = ""

    def select(self):
        item_list = []
        try:
            re2 = requests.get(self.url)
            re = re2.json()['rows']
            for i in re:
                item_list.append(i['itemName'])

            if len(item_list) == 0:
                print('\n결과가 없습니다.\n')
                return

            num = 1
            for item in item_list:
                print(str(num) + '. ' + item)
                num += 1
        except requests.exceptions.ConnectionError:
            print('\n아이템 정보를 가져오지 못했습니다.\n')
            return

        while 1:
            try:
                a = input('아이템을 선택하세요 : ')
                if a == '다시 검색':
                    break
                else:
                    self.itemId = re[int(a) - 1]['itemId']
                    self.run()
                    return
            except IndexError:
                print('\n정확한 번호를 입력해주세요! 다시 검색하시려면 "다시 검색"을 입력하세요\n')
                continue
        re2.close()

    def run(self):
        self.url2 = 'https://api.neople.co.kr/df/items/{id}?apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'.format(id=self.itemId)
        try:
            o1 = requests.get(self.url2)
            o = o1.json()
        except requests.exceptions.ConnectionError:  # 인터넷 연결 문제
            print('\n' + '아이템 정보를 가져오지 못했습니다.' + '\n')
            return
        self.itemName = o['itemName']
        self.itemRarity = o['itemRarity']
        self.itemType = o['itemType']
        self.itemTypeDetail = o['itemTypeDetail']
        self.itemAvailableLevel = o['itemAvailableLevel']
        self.itemObtainInfo = o['itemObtainInfo']
        self.itemExplainDetail = o['itemExplainDetail']
        try:
            self.itemFlavorText = o['itemFlavorText']
        except KeyError:
            self.itemFlavorText = None
        self.setItemName = o['setItemName']
        try:
            self.itemStatus = o['itemStatus']
        except KeyError:
            pass
        try:
            self.itemReinforceSkill = o['itemReinforceSkill']
        except KeyError:
            self.itemReinforceSkill = None

        o1.close()
        self.print_info()

    def print_info(self):
        if self.setItemName == "":
            print("\n{name}\n".format(name=self.itemName))
        else:
            print("\n{name}\n{setName}\n".format(name=self.itemName, setName=self.setItemName))
        print(self.itemRarity + ' ' + self.itemTypeDetail)
        print('레벨제한 ' + str(self.itemAvailableLevel))
        print(self.itemObtainInfo)
        print(self.itemExplainDetail + '\n')

        for status in self.itemStatus:
            if str(status['value'])[0] == '-':
                print("{name} {value}".format(name=status['name'], value=status['value']))
            else:
                print("{name} +{value}".format(name=status['name'], value=status['value']))

        for skill in self.itemReinforceSkill:
            print('\n' + skill['jobName'])
            if 'skills' in skill.keys():
                for skill in skill['skills']:
                    print("{name} +{value}".format(name=skill['name'], value=skill['value']))
            if 'levelRange' in skill.keys():
                for range in skill['levelRange']:
                    if range['minLevel'] != range['maxLevel']:
                        print("{min} ~ {max} Lv 스킬 + {value}".format(min=range['minLevel'], max=range['maxLevel'], value=range['value']))
                    else:
                        print("{min} Lv 스킬 + {value}".format(min=range['minLevel'], value=range['value']))

        if self.itemFlavorText is not None:
            print('\n' + self.itemFlavorText + '\n')

        self.price()

    def price(self):
        f = Auc(self.itemName)
        if not f.price:
            return
        else:
            print('어제 평균가 : ' + str(f.price[0][3]))
            print()
