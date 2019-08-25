import requests
import time
import sys


class Auc:
    def __init__(self, itemname):
        self.itemname = itemname
        self.url = 'https://api.neople.co.kr/df/auction?itemName=' + itemname + '&limit=5&sort=unitPrice:asc&apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'

    def crawl(self):   # json 처리만 된 row들의 list
        try:
            k = requests.get(self.url)
        except:
            print("경매장 정보를 가져오지 못했습니다."); return
        k = k.json()
        if 'error' in k.keys():
            print("Error code : {code}\nError message : {message}".format(code=k['error']['status'], message=k['error']['message']))
            return 0

        if len(k['rows']) == 0:
            print('등록된 아이템이 없거나 경매장에 등록할 수 없는 아이템입니다.\n')
            return
        else:
            return k['rows']

    def get_avgPrice(self):
        self.price = []
        # self.now = "%04d-%02d-%02d %02d:%02d" % (time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday,
        #                                               time.localtime().tm_hour, time.localtime().tm_min)
        # 어제의 평균가기 때문에 어제 요일을 찾음
        t = time.localtime()
        if t.tm_hour <= 5:
            t = time.localtime(time.time()-86400.0*2.0)
            self.now = '%04d-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday)
        else:
            t = time.localtime(time.time()-86400.0)
            self.now = '%04d-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday)
        wday = {0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}

        registed_list = self.crawl(self.url)
        try:
            for i in registed_list:
                if i['unitPrice'] != 0:
                    self.price.append([self.now, wday[t.tm_wday], i['itemName'], i['averagePrice']])
        except:
            print('경매장 정보를 가져오지 못했습니다.'); time.sleep(5); sys.exit()
        return self.price
