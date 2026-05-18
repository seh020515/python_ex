# print('회원정보를 입력하세요.')
# userName = input('이름: ')
# userMail = input('메일: ')
# userId = input('아이디: ')
# userPw = input('비밀번호: ')

# print('--------------------------------------------------------')
# print('To. '+ userMail)
# print('▶아이디 및 비밀번호 확인')
# print(userName + ' 고객님 안녕하세요.')
# print(userName + ' 고객님의 아이디와 비밀번호는 아래와 같습니다.')
# print('아이디: ' + userId)
# print('비밀번호: ' + userPw)
# print('감사합니다.')
# print('Naver 담당자.')
# print('--------------------------------------------------------')

# usermail = 'gildong@gmail.com'
# print('To. '+ userMail)
# print('To. '+ userMail)

#print('이름:','홍길동') 이름: 홍길동 *** ,연산자를 하면 무조건 공백이 들어감

#end = " " 개행을 막고 공백 end = "" 개행을 막고 바로 뒷문장을 붙힘 ***

#f-string*****(포맷문자열)
#이름은 철수, 나이는 25입니다.
name = '철수'
age = 25
print('이름은 ' + name + ', 나이는 ' + str(age) + '입니다.' )
print(f'이름은 {name}, 나이는 {age}입니다.')

#format()****
print('이름은 {}, 나이는 {}입니다.'.format(name,age))

print('이름은 {1}, 나이는 {0}입니다.'.format(age,name))  #그닥 덜중요...참고만하시긔


# korScore = input('국어 점수를 입력하시오.')
# engScore = input('영어 점수를 입력하시오.')
# mathScore = input('수학 점수를 입력하시오.')

# print(f'국어점수: {kor}')
# print(f'영어점수: {eng}')
# print(f'수학점수: {math}')


firstNum = input('첫 번째 정수를 입력하시오.')
secondNum = input('두 번째 정수를 입력하시오.')

firstNum = int(firstNum)
secondNum = int(secondNum)

sum = firstNum + secondNum
average = sum / 2
print(f'합:{sum}')
print(f'평균: {average}')

var1=10
var2=20

print(f'var1: {var1}, var2: {var2}')

temp=var1
var1=var2
var2=temp

print(f'var1: {var1}, var2: {var2}')