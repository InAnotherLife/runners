import configparser


class Settings:
    def __init__(self):
        """
        Родительский класс для работы с файлом конфигурации. Переменная
        __settings_file задает имя файла конфигурации. Для чтения
        конфигурационного файла используется модуль ConfigParser.
        """
        __settings_file = 'settings.ini'
        self._config = configparser.ConfigParser()
        self._config.read(__settings_file, encoding='utf-8')
