#튜플에 포함된 아이템을 수정할 수 없다.
#리스트와 같은 구조인데 소괄호를 쓴다.
fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
print(f'{type(fruits)}')

#튜플 조회하기
#수정이 불가능해 삽입, 삭제, 정렬 기능이 없다. 조회하는 기능만 사용함.
fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
print(f'{fruits[3]}') #참외

#튜플에서 인덱스 홀수인 아이템 조회
sports = ('태권도', '야구', '농구', '축구', '배구', '권투', '양궁')

for idx, item in enumerate(sports):
    if idx % 2 == 1:
        print(f'idx {idx}, item {item}')

#특정 아이템의 인덱스 조회
#index()사용
fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
print(f'{fruits.index('바나나')}')

#아이템 값으로 인덱스 출력
names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')

# inputData = input('이름을 입력하세요. ')
# print(f'이름 {inputData}, index {names.index(inputData)}')

#아이템 유/무 확인
#in / not in
colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
print(f'{'Green' in colors}')    #Green유무 확인하기 > True
print(f'{'Green+' in colors}')   #Green+유무 확인하기 > False

if 'Green' in colors:    #'Green' in colors > True
    print('colors에는 Green이 있습니다.')
else:
    print('colors에는 Green이 없습니다.')

if 'Green' not in colors:    #'Green' not in colors > True
    print('colors에는 Green이 없습니다.')
else:
    print('colors에는 Green이 있습니다.')

#학점 경고 프로그램 만들기
#F가 있으면 경고 출력
scores = ('A', 'A+', 'B', 'B-', 'F')

if 'F' in scores:
    print(f'경고')
else:
    print(f'경고 없음')

scores = ('A', 'A+', 'F', 'B', 'B-', 'F')
fCnt = scores.count('F')
print(f'F학점의 개수 : {fCnt}')

#tuple결합
nums1 = (1, 2, 3)
nums2 =(10, 20, 30)

# nums1.extend(nums2)  #AttributeError 문법에러 튜플은 수정이 불가하기 때문에
result = nums1 + nums2
print(f'{nums1}')
print(f'{nums2}')
print(f'{result}')

num1 = 10
num2 = num1
print(f'{num1}')
print(f'{num2}')

num1 =100
print(f'{num1}')
print(f'{num2}')

#------------------------------------------------------------------------
nums1 = [1,2,3]
# nums2 = nums1
# print(f'{nums1}')
# print(f'{nums2}')

# nums1[0] = 100
# print(f'---{nums1}')
# print(f'---{nums2}')          #얕은 복사
nums1 = [1, 2, 3]
nums2 = [0, 0, 0]

for idx, num in enumerate(nums1):     #깊은 복사
    nums2[idx] = num

print(f'{nums1}')
print(f'{nums2}')

nums1[0] = 100
print(f'{nums1}')
print(f'{nums2}')

a = [1,2,3,4,5]
b = a #얕은 복사
import copy
b = copy.deepcopy(a) #깊은 복사 모듈
#b = a.copy()

b[0] = 100
print(f'{a}') 
print(f'{b}')

#튜플 슬라이싱
animals = ('호랑이', '사자', '곰', '여우', '늑대')
print(f'{animals}')
print(f'{animals[:3]}')  #인덱스 2 까지
print(f'{animals[1:4]}') 
print(f'{animals[:-2]}') 
print(f'{animals[-1:]}') #헷갈린다..
print(f'{animals[-1:-2]}') 
print(f'{animals[-3:-1]}') 

#슬라이싱 연습
'''
fruits 튜플에서 주어진 요구사항에 맞게 슬라이싱해봅시다.
fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
 - 인덱스 2부터 4까지의 아이템을 출력하시오.
 - 인덱스 0부터 3까지의 아이템을 출력하시오.
 - 인덱스 3부터 끝까지의 아이템을 출력하시오.
'''
fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
print(f'{fruits[2:5]}')
print(f'{fruits[:4]}')
print(f'{fruits[3:]}')

#리스트와 튜플간 변환(형변화, casting)
'''
불가피하게 튜플의 아이템을 수정하려면 리스트로 변환해야 합니다.
또한 리스트로 선언된 데이 터를 수정이 안 되게 하려면 튜플로 변환해야 합니다.
다음은 데이터 변환을 통해 리스트와 튜플을 변환하고 있습니다.
'''
colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
#데이터를 바꾸고싶음
# colors[1] = '오렌지' #typeerror
colors = list(colors)
print(f'{type(colors)}')  #list

colors[1] = '오렌지'
print(f'{colors}')

colors = tuple(colors)
print(f'{type(colors)}') #tuple

#튜플 정렬
colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
colors = list(colors)
colors.sort()
colors = tuple(colors)
print(f'{colors}')

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
cs = tuple(sorted(colors))  #오름차순으로만 정렬됨
print(f'{cs}')