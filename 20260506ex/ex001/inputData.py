#데이터 입력(input data)
#input() 외부에서 데이터 입력

'''
print('데이터를 입력하세요.')
inputdata=input()
print(inputdata)
'''

'''
print('정수를 입력하세요.')
inputInteger=input()
print(inputInteger)

print(type(inputInteger))  #****input으로 입력한 데이터는 무조건 자료형이 str(문자형)****
'''

'''
print("실수 입력하세요.")
inputFloat=input()
print(inputFloat)
print(type(inputFloat))
'''
'''
print("논리형 데이터 입력하세요.")
inputBoolean=input()
print(inputBoolean)
print(type(inputBoolean))
'''
#inputBoolean=input('논리형 데이터 입력하세요.\n')  #위 함수 위에 두줄 요약
#\n 강제 행바꿈 개행 **외우기
#print의 강제개행을 없애는 것 end=' 를 넣어준다

#자료형을 변환해야 str가 아닌 형태로 나온다. 자료형변환(data type casting)

# userInputData=input('사용자야 정수 입력해라')
# print(userInputData)
# print(type(userInputData))
# userInputData=int(userInputData) #int는 원본데이터를 훼손시키지 않음
# print(type(userInputData))

#str > boolean
# userInputData=input('True or False입력하세요.')
# print(userInputData)
# print(type(userInputData))
# userInputData=bool(userInputData)
# print(type(userInputData))

#str>float
# userInputData=input('실수 입력하세요')
# print(userInputData)
# print(type(userInputData))
# userInputData=float(userInputData)
# print(type(userInputData))

x=3
y=float(x)
print(y)

x=3.141592
y=int(x)
print(y) #소수점이 다 날아감 복구 x
print(float(y))