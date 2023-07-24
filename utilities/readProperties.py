import configparser


config = configparser.RawConfigParser()
config.read("Configuration/config.ini")


class ReadConfig:
    @staticmethod
    def get_app_url():
        return config.get('common info', 'base_url')

    @staticmethod
    def get_email():
        return config.get('common info', 'email')

    @staticmethod
    def get_password():
        return config.get('common info', 'password')


# print(ReadConfig.get_app_url())
# print(ReadConfig.get_email())
# print(ReadConfig.get_password())
