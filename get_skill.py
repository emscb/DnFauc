from set_skill import skill

while(True):
    try:
        f = skill(input("이름을 입력하세요 : "))
        f.listing()
        print()
        f.run()
    except Exception as e:
        print(e)

print()