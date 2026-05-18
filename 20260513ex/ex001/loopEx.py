for num in range(1,100):
    if num <= 9:
        if num % 3 == 0:
            print(f'{num}, 짝!')
        else:
            print(f'{num}')
    else:
       #print(f'{num}') 
        printStr = str(num)
        firstnum = num // 10
        secondnum = num % 10
        if firstnum % 3 ==0:
            # print(f'짝!')
            printStr += ', 짝!'

        if secondnum % 3 == 0 and secondnum != 0:
            # print(f'짝!')
            printStr += ', 짝!'

        print(f'{printStr}')
#---------------------------------------------------------------------------------------------------------------
'''
A열차 : 첫차 오전 9시  막차 오후 6시  운행 간격 10분
B열차 : 첫차 오전 9시  막차 오후 6시  운행 간격 25분
C열차 : 첫차 오전 9시  막차 오후 6시  운행 간격 30분
'''

trainA = 10
trainB = 25
trainC = 30

for n in range(1, 541):
    if n % trainA == 0 and n % trainB == 0 and n % trainC == 0:
        print('trainA <-> trainB <-> trainC')
        print(9 + n // 60, end='')           #시
        print('시', end='')
        print(n % 60, end='')                #분
        print('분')
    elif n % trainA == 0 and n % trainB == 0:
        print('trainA <-> trainB')
        print(9 + n // 60, end='')           #시
        print('시', end='')
        print(n % 60, end='')                #분
        print('분')
    elif n % trainB == 0 and n % trainC == 0:
        print('trainA <-> trainB')
        print(9 + n // 60, end='')           #시
        print('시', end='')
        print(n % 60, end='')                #분
        print('분')
    elif n % trainA == 0 and n % trainC == 0:
        print('trainA <-> trainB')
        print(9 + n // 60, end='')           #시
        print('시', end='')
        print(n % 60, end='')                #분
        print('분')

for n in range(1, 541):
    if n % trainA == 0 and n % trainB == 0 and n % trainC == 0:
        print('trainA <-> trainB <-> trainC')
        # print(9 + n // 60, end='')           #시
        # print('시', end='')
        # print(n % 60, end='')                #분
        # print('분')
        print(f'{9 + n // 60}시 {n % 60}분')
    elif n % trainA == 0 and n % trainB == 0:
        print('trainA <-> trainB')
        # print(9 + n // 60, end='')           #시
        # print('시', end='')
        # print(n % 60, end='')                #분
        # print('분')
        print(f'{9 + n // 60}시 {n % 60}분')
    elif n % trainB == 0 and n % trainC == 0:
        print('trainA <-> trainB')
        # print(9 + n // 60, end='')           #시
        # print('시', end='')
        # print(n % 60, end='')                #분
        # print('분')
        print(f'{9 + n // 60}시 {n % 60}분')
    elif n % trainA == 0 and n % trainC == 0:
        print('trainA <-> trainB')
        # print(9 + n // 60, end='')           #시
        # print('시', end='')
        # print(n % 60, end='')                #분
        # print('분')
        print(f'{9 + n // 60}시 {n % 60}분')

 #print(f'{9 + n // 60}시 {'00' if n % 60 == 0 else str(n % 60)}분') 자리 맞춤 00분
#----------------------------------------------------------------------------------------------------------------

#로그인 기능 만들기
#올바른 암호 dwac1234
'''
ADMIN_PW = 'dwac1234'
count = 1

while True:
    inputPw = input('관리자 암호를 입력하세요. ')
    if count > 5:
        print('로그인 실패')
        break

    if inputPw != ADMIN_PW:
        print('암호를 다시 입력하세요.')
        count += 1

    elif inputPw == ADMIN_PW:
        print('로그인 됐습니다.')
        break
'''

# integerdata = int(input('양의 정수를 입력하시오. '))
# result = 1
# for num in range(1, integerdata+1):
#     result *= num
# print(f'{integerdata}의 !값 : {result}')


'''
0부터 100사이의 난수를 발생시키고 사용자가 난수를 맞힐 때까지 계속해서 물어보는 게임을 만드시오. 
다음은 프로그램 개발에 필요한 요구사항이다.
--- 요구사항 ---
- 1부터 100까지의 난수를 발생시킨다.
- 사용자가 입력한 숫자가 난수와 일치하면 ‘정답입니다.’를 출력하고 게임을 종료한다.
- 사용자가 입력한 숫자가 난수와 일치하지 않으면 ‘틀렸습니다. 다시 입력하세요.’를 출력하고, 다시 물어본다.
- 기회는 10회로 제한한다. 만약 열 번을 넘어가면 ‘게임에 졌습니다.’를 출력하고 게임을 종료한다.
- 사용자가 틀릴 때마다 사용자가 입력한 숫자와 난수를 비교해서 크고, 작음을 출력한다. 
- 게임이 종료하기 전 난수를 출력한다.

'''

# import random
# randomNum = random.randint(1, 100)

# userNum = int(input('1~100의 숫자를 입력하세요. '))
# count = 1
# while True:
#     if randomNum == userNum:
#         print('정답입니다.')
#         break

#     elif randomNum < userNum:
#         print('틀렸습니다. 다시 입력하세요.DOWN ')
#     elif randomNum > userNum:
#         print('틀렸습니다. 다시 입력하세요.UP')
      
#     userNum = int(input('1~100의 숫자를 입력하세요. '))
#     count += 1
    
#     if count > 10:
#         print('게임에 졌습니다.')
#         break

# print(f'{randomNum}')

#--------------------------------------------------------------------------------------------------------------

# quiz) 다음 요구조건을 참고하여 가로와 세로 길이의 변화에 따른 사각형의 넓이를 구하는 프로그램을 만드시오.
'''
 - 가로 길이는 1부터 2의 배수로 증가한다.
 - 세로 길이는 1부터 3의 배수로 증가한다.
 - 사각형의 넓이가 150 보다 크면 프로그램을 종료한다. 
 - 가장 작은 사각형과 가장 큰 사각형의 넓이를 출력한다.
'''
width = 1
height = 1

smallQuadrangle = width*height
quadrangle = width*height

while quadrangle <= 150:
    bigQuadrangle = quadrangle
    if width == 1:
        width = 2
    else:
        width += 2

    if height == 1:
        height = 3
    else:
        height += 3
    quadrangle = (width * height)

print(f'가장 작은 사각형의 넓이 : {smallQuadrangle}, 가장 큰 사각형의 넓이 : {bigQuadrangle}')


# minArea = width * height
# maxArea = width * height

# while True:
#     area = width * height
#     if area > 150 :
#         break
#     print(f'가로 {width}, 세로 {height}, 넓이 {area}')
    
#     if area < minArea:
#         minArea = area

#     if area > maxArea:
#         maxArea = area

#     if width == 1:
#         width = 2
#     else:
#         width += 2

#     if height == 1:
#         height = 3
#     else:
#         height += 3
