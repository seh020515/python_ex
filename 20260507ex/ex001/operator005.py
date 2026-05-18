#모듈
#특정 기능을 모아놓은 파일. 직접 코딩하는 수고를 덜 수 있음.
#먼저 import를 이용해 모듈을 가져와야함

#다음은 random모듈을 이용해 난수를 발생시키는 코드다

import random
randomNum = random.randrange(1, 7) #1이상 7미만의 숫자에서 난수를 발생
print(f'randomNum: {randomNum}')

#operator모듈 + - * / 등등
import operator
print(10+20)
print(operator.add(10, 20))

print(10-20)
print(operator.sub(10, 20))

print(10*20)
print(operator.mul(10, 20))

print(10/20)
print(operator.truediv(10, 20))

print(10%20)
print(operator.mod(10, 20))

print(10//20)
print(operator.floordiv(10, 20))

print(10**20)
print(operator.pow(10, 20))

print(10==20)
print(operator.eq(10, 20))

print(10!=20)
print(operator.ne(10, 20))

print(10>20)
print(operator.gt(10, 20))

print(10>=20)
print(operator.ge(10, 20))

print(10<20)
print(operator.lt(10, 20))

print(10<=20)
print(operator.le(10, 20))

print(True and False)
print(operator.and_(True, False))

print(True or False)
print(operator.or_(True, False))

print(True not False)
print(operator.not_(True, False))