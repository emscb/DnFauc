import requests

itemname = "시간의 인도석"
limit = 5
url = 'https://api.neople.co.kr/df/auction?itemName=' + itemname + '&limit=' + str(limit) + '&sort=unitPrice:asc&apikey=nJeolB5EWc0nUNTYk62nFcPH3e9L9WJG'

k = requests.get(url)
k = k.json()
for i in k['rows']:
    if i['unitPrice'] != 0:
        print(i['itemName'], i['averagePrice'])

print(k)
