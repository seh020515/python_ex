#CRUD
'''
C : Creat  생성, 추가
R : Read   조회
U : Update 수정
D : Delete 삭제
'''

'''
딕셔너리(Dictionary) : {key : value}
'''
#C : Creat
student = {
    '학번' : 123456789,
    '이름' : '홍길동',
    '나이' : 20,
    '성별' : 'M',
    '연락처' : '010-2345-5324'
}

print(f'student : {student}')
print(f'student type : {type(student)}')

#R : Read
sNo = student['학번']
print(f'sNo : {sNo}')
print(f'sNo type : {type(sNo)}')

# U : Update
sName = student['이름']
print(f'sName : {sName}')
student['이름'] = '홍길자'
sName = student['이름']
print(f'sName : {sName}')

# D : Delete
del student['연락처']
print(f'student : {student}')

# keys(), Values(), items()
# keys() : 딕셔너리 자료형에서 키값들만 몽땅 뽑음. 뽑은 키들은 리스트와 비슷한 데이터 타입이다.
keys = student.keys()
print(f'keys : {keys}')
print(f'keys type : {type(keys)}')

for key in keys:
    print(f'key : value = {key} : {student[key]}')

# values() : 딕셔너리에서 밸류 값들만 몽땅 뽑음. 뽑은 밸류들은 리스트와 비슷한 데이터 타입이다.
values = student.values()
print(f'values : {values}')
print(f'values type : {type(values)}')

for value in values:
    print(f'value : {value}')

items = student.items() #key & value
print(f'items : {items}')

for item in items:
    print(f'item : {item}')
    print(f'item [0], item[1]: {item[0], item[1]}')

for key, value in items:     #구조분해할당 문법
    print(f'key : value = {key} : {value}')

#구조분해할당
a, b = (10, 20)
print(f'a: {a},b: {b}')

a = 10
b = 20

# swapping-> a = 20, b =10
a, b = b, a

scores = [10, 20, 30, 40, 50, 60]
'''
a = 10
b = 20
c = [30, 40, 50, 60]
'''
a, b, *c = scores  #* 이후 나머지란 뜻
print(f'a :{a}')
print(f'b :{b}')
print(f'c :{c}')

#quiz
members = {
    '2019-052001' : {
        '이름' : '박찬호',
        '나이' : 25,
        '성별' : 'M',
        '연락처' : '010-1234-5678',
        '이용서비스' : ['헬스', '수영'],
        '할인율' : 0

    }
    
}

print(members["2019-052001"])
print(members["2019-052001"]['이름'])
print(members["2019-052001"]['나이'])
print(members["2019-052001"]['이용서비스'])
print(members["2019-052001"]['할인율'])