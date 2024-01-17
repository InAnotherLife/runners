import datetime
import json
import random

from settings import Settings


class CompetitorsResults(Settings):
    def __init__(self, competitors_amount):
        super().__init__()
        self.__competitors_amount = competitors_amount
        self.__competitors_results = self.get_results()

    def get_numbers(self):
        """Чтение файла с данными спортсменов."""
        with open(self._config.get('Paths', 'competitors_data_file'), 'r',
                  encoding='utf-8') as competitors_file:
            competitors_data = json.load(competitors_file)
            return competitors_data.keys()

            # numbers = []
            # for i in range(1, self.__competitors_amount + 1):
            #     numbers.append(str(i).zfill(3))
            # random.shuffle(numbers)
            # return numbers

    def get_times(self):
        start_time = datetime.datetime.now()
        finish_time = start_time + datetime.timedelta(
            minutes=random.randint(1, 59), seconds=random.randint(0, 59),
            microseconds=random.randint(0, 999999))
        return start_time.strftime('%H:%M:%S,%f'), finish_time.strftime(
            '%H:%M:%S,%f')

    def get_results(self):
        results = []
        competitors_numbers = self.get_numbers()
        for value in competitors_numbers:
            start_time, finish_time = self.get_times()
            results += f'{value} start {start_time}\n'
            results += f'{value} finish {finish_time}\n'
        return results

    def show_results(self):
        print(''.join(self.__competitors_results))

    def save_results(self):
        with open(self._config.get('Paths', 'results_file'), 'w',
                  encoding='utf-8') as output_file:
            for value in self.__competitors_results:
                output_file.write(str(value))


if __name__ == '__main__':
    results = CompetitorsResults(100)
    results.show_results()
    results.save_results()
