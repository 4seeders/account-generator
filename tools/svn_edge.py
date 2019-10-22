import requests 
from tools.account_base import AccountBase
from bs4 import BeautifulSoup

class SvnEdge(AccountBase):
    __KEY = 'svn'
    __CONTEXT = '/csvn'
    __LOGIN_URI = '/j_spring_security_check'
    __CREATE_USER_URI = '/user/save'
    __CREATE_USER_FORM_URI = '/user/index'       

    def __init__(self):
        self._session = requests.Session()

    ## account base 추상메소드
    def _get_config_key(self):
        return self.__KEY
        
    def _get_context(self):
        return self.__CONTEXT

    def _login(self):
        login_data = {
            'j_username':self._admin_id,
            'j_password':self._admin_pw
        }

        login_url = self._endpoint + self.__LOGIN_URI
        login_res = self._session.post(login_url, data=login_data)

        if login_res.status_code != 200:
            return False

        bs = BeautifulSoup(login_res.text, 'html.parser')
        sync_token_input = bs.find('input', {'id' : 'SYNCHRONIZER_TOKEN'})

        if sync_token_input == None:
            raise BaseException('로그인에 실패하였습니다.')

    def _get_sync_value(self):
        #sync* 값을 얻기 위한 페이지 호출
        user_form_url = self._endpoint + self.__CREATE_USER_FORM_URI
        user_form_res = self._session.get(user_form_url)
        
        #파싱시작
        bs = BeautifulSoup(user_form_res.text, 'html.parser')
        sync_token_input = bs.find('input', {'id' : 'SYNCHRONIZER_TOKEN'})

        if sync_token_input == None:
            raise BaseException('보안값을 가져오는데 실패하였습니다.')

        sync_token = sync_token_input['value']
        sync_uri = bs.find('input', {'id' : 'SYNCHRONIZER_URI'})['value']

        return {'SYNCHRONIZER_TOKEN':sync_token, 'SYNCHRONIZER_URI':sync_uri}

    def get_endpoint(self):
        return self._endpoint

    def create_account(self, user):

        # session 유지
        with self._session as s:
            # 로그인 요청
            if self._login() == False:
                return False

            # sync 값 가져오기
            sync_value = self._get_sync_value()
            if sync_value == None :
                return False

            user_data = {'username': user.get_id()
                ,'realUserName': user.get_full_name()
                ,'passwd': user.get_password()
                ,'passwordConfirm': user.get_password()
                ,'email': user.get_email()
                ,'description': 'developer'
                ,'authorities': '2'}

            user_data.update(sync_value)

            create_user_url = self._endpoint + self.__CREATE_USER_URI
            new_user_res = s.post(create_user_url, data=user_data)

            if (new_user_res.status_code!=200):
                raise BaseException('계정생성에 실패하였습니다.')

            bs = BeautifulSoup(new_user_res.text, 'html.parser')
            success_msg = bs.find('div', {'class' : 'alert alert-success'})    
            
            # 성공메시지가 존재하는지 확인.
            if success_msg == None:
                raise BaseException('계정생성에 실패하였습니다.')

        return True