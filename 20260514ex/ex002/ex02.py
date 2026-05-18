flag = True

members = {}

while flag:
    selectedMenuNum = int(input('1.회원가입  2.프로그램 종료'))

    if selectedMenuNum == 1:
        id = input('아이디 : ')
        pw = input('비밀번호 : ')
        members[id] = pw

    elif selectedMenuNum == 2:
        flag = False
    
        for key in members.keys():
            print(f'ID : {key}, pw : {members[key]}')

classes =  {'python':'5학점', 'C/C++':'5학점', 
            'HTML5':'3학점', 'Java':'5학점', 
            'Javascript':'3학점'}
classes['HTML5'] = '5학점'
classes["Javascript"] = '5학점'
print(f'classes : {classes}')


for key in classes:
    if classes[key] == '3학점':
        classes[key] = '5학점'
print(f'classes : {classes}')

#________________________________________________________________________

'''
members = {
    '2019-052001': ['박찬호', 25, 'M', '010-1234-5678', '헬스, 수영', 0],
    '2019-052004': ['박용택', 65, 'M', '010-9012-3456', '수영', 50],
    '2019-052003': ['박세리', 70, 'W', '010-7890-1234', '아쿠아로빅', 50]
}

# 전체 회원 정보 출력
for key in members:
    print(f'회원번호: {key}, 회원정보: {members[key]}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이때 회원의 '이름'과 '성별'만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value[0]}, {value[2]}')
'''

members = {
    '2019-052001': {
        '이름': '박찬호',
        '나이': 25,
        '성별': 'M',
        '연락처': '010-1234-5678',
        '이용서비스': ['헬스', '수영'],
        '할인율': 0
    },
    '2019-052004': {
        '이름': '박용택',
        '나이': 65,
        '성별': 'M',
        '연락처': '010-9012-3456',
        '이용서비스': ['수영'],
        '할인율': 50
    },
    '2019-052003': {
        '이름': '박세리',
        '나이': 70,
        '성별': 'W',
        '연락처': '010-7890-1234',
        '이용서비스': ['아쿠아로빅'],
        '할인율': 50
    }
}

# 전체 회원 정보 출력
for key in members:
    print(f'회원번호: {key}, 회원정보: {members[key]}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이때 회원의 '이름'과 '성별'만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이때 회원의 '이름', '성별', '이용서비스' 그리고 이용서비스개수 만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}, {value['이용서비스']}, {len(value['이용서비스'])}')

refrigerator = {}
foods = [['당근',0],
        ['건대추', 0],
        ['대파',0],
        ['애호박',0],
         ['부추',0]
         ]
for food,count in foods:
    if food == '당근':
        count += 10
        refrigerator[food] = count
    elif food == '건대추':
        count += 100
        refrigerator[food]  = count
    elif food == '대파':
        count += 20
        refrigerator[food]  = count
    elif food == '애호박':
        count += 3
        refrigerator[food]  = count
    elif food == '부추':
        count += 1
        refrigerator[food]  = count
print(f'refrigerator : {refrigerator}')

for food,count in refrigerator.items():
    if food == '당근':
        count -= 1
        refrigerator[food] = count
    elif food == '건대추':
        count -= 10
        refrigerator[food]  = count
    elif food == '대파':
        count -= 1
        refrigerator[food]  = count
    elif food == '애호박':
        count -= 1
        refrigerator[food]  = count
    elif food == '부추':
        count -= 1
        refrigerator[food]  = count

print(f'refrigerator : {refrigerator}')

#______________________________________________________________________________

flag = True
studentScores = {}
while flag:
    name = input('이름 입력 : ')
    if name == '종료':
        break
    score = int(input('점수 입력 : '))
    studentScores[name] = score

print(f'전체 학생 목록 : {studentScores}')

totalScore = 0
for name in studentScores:
    totalScore += studentScores[name]

averageScore = totalScore / len(studentScores)
print(f'평균 점수 : {averageScore}')

bestScore = 0
bestStudent = ''

for name in studentScores:
    if studentScores[name] > bestScore:
        bestStudent = name
        bestScore = studentScores[name]
        
print(f'최고 점수 학생{bestStudent}')


for name in studentScores:
    if studentScores[name] >= 80:
        print(f'80점 이상 학생{name}')