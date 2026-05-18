goods = {
    '새우깡' : 1200,
    '비비빅' : 400,
    '초코파이' : 500,
    '맛동산' : 1500
}
totalPrice = 0

def shrimpCrackersPrice():
    global totalPrice            #전역변수/ 지역변수 차이와 우선순위 알기
    totalPrice += goods['새우깡'] * shrimpCrackers
    print(f'새우깡 구매 금액 :\t{goods['새우깡'] * shrimpCrackers}원')
def bibibigsPrice():
    global totalPrice            #함수 내부에서 전역변수를 수정하고싶을때 쓰는 키워드 ***global***
    totalPrice += goods['비비빅'] * bibibigs           #파이썬에만 있는 문법이다
    print(f'비비빅 구매 금액 :\t{goods['비비빅'] * bibibigs}원')
def chocopiesPrice():
    global totalPrice
    totalPrice += goods['초코파이'] * chocopies
    print(f'초코파이 구매 금액 :\t{goods['초코파이'] * chocopies}원')
def matdongsansPrice():
    global totalPrice
    totalPrice += goods['맛동산'] * matdongsans
    print(f'맛동산 구매 금액 :\t{goods['맛동산'] * matdongsans}원')

shrimpCrackers = int(input('새우깡 구매 개수:\t'))
bibibigs = int(input('비비빅 구매 개수:\t'))
chocopies = int(input('초코파이 구매 개수:\t'))
matdongsans = int(input('맛동산 구매 개수:\t'))

print(f'새우깡 구매 개수 :\t{shrimpCrackers}')
print(f'비비빅 구매 개수 :\t{bibibigs}')
print(f'초코파이 구매 개수 :\t{chocopies}')
print(f'맛동산 구매 개수 :\t{matdongsans}')
print('='*40)
shrimpCrackersPrice()
bibibigsPrice()
chocopiesPrice()
matdongsansPrice()
print('='*40)
print(f'총 구매 금액 :\t {totalPrice}')
print('='*40)