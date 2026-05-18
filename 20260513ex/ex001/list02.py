#리스트 정렬
'''
sort()함수 사용
reverse옵션이 False면 오름차순(ASC)
True면 내림차순(DESC)
'''
numbers = [5, 1, 3, 4, 2, 6]
print(f'numbers : {numbers}')

#오름차순(ASC)
numbers.sort()        #numbers.sort(reverse=False)
print(f'numbers : {numbers}')

#내림차순(DESC)
numbers.sort(reverse=True)
print(f'numbers : {numbers}')

kor = ['카', '가', '다', '하', '나']
kor.sort()
print(f'{kor}')

kor.sort(reverse=True)
print(f'{kor}')

scores = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]
scores.sort()
print(f'{scores}')

scores.sort(reverse=True)
print(f'{scores}')

#회의 참석자 정렬
# 다음은 회의 참석자 명단입니다. 참석자 명단을 오름차순과 내림차순으로 정렬해봅시다.
names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
names.sort()
print(f'{names}')
names.sort(reverse=True)
print(f'{names}')

#리스트 순서 뒤집기------------------------------------------------------------------
#reverse() 역순으로 뒤집음
vegetables = ['당근', '오이','양파','감자', '고구마']
vegetables.reverse()
print(f'{vegetables}')

#리스트 슬라이싱***** ---------------------------------------------------------------
#필요한 아이템만 뽑아내는 것
animals = ['호랑이', '사자', '곰', '여우', '늑대']
'''
            |1-------------3| 
['호랑이', '사자', '곰', '여우', '늑대']
'''
animals[1:4] #index 1~3 슬라이싱
print(f'{animals[1:4]}')
print(f'{animals}') #원본 데이터는 유지됨

sliceAnimals = animals[1:4]
print(f'{sliceAnimals}')

#[n:m]  -> n인덱스부터 (m-1)인덱스까지 아이템을 슬라이싱(추출)한다.
animals = ['호랑이', '사자', '곰', '여우', '늑대']
print(f'{animals[:4]}')  # : 앞에를 생략하면 0부터 시작


print(f'{animals[3:]}')  # : 뒤에를 생략하면 3부터 마지막까지라는 뜻

#뒤에서 두개의 아이템을 슬라이싱하자
print(f'{animals[len(animals)-2:]}')

print(f'{animals[:-1]}') #뒤에서 하나빼고 슬라이싱
print(f'{animals[1:-1]}') 

print(f'{animals[:]}') #전체데이터조회
print(f'{animals[::2]}') #스텝 2칸씩 건너뜀

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#역순 출력
alphabet.reverse()
print(f'alphabet : {alphabet}')
#리스트 슬라이싱
'''
 - 인덱스 2부터 5까지의 아이템을 출력하시오.
 - 인덱스 0부터 4까지의 아이템을 출력하시오.
 - 인덱스 3부터 7까지의 아이템을 출력하시오.
 - 인덱스 5부터 끝까지의 아이템을 출력하시오.
 - 인덱스 3부터 8까지의 아이템을 출력하시오.
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(f'{alphabet[2:6]}')
print(f'{alphabet[:5]}')
print(f'{alphabet[3:8]}')
print(f'{alphabet[5:]}')
print(f'{alphabet[3:9]}')

#뒤에서 4개 출력
print(f'{alphabet[len(alphabet)-4:]}')
print(f'{alphabet[-4:]}')

#-------------------------------------------------------------------------------------
'''
1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
 [3, 7, 1, 9, 5]

2. 사용자에게 숫자 입력받아서
1부터 입력한 숫자까지 합계 출력하기 ( 5 )

3. 리스트에 있는 숫자 중 짝수만 출력하기
 [1,2,3,4,5,6]

4. 리스트 숫자를 오름차순 정렬하기
[5,1,7,3]

5. 리스트 숫자를 내림차순 정렬하기
 [5,1,7,3]

6. 리스트 안 숫자의 평균 구하기 [10,20,30]

7. 리스트에서 가장 작은 숫자 찾기
 (min() 사용 금지)

8. 1부터 100까지 숫자 중
3의 배수와 5의 배수 출력하기

9. 사용자가 입력한 숫자를 리스트에 저장하다가
0 입력하면 종료 후 리스트 출력하기
[입력: 3 ,입력: 7, 입력: 2 ,입력: 0]
'''
#1
numbers = [3, 7, 1, 9, 5]
maxnum = 0
for num in numbers:
    if maxnum < num:
        maxnum = num
print(f'{maxnum}')

#2
num = int(input('숫자를 입력하세요. '))
i = 1
total = 0
while i <= num:
    total += i
    i += 1
print(f'{total}')

#3
numbers = [1,2,3,4,5,6]
for num in numbers:
    if num % 2 == 0:
        print(f'{num}')

#4
numbers = [5,1,7,3]
numbers.sort()
print(f'{numbers}')

#5
numbers = [5,1,7,3]
numbers.sort(reverse=True)
print(f'{numbers}')

#6
numbers = [10,20,30]
averege = 0
total = 0
for num in numbers:
    total += num
    averege = total / len(numbers)
print(f'{averege}')

#7
numbers = [10, 20, 30]
minnum = numbers[0]
for num in numbers:
    if minnum > num:
        minnum = num
print(f'{minnum}')

#8
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num}')

#9
num = int(input('숫자를 입력하세요. '))
numbers = []
while True:
    if num > 0:
        numbers.append(num)
        num = int(input('숫자를 입력하세요. '))
    elif num == 0:
        numbers.append(num)
        print(f'{numbers}')
        break