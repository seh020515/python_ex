#나눗셈 연산자 /
print(10/2)  #5.0
#나눗셈의 결과는 실수형
print(3.14/.5) #0.5를 .5로 쓰기도 한다

num1 = 100
num2 = 10
print(f'num1 / num2 = {num1/num2}') #문자열 지원X

#신체질량지수구하기 몸무게 신장 입력시 bmi=몸무게/신장의제곱
# weight = float(input('몸무게(kg): '))
# height = float(input('신장(m): '))

# bmi = weight / (height*height)
# print(f'BMI : {bmi:.2f}')

#숫자 0을 어떤수로 나누어도 결과는 항상 0이다.
print(0 / 120)
#숫자를 0으로 나눌수 없다 .error
# print(10 / 0)

#나머지만 %, 몫만 //, 거듭제곱** 
print(10%2)  #나머지만 구함
print(10%3)

#홀짝게임 동전개수입력하면 짝수는 0 홀수는 1을 출력하는 프로그램
# inputdata = int(input('손 안의 동전 개수: '))
# result = inputdata % 2
# print(f'홀짝!: {result}')

print(10//3)
print(6//2) #정수로 나옴

#빵을 나눠줄수있는 학생 수 구하기 97개의 빵을 3개씩. 최대 몇명? 남는 빵의 개수?
bread=97
breadCnt = 3
maxFriendCnt = bread//breadCnt
print(f'빵을 나누어 줄 수 있는 학생 수: {maxFriendCnt}')
restbreadCnt = bread%breadCnt
print(f'남은 빵의 개수: {restbreadCnt}')

print(2**2) #2의 2승
print(2**3)
print(2**10)

#전염병 예상 감염자 수 구하기
#하루에 한사람이 한명씩. 확진자 한사람이 나올 경우 30일 이후 몇명의 감염자?

man = 2
date = 30
total = man**date
print(f'{date}일 이후 예상 감염자 수: {total}')