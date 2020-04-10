# 캐릭터 스킬 정보 조회 및 스킬 정보 저장
from src.Char import CharId, CharSkill

serverList = {'안톤': 'anton', '바칼': 'bakal', '카인': 'cain', '카시야스': 'casillas', '디레지에': 'diregie', '힐더': 'hilder',
              '프레이': 'prey', '시로코': 'siroco'}
while 1:
    try:
        characterName = input('캐릭터명을 입력하세요 : ')
        serverId = serverList[input('서버를 입력하세요 : ')]

        char = CharId(characterName, serverId)
        char.run()

        # charIf = charInf(char.characterId, serverId)
        # charIf.run()

        charSk = CharSkill(char.characterId, serverId)
        charSk.run()
    except Exception as e:
        print(e)
