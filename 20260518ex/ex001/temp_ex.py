'''
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
'''

# movies = {}

# def addMovie():
#     name = input('영화 제목 : ') 
#     score = int(input('평점 : '))
#     movies[name] = score

# def showMovies():
#     for name in movies:
#         print(f'{name} : {movies[name]}')

# def showAverage():
#     total = 0
#     for name in movies:
#         total += movies[name]
#     print(f'평균 평점 : {total / len(movies)}')

# def showBestMovie():

#     bestScore = 0
#     bestMovie = ''
#     for name in movies:
#         if bestScore < movies[name]:
#             bestScore = movies[name]
#             bestMovie = name
#     print(f'최고 평점 영화 : {bestMovie}({bestScore})')


# def searchMovie():
#     inputData = input('검색할 영화 : ')
#     found = False
#     for movieName in movies.keys():
#         if movieName == inputData:
#             found = True
#             print(f'{movieName}')
#             print(f'{movieName}평점 : {movies[movieName]}')
#     if found == False:
#         print('등록되지 않은 영화입니다')
            
            
    

# while True:
#     print('1. 영화 추가 2. 전체 영화 조회 3. 평균 평점 조회 4. 최고 평점 영화 조회 5. 특정 영화 검색 6. 종료')
#     num = int(input('번호를 입력하세요 .'))
#     if num == 1:
#         addMovie()
#     elif num == 2:
#         showMovies()
#     elif num == 3:
#         showAverage()
#     elif num == 4:
#         showBestMovie()
#     elif num == 5:
#         searchMovie()
#     elif num == 6:
#         break

#-------------------------------------------------------------------------------------------------
# Toy 프로젝트 진행
'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입    2.로그인     3.특정 회원 정보 출력     4.모든 회원 정보 출력     99.종료
사용자가
'1.회원가입'을 선택하면 회원ID, 회원PW, 회원Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
'2.로그인'을 선책하면 회원ID, 회원PW를 입력받아 로그인 '성공' 또는 '실패'를 출력한다.
'3.특정 회원 정보 출력'를 선택하면 회원ID와 회원PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
'4.모든 회원 정보 출력'를 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99.종료'를 선택하면 프로그램 종료 시킨다.

심심하면> 특정 회원의 회원ID와 회원PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해 보자!
'''
memberInfo = {}

def joinId():
    userId = input('ID 입력 : ')
    return userId
def joinPw():
    pw = input('비밀번호 입력 : ')
    return pw
def joinEmail():
    email = input('e - mail 입력 : ')
    return email
def joinPhone():
    phone = input('전화번호 입력 : ')
    return phone

def joinMember():
    userId = joinId()
    memberInfo[userId] = {'pw' : joinPw(), 'email' : joinEmail(), 'phone' : joinPhone()}

    print('회원가입이 완료되었습니다.')

def login():
    userInputId = input('회원 ID : ')
    userInputPw = input('회원 비밀번호 : ')
    if userInputId in memberInfo:
        if userInputPw == memberInfo[userInputId]['pw']:
            print('로그인 성공')
        else:
            print('로그인 실패')
    else:
        print('존재하지 않는 회원입니다.')

def searchPersonalMember():
    userInputId = input('회원 ID : ')
    userInputPw = input('회원 비밀번호 : ')
    if userInputId in memberInfo:
        if userInputPw == memberInfo[userInputId]['pw']:
            print(memberInfo[userInputId])
        else:
            print('일치하지 않습니다.')
    else:
            print('일치하지 않습니다.')
def searchAllMember():
    print(memberInfo)

def editMemberInfo():
    userInputId = input('회원 ID : ')
    userInputPw = input('회원 비밀번호 : ')
    if userInputId in memberInfo:
        if userInputPw == memberInfo[userInputId]['pw']:
            selectedNum = int(input('1.비밀번호 수정 2.Email수정 3. 전화번호 수정'))
            if selectedNum == 1:
                var = 'pw'
            elif selectedNum == 2:
                var = 'email'    
            elif selectedNum == 3:
                var = 'phone'
            else:
                print('잘못된 번호입니다.')
                return
            memberInfo[userInputId][var] = input('수정 정보 입력 : ')
            print('회원 정보가 수정되었습니다.')
        else:
            print('일치하지 않습니다')
    else:
            print('일치하지 않습니다')

flag = True
while flag:
    print('1.회원가입    2.로그인     3.특정 회원 정보 출력     4.모든 회원 정보 출력    5.회원 정보 수정     99.종료')
    num = int(input('번호를 입력하세요 .'))
    if num == 1:
        joinMember()
    elif num == 2:
        login()
    elif num == 3:
        searchPersonalMember()
    elif num == 4:
        searchAllMember()
    elif num == 5:
        editMemberInfo()
    elif num == 99:
        flag = False