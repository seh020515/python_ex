'''
data=int(input('수심을 입력하세요.'))
temperature = 20 - (data // 10 * .7)
print(f'temprature: {temperature}')
'''

#거리 = 속도*시간
# speed = int(input('주행속도를 입력하세요.'))
# time = int(input('주행시간을 입력하세요.'))

# distanse = speed * time
# print(f'주행 거리: {distanse}')

# time = int(input('근무시간을 입력하세요. '))
# computer = 3*8 // time
# addcomputer = 1 if(3 * 8 % time) > 0 else 0 #너무 어렵다..

# totalcomputer = computer + addcomputer
# print(f'필요한 컴퓨터 수량: {totalcomputer}')

# maskPrice = 340
# maskCnt = int(input('마스크 구매 갯수: '))
# totalPrice =maskPrice * maskCnt

# cash = int(input('지불 금액: '))

# change = cash - totalPrice
# print(f'거스름돈: {change}')

#13시 30분 25초를 초단위로
print(f'sec: {25+ (60*30) + (60*60*13)}')

# kor = int(input('국어점수: '))
# eng = int(input('영어점수: '))
# math = int(input('수학점수: '))

# totalScore = (kor + eng + math)
# avrageScore = totalScore/3

# print(f'totalScore: {totalScore}')
# print(f'averageScore: {avrageScore}')

# night = int(input('밤 최저 기온: '))
# mornig = int(input('낮 최고 기온: '))
# temperatureRange = mornig - night

# print(f'일교차: {temperatureRange}')

length = int(input('길이(cm)를 입력하시오. '))
inch = 0.39
cm = length * inch

print(f'inch: {cm}')