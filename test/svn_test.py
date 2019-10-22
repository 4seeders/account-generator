import os
import sys
# 부모디렉토리 참조를 위한 설정추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.svn_edge import SvnEdge
from utils.config_utils import ConfigUtils
from user import User

# given
config = ConfigUtils().set_config_path('../config.yml').get_config()

user = User('test001', '홍길동', 'test126@4seeders.com')

svn = SvnEdge()
svn.set_config(config)


# when - login
## login 성공 케이스
svn._login()

# when - get sync
svn._admin_id = 'admin'
svn._login()
svn._get_sync_value()

# when - create account
svn.create_account(user)

# then - exception이 발생하지 않았으면 성공
print('테스트 성공')