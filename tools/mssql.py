
import sys
import pymssql
from tools.account_base import AccountBase
from utils.mail_utils import Mailer

class Mssql(AccountBase):

    __KEY = 'mssql'
    __DBA_MAIL = 'dba-email'
    __MANAGER_MAIL = 'manager-email'
    __SUBJECT = 'DB 계정생성 요청'

    def _get_config_key(self):
        return self.__KEY

    def _get_context(self):
        return ''

    def _create_db_user(self, user):
        # MSSQL 접속
        conn = pymssql.connect(host=self._host, user=self._admin_id, password=self._admin_pw, database=self._database)
        
        # Connection 으로부터 Cursor 생성
        cursor = conn.cursor()
        
        # SQL문 실행
        create_query = "CREATE LOGIN "+user.get_id()+" WITH PASSWORD = '"+user.get_password()+"';"
        cursor.execute(create_query)
        conn.commit()
        
        # 연결 끊기
        conn.close()
        
    def _request_dba_mail(self, user):
        mailer = Mailer()
        mail_config = mailer.get_config()
        dba_mail = mail_config[self.__DBA_MAIL]
        msg = 'DB 계정생성 요청\n'
        msg += 'ID : '+user.get_id()+'\n'
        msg += 'Role : 개발자\n'
        msg += '\n'
        mailer.send(user.get_email(), dba_mail, self.__SUBJECT, msg)

    def create_account(self, user):
        if self._auto_create:
            self._create_db_user(user)
        else:
            self._request_dba_mail(user)