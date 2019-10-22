import argparse


from tools.redmine import Redmine
from tools.svn_edge import SvnEdge
from tools.mssql import Mssql
from user import User
from utils.config_utils import ConfigUtils
from utils.mail_utils import Mailer
from utils.template_utils import Template

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo account -i id -n name")
    parser.add_argument('-i', help="develper_id", required=True)
    parser.add_argument('-n', help="develper_name", required=True)
    
    args = parser.parse_args()
    config = ConfigUtils().get_config()
    email_config = config['email']
    
    eamil_addr = args.i+'@'+email_config['service-host']

    #user 객체 새성
    user = User(args.i, args.n, eamil_addr)

    #계정 생성이 필요한 서비스를 list에 넣는다.
    services = []
    services.append(SvnEdge())
    services.append(Redmine())
    services.append(Mssql())

    #성공과 실패를 분리
    success = []
    fail = []

    #처리해야 하는 서비스 처리
    for i in range(len(services)):
        try:
            service = services.pop()
            service.set_config(config)
            service.create_account(user)
            if not service.is_auto_create():
                continue
            success.append(service)
        except:
            fail.append(service)
    
    manager_email = email_config['manager-email']
    template = Template()

    success_msg = template.success(user, success, manager_email)
    fail_msg = template.fail(user,fail)

    mailer = Mailer()
    if success_msg:
        mailer.send(manager_email, user.get_email(), '개발계정발급 및 안내', success_msg)

    if fail_msg:
        mailer.send(manager_email, manager_email, '개발계정발급 실패', fail_msg)