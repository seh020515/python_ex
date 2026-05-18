#출석부 관리 시스템
'''
이번에 만들 출석부 관리 시스템은 리스트를 이용해서 학급의 학생 명단을 관리하는 프로그램으로, 시나리오에 따라 
프로그래밍을 전개합니다. 예제가 쉬운 만큼 시나리오만 보고 직접 코딩해 보는 것을 추천합니다
[[ 시나리오 ]]
 #1 :  학급 학생수가 10명(정우람, 박으뜸, 배힘찬, 천영웅, 신석기, 배민규, 전민수, 박건
 우, 박찬호, 이승엽)인 리스트를 만든다.
 #2 :  ‘가나다’ 순으로 정렬한다.
 #3 :  ‘박찬호’ 학생이 전학을 가게 되었다. 출석부에서 삭제한 후 전체 학생과 학생 수를 출력한다.
 #4 :  선생님을 돕기 위한 학생으로 앞에서 3명을 뽑는다.
 #5 :  새로운 친구가 전학 왔다. 이름은 ‘이병규’이다.
 #6 :  자리를 바꾸기 위해서 학생 순서를 역순으로 뒤집는다.
 #7 :  ‘정우람’ 학생이 이름을 ‘정잘남’으로 개명했다.
'''
#1
students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', 
            '배민규', '전민수', '박건우', '박찬호', '이승엽']
print(f'{students}')
#2
students.sort()
print(f'{students}')
#3
students.remove('박찬호')
print(f'전체 학생 : {students}')
print(f'학생 수 : {len(students)}명')
#4
studentsForHelp = students[0:3]
print(f'{studentsForHelp}')
#5
students.append('이병규')
students.sort()
print(f'전체 학생 : {students}')
print(f'학생 수 : {len(students)}명')
#6
students.reverse()
print(f'전체 학생 : {students}')
#7
idx = students.index('정우람') #인덱스 조회
students[idx] = '정잘남'
print(f'전체 학생 : {students}')
#번외 셔플
import random
random.shuffle(students)
print(f'{students}')

#혈액 보관 시스템
LOOP_COUNT = 10
bloods = []
for i in range(LOOP_COUNT):
    print('헌혈해주셔서 감사합니다. 혈액형을 선택하세요. A B AB O')
    bloods.append(input())
print(f'{bloods}')
print(f'혈액형\t|개수')
print('-'*30)
print(f'A형\t: {bloods.count('A')}')
print(f'B형\t: {bloods.count('B')}')
print(f'AB형\t: {bloods.count('AB')}')
print(f'O형\t: {bloods.count('O')}')
print('-'*30)