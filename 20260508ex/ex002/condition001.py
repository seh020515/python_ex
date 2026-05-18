#조건문(if문)
'''
if 조건식:(콜론 무조건 찍어야함)
    실행문(4칸띄움)
'''
num = 50
if num > 10:
    print('num은 10보다 크다.')
'''
if키워드: 조건문을 선언하기 위한 키워드로 '만약 ~라면'의 뜻을 가짐
조건식: 특정 조건을 기술함. 조건식의 결과에 따라 실행문의 실행여부가 결정됨.
콜론: 코드 블록의 시작을 나타내는 것으로 콜론 이후부터가 실행될 문장이다.들여쓰기로 끝냄
    4칸이 이상적이나 띄우기만 하면 됨. 띄어쓰기를 통일시켜야 코드블록 적용이 됨.
실행문: 조건식의 결과가 참(True)일 경우 실행하는 명령문. 조건식이 거짓(False)이면 실행X
'''

# num = int(input('정수를 입력하시오. '))

# if num > 10:
#     print(f'{num}은 10보다 크다.')

# if num == 10:
#     print(f'{num}은 10과 같다.')

# if num < 10:
#     print(f'{num}은 10보다 작다.')

'''
speed = int(input('속도를 입력하시오. '))

if speed > 50:
    print(f'속도위반 경고')

if speed <= 50:
    print(f'정상 운행')
'''
speed = 40
if speed <= 50: print(f'정상 운행') #실행구문이 하나일 경우 들여쓰기 생략 가능

num = 5
if num > 0:
    pass

#if ~ else 구문 양자택일일 경우에
#else 그렇지않으면
myScore = 70
if myScore >= 90:
    print('용돈')
if myScore < 90:
    print('빠땈ㅋ')

myScore = 90
if myScore >= 90:
    print('용돈')
else: 
    print('빠땈ㅋ')

#if ~ elif 구문 다중선택
'''
점수가 90점 이상이면 'A'
점수가 80점 이상~90점미만 이면 'B'
점수가 70점 이상~80점미만 이면 'C'
점수가 60점 이상~70점미만 이면 'D'
'''

'''
myScore = int(input('점수 입력: '))
if myScore >=90:
    print('A')
elif myScore >= 70:
    print('c')            #순차적으로 내려오다 True발생시 밑은 실행X
elif myScore >= 80:       #논리 에러
    print('B')
elif myScore >= 60:
    print('D')
else:
    print('F')
'''
# elif (myScore >= 70) and (myScore < 80):     논리 연산자를 활용해서 에러를 줄임
#     print('c')

KOREA_NUMBER = 1 #상수를 강제하는 문법은 없으나 상수처럼 사용하자는 의미로 대문자로 지정 스네이크 표기법 사용
USA_NUMBER = 2   #CONST를 붙히기도 함
CHINA_NUMBER = 3

# selectedNum = int(input('1.대한민국 2.USA 3.中國'))
# if selectedNum == KOREA_NUMBER:   #하드코딩XX
#     print('1: 주문하시겠습니까?')
# elif selectedNum == USA_NUMBER:
#     print('2: Would you like to order?')
# elif selectedNum == CHINA_NUMBER:
#     print('3: 您想订购吗？')
# else:
#     print('Would you like to order?')

'''
familyMembers = int(input('가구 인원수를 입력하시오. '))

ONE_PERSON = 1


if familyMembers == ONE_PERSON: # 1-> ONE_PERSON 리펙토링*****
    print('400,000원')
elif familyMembers == 2:
    print('600,000원')
elif familyMembers == 3:
    print('800,000원')
else:
    print('1,000,000원')
'''
'''
bmi = int(input('BMI지수를 입력하시오. '))
if bmi <= 90:
    print('저체중')
elif 110 >= bmi > 90:
    print('정상 체중')
elif 120 >= bmi > 110:
    print('과체중')
elif 140 >= bmi > 120:
    print('비만')
elif bmi > 140:
    print('고도 비만')   #맞는 코드이나 왼쪽부터 작은 숫자를 쓰도록 하자
'''

#중첩 조건문
#조건문 내에 또 다른 조건문을 쓰는 것

#사용자가 입력한 정수에서 양수(0포함)인지 판단하고 양수라면 홀/짝을 구분하라.
'''
myInteger = int(input('정수 입력: '))
if myInteger >= 0:
    print('양수')
    if myInteger % 2 == 0:
        print('짝수')
    else:
        print('홀수')
else:
    print('음수')
'''

#홀짝판단 프로그램 만들기
# num = int(input('양의 정수를 음력하시오. '))
# if num > 0:
#     if num % 2 == 0:
#         print('짝수')
#     else:
#         print('홀수')
# else:
#     print('입력한 정수는 0또는 음수입니다.')

# endBirthYear = int(input('출생연도 끝자리를 입력하세요. '))
# age = int(input('나이를 입력하세요. '))

# if age < 65:
#     if endBirthYear == 1 or endBirthYear == 6:
#         print('월요일')
#     elif endBirthYear == 2 or endBirthYear == 7:
#         print('화요일')
#     elif endBirthYear == 3 or endBirthYear == 8:
#         print('수요일')
#     elif endBirthYear == 4 or endBirthYear == 9:
#         print('목요일')
#     elif endBirthYear == 5 or endBirthYear == 0:
#         print('금요일')
    
# else:
#     print('언제나 구매 가능')

# age = int(input('나이를 입력하세요: '))
# member = input('회원입니까?')

# if age <20:
#     if member == 'Y':
#         print('청소년 회원 할인 적용')
#     else:
#         print('청소년 할인 적용')
# else:
#     if member == 'Y':
#         print('성인 회원 할인 적용')
#     else:
#         print('일반 요금 적용')

#날짜관련모듈
from datetime import datetime

#현재 요일 구하기
# print(datetime.today().weekday()) #0:월 1:화 2:수 ...

# day = datetime.today().day
# carNum = int(input('차량 번호 4자리를 입력하세요. '))
# print(f'오늘 날짜 : {day}일')
# if day % 2 == 0:
#     print('오늘 입차 : 번호가 짝수인 차량')
#     if carNum % 2 == 0:
#         print('귀하의 차량은 입차 가능합니다.')
#     else:
#         print('귀하의 차량은 입차 불가합니다.')         #내가 한거... 좀 복잡하네예
# else:
#     print('오늘 입차 : 번호가 홀수인 차량')
#     if carNum % 2 != 0:
#         print('귀하의 차량은 입차 가능합니다.')
#     else:
#         print('귀하의 차량은 입차 불가합니다.')
'''
if day % 2 == 0:
    print('오늘 입차 : 번호가 짝수인 차량')
else:
    print('오늘 입차 : 번호가 홀수인 차량')

if day % 2 == carNum % 2:
    print('귀하의 차랑은 입차 가능합니다.')
else:
    print('귀하의 차량은 입차 불가합니다.')
'''

# time = int(input('최초 장비를 사용하기까지 걸린 시간(초)를 입력하세요. '))
# if time <= 60:
#     print('생존율 : 85%')
# elif time <= 120:
#     print('생존율 : 76%')
# elif time <= 180:
#     print('생존율 : 66%')
# elif time <= 240:
#     print('생존율 : 57%')
# elif time <= 300:
#     print('생존율 : 47%')
# else:
#     print('생존율 : 25% 미만')

import random
ranNum = random.randint(1, 3)

# myNum = int(input('1.가위 2.바위 3.보 를 선택하세요. '))

# if (ranNum == myNum):
#     print('무승부')
# elif (ranNum == 1 and myNum == 2) or \
#     (ranNum == 2 and myNum == 3) or \
#         (ranNum == 3 and myNum == 1):
#     print('사용자 승리')
# elif (ranNum == 1 and myNum == 3) or \
#     (ranNum == 2 and myNum == 1) or \
#         (ranNum == 3 and myNum == 2):
#     print('컴퓨터 승리')

#문자열의 길이를 구하는 함수
<<<<<<< HEAD
str = 'hello'
print(f'{len(str)}')

userMessage = input('메시지를 입력하세요. ')
msgLen = len(userMessage)
if msgLen <= 50:
    print('SMS 발송')
else:
    print('MMS 발송')
=======
# str = 'hello'
# print(f'{len(str)}')

# userMessage = input('메시지를 입력하세요. ')
# msgLen = len(userMessage)
# if msgLen <= 50:
#     print('SMS 발송')
# else:
#     print('MMS 발송')

 
 
 
 
electricity = int(input('전기 사용량을 입력하세요. '))
print(f'사용량 : {electricity}kwh')

PRICE1 = 910
PRICE2 = 1600
PRICE3 = 7300

UNITPRICE1 = 99.3
UNITPRICE2 = 187.9
UNITPRICE3 = 280.6

if electricity <= 200:
    price = PRICE1
    unit_price = UNITPRICE1
elif electricity <= 400:
    price = PRICE2
    unit_price = UNITPRICE2
else:
    price = PRICE3
    unit_price = UNITPRICE3

print(f'기본요금 : {price}원')
print(f'단가 : {unit_price}원')

total = price + (electricity * unit_price)
print(f'전기 요금 : {total}원')
>>>>>>> ad9a779 (20260508 ex complete