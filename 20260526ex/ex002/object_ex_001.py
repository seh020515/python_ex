# 클래스(객체를 만들기 위한 틀(설계도)) 문법

#붕어빵 클래스
class FishBread: #클래스 선언 앞글자는 대문자로 약속~
    #속성(attribute)
    def __init__(self, f, b): #__init__ : class 생성자. 객체를 초기화 해줌. 꼭 있어야함~
        self.flour = f        #self : 변수를 객체에 지정해 주는 키워드. class 자신을 가리킴
        self.bean = b

    #기능(methodm,function)
    def makeFishBread(self): #이름 맘대로 지어도 o
        print('붕어빵 제조')

#속성은 def __init__(): 형태로 정의 기능은 함수형태로 정의.

#붕어빵 클래스로부터 객체를 만들어봅시다(객체 생성.실체화.인스턴스)
myFishBread = FishBread('밀가루', '팥') #레퍼런스 타입 데이터
friendFishBread = FishBread('쌀가루', '슈크림')
hisFishBread = FishBread('밀가루', '꿀')

print(f'내 붕어빵의 속 내용물: {myFishBread.bean}') #팥
print(f'내 붕어빵의 반죽: {myFishBread.flour}') #밀가루

print(f'친구 붕어빵의 속 내용물: {friendFishBread.bean}') #슈크림
print(f'친구 붕어빵의 반죽: {friendFishBread.flour}') #쌀가루

print(f'그의 붕어빵의 속 내용물: {hisFishBread.bean}') #꿀
print(f'그의 붕어빵의 반죽: {hisFishBread.flour}') #밀가루

#----------------------------------------------------------------------------------------
#계산기 클래스
class Calculator:
    #속성
    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2

    #기능
    def add(self):
        print(f'add : {self.num1 + self.num2}')

    def sub(self):
        print(f'sub : {self.num1 - self.num2}')

    def mul(self):
        print(f'mul : {self.num1 * self.num2}')

    def div(self):
        print(f'div : {self.num1 / self.num2}')

myCalculator = Calculator(10,20)
friendCalculator = Calculator(100,200)

myCalculator.add()
myCalculator.sub()
myCalculator.mul()
myCalculator.div()

friendCalculator.add()
friendCalculator.sub()
friendCalculator.mul()
friendCalculator.div()

#인간 클래스
class Human:
    def __init__(self, height, weight): #매개변수. 변수명 이름 똑바로 짓긔
        self.height = height            #self.은 클래스안의 변수
        self.weight = weight

    def walk(self):
        print('걷는다')
    def run(self):
        print('달린다')
    def printMyInfo(self):
        print(f'나의 신장 {self.height}')
        print(f'나의 체중 {self.weight}')

human1 = Human(188,87)
human2 = Human(165,50)

human1.printMyInfo()
human2.printMyInfo()

human1 = human2       #human1의 객체가 사라짐
human1.printMyInfo()

human1.height = 200
human1.weight = 38
human2.printMyInfo()

#개인 공부중--------------------------------------------------------------------------------
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f'{self.name}이가 짖습니다! 멍멍!')
    def info(self):
        print(f'이름 : {self.name}, 나이 : {self.age}살')

choco = Dog('초코', 2)
choco.bark()
choco.info()

white = Dog('흰둥이', 1)
white.bark()
white.info()


class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, n):
        self.result = self.result + n
        print(f'{self.result}')
    def sub(self, n):
        self.result = self.result - n
        print(f'{self.result}')
    def mul(self, n):
        self.result = self.result * n
        print(f'{self.result}') 
    def reset(self):
        self.result = 0
        print(f'{self.result}')

calc = Calculator()
calc.add(10)
calc.add(5)
calc.sub(3)
calc.mul(2)
calc.reset()

class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'잔액 : {self.balance}')
    def withdraw(self, amount):
        if  self.balance < amount:
            print('잔액이 부족합니다')
        else:
            self.balance = self.balance - amount
        print(f'잔액 : {self.balance}')
    def check(self):
        print(f'{self.owner}님의 잔액 : {self.balance}원')

account = Account('은호')
account.deposit(10000)
account.deposit(5000)
account.withdraw(3000)
account.withdraw(20000)
account.check()

#----------------------------------------------------------------------------------------
students = {}

def add_student(name, score):
    students[name] = score
    print(f'{name} 학생 추가 완료!')

def get_average():
    if len(students) == 0:
        print('학생이 없습니다')
        return
    avg = sum(students.values()) / len(students)
    print(f'평균 점수 : {avg:.1f}점')

def get_highest():
    if len(students) == 0:
        print('학생이 없습니다')
        return
    top = max(students, key=lambda x: students[x])
    print(f'최고 점수 : {top} ({students[top]}점)')

def show_all():
    if len(students) == 0:
        print('학생이 없습니다')
        return
    for name, score in students.items():
        print(f'{name} : {score}점')

add_student('은호', 90)
add_student('철수', 85)
add_student('영희', 92)
show_all()
get_average()
get_highest()

class ScoreManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, score):
        self.students[name] = score
        print(f'{name} 학생 추가 완료!')
    def get_average(self):
        if len(self.students) == 0:
            print('학생이 없습니다')
            return
        avg = sum(self.students.values()) / len(self.students)
        print(f'평균 점수 : {avg:.1f}점')
    def get_highest(self):
        if len(self.students) == 0:
            print('학생이 없습니다')
            return
        top = max(self.students, key=lambda x: self.students[x])
        print(f'최고 점수 : {top} ({self.students[top]}점)')
    def show_all(self):
        if len(self.students) == 0:
            print('학생이 없습니다')
            return
        for name, score in self.students.items():
            print(f'{name} : {score}점')

sm = ScoreManager()
sm.add_student('은호', 90)
sm.add_student('철수', 85)
sm.add_student('영희', 92)
sm.show_all()
sm.get_average()
sm.get_highest()
#----------------------------------------------------------------------------------
class WorkoutManager:
    def __init__(self):
        self.records = {}

    def add_record(self, date, exercise, time):
        self.records[date] = {'exercise': exercise, 'time': time}
        print(f'{self.records}')

    def show_all(self):
        if len(self.records) == 0:
            print('저장된 기록이 없습니다.')
            return
        for date, value in self.records.items():
            print(f'{date} : {value['exercise']} {value['time']}분 ')

    def get_total(self):
        if len(self.records) == 0:
            print('저장된 기록이 없습니다.')
            return
        
        total = 0
        for value in self.records.values():
            total = total + value['time']
        print(f'총 운동 시간 : {total}')

    def get_best(self):
        best_date = None
        best_time = 0

        for date, value in self.records.items():
            if value['time'] > best_time:
                best_time = value['time']
                best_date = date
        print(f'best : {best_date} ({best_time}분)')

wm = WorkoutManager()
wm.add_record('5/20', '달리기', 30)
wm.add_record('5/21', '수영', 60)
wm.add_record('5/22', '헬스', 45)
wm.show_all()
wm.get_total()
wm.get_best()