# 스킬별 레벨링 장비 검색
from src.set_seaskill import seaSkill

while 1:
    try:
        a = input("스킬 이름을 입력하세요 : ")
        f = seaSkill(a)
    except Exception as e:
        print(e)