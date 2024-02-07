import datetime
import json
import random

from settings import Settings


class Race(Settings):
    def __init__(self):
        super().__init__()
        self.__results = []

    @property
    def results(self):
        """
        Геттер, возвращает значение переменной __results.
        arg: None
        return: list
        """
        return self.__results

    def read_numbers_file(self):
        """
        Чтение файла с номерами спортсменов.
        arg: None
        return: dict
        """
        with open(self._config.get('Paths', 'competitors_data_file'), 'r',
                  encoding='utf-8') as competitors_data_file:
            return json.load(competitors_data_file)

    def get_times(self):
        """
        Генерация случайного времени забега. Метод получает текущее время и
        прибавляет к нему случайное количество минут, секунд и микросекунд.
        Метод возвращает время старта и время финиша в формате %H:%M:%S.%f в
        виде строк.
        arg: None
        return: str, str
        """
        start_time = datetime.datetime.now()
        finish_time = start_time + datetime.timedelta(
            minutes=random.randint(1, 59), seconds=random.randint(0, 59),
            microseconds=random.randint(0, 999999))
        return start_time.time().isoformat(), finish_time.time().isoformat()

    def calc_race(self):
        """
        Расчет времени забега каждого спортсмена. Метод получает номера
        спортсменов и для каждого спортсмена генерирует время старта и время
        финиша забега.
        arg: None
        return: None
        """
        competitors_numbers = self.read_numbers_file()
        for value in competitors_numbers:
            start_time, finish_time = self.get_times()
            self.__results += f'{value} {start_time} {finish_time}\n'

    def show_race(self):
        """
        Выводит итоговую таблицу с временем забега спортсменов в консоль.
        arg: None
        return: None
        """
        print(''.join(self.__results))

    def save_race(self):
        """
        Сохраняет итоговую таблицу с временем забега спортсменов в файл.
        arg: None
        return: None
        """
        with open(self._config.get('Paths', 'results_file'), 'w',
                  encoding='utf-8') as output_file:
            for value in self.__results:
                output_file.write(str(value))
