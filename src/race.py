import datetime
import json
import random

from settings import Settings


class Race(Settings):
    def __init__(self):
        super().__init__()
        self.__results = []

    def get_numbers(self):
        """Чтение файла с номерами спортсменов."""
        with open(self._config.get('Paths', 'competitors_data_file'), 'r',
                  encoding='utf-8') as competitors_data_file:
            competitors_data = json.load(competitors_data_file)
            return competitors_data.keys()

    def get_times(self):
        start_time = datetime.datetime.now()
        finish_time = start_time + datetime.timedelta(
            minutes=random.randint(1, 59), seconds=random.randint(0, 59),
            microseconds=random.randint(0, 999999))
        return start_time.strftime('%H:%M:%S,%f'), finish_time.strftime(
            '%H:%M:%S,%f')

    def calc_race(self):
        competitors_numbers = self.get_numbers()
        for value in competitors_numbers:
            start_time, finish_time = self.get_times()
            self.__results += f'{value} старт {start_time}\n'
            self.__results += f'{value} финиш {finish_time}\n'

    def show_race(self):
        print(''.join(self.__results))

    def save_race(self):
        with open(self._config.get('Paths', 'results_file'), 'w',
                  encoding='utf-8') as output_file:
            for value in self.__results:
                output_file.write(str(value))


if __name__ == '__main__':
    race = Race()
    race.calc_race()
    race.show_race()
    race.save_race()
