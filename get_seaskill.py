from src.set_seaskill import seaskill

while(True):
    try:
        a = input("스킬 이름을 입력하세요 : ")
        f = seaskill(a)
    except Exception as e:
        print(e)


print()