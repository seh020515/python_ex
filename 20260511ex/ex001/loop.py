#반복문(for, while)

#for문 : ~하는 동안 / 횟수에 대한 반복
#while : ~하는 동안 / 조건에 의한 반복
'''
for 변수 in 반복되는 범위:
    실행구문
'''
#1 ~ 10 정수 출력
#for 변수 in range(시작값, 끝값, 단계)
#1 ~ n까지의 정수 range(1, (n+1),1)
'''
for num in range(1, 11, 1):
    print(f'{num} : hello')
'''
#0부터 10까지 정수출력
# for num in range(0, 11, 1):
#     print(f'num : {num}')

#range() 간략화 - 단계가 1인 경우 단계 생략 가능
# for num in range(0, 11):
#     print(f'num : {num}')

#range() 간략화 - 단계가 생략되고, 시작이 0이면 시작도 생략 가능하다
# for num in range(11):  -> range(0, 11 , 1)
#     print(f'num : {num}')

# for num in range(2, 9, 2):
    # print(f'num : {num}')

# for num in range(1,16):
#     if num <= 8 and num % 2 ==0:
#         print(f'num : {num}')

# num = int(input('숫자를 입력하세요. '))
# for mail in range(num):
#     print('메일 발송!')

# for num in range(1, 11):
#     if num % 3 == 0:
#         print('3의 배수!')
#     else:
#         print(num)

# dan = int(input('단을 입력하세요. '))
# for num in range(1, 10):
#     print(f'{dan} x {num} = {dan*num}')
total = 0
for num in range(1, 11):
    total += num
    
print(total)

#range() 정리
'''
단계가 1인 경우 생략 가능
단계가 생략 되었다면 시작 데이터도 생략가능하다. 생략 시 0부터 시작
단계가 감소하는경우 (10, 0, -1) 10 ~ 1
'''
'''
****문자열을 이용한 for문
이터러블에는 문자열도 사용할수있다
'''

for ch in 'hello':
    print(ch)  #공백도 포함


for num in range(1,51):
    if num % 7 == 0:
        print(f'{num}')


#while
#조건식의 결과에 따라 반복실행이 결정됨. 참이면 실행 거짓이면 중단
'''
num=1
while num<5:
    print(num)
    num += 1 #언젠가는 거짓으로 해서 while문을 빠져나올수있게 해야 무한루프에 걸리지 않음
'''  #강제 종료는 컨트롤+C

# num=1
# while num <= 10:
#     print(f'num : {num}')
#     num += 2

#for num in range(1, 31):
    #pass

'''
num = 1          #시작

while num < 31:  #조건(끝)
    if num % 2 == 0:
        print(f'{num}은 짝수')
    else:
        print(f'{num}은 홀수')
    num += 1     #단계
'''

# num = 1
# while num < 10:
#     print(f'3 X {num} = {num*3}')
#     num += 1

# num = 1
# while num < 10:
#     for number in range(1, 10):
#         print(f'{num} X {number} = {num * number}')
#     num += 1

#순수 while문으로 바꾸기
# num1=2
# while num1 < 10:
    
#     num2 = 1
#     while num2 <10:
#         print(f'{num1} X {num2} = {num1 * num2}')
#         num2 += 1
    
#     num1 += 1

# num1 = 1
# while num1 < 10:
#     num2 = 2
#     str = ''
#     while num2 < 10:
#         str += f'{num2} X {num1} = {num2 * num1}\t'
#         num2 += 1
    
#     print(str)
#     num1 += 1


num = 1   #반복문의 시작(초기값)
minNum = 0 #최소공배수
while num <= 100:
    if num % 3 == 0 and num % 8 == 0:
        print(f'3과 8의 공배수 : {num}') #공배수 출력
 
        if minNum == 0:
            minNum = num
    num += 1 

print(f'최소공배수 : {minNum}')

#반복문 내 실행 제어(continue, break)
#continue : 실행을 생략하고 다시 처음으로 돌아감

#1부터 10까지 홀수만 출력
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(f'num : {num}')

#break : 실행을 중단하고 반복문을 빠져나옴
#1부터 10을 더하되, 결과가 30이상이 될때 정수를 찾는 프로그램
num = 1
sum = 0

while num < 11:
    sum += num
    if sum >= 30:
        print(f'num: {num}')
        break
    num += 1

#pass
for num in range(1, 10):
    pass

count = 1
maxArea = 150

while True:
    result = ((count * 2) * ( count * 3 )) /2
    if result > 150: break
    print(f'삼각형의 넓이는 : {result}')
    
    count += 1                                                          #ws뭐라는지모르갯다;;;

# num = int(input('숫자를 입력하세요. '))
# total = 0

# for i in range(1, num+1):
#     if i % 2 == 0:
#         total += i
# print(total)

for i in range( 5, 0, -1):
    print(i)

star = str('*')

for i in range(1, 6):
    print(star*i)

num = 1
while num < 6:
    print(num)

    num += 1

num = 1
while num < 11:
    if num % 2 != 0:
        print(num)

    num += 1

num = 1