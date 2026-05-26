import random

userNums = []
randNums = []
collect = []

def setUNumbers(ns): #userNums를 채워줄 함수. setter. 데이터를 세팅해주는 함수 set + UserNums처럼 변수명을 지음
    global userNums
    userNums = ns

def getUNumbers():   # getter get + UNumbers 데이터를 가져오는 함수
    return userNums  
#세터 게터의 기본 꼴

def setRNumbers():
    global randNums
    randNums = random.sample(range(1,46),6)

def getRNumbers():
    return randNums

def compareNumbers():
    global  userNums
    global  randNums
    global  collect

    collect = []
    for item in userNums:
        if randNums.count(item) != 0:
            collect.append(item)
    return collect