import yaml
import os

class ConfigReader:
    _config = None
    _env_config = None

    @staticmethod
    def load_config(env=None):
        if ConfigReader._config is None:
            with open("config/config.yaml") as f:
                ConfigReader._config = yaml.safe_load(f)

            if env is None:
                env = ConfigReader._config["default_env"]

            env_file = f"config/env_{env}.yaml"
            with open(env_file) as f:
                ConfigReader._env_config = yaml.safe_load(f)

    @staticmethod
    def get(key):
        return ConfigReader._config.get(key)

    @staticmethod
    def get_env(key):
        return ConfigReader._env_config.get(key)
