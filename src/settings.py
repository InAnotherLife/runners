import configparser


class Settings:
    def __init__(self):
        # Для работы с файлом конфигурации используется модуль ConfigParser
        __settings_file = 'settings.ini'
        self._config = configparser.ConfigParser()
        self._config.read(__settings_file, encoding='utf-8')
