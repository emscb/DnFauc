# 아이템 상세 정보 검색
from src.set_item import item

while(True):
    name = input('아이템 이름을 입력하세요 : ')
    f = item(name)
    f.select()


print('R')