from tele_api import *
import requests
import time
from bs4 import BeautifulSoup

T = Telegram('@dnfdodododo')
trs = []
while 1:
    try:
        response = requests.get("http://df.nexon.com/df/testinfo/notice")
    except requests.exceptions.ConnectionError:
        print("인터넷 연결 실패")
        continue

    if response.status_code != 200:
        print("Error code : {code}".format(code=response.status_code))
        continue
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        tr = soup.select('table.tbl > tbody > tr > td > a')
        if not trs:
            for t in tr:
                trs.append(t.text)
        else:
            for t in tr:
                if t.text not in trs:
                    trs.append(t.text)
                    T.send("<퍼섭 공지사항>\n{title}".format(title=t.text))
    time.sleep(10 * 60)