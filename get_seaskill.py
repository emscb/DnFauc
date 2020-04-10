# 스킬별 레벨링 장비 검색
from src.SearchSkill import SearchSkill

while 1:
    try:
        a = input("스킬 이름을 입력하세요 : ")
        f = SearchSkill(a)
    except Exception as e:
        print(e)