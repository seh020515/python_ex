#딕셔너리
#딕셔너리란, 파이썬에서 묶음 데이터를 관리하기 위한 컨테이너 자료형 중 하나이다.
#key : value로 데이터를 관리함. 이 말은 딕셔너리에는 인덱스가 존재하지 않는다.

#함수 기본
#함수란, 특정 기능을 정의한 구문으로 기능을 재사용하기 위해서 사용함
#VS 변수란, 데이터를 관리하기 위한 메모리 공간으로 데이터를 재사용하기 위해 사용함.

'''
-함수 기본 문법 구조-
def 함수이름():
    기능(실행문)
'''

#인사말 출력 함수
#함수를 정의(선언) 했다 ---> 함수 선언부
def printIntro():
    print('안녕하세요. 좋은 아침일까요?')

#함수는 호출(call)했을 때 동작함.
printIntro()      #-->함수 호출부

#함수는 기능을 최대한 작게. 그리고 다른 프로그램에 이식하기 쉽게 만들자.

#계산기 프로그램을 함수로 만들어보자
def add():
    print(f'덧셈 결과 : {num1 + num2}')
def sub():
    print(f'뺄셈 결과 : {num1 - num2}')
def mul():
    print(f'곱셈 결과 : {num1 * num2}')
def div():
    print(f'나눗셈 결과 : {num1 / num2}')

def calculator():
    if operator == 1:
        add()
    elif operator == 2:
        sub()
    elif operator == 3:
        mul()
    elif operator == 4:
        div()

num1 = float(input('첫 번째 숫자 입력 : '))
operator = int(input('연산자 입력 : 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈'))
num2 = float(input('두 번째 숫자 입력 : '))

calculator()

def lowCalculator():
    if operator == 1:
        add()
    elif operator == 2:
        sub()