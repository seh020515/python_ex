#지역변수vs전역변수
#지역변수(local varialble)는 함수 내부에서 선언된 변수로 함수 내부에서만 사용 가능함
#전역변수(global varialble)는 함수 외부에서 선언된 변수로 함수 내외 모두 사용 가능함

# num = 10                  #전역변수

# def fun():
#     num = 20              #지역변수
#     print(f'num : {num}') #지역변수

# print(f'num : {num}')     #전역변수 num
# fun()                     #지역변수 num

num = 10                  #전역변수

def fun():
    global num            #전역변수 참조 (파이썬에만 있는 기능) ----> 에러 안남
    num += 1              #데이터 수정(전역변수) -->함수내부에서 전역변수를 수정하려하면 에러.
    print(f'num : {num}') #지역변수

print(f'num : {num}')     #전역변수 num
fun()

'''
global 키워드는 함수 내에서 전역변수의 값을 수정하고자 할때 반드시 명시하자.
'''

#웹사이트 누적 방문 횟수 프로그램
# flag = True

# totalVisitor = 0  #전역변수

# def countVisitor():
#     global totalVisitor
#     totalVisitor += 1

# while flag:
#     selectedMenuNum = int(input('1.웹사이트 방문   2.종료'))

#     if selectedMenuNum == 1:
#         countVisitor()
#         print(f'누적 방문 횟수 : {totalVisitor}')
#     else:
#         flag = False
#         print(f'안녕히 가세요.')

#매개변수*********************************************중요!
#매개 : 둘 사이에서 양편의 관계를 맺어줌.
'''
함수를 사용하기 위해 먼저 함수를 정의하고 필요할때 호출한다.
이때 함수를 정의하는 쪽을 함수 정의부(선언부), 함수를 호출하는 쪽을 함수 호출부라고 합니다.

함수를 호출할 때 데이터를 넘겨줄 수 있다. 이 데이터를 '인수'라고 한다.
함수 정의부는 인수를 받으면 '매개변수'라는 변수에 저장한다. 그리고 매개변수는 지역변수의 일종이다.
'''

def greet(name, age): # name, age : 매개변수이자 지역변수
    #name = 홍길동 박찬호 박세리
    print(f'{name}님 안녕하세요.나이는 {age}입니다.')

greet('홍길동', 20)
greet('박찬호', 21)  #'박찬호' --> 인수
greet('박세리', 47)
#매개변수는 호출부에서 전달하는 인수의 개수와 순서에 맞춰서 선언한다.

#인수를 변수에 전달하는 것을 인젝션이라 함.
def forecastWeather(temp, humi, rain):
    print('날씨 예보 입니다.')
    print(f'최고온도 : {temp}도')
    print(f'평균습도 : {humi}%')
    print(f'비올확률 : {rain}%')

# forecastWeather(32,74,50)

#인수의 개수를 모르는 경우
#학급 학생들의 시험 점수 총합과 평균을 구하는 함수
#학급 학생 수 : 3명
'''
def printScoresForStudent(score1, score2, score3):
    totalScore = score1 + score2 + score3
    averageScore = totalScore / 3

    print(f'총 합 : {totalScore}, 평균 : {averageScore}')

printScoresForStudent(90, 80, 100)
'''
def printScoresForStudent(subject, *scores):  #-->호출부의 인수 갯수대로 매개변수가 만들어짐(데이터타입 : 레퍼런스, 리스트 > 튜플 형태)
    print(f'{type(scores)}, {len(scores)}')  # * --> 가변인자. 가변인자 매개변수는 맨 뒤에 만들어져야한다.

    totalScore = 0
    for score in scores:
        totalScore += score
        
    print(f'{subject}과목 총 합 : {totalScore}, 평균 : {totalScore / len(scores)}')

    # totalScore = score1 + score2 + score3
    # averageScore = totalScore / 3

    # print(f'총 합 : {totalScore}, 평균 : {averageScore}')

# printScoresForStudent('국어', 90, 80, 100) #국어 --> subject

def printScoresForStudent(scores):  #scores = [,,,]
    totalScore = 0
    for score in scores:
        totalScore += score
    print(f'총점 {totalScore}')
    print(f'평균 {totalScore/len(scores)}')
    
flag = True

studentScores = []

# while flag:
#     selectedMenuNum = int(input('1. 학생 점수 입력  2. 종료'))
#     if selectedMenuNum == 1:
#         score = int(input('학생 점수 입력 : '))
#         studentScores.append(score)
#     else:
#         flag = False

# printScoresForStudent(studentScores)



# quiz) SMS와 MMS 구별하기
'''
문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다. 그런데 100자를 
넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 단문과 장문을 구별해서 돈을 부
과하는 프로그램을 만들어봅시다. 
'''
# def sendUserMessage(str):
#     strLength = len(str)
#     print(f'문자 길이 : {strLength}')

#     if strLength <= 100:
#         print(f'SMS발송 완료')
#         print(f'50원 부과')
#     else:
#         print(f'MMS발송 완료')
#         print(f'100원 부과')


# inputData = input('문자 입력 : ')
# sendUserMessage(inputData)

#인수와 매개변수의 순서가 일치하지 않을 경우
# def printMemberInfo(name, email, major, grade):
#     print(f'name : {name} / email :{email} /  major : {major} / grade : {grade}')
#     print('-------------------------------------------------------------------------')

# printMemberInfo('Honggildong', 'gildong@gmail.com', 'art', 1)

# printMemberInfo(major = 'art', 
#                 grade = 1, 
#                 name ='Honggildong', 
#                 email = 'gildong@gmail.com')  #좋지않은 방법(함수는 순서를 엄격하게 정하고 쓰는게 좋다.)

# def printMemberInfo(info):
#     print(f'name : {info['name']} / email :{info['email']} /  major : {info['major']} / grade : {info['grade']}')
#     print('-------------------------------------------------------------------------')
# printMemberInfo({
#     'name' : 'Honggildong',
#     'email' : 'gildong@gmail.com',
#     'major' : 'art',
#     'grade' : 1
# })


#매개변수 기본값 설정
#직원 급여 지금 프로그램
# def setSalary(name, pay):
#     print(f'{name}의 급여 : {pay}원 지급')

# setSalary('박찬호',400)
# setSalary('박세리',600)
# setSalary('박용택') # 오류발생

def setSalary(name, pay = 200): #기본값 설정
    print(f'{name}의 급여 : {pay}원 지급')

setSalary('박찬호',400)
setSalary('박세리',600)
setSalary('박용택')

#데이터반환(return)
#데이터 반환이란, 함수는 실행이 끝난 후에 결과물(값)을 호출부로 반환할수있다
#이때 사용하는 키워드가 return이다

#덧셈 연산 함수를 만들어 결과를 출력하는 프로그램을 만들어보자

def printResult(value):
    print(value)

def addFunction(n1, n2):
    sum = n1 + n2
    # print(f'결과 : {sum}')
    printResult(sum)
    return sum

result = addFunction(10, 20)
print(result)

DEV_MOD = True

def fun1():
    print('1111111')
    return               #함수를 종결시키는 기능도 있다
    print('2222222')
    print('3333333')

fun1()

#별탑 만들기
def increaseStart(limintStarCount):
    # print('*')
    # print('**')
    # print('***')
    # return
    # print('****')
    # print('*****')
    # print('******')
    # print('*******')
    for n in range(1, 8):
        print('*' * n)
        if n == limintStarCount:
            break

increaseStart(5) #호출부에서 데이터를 조종하는 편이 좋음