import csv
import requests
from Config import API_KEY


class Skill:
    def __init__(self, name):
        self.url = 'https://api.neople.co.kr/df/items?itemName={name}&limit=30&wordType=match&apikey={key}'\
            .format(name=name, key=API_KEY)
        self.itemList = []
        self.idList = []

    def listing(self):
        try:
            ce2 = requests.get(self.url)
            ce = ce2.json()['rows']
            for i in ce:
                self.idList.append(i['itemId'])
            if len(self.idList) == 0:
                print('\n결과가 없습니다.\n')
                return
        except requests.exceptions.ConnectionError:
            print('\n아이템 정보를 가져오지 못했습니다.\n')
            return

    def run(self):
        for id in self.idList:
            url2 = 'https://api.neople.co.kr/df/items/{id}?apikey={key}'.format(id=id, key=API_KEY)
            try:
                re2 = requests.get(url2)
                re = re2.json()
            except requests.exceptions.ConnectionError:
                print("\n아이템 정보를 가져오지 못했습니다.\n")
                return

            try:
                reinforce_skill = re['itemReinforceSkill']
            except KeyError:
                reinforce_skill = re['itemBuff']['reinforceSkill']

            for i in reinforce_skill:
                try:
                    for j in range(len(i['skills'])):
                        self.itemList.append([re['itemName'], id, i['jobName'], re['itemTypeDetail'],
                                              i['skills'][j]['name'], i['skills'][j]['value']])
                        print(re['itemName'] + ' 입력되었습니다.')
                except KeyError:
                    for j in range(len(i['levelRange'])):
                        self.itemList.append([re['itemName'], id, i['jobName'], re['itemTypeDetail'], '모든 스킬',
                                              i['levelRange'][j]['minLevel'], i['levelRange'][j]['maxLevel'],
                                              i['levelRange'][j]['value']])
                        print(re['itemName'] + ' 입력되었습니다.')

            re2.close()
        self.save()

    def save(self):
        g = open('itemList.csv', 'a', newline='')
        wr = csv.writer(g)
        for k in self.itemList:
            wr.writerow(k)
        g.close()
        print('\n최종 입력이 완료되었습니다.\n')
