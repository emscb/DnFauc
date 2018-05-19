import csv
import requests

class skill:
    def __init__(self, name):
        self.url = 'https://api.neople.co.kr/df/items?itemName=' + name + '&limit=30&wordType=full&apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'

    def listing(self):
        self.idList = []
        try:
            ce2 = requests.get(self.url)
            ce = ce2.json()['rows']
            for i in ce:
                self.idList.append(i['itemId'])
            if len(self.idList) == 0:
                print('\n' + '결과가 없습니다.' + '\n')
                return
        except:
            print('\n' + '아이템 정보를 가져오지 못했습니다.' + '\n'); return

    def run(self):
        self.itemList = []
        for l in self.idList:
            self.url2 = 'https://api.neople.co.kr/df/items/' + l + '?apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'
            re2 = requests.get(self.url2)
            re = re2.json()
            try:
                for i in re['itemReinforceSkill']:
                    try:
                        for j in range(len(i['skills'])):
                            self.itemList.append([re['itemName'], l, i['jobName'], re['itemTypeDetail'],
                                                  i['skills'][j]['name'], i['skills'][j]['value']])
                            print(re['itemName'] + ' 입력되었습니다.')
                    except:
                        for j in range(len(i['levelRange'])):
                            self.itemList.append([re['itemName'], l, i['jobName'], re['itemTypeDetail'], '모든 스킬',
                                                  i['levelRange'][j]['minLevel'], i['levelRange'][j]['maxLevel'], i['levelRange'][j]['value']])
                            print(re['itemName'] + ' 입력되었습니다.')
                    else:
                        try:
                            for j in range(len(i['levelRange'])):
                                self.itemList.append([re['itemName'], l, i['jobName'], re['itemTypeDetail'], '모든 스킬',
                                                      i['levelRange'][j]['minLevel'], i['levelRange'][j]['maxLevel'], i['levelRange'][j]['value']])
                                print(re['itemName'] + ' 입력되었습니다.')
                        except: continue
            except:
                pass

            re2.close()
        self.save()

    def save(self):
        g = open('C:/Users/관리자/Desktop/itemList.csv', 'a', newline='')
        wr = csv.writer(g)
        for k in self.itemList:
            wr.writerow(k)
        g.close()
        print('\n최종 입력이 완료되었습니다.\n')

