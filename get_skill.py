# 아이템 스킬 레벨링 정보 저장
from src.set_skill import skill

while 1:
    try:
        f = skill(input("아이템 이름을 입력하세요 : "))
        f.listing()
        print()
        f.run()
    except Exception as e:
        print(e)
