#비교 연산자
'''
== 같다  -> True or False
!= 같지않다 -> True or False
> < 크다 작다-> True or False
>= <= 크거나같다 작거나같다 -> True or False
'''

num1=10; num2=20

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 >= num2)
print(num1 < num2)
print(num1 <= num2)

#범퍼카 탑승가능 판별
#신장이 120이상인 어린이만 탑승할 수 있음
#신장을 입력하면 범퍼카를 탑승할 수 있는지 여부를 출력하는 프로그램을 만드시오
#True :  탑승가능 False : 탑승불가능
# height = int(input('어린이의 신장을 입력하세요'))
# print(height >= 120)

#문자 비교(하나의 단어) => 아스키코드(ASCII)값을 비교
print('a'=='b') #a=97 b=98
print('a'<'b')
print('a'>'b')

#문자열 비교 => 보이는 그대로를 비교
str1 ="hello"
str2 ='hello'
print(str1==str2)
print(str1!=str2)
print('---------')
str1 ="hello"
str2 ='hello '  #공백이 있음
print(str1==str2)
print(str1!=str2)