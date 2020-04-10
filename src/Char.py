import requests
import csv


class CharId:
    def __init__(self, name, server):
        self.url = 'https://api.neople.co.kr/df/servers/' + server + '/characters?characterName=' + name + '&apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'
        self.characterId = self.level = self.jobId = self.jodGrowId = self.jobName = self.jobGrowName = ""

    def run(self):
        try:
            k1 = requests.get(self.url)
            k = k1.json()['rows'][0]
        except requests.exceptions.ConnectionError:
            print('캐릭터 정보를 가져오지 못했습니다.'); return
        self.characterId = k['characterId']
        self.level = k['level']
        self.jobId = k['jobId']
        self.jodGrowId = k['jobGrowId']
        self.jobName = k['jobName']
        self.jobGrowName = k['jobGrowName']

        k1.close()


class CharInf:
    def __init__(self, id, server):
        self.url = 'https://api.neople.co.kr/df/servers/' + server + '/characters/' + id + '?apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'
        self.adventureName = self.guildId = self.guildName = ""

    def run(self):
        try:
            k1 = requests.get(self.url)
            k = k1.json()
        except requests.exceptions.ConnectionError:
            print('캐릭터 정보를 가져오지 못했습니다.'); return
        self.adventureName = k['adventureName']
        self.guildId = k['guildId']
        self.guildName = k['guildName']

        k1.close()


class CharSkill:
    def __init__(self, id, server):
        self.url = 'https://api.neople.co.kr/df/servers/' + server + '/characters/' + id + '/skill/style?apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'
        self.skillList = []

    def run(self):
        self.skillList = []
        try:
            k1 = requests.get(self.url)
            k = k1.json()
        except requests.exceptions.ConnectionError:
            print('캐릭터 정보를 가져오지 못했습니다.'); return
        for i in k['skill']['style']:
            for j in k['skill']['style'][i]:
                self.skillList.append([k['jobName'], j['name'], j['requiredLevel']])
                print(k['jobName'] + ' ' + j['name'] + ' 입력되었습니다.')
        self.save()

    def save(self):
        g = open('skillList.csv', 'a', newline='')
        wr = csv.writer(g)
        for k in self.skillList:
            wr.writerow(k)
        g.close()
        print('\n최종 입력이 완료되었습니다.\n')

