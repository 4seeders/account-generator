import requests 
from tools.account_base import AccountBase

class Redmine(AccountBase):

    __KEY = 'redmine'
    __CONTEXT = '/redmine'
    __LOGIN_URI = '/login'
    __CREATE_USER_URI = '/users.json'
    __MEMBERSHIP_URI='/projects/mes/memberships.json'
    __FIND_USER_URI='/users.json'

    def __init__(self):
        self._session = requests.Session()

    def _get_config_key(self):
        return self.__KEY
        
    def _get_context(self):
        return self.__CONTEXT

    def _create_user(self, user):
        # 계정생성
        create_user_url = self._endpoint + self.__CREATE_USER_URI

        # 유저정보설정
        user_data = {
            'user': {
                    'login': user.get_id(),
                    'firstname': user.get_first_name(),
                    'lastname': user.get_last_name(),
                    'mail': user.get_email(),
                    'password': user.get_password()
                }
        }
        
        #생성요청
        new_user_res = self._session.post(create_user_url, headers=self._headers, json=user_data)

        #실패일 경우 exception 발생
        if (new_user_res.status_code!=200 and new_user_res.status_code!=201):
            raise BaseException('계정생성에 실패하였습니다.')  

    def _add_project_user(self, new_id):
        # 프로젝트 구성원으로 등록하기 위한 url
        membership_url = self._endpoint + self.__MEMBERSHIP_URI

        # 프로젝트 구성원 url
        membership_data = {
            'membership':{'user_id': new_id, 'role_ids': [4]}
        }

        membership_res = self._session.post(membership_url, headers=self._headers, json=membership_data)

        #성공일 경우 처리
        if (membership_res.status_code!=200 and membership_res.status_code!=201):
            raise BaseException(membership_res.text, '계정생성에 실패하였습니다.')

    def _find_user(self, login):
        find_user_url = self._endpoint + self.__FIND_USER_URI
        find_user = {'name':login}
        find_user_res = self._session.get(find_user_url, headers=self._headers, json=find_user)
        new_id = find_user_res.json()['users'][0]['id']
        return new_id

    def set_config(self, config):
        super().set_config(config)
        self._headers = {'X-Redmine-API-Key':self._auth_key}

    def get_endpoint(self):
        return self._endpoint

    def create_account(self, user):


        #사용자등록
        self._create_user(user)
        #등록한 user id를 가져와서 프로젝트에 등록
        new_id = self._find_user(user.get_id())
        self._add_project_user(new_id)