import requests
from set_auc import Auc

class item:
    def __init__(self, name):
        # self.url = 'https://api.neople.co.kr/df/items?itemName=' + name + '&apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'
        self.url = 'https://api.neople.co.kr/df/items?itemName=' + name + '&limit=20&wordType=full&apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'

    def select(self):
        itemList = []
        try:
            re2 = requests.get(self.url)
            re = re2.json()['rows']
            for i in re:
                itemList.append(i['itemName'])

            if len(itemList) == 0:
                print('\n결과가 없습니다.\n')
                return

            num = 1
            for l in itemList:
                print(str(num) + '. ' + l)
                num += 1
        except:
            print('\n' + '아이템 정보를 가져오지 못했습니다.' + '\n'); return

        while(True):
            try:
                a = input('아이템을 선택하세요 : ')
                if a == '다시 검색': break
                else:
                    self.itemId = re[int(a) - 1]['itemId']
                    self.run(); return
            except:
                print('\n' + "정확한 번호를 입력해주세요! 다시 검색하시려면 '다시 검색'을 입력하세요" + '\n'); continue
        re2.close()

    def run(self):
        # try:
        self.url2 = 'https://api.neople.co.kr/df/items/' + self.itemId + '?apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'
        # except:
        #     print('\n' + '아이템 이름이 잘못되었습니다.' + '\n'); return
        try:
            o1 = requests.get(self.url2)
            o = o1.json()
        except:  # 인터넷 연결 문제
            print('\n' + '아이템 정보를 가져오지 못했습니다.' + '\n'); return
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
        self.printInf()

    def printInf(self):
        try:
            print('\n' + self.itemName + '\n' + self.setItemName + '\n')
        except:
            print('\n' + self.itemName + '\n')
        print(self.itemRarity + ' ' + self.itemTypeDetail)
        print('레벨제한 ' + str(self.itemAvailableLevel))
        print(self.itemObtainInfo)
        print(self.itemExplainDetail + '\n')
        try:
            for i in self.itemStatus:
                if str(i['value'])[0] == '-':
                    print(i['name'] + ' ' + str(i['value']))
                else:
                    print(i['name'] + ' +' + str(i['value']))
        except:
            pass

        try:
            for k in self.itemReinforceSkill:
                print('\n' + k['jobName'])
                try:
                    for l in k['skills']:
                        print(l['name'] + ' +' + str(l['value']))
                except KeyError:
                    for l in k['levelRange']:
                        if l['minLevel'] != l['maxLevel']:
                            print(str(l['minLevel']) + ' ~ ' + str(l['maxLevel']) + ' Lv 스킬 + ' + str(l['value']))
                        else:
                            print(str(l['minLevel']) + ' Lv 스킬 + ' + str(l['value']))
                else:
                    try:
                        for l in k['levelRange']:
                            if l['minLevel'] != l['maxLevel']:
                                print(str(l['minLevel']) + ' ~ ' + str(l['maxLevel']) + ' Lv 스킬 + ' + str(l['value']))
                            else:
                                print(str(l['minLevel']) + ' Lv 스킬 + ' + str(l['value']))
                    except KeyError:
                        continue
        except:
            pass

        if self.itemFlavorText != None:
            print('\n' + self.itemFlavorText)
            print()
        else: pass

        self.price()

    def price(self):
        f = Auc(self.itemName)
        f.run()
        if len(f.price) == 0:
            return
        else:
            print('어제 평균가 : ' + str(f.price[0][3]))
            print()