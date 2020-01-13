from tele_api import *
import requests
from bs4 import BeautifulSoup

url = "http://df.nexon.com/df/testinfo/notice"
k = requests.get(url)
bs = BeautifulSoup(k.text, 'html.parser')
all_strong = bs.find_all("strong")


T = Telegram('@dnfdodododo')
T.send()
