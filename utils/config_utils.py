import yaml

class ConfigUtils :
    _config_path = 'config.yml'

    def set_config_path(self, path):
        self._config_path = path
        return self

    def get_config(self) :
        config = None
        with open(self._config_path) as f:
            config = yaml.load(f)
        return config