#컨테이너 자료형 > 자료형 (container data type)

'''
*****(중요)
list
tuple
dictionary
*****
'''

#컨테이너 자료형 -> 데이터 집합체 : 많은 데이터를 효율적으로 관리하기 위해 사용
#fruits = ['사과', '포도', '복숭아']

#list : 같은 유형의 데이터를 나열.데이터의 갯수를 길이라고 말한다.
#선언할때 대괄호로 묶고 쉼표로 구분, [, , , ,]로 구분지어 표기. 구분자(separator)
#메모리에 순차적으로 저장

#변수에 리스트자체가 담기는게 아닌 데이터 첫번째 메모리 주소가 담김
#메모리 주소를 할당한다 라고 함

#리스트list
fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나']
print(fruits)
print(f'type of fruits : {type(fruits)}')

#리스트와 데이터
'''
리스트에 포함되는 데이터는 어떤 자료형이든 상관X
정수, 실수, 문자(열) 등 모두 하나의 리스트로 묶일 수 있음
'''

complexlist =[10, 3.14, 'a', 'hello']
#이렇게 하나의 리스트에 다양한 데이터 타입의 데이터를 넣을 수 있는 언어는
#파이썬과 javascript 뿐이다. java 불가
print(complexlist)
print(f'type of complexlist : {type(complexlist)}')

member = [] #비어있어도 리스트
print(member)
print(f'type of member : {type(member)}')

attendList = ['이순철', '김병헌', '김민우', '박찬호', '김민태']


#how to 리스트 아이템 조회
#특정 아이템 조회
#INDEX 0부터 시작. 자동으로 부여되는 일종의 번호표. 아이템이 추가되거나 삭제되어도 자동으로 부여


#           0      1       2      3      4     5       6        7
fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나']
print(fruits[5])  #자두
print(fruits[0])  #사과
#리스트에 없는 인덱스를 참조하면 index error발생

#리스트 길이(아이템 개수)조회
# len()함수를 사용하면 알수있습니다.

numbers = [ 1, 2, 3, 4, 5]
print(f'numbers : {numbers}')
print(f'numbers len : {len(numbers)}')


numbers = [ 1, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 88]
#첫 번째 데이터 조회
print(f'첫 번째 데이터 : {numbers[0]}')
#마지막 데이터 조회 (index()-1)
print(f'마지막 데이터 : {numbers[len(numbers)-1]}')

#len() 함수는 문자열의 길이를 조회하는데에도 사용된다.
str = 'hellllllllllllllllllllllllo'
print(len(str))

#quiz입력한 글자수 확인
'''
메시지를 입력받아 문자열의 길이를 출력
'''
# messege = input('메시지를 입력하세요. ')
# msglen = len(messege)
# print(f'msglen : {msglen}')

#리스트 전체 데이터 조회
balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
print(f'{balls[0]}')
print(f'{balls[1]}')
print(f'{balls[2]}')
print(f'{balls[3]}')
print(f'{balls[4]}') #데이터 수가 많아지면 쓸 수 없는 방식

#for문을 이용해 전체 데이터를 조회할수있다
# for 변수 in 이터러블데이터:
#     pass
for item in balls:
    print(f'item : {item}')

#아이템의 인덱스값까지 조회 enumerate라는 함수 사용.
for idx, item in enumerate(balls):
    print(f'item : {item}, index : {idx}')

#while문 사용
balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
i = 0
while i < len(balls):
    print(f'item : {balls[i]}, index : {i}')
    i += 1

#quiz 다음 리스트에서 '마지막 인덱스 값'을 구하는 프로그램을 만드세요
sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']
lenVar = len(sports)-1
print(sports[lenVar])

#다음리스트에서 'python' 문자열의 인덱스값을 출력하는 프로그램을 만드세요.
languages = ['c/c++', 'c#', 'python', 'java']
for idx, str in enumerate(languages):
    if str == 'python':
        print(f'idx : {idx}')

targetIdx = languages.index('python')
print(f'targetIdx : {targetIdx}')

#아이템 기존 리스트에 삽입
#리스트 마지막에 삽입
sports = ['football', 'baseball', 'volleyball']
print(f'sports : {sports}') #마지막에 basketball을 넣으려함

sports.append('basketball')
print(f'sports : {sports}')
print(f'sports : {len(sports)}')

#취미 추가하기
'''
취미들을 저장할 리스트를 정의하고 사용자가 입력한 취미가 추가되는 프로그램을 만드시오.
그리고 취미의 갯수를 출력하시오.
'''

# hobbies = []

# flag = True

# while flag:
#     hobby = input('취미 입력 : ')
#     hobbies.append(hobby) 
#     print(f'hobbies : {hobbies}')
#     selectedMenuNumber = int(input('1. 계속 입력 2. 종료'))
#     if selectedMenuNumber == 2:
#         print(f'총 개수 : {len(hobbies)}')
#         flag = False #break를 써도 됨

#특정한 위치에 아이템을 추가하는 방법
#insert()함수 이용

countries = ['korea', 'china', 'japan']  #korea usa china japan 으로 만들려함
countries.insert(1, 'usa')
print(f'countries : {countries}')

#quiz 누락숫자 추가
numbers = [ 1, 2, 3, 4, 5, 7, 8, 9] #6,10 추가
numbers.insert(5, 6)
print(f'numbers : {numbers}')
numbers.insert(9, 10) #append 써도 됨.
print(f'numbers : {numbers}')

#리스트 연결하기
#extend() 사용
list1 = [1, 2, 3]
print(f'{list1}')

list2 = [10, 20, 30]
print(f'{list2}')

list1.extend(list2)
print(f'{list1}')
#------------------------------------------------------

# list3 = list1 + list2
# print(f'{list1}')
# print(f'{list2}')
# print(f'{list3}')

#리스트 아이템 삭제
#마지막 아이템 삭제
sports = ['football', 'baseball', 'volleyball', 'basketball']
print(f'{sports}')
sports.pop() #마지막 데이터가 날라감
print(f'{sports}')
sports.pop(1) #인덱스 1이 날라감
print(f'{sports}')

removeItem = sports.pop()
print(f'removeItem : {removeItem}') #지워지는 데이터 변수에 저장 가능

#pop()대신 del키워드를 이용할수도 있다
sports = ['football', 'baseball', 'volleyball', 'basketball']
del sports[2] #삭제된 데이터를 얻지 못함
print(f'{sports}') 

#아래리스트에서 발리볼 삭제
sports = ['football', 'baseball', 'volleyball', 'basketball']
volleyballIdx = sports.index('volleyball')
sports.pop(volleyballIdx)
print(f'{sports}')



#개인 문제풀이-----------------------------------------------------------------------------------------------

list = []
i = 0 
while i < 5:
    i += 1
    list.append(i)
print(f'{list}')


fruits = ['apple', 'banana', 'orange']
print(fruits[1])

fruits = ['apple', 'banana', 'orange']
fruits.pop(1)
fruits.insert(1,'grape')
print(fruits)


numbers = [10, 20, 30, 40, 50]
for i in numbers:
    print(i)

print('-------------------------')


total = 0
numbers = [10, 20, 30, 40, 50]
for i in numbers:
    total += i
print(total)


numbers = [3, 8, 5, 12, 7, 20]

for i in numbers:
    if i % 2 == 0:
        print(i)
    
numbers = [3, 8, 5, 12, 7, 20]
total = 0
for i in numbers:
    if i % 2 == 0:
        total += i
print(total)

i = 1
while i < 11:
    if i % 3 == 0:
        print(i)
    i += 1


num = int(input('숫자를 입력하세요: '))
i = 1
total = 0
while i <= num:
    total += i
    i += 1
print(total)


numbers = [3, 8, 5, 12, 7, 20]
total = 0
for i in numbers:
    if i % 2 == 0:
        total += i
print(total)

numbers = [5, 12, 7, 20, 3, 15]

for i in numbers:
    if i > 10:
        print(f'{i}')

fruits = ['apple', 'kiwi', 'banana', 'fig', 'orange']

for i in fruits:
    int(len(i))
    if int(len(i)) >= 5:
        print(i)