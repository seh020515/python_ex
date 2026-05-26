#파일 다루기 3단계
'''
1. open
    open()함수를 사용한다. 열기에 성공하면 파일은 객체로 만들어져 메모리에 생성된다.
2. write/read
    write()로 쓰기를 read()로 읽기
3. close
    close()함수를 사용. 객체와 커넥션을 끊는다.
'''
            # 파일 경로             파일 사용 목적
# file = open('C:\\seh\\python\\test.txt', 'w')  #파일을 '쓰기'모드로 open한다
# result = file.write('hello python~')           #쓰기
# print(f'result : {result}')                    #문자열의 길이를 반환받을 수 있다
# file.close()                                   #닫기(외부 자원 해제)

# file = open('C:\\seh\\python\\test.txt', 'r')    #읽기모드로 open
# readResult = file.read()
# print(f'readResult : {readResult}')
# print(f'readResult : {type(readResult)}')

# readResult = int(readResult)
# readResult += 1
# print(f'readResult : {readResult}')
# file.close()

# file = open('C:\\seh\\python\\test.txt', 'a')
# file.write('\nhello!')
# file.close()

with open('C:\\seh\\python\\test.txt', 'a') as file:  #with as구문 -> close가 숨겨져있는 구문
    file.write('\nhello~')

# file = open('C:\\seh\\python\\test.txt', 'a') #그냥 w를 하면 덮어쓰기를 해버림!! a는 이어붙힘
# file.write('\nhi~')
# file.close()

#예외 처리(보험)
#세상에 모든 프로그램은 100% 완벽할 수 없음

print(10 + 20)
try: #메모리를 많이 잡아먹으니 자제
    print(10 / 0)  #에러 발생
except Exception as e:  #에러객체를 담음
    print(f'e : {e}')
else: #트라이익셉트의 옵션
    print('에러가 발생하지 않으면 실행되는 코드')
finally:
    print('에러가 발생하던 안하던 무조건 실행되는 코드')

print(10 - 20)
print(10 * 20)
#예외 처리 기본 문법
'''
try ~ except
'''