import requests
import time


class Auc:
    def __init__(self, itemname):
        self.itemname = itemname
        self.limit = 5
        self.url = 'https://api.neople.co.kr/df/auction?itemName=' + itemname + \
                   '&limit=' + str(self.limit) + '&sort=unitPrice:asc&apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'

    # 처리된 row list 반환
    def crawl(self):
        try:
            k = requests.get(self.url)
        except: # 인터넷이 되지 않는 경우
            print("경매장 정보를 가져오지 못했습니다. 인터넷 연결을 확인하세요.")
            return -1

        k = k.json()
        if 'error' in k.keys(): # 서버에서 에러가 넘어온 경우
            print("Error code : {code}\nError message : {message}".format(code=k['error']['status'], message=k['error']['message']))
            return -1
        if len(k['rows']) == 0: # 결과가 없는 경우
            print('등록된 아이템이 없거나 경매장에 등록할 수 없는 아이템입니다.')
            return -1
        else:
            return k['rows']

    def get_avgPrice(self):
        self.price = []

        # 어제의 평균가이기 때문에 어제 요일을 찾음
        t = time.localtime()
        if t.tm_hour <= 5:
            t = time.localtime(time.time()-86400.0*2.0)
            self.now = '%04d-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday)
        else:
            t = time.localtime(time.time()-86400.0)
            self.now = '%04d-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday)
        wday = {0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}

        registed_list = self.crawl()
        if registed_list == -1:
            return -1

        try:
            for i in registed_list:
                if i['unitPrice'] != 0:
                    self.price.append([self.now, wday[t.tm_wday], i['itemName'], i['averagePrice']])
        except KeyError: # unitPrice가 없으면 평균가가 적혀있지 않음
            print('경매 중이 아닌 아이템이 없어 넘어갑니다.')
            return -1
        return self.price
