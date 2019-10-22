import os
import sys
# 부모디렉토리 참조를 위한 설정추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.redmine import Redmine
from utils.config_utils import ConfigUtils
from user import User

# given
config = ConfigUtils().set_config_path('../config.yml').get_config()

user = User('test001', '홍길동', 'test126@4seeders.com')

redmine = Redmine()
redmine.set_config(config)


# when 계정생성
redmine._create_user(user)

# when - get sync
new_id = redmine._find_user(user.get_id())

print(new_id)

# when - create account
redmine._add_project_user(new_id)

# then - exception이 발생하지 않았으면 성공
print('테스트 성공')