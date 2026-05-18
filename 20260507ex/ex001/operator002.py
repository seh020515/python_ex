#할당연산자(대입연산자)
#할당연산자(=)
# num = 5

#복합대입연산자(+=,-=,*=,/=,%=,//=,**=)
'''
num = num + 5
num += 5

num = num - 5
num -= 5

num = num * 5
num *= 5

num = num / 5
num /= 5

num = num % 5
num %= 5

num = num // 5
num //= 5

num = num ** 5
num **= 5
'''

#복리 계산기 만들기
#500만원씩 5년만기, 5년후 받을 총 수령액(이자율 연 5%)

mymoney = 5000000
rate = 0.05

#1년 후 총 금액
mymoney = mymoney + (mymoney * rate)
#2년 후
mymoney = mymoney + (mymoney * rate)

mymoney = mymoney + (mymoney * rate)
mymoney = mymoney + (mymoney * rate)
mymoney = mymoney + (mymoney * rate) #5년후

print(f'5년 후 총 수령액: {int(mymoney):,}원')