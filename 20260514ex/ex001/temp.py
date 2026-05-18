#split(쪼갠다)
names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
print(f'{names}')
print(f'{type(names)}')

str = "박찬호 이승엽 박세리 박지성 이순철 선동열 손흥민 김연아"
splitedStr = str.split(" ")
print(f'{splitedStr}')       #결과 -> list
print(f'{type(splitedStr)}') #결과 -> list


str = "박찬호+이승엽+박세리+박지성+이순철+선동열+손흥민+김연아"
splitedStr = str.split("+")
print(f'{splitedStr}')       #결과 -> list
print(f'{type(splitedStr)}') #결과 -> list

str = "박찬호+이승엽+박세리+박지성+이순철+선동열+손흥민+김연아"
splitedStr = str.split("+")
print(f'{splitedStr}')       
print(f'{type(splitedStr)}')
splitedStr = tuple(splitedStr) #형변환
print(f'{splitedStr}')        #결과 -> tuple
print(f'{type(splitedStr)}')  #결과 -> tuple