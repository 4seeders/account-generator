
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from utils.config_utils import ConfigUtils

class Mailer:
    __KEY = 'email'

    def __init__(self):
        config = ConfigUtils().get_config()
        self._mail_config = mail_config = config[self.__KEY]
        self._smtp_host = mail_config['smtp-host']
        self._login_id = mail_config['login-id']
        self._login_pw = mail_config['login-pw']

    def get_config(self):
        return self._mail_config

    def send(self, from_addr, to_addr, subject, content):
        msg = MIMEText(content)
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = from_addr
        msg['To'] = to_addr

        with smtplib.SMTP_SSL(self._smtp_host) as smtp:
            smtp.login(self._login_id, self._login_pw)
            smtp.send_message(msg)