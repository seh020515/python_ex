#데이터 중에서 실수는 현존하는 어떤 언어도 완벽하게 다룰 수 없다.
# print(0.1 + 0.2)    #0.30000000000000004


'''
.1 
.2
.3
.4
.5
...
1.0
'''
# flt = .1

# while True:
#     print(f'flt : {flt}')
#     flt += .1

#     if flt >= 1:
#         break   #실수는 결과값이 틀어짐

total = .1 + .2
print(f'total : {total}')
if total > 0.3:
    print('total은 3보다 크다.')   #논리적 오류 발생