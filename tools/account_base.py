from abc import *

class ConfigKeys():
    HOST = 'host'
    ADMIN_ID = 'admin-id'
    ADMIN_PW = 'admin-pw'
    AUTH_KEY = 'auth-key'
    DATABASE = 'database'
    SERVICE_NAME = 'service-name'
    SERVICE_HOST = 'service-host'
    AUTO_CREATE = 'auto_create'

class AccountBase(metaclass=ABCMeta):

    @abstractmethod
    def _get_config_key(self):
        pass

    @abstractmethod
    def _get_context(self):
        pass

    @abstractmethod
    def create_account(self, user):
        pass

    def get_service_host(self):
        return self._service_host

    def get_service_name(self):
        return self._service_name

    def is_auto_create(self):
        return self._auto_create

    # config 설정 셋팅
    def set_config(self, configs):
        config_keys = ConfigKeys()
        self._config = config = configs[self._get_config_key()]
        self._host = config[config_keys.HOST]
        self._endpoint = self._host + self._get_context()
        
        if (config_keys.ADMIN_ID in config):
            self._admin_id = config[config_keys.ADMIN_ID]

        if (config_keys.ADMIN_PW in config):
            self._admin_pw = config[config_keys.ADMIN_PW]

        if (config_keys.AUTH_KEY in config):
            self._auth_key = config[config_keys.AUTH_KEY]

        if (config_keys.DATABASE in config):
            self._database = config[config_keys.DATABASE]

        if (config_keys.SERVICE_NAME in config):
            self._service_name = config[config_keys.SERVICE_NAME]

        if (config_keys.SERVICE_HOST in config):
            self._service_host = config[config_keys.SERVICE_HOST]
        else:
            self._service_host = self._endpoint

        if (config_keys.AUTO_CREATE in config):
            self._auto_create = config[config_keys.AUTO_CREATE]
        else:
            self._auto_create = True
        