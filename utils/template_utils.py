
class Template:
    def success(self, user, services, manager_email):
        if not services:
            return None
        success_msg = '발급된 개발용 계정을 아래와 같이 안내해 드립니다.\n'
        success_msg += '\n'
        success_msg += '\n'
        success_msg += 'ID : ' + user.get_id()
        success_msg += '\n'
        success_msg += 'PW : ' + user.get_password()
        success_msg += '\n'
        success_msg += '---- 접속정보 ----\n'

        for i in range(len(services)):
            service = services.pop()
            success_msg += service.get_service_name()
            success_msg += ' : '
            success_msg += service.get_service_host()
            success_msg += '\n'

        success_msg += '\n'
        success_msg += '\n'
        success_msg += '접속에 문제가 있거나 기타문의는 '+manager_email+'로 문의 바랍니다.'
        return success_msg
    
    def fail(self, user, services):
        if not services:
            return None
        fail_msg = '아래의 사용자 계정생성에 실패하였습니다. 조치 바랍니다.'
        fail_msg += '\n'
        fail_msg += '\n'
        fail_msg += 'ID : ' + user.get_id()
        fail_msg += '\n'
        fail_msg += '이름 : ' + user.get_full_name()
        fail_msg += '\n'
        fail_msg += '---- 정보 ----\n'

        for i in range(len(services)):
            service = services.pop()
            fail_msg += service.get_service_name()
            fail_msg += ' : '
            fail_msg += service.get_service_host()
            fail_msg += '\n'

        fail_msg += '\n'
        fail_msg += '\n'
        return fail_msg