import requests
from set_charId import charId, charInf

serverList = {'안톤' : 'anton', '바칼' : 'bakal', '카인' : 'cain', '카시야스' : 'casillas', '디레지에' : 'diregie', '힐더' : 'hilder', '프레이' : 'prey', '시로코' : 'siroco'}

characterName = input('캐릭터명을 입력하세요 : ')
serverId = serverList[input('서버를 입력하세요 : ')]

char = charId(characterName, serverId)
char.run()

charIf = charInf(char.characterId, serverId)
charIf.run()
