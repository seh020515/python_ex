def fun():
    print('module01함수 실행.')


# print(f'module1{__name__}')   # __name__ 파이썬 내 전역변수


#*******모듈을 만들고 넣어야할 구조********
if __name__ == '__main__':
    fun()