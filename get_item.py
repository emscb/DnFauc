# 아이템 상세 정보 검색
from src.Item import Item

while 1:
    name = input('아이템 이름을 입력하세요 : ')
    f = Item(name)
    f.select()


print('R')