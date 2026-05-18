# 함수(funtion)
#python에서 가장 중요하다!
#다른말로 모듈이라고도 함
#사용자는 함수에 값만 집어넣으면 원하는 결과를 얻을 수 있다.
#함수를 만들지 않은 사람은 함수를 수정하지않는다.*****
#기능 재사용을 하기 위해서 함수를 쓴다.
#그리고 검증된 소스를 갖다 쓸수있다.

#함수 정의하기
'''
사용자 함수를 만든다는 것을 함수를 정의한다라고 함.
함수를 정의할 때 def 키워드를 사용함. 그리고 함수명, 콜론(:), 실행부를 이용함.
'''
'''
def 함수명():
     실행부(함수 기능)
'''
def greet():
    print('안녕하세요.')
    print('반갑습니다.')
    print('저는 홍길동 입니다.')

'''
함수명 규칙
1. 내장 함수명과 동일하면 안된다
2. 첫글자는 소문자로 시작한다
3. 첫글자로 숫자를 사용할 수 없다 ex : 1greet X gr1eet O greet1 O
4. 특수문자는 사용할 수 없지만 언더바_는 사용가능
5. 두개 이상의 단어가 조합되는 경우 스네이크 또는 카멜 표기법을 사용
'''

#온도센서 작동 시스템 만들기
#함수 정의부
#함수 선언부
def startTemperatureSensor():
    print('온도 센서 작동을 시작합니다.')

def stopTemperatureSensor():
    print('온도 센서 작동을 중지합니다.')

#함수 호출부
startTemperatureSensor()
stopTemperatureSensor()

#cm를 인치로 바꿔주는 함수 만들기
#1inch = 0.393701cm

def convertUnit():
    lengthCM = float(input('길이(cm)입력: '))
    print(f'{lengthCM * 0.393701}inch')

#이동 거리 계산 함수
def calculateDistance():
    print(f'이동거리 :{hourData*speedData}km')

hourData = float(input('이동 시간: '))
speedData = float(input('이동 속도: '))


#pass 키워드
def calculateNumber():
    pass

#함수 내에서 또 다른 함수 호출
def fun1():
    print('fun1()CALLED!')

def fun2():
    print('fun2()CALLED!')

def fun3():
    fun1()
    fun2()
    print('fun3()CALLED!')

#재귀함수
def fun4():
    print('fun4()CALLED!')
    fun4()


#다국어 인사말 프로그램
def introKor():
    print('안녕')

def introEng():
    print('hello')

def introJap():
    print('こんにちは')

selectedMenuNum = int(input('1.한국   2.USA   3.JAPAN'))

if selectedMenuNum == 1:
    introKor()
elif selectedMenuNum == 2:
    introEng()
elif selectedMenuNum == 3:
    introJap()

# 계산기 프로그램
def add():
    print(f'{inputNum1 + inputNum2}')
def sub():
    print(f'{inputNum1 - inputNum2}')
def mul():
    print(f'{inputNum1 * inputNum2}')
def div():
    print(f'{inputNum1 / inputNum2}')

def calculator():
    if selectedOperator == 1:
        add()
    elif selectedOperator == 2:
        sub()
    elif selectedOperator == 3:     #하드코딩 지양!!! 기능을 분리하여 여러곳에서 쓰일수있게
        mul()
    elif selectedOperator == 4:     #TDD개념만 알아놓을것
        div()

inputNum1 = float(input('숫자를 입력하세요. '))
selectedOperator = int(input('1. + 2. - 3. * 4. /'))
inputNum2 = float(input('숫자를 입력하세요. '))

calculator()