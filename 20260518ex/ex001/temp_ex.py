students = {}

def addStudent():
    name = input('학생 이름 : ') 
    score = int(input('점수 : '))
    students[name] = score
def showStudent():
    for name in students:
        print(f'전체 조회 : {name} : {students[name]}')
def showAverage():
    total = 0
    for name in students:
        total += students[name]
    print(f'평균 점수 : {total / len(students)}')
def showBestStudent():
    bestScore = 0
    bestStudent = ''
    for name in students:
        if students[name] > bestScore:
            bestScore = students[name]
            bestStudent = name
            
    print(f'{bestStudent} : {bestScore}')

while True:
    print('1. 학생 추가   2. 전체 조회   3. 평균 조회   4. 최고 점수 학생   5. 종료')
    num = int(input('번호를 입력하세요 .'))
    if num == 1:
        addStudent()
    elif num == 2:
        showStudent()
    elif num == 3:
        showAverage()
    elif num == 4:
        showBestStudent()
    elif num == 5:
        break