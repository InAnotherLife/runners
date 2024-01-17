import json
import re
from datetime import datetime as dt

from settings import Settings


class CompetitorsResults(Settings):
    def __init__(self):
        super().__init__()
        self.__results = self.get_results()

    def read_competitors_file(self):
        """Чтение файла с данными спортсменов."""
        with open(self._config.get('Paths', 'competitors_data_file'), 'r',
                  encoding='utf-8') as competitors_file:
            competitors_data = json.load(competitors_file)
            return competitors_data

    def check_str(self, number, action, time):
        """
        Проверка строки на валидность.
        arg: 1. Порядковый номер спортсмена
             2. Действие (start или finish)
             3. Время в формате ЧЧ:ММ:СС,дст
        return: None
        """
        if not number.isdigit():
            raise Exception('File is damaged1!')
        if action not in ['start', 'finish']:
            raise Exception('File is damaged2!')
        if not re.match(r'^(0\d|1\d|2[0-4]):([0-5]\d):([0-5]\d),\d{6}$', time):
            raise Exception('File is damaged3!')

    def parse_results_file(self):
        """
        Чтение файла с результатами первой попытки и его парсинг.
        Метод возвращает список внутри, которого находится словарь с
        порядковыми номерами спортсменов и, соответствующим ему, временем.
        """
        results_list = []
        competitors_data = self.read_competitors_file()
        with open(self._config.get('Paths', 'results_file'), 'r',
                  encoding='utf-8-sig') as results_file:
            try:
                for line_1 in results_file:
                    line_2 = next(results_file)
                    str_1 = line_1.strip().split(' ')
                    str_2 = line_2.strip().split(' ')
                    if len(str_1) != 3 or len(str_2) != 3:
                        raise Exception('File is damaged4!')
                    self.check_str(str_1[0], str_1[1], str_1[2])
                    self.check_str(str_2[0], str_2[1], str_2[2])
                    number = str_1[0]
                    competitor = competitors_data[number]
                    time = dt.strptime(str_2[2], '%H:%M:%S,%f') - \
                        dt.strptime(str_1[2], '%H:%M:%S,%f')
                    results_list.append(
                        {'Нагрудный номер': number,
                         'Имя': competitor['First name'],
                         'Фамилия': competitor['Last name'],
                         'Результат': str(time).replace('.', ',')[2:-4]}
                    )
                return results_list
            except IndexError:
                print('File is damaged!')
            except KeyError:
                print('This key does not exist!')

    def get_results(self):
        """
        Метод сортирует результаты первой попытки и возвращает словарь, в
        котором ключи - места занятые спортсменами в порядке возрастания, а
        значения ключей - данные о спортсменах и результаты.
        """
        results_data = self.parse_results_file()
        results_dict = {}
        results_data.sort(key=lambda x: x['Результат'])
        for i, data in enumerate(results_data, start=1):
            results_dict[i] = data
        return results_dict

    def show_results(self):
        """Вывод данных о спортсменах и результатов в консоль."""
        print(f"{'Занятое место':<15}{'Нагрудный номер':<20}{'Имя':<15}"
              f"{'Фамилия':<15}{'Результат':<15}")
        for place, data in self.__results.items():
            print(f"{place:<15}{data['Нагрудный номер']:<20}{data['Имя']:<15}"
                  f"{data['Фамилия']:<15}{data['Результат']:<15}")

    def save_results(self):
        """Сохранение данных о спортсменах и результатов в файл."""
        with open(self._config.get('Paths', 'output_file'), 'w',
                  encoding='utf-8') as output_file:
            json.dump(self.__results, output_file, ensure_ascii=False,
                      indent=4)
