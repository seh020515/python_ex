#논리 연산자
#피연산자의 논리 자료형(True/False)을 이용하는 연산자

#and (&)
#그리고라는 뜻. 피연산자가 모두 결과가 True인 경우에만 True, 하나라도 False라면 False
var1=True
var2=True
print(var1 and var2)

var1=True
var2=False
print(var1 and var2)

var1=False
var2=False
print(var1 and var2)

#or(|)
#또는 이라는 뜻. 하나라도 True라면 True
var1=True
var2=True
print(var1 or var2)

var1=True
var2=False
print(var1 or var2)

var1=False
var2=False
print(var1 or var2)

#not(부정)연산자
#부정이라는 뜻 .현재 상태를 부정함. True면 False, False면 True
var1=True
print(not var1)

var1=False
print(not var1)

#quiz
num1=10
num2=20
num3=30
result = (num1 < num3) and (num2 < num3)
print(f'result: {result}')

result = (num1 > num3) and (num2 < num3)
print(f'result: {result}')

result = (num1 > num3) and (num2 > num3)
print(f'result: {result}')

result = (num1 < num3) and (num2 < num3) and (num3 > num1)
print(f'result: {result}')

#and, or, 연산시 주의사항
'''
and는 모든 연산자가 True인 겨우만 결과를 True를 출력하기에
첫번째 연산의 결과가 False면더이상 연산을 실행하지 않음
'''
num1=10; num2=20
result = (num1<15) and (num2>15)

num1=17; num2=20
result = (num1<15) and (num2>15) #num1<15만 계산 후 연산을 끝냄

#or 피연산자 중 하나라도 True가 있다면 True라서 만나면 이후 연산 무시 후 True 출력

num1 = 10
# print(f'num1{num1}')
# print(asd) name error

print((num1 > 5) or asd)

#quiz
#어린이용 범퍼카 탑승 가능 판별. 신장이 120이상 170미만.탑승가능 True, 탑승 불가능 False
'''
height = int(input('어린이의 신장을 입력하시오.'))
result = (height >= 120) and (height < 170)

print(f'result: {result}')
'''
#조건식 == 삼항연산자
num1 == 10 #이항연산자(항이 두개 있다)
not True   #단항연산자

targetScore = 90
myScore = 95
#myScore가 targetScore보다 크거나 같으면 합, 그렇지 않으면 불합
result = '합격' if myScore >= targetScore else '불합격' #삼항연산자

print(f'result: {result}')

#quiz 적자흑자 판단
#수입과 지출을 입력하면 적자/흑자를 판별하는 프로그램을 만들어라
'''
incoming = int(input("수입: "))
outgoing = int(input("지출: "))
result = '흑자' if incoming > outgoing else '적자'

print(f'result: {result}')
'''

#조명장치 on/off 프로그램 만들기

currentLight = 50
targetLight = 60
result = 'Turn on' if currentLight < targetLight else 'turn off'
print(f"result: {result}")