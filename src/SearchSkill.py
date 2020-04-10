import csv


class SearchSkill:
    def __init__(self, name):
        self.skillName = name
        self.weaponList = {'프리스트(남)': ['낫', '베틀액스', '십자가', '토템', '염주'],
                           '프리스트(여)': ['낫', '베틀액스', '십자가', '토템', '염주'],
                           '거너(남)': ['자동권총', '리볼버', '머스켓', '보우건', '핸드캐넌'],
                           '거너(여)': ['자동권총', '리볼버', '머스켓', '보우건', '핸드캐넌'],
                           '격투가(남)': ['너클', '통파', '권투글러브', '클로', '건틀릿'],
                           '격투가(여)': ['너클', '통파', '권투글러브', '클로', '건틀릿'],
                           '귀검사(남)': ['소검', '도', '대검', '둔기', '광검'],
                           '귀검사(여)': ['소검', '도', '대검', '둔기', '광검'],
                           '나이트': ['소검', '도', '대검', '둔기', '광검'],
                           '다크나이트': ['소검', '도', '대검', '둔기', '광검'],
                           '도적': ['쌍검', '단검', '차크라웨펀', '완드'],
                           '마창사': ['광창', '미늘창', '장창', '투창'],
                           '총검사': ['코어블레이드', '소태도', '중검', '장도'],
                           '마법사(남)': ['스탭', '로드', '빗자루', '창', '봉'],
                           '마법사(여)': ['스탭', '로드', '빗자루', '창', '봉'],
                           '크리에이터': ['스탭', '로드', '빗자루', '창', '봉']}
        self.equipmentList = ['경갑 머리어깨', '경갑 상의', '경갑 하의', '경갑 허리', '경갑 신발',
                              '중갑 머리어깨', '중갑 상의', '중갑 하의', '중갑 허리', '중갑 신발',
                              '천 머리어깨', '천 상의', '천 하의', '천 허리', '천 신발',
                              '판금 머리어깨', '판금 상의', '판금 하의', '판금 허리', '판금 신발',
                              '가죽 머리어깨', '가죽 상의', '가죽 하의', '가죽 허리', '가죽 신발',
                              '목걸이', '팔찌', '반지',
                              '칭호', '마법석', '보조장비', '귀걸이']

        h2 = open('./src/skillList.csv', 'r')
        h = csv.reader(h2)
        self.jobList = []
        for line in h:
            if line[1] == self.skillName:
                self.jobList.append(line[0])
                self.skillReLevel = line[2]
        if len(self.jobList) > 1:
            num = 0
            for i in self.jobList:
                print(str(num + 1) + '. ' + i)
                num += 1
            a = int(input('직업군을 선택하세요 : '))
            self.jobName = self.jobList[a - 1]
        elif len(self.jobList) == 1:
            self.jobName = self.jobList[0]
        elif not self.jobList:
            print('\n스킬 정보가 없습니다.\n')
            return
        h2.close()
        self.open()

    def open(self):
        f2 = open('./src/itemList.csv', 'r')
        f = csv.reader(f2)
        print()

        for line in f:
            if line[4] == self.skillName and (line[2] == self.jobName or line[2] == '공통'):
                print('+' + line[5] + ' (' + line[3] + ') ' + line[0])
            elif line[4] == '모든 스킬' and line[2] == self.jobName:
                if int(self.skillReLevel) in range(int(line[5]), int(line[6]) + 1):
                    print('+' + line[7] + ' (' + line[3] + ') ' + line[0])
            elif line[4] == '모든 스킬' and line[2] == '공통':
                if line[3] in self.equipmentList:
                    if int(self.skillReLevel) in range(int(line[5]), int(line[6]) + 1):
                        print('+' + line[7] + ' (' + line[3] + ') ' + line[0])
                elif line[3] in self.weaponList[self.jobName]:
                    if int(self.skillReLevel) in range(int(line[5]), int(line[6]) + 1):
                        print('+' + line[7] + ' (' + line[3] + ') ' + line[0])
        print()
        f2.close()
