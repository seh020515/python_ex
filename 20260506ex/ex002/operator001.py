#산술 연산자
#산술 연산자는 우리가 자주 사용하는 사칙 연산자와
#컴퓨터 프로그램에서만 사용하는 나머지, 몫, 지수 연산자를 뜻합니다
#+ - * /
#나머지 % 몫 // 지수 **

#덧셈 연산자(+)
print(10+20)
print(3.14+5)
num1=19; num2=100
print(num1+num2)

#전자 회사에서 1분기 매출의 총합을 구하고자 합니다. 프로그램을 작성해봅시다.
'''
sales1=int(input('1월 매출을 입력하세요'))
sales2=int(input('2월 매출을 입력하세요'))
sales3=int(input('3월 매출을 입력하세요'))

total = sales1+sales2+sales3

# print(f'1분기 매출: {total}')
print(f'1분기 매출: {total:,}원')  #콤마 찍어주는 명령어
'''

#문자열 덧셈
print('a'+'b')

#문자열 + 숫자 ---> type error

#뺄셈 연산자 -
print(10 - 5)
print(3.14 - 0.1)
#문자열 지원 X

'''
#1분기 매출 계산. 매출액과 매입액을 입력하면 수익을 계산하는 프로그램
sales=int(input('1분기 매출: '))
purchase=int(input('1분기 매입: '))

profit= sales-purchase

print(f'수익: {profit:,}원')
'''

#곱셉 연산자 *
print(10*20)
print(3.12*2.4)

#문자열 곱셈  O ***
str='hello ' #세번을 연달아 출력하고픔
print(str * 3)

'''
#가로 세로 길이입력하면 방의 넓이를 계산하는 프로그램
width = int(input('가로 입력: '))
legth = int(input('세로 입력: '))
area = width*legth
print(f'방의 넓이: {area}')
'''

#'good morning'문자열을 사용자가 입력한 만큼 출력하는 프로그램
intro = 'Good morning '
cnt = int(input('출력을 원하는 횟수를 입력하세요.'))
print(intro*cnt)