import os
import sys

# 부모디렉토리 참조를 위한 설정추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from user import User

user = User('test123','홍길동')


# 초기패스워드 조회 
print(user.get_passowrd())


# get full name
if user.get_full_name() == '홍길동':
    print('pass => get full name : ', user.get_full_name())
else:
    raise ValueError()


# 성 출력
if user.get_last_name() == '홍':
    print('pass => get last name : ', user.get_last_name())
else:
    raise ValueError()


# 이름 출력
if user.get_first_name() == '길동':
    print('pass => get first name : ', user.get_first_name())
else:
    raise ValueError()