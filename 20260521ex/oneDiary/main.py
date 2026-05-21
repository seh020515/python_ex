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

if config.DEV_MOD:
    member_dumy.memberDumyInit()
    print(f'memberDB : {member_db.memberDB}')

while flag:
    menuNum = ''
    if session.signInedMemberId == '':
        menuNum = int(input('1.sign up  2. sign in  99.end'))                                #sign아웃상태
    else:
        menuNum = int(input('3.modify  4. delete  5.sign out  99.end'))                      #sign인 상태

    
    if menuNum == config.SIGN_UP:
        print('1.sign up')
        uId = input('please input new member ID: ')
        uPw = input('please input new member PW: ')
        uMail = input('please input new member Mail: ')
        uPhone = input('please input new member Phone Number: ')
        
        member_db.memberDB[uId] = {
            'uId' : uId,
            'uPw' : uPw,
            'uMail' : uMail,
            'uPhone' : uPhone
            }
        
        print('New member sign-up success!!')
        
        if config.DEV_MOD:
            print(f'memberDB : {member_db.memberDB}')

    elif menuNum == config.SIGN_IN:
        print('2. sign in')
        uId = input('please input member ID: ')
        uPw = input('please input member PW: ')
        
        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['uPw'] == uPw:
                print('sign in success!!')
            else:
                print('sign in fail -- pw error')
        else:
            print('sign in fail -- id error')        
      
    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
    elif menuNum == config.MEMBER_DELETE:
        print('4. delete')
    elif menuNum == config.SYSTEM_OUT:
        print('99.end')
        flag = False
    elif menuNum == config.SIGN_OUT:
        print('5.sign out')