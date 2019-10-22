import os
import sys
# 부모디렉토리 참조를 위한 설정추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.mssql import Mssql
from utils.config_utils import ConfigUtils
from user import User

# given
config = ConfigUtils().set_config_path('../config.yml').get_config()

user = User('test001', '홍길동', 'test125@4seeders.com')

mssql = Mssql()
mssql.set_config(config)

#DBA에게 계정생성 요청 메일 전송
mssql._request_dba_mail(user)

#DB 계정생성
mssql._create_db_user(user)

#
print('테스트성공')