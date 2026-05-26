import lotto_ex as lm

nums = []

print('1부터 45까지의 정수 6개를 입력하시오.')
nums.append(int(input('1번째 숫자 입력 : ')))
nums.append(int(input('2번째 숫자 입력 : ')))
nums.append(int(input('3번째 숫자 입력 : ')))
nums.append(int(input('4번째 숫자 입력 : ')))
nums.append(int(input('5번째 숫자 입력 : ')))
nums.append(int(input('6번째 숫자 입력 : ')))

lm.setUNumbers(nums) #사용자 선택 번호

lm.setRNumbers() #컴퓨터 선택 번호

print(f'이번 주 로또 번호 : {lm.getRNumbers()}')
print(f'내가 선택한 로또 번호 : {lm.getUNumbers()}')
print(f'일치하는 로또 번호 : {lm.compareNumbers()}')