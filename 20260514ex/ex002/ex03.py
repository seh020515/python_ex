flag = True
fruits = {}
while flag:
    fruit = input('과일 이름 입력 : ')
    if fruit == '종료':
        break
    count = int(input('판매 개수 입력 : '))
    fruits[fruit] = count

print(f'전체 판매 목록 : {fruits}')

totalCount = 0
for fruit in fruits:
    totalCount += fruits[fruit]
print(f'총 판매 개수 : {totalCount}')

bestCount = 0
bestFruit = ''
for fruit in fruits:
    if fruits[fruit] > bestCount:
        bestCount = fruits[fruit]
        bestFruit = fruit
print(f'가장 많이 팔린 과일 : {bestFruit}')

for fruit in fruits:
    if fruits[fruit] >= 10:
        print(f'10개 이상 팔린 과일 : {fruit}')
