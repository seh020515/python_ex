'''
oneDiary
 - member service
   - sign-up, sign-in, modify, delete
 - diary service
   - write, read
'''
flag = True



from config_dir.dir import config   #***
from member import session
from db import member_db
from member import member_dumy
from db import diary_db
from datetime import datetime
import copy

if config.DEV_MOD:
    member_dumy.dumyInit()
    print(f'memberDB : {member_db.memberDB}')
    print(f'diaryDB : {diary_db.diaryDB}')

while flag:
    menuNum = ''
    if session.signInedMemberId == '':
        menuNum = int(input('1.sign up  2. sign in  6.write  7.read  99.end'))                                #sign아웃상태
    else:
        menuNum = int(input('3.modify  4. delete  5.sign out  6.write  7.read  99.end'))                      #sign인 상태

    
    if menuNum == config.SIGN_UP:
        print('1.sign up')
        uId = input('please input new member ID: ')
        uPw = input('please input new member PW: ')
        uMail = input('please input new member Mail: ')
        uPhone = input('please input new member Phone Number: ')
        uRegData = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        member_db.memberDB[uId] = {
            'uId' : uId,
            'uPw' : uPw,
            'uMail' : uMail,
            'uPhone' : uPhone,
            'uRegData' : uRegData
            }
        
        print('New member sign-up success!!')
        
        if config.DEV_MOD:
            print(f'memberDB : {member_db.memberDB}')

        diary_db.diaryDB[uId] = []
        if config.DEV_MOD:
            print(f'diaryDB : {diary_db.diaryDB}')

    elif menuNum == config.SIGN_IN:
        print('2. sign in')
        uId = input('please input member ID: ')
        uPw = input('please input member PW: ')
        
        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['uPw'] == uPw:
                print('sign in success!!')
                session.signInedMemberId = uId
            else:
                print('sign in fail -- pw error')
        else:
            print('sign in fail -- id error')        
      
    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
        '''
        id pw email phone 이중에서 어떤 정보들만 수정 가능하게 할 것인지 정해야함
        id는 수정 XXXX 또한 이미 탈퇴한 회원의 아이디라도 절대 변경사용할 수 없는게 원칙
        pw 절대 수정 불가는 아님 하지만 쉽게 변경할 수는 없음
        mail 비교적 단순하게 수정 가능 
        phone 비교적 단순하게 수정 가능 
        '''
        uPw = input('please input member PW: ')         #변경될 정보
        uMail = input('please input member Mail: ')
        uPhone = input('please input member Phone Number: ')
        '''
        member_db.memberDB 딕셔너리에 회원정보를 변경한다
        현재 딕셔너리에는 길동 찬호가 있음
        현재 로그인 되어있는 회원 정보를 불러와서 그 정보를 수정하게함
        즉. session.signInedMemberId에서 현재 로그인 되어있는 회원 아이디를 가져와서 사용한다
        '''

        currentSignInedMemberId = session.signInedMemberId
        memberInfo = member_db.memberDB[currentSignInedMemberId]
        if config.DEV_MOD : print(memberInfo)

        memberInfo['uPw'] = uPw
        memberInfo['uMail'] = uMail
        memberInfo['uPhone'] = uPhone

        if config.DEV_MOD : print(memberInfo)

    elif menuNum == config.MEMBER_DELETE:
        print('4. delete')
        '''
        현재 로그인이 된 회원의 정보를 삭제 함 
        session.signInedMemberId에서 가져와서 해당하는 회원의 정보를 member_db.memberDB에서 삭제한다
        '''
        currentSignInedMemberId = session.signInedMemberId
        del member_db.memberDB[currentSignInedMemberId]

        print('member info deleted')
        session.signInedMemberId = ''
        if config.DEV_MOD : print(f'member_db.memberDB : {member_db.memberDB}')

    elif menuNum == config.SYSTEM_OUT:
        print('99.end')
        flag = False
    elif menuNum == config.SIGN_OUT:
        print('5.sign out')
        '''
        메뉴 변경
        로그인 값을 없앰
         ->session모듈 signInedMemberId 변수에 있다
        변수를 ''로 변경
        '''
        print('sign out success')
        session.signInedMemberId = ''
    elif menuNum == config.DIARY_WRITE:
        print('6.write')
        #로그인 먼저 혹은 회원이 아니라면 가입을 시켜야함
        if session.signInedMemberId == '':
            print('sorry! please SIGN IN!!')
        else:
            while True:
                diaryTxt = input('10자 이하의 짧은 일기를 작성하세요. ')
                if len(diaryTxt) > 10:
                    print(f'글자 수 초과({len(diaryTxt)})')
                else:
                    diary_db.diaryDB[session.signInedMemberId].append(diaryTxt)
                    if config.DEV_MOD : print(diary_db.diaryDB)
                    break
                
    elif menuNum == config.DIARY_READ:
        print('7.read')
        
        if session.signInedMemberId == '':
            print('sorry! please SIGN IN!!')
        else:
            currentSignInedMemberId = session.signInedMemberId
            myDiarys = diary_db.diaryDB[currentSignInedMemberId]

            deepCopyDiarys = copy.deepcopy(myDiarys)
            deepCopyDiarys.reverse()    #순서가 바뀐다

            for idx, diaryTxt in enumerate(deepCopyDiarys):
                print(f'({idx+1}): {diaryTxt}')