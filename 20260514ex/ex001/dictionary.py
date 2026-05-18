#딕셔너리(dictionary)
#인덱스대신 키를 이용함. 키는 인덱스와 달리 사용자가 직접 지정해야함.

#딕셔너리 정의
#딕셔너리는  {}

# ages = {'박찬호': 48, '박지성': 40, '박세리' : 50, '이승엽' : 43} 
# ages = {'박찬호': 48, '박지성': 40, '박세리' : 50, '이승엽' : 43, '박지성' : 40} #키가 중복됨 절대 안돼!!
ages = {'박찬호': 48, '박지성': 40, '박세리' : 50, '이승엽' : 43, '박쥐성' : 100} #밸류가 중복됨 O
print(f'ages : {ages}')
print(f'ages type : {type(ages)}')

scores = {'C/C++' : 'A', 'Java' : 'B', '네트워킹' : 'C', '보안' : 'A+', '해킹' : 'F', '시스템' : 'C+'}

print(f'scores : {scores}')

#********(중요)!
#리스트, 튜플, 딕셔너리
#들어가는 데이터는 모든 자료형이 들어가도 된다, dict에는 key/value 모든 값이 들어갈수있다.하지만 리스트는 key값으론 쓸수없다
#변경이 가능하기 때문.

listVar = [3, 3.13, 'hello']
tupleVar = (3, 3.13, 'hello')
dictVar = {'홍길동' : 10, '박찬호' : '열살', '박세리' : 3.14}

#--------2차원 배열-------------------------------------------------
listVar1 = [1, 2, 3]
listVar2 = [1, 2, 3, listVar1] #리스트안에 리스트

print(f'listVar1 : {listVar1}')
print(f'listVar2 : {listVar2}')

print(listVar2[3][2])
print(type(listVar2[3]))    #list
print(type(listVar2[3][1])) #int

dicts = {'name' : '박찬호',
         'age': 20, 
         'addr' : '대전 중구', 
         'hobby' : ['축구', '농구', '배구']
         }
print(f'{dicts}')
print(f'{dicts['hobby'][1]}')
print(f'{dicts['name']}')

#딕셔너리 조회/삽입/수정/삭제
#컴퓨터 프로그램에서 조회/삽입/수정/삭제 CRUD라고 함
#CRUD라는 용어를 반드시 알것
#Create, Read, Update, Delete
#데이터 생성, 조회, 수정, 삭제하는 것을 말함
#그렇다면 딕셔너리에서 CRUD는 딕셔너리 컨테이너 자료형에
#데이터를 추가, 조회, 수정, 삭제하는 것을 말할 것
#CRUD는 프로그래밍 뿐만아니라 데이터 베이스에서도 사용되는 용어이다.

#추가(Create)
dicContainer = {
    '이름' : '홍길동',
    '나이' : 25,
    '주소' : '대전 중구',
    '취미' : ['축구', '수영', '조깅'],
    '몸무게' : 87.5
}
print(f'dicContainer : {dicContainer}')

dicContainer['연락처'] = '010-1234-1234'
print(f'dicContainer : {dicContainer}')

#조회(Read)
print(f' 이름 : {dicContainer['이름']}')

#수정(Update)
dicContainer['몸무게'] = 50
print(f'dicContainer : {dicContainer}')

#삭제(Delete)
del dicContainer['몸무게']
print(f'dicContainer : {dicContainer}') #데이터 복구 불가

#부가기능
#아이템 개수 조회
print(f'아이템 개수: {len(dicContainer)}')

#전체 키 & 밸류 조회
#전체 키
dickeys = dicContainer.keys()
print(f'dickeys: {dickeys}') #결과 list
for key in dickeys:
    print(f'key : {dicContainer[key]}')

#밸류
dicValues = dicContainer.values()
print(f'dicValues : {dicValues}')

#키 밸류 한번에 조회
for key, value in dicContainer.items():
    print(f'{key}, {value}')

# 중간고사 성적 관리 프로그램 만들기
'''
아래 시나리오를 기반으로 딕셔너리를 이용해서 중간고사 성적 관리 프로그램을 만들어봅시다.
 -1 : 중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C, 보안은 A+, 해킹은 F, 시스템은 C+)을 저장하는 
      딕셔너리를 만든다.
 -2 : 'Java'와 '시스템' 과목의 성적을 조회한다.
 -3 : 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다.
 -4 : 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다.
 -5 : 전체 과목과 성적을 조회하여 최종 성적표를 출력한다.
'''

scores = {
    'C/C++' : 'A', 
    'Java': 'B+', 
    '모바일': 'C', 
    '보안' : 'A+', 
    '해킹' : 'F', 
    '시스템' : 'C+'
}
print(f'{scores['Java']}')
print(f'{scores['시스템']}')

scores['python'] = 'A'
scores['OS'] = 'A+'
print(f'scores : {scores}')

scores['Java'] = 'F'
scores['시스템'] = 'A'
print(f'scores : {scores}')

for key in scores.keys():
    print(f'{key}:\t{scores[key]}')



creditScores = {
    'A+': 4.5,
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'C+': 2.5,
    'C': 2.0,
    'F': 0.0,
}

totalScore = 0
averageScore = 0

for key in scores.keys():
    totalScore += creditScores[scores[key]]
    print(f'{key}:\t{scores[key]}')     # A+ > 4.5, A > 4.0, B+ > 3.5 ... 

print(f'totalScore: {totalScore}')      # 23.0
averageScore = totalScore / len(scores)
print(f'averageScore: {averageScore}')  # 2.875

'''
C/C++:  A       4.0
Java:   F       0.0
모바일: C        2.0
보안:   A+       4.5
해킹:   F        0.0
시스템: A        4.0
파이썬: A        4.0
OS:     A+      4.5

A+      : 4.5
A       : 4.0
B+      : 3.5
B       : 3.0
C+      : 2.5
C       : 2.0
F       : 0.0
'''