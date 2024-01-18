import json
import re
from datetime import datetime as dt

from settings import Settings


class Results(Settings):
    def __init__(self):
        super().__init__()
        self.__results = {}

    def read_competitors_file(self):
        """
        Чтение файла с данными спортсменов.
        arg: None
        return: Dict
        """
        with open(self._config.get('Paths', 'competitors_data_file'), 'r',
                  encoding='utf-8') as competitors_file:
            competitors_data = json.load(competitors_file)
            return competitors_data

    def check_str(self, number, action, time):
        """
        Проверка строки на валидность. Если какой-либо из элементов строки не 
        соответствует формату, то выбрасывается исключение.
        arg: 1. Порядковый номер спортсмена
             2. Действие (старт или финиш)
             3. Время в формате ЧЧ:ММ:СС,дст
        return: None
        """
        if not number.isdigit():
            raise Exception(
                'Ошибка! Номер спортсмена может содержать только цифры.')
        if action not in ['старт', 'финиш']:
            raise Exception(
                "Ошибка! Действие может быть только 'старт' или 'финиш'.")
        if not re.match(r'^(0\d|1\d|2[0-4]):([0-5]\d):([0-5]\d),\d{6}$', time):
            raise Exception('Ошибка! Неправильный формат времени забега.')

    def parse_results_file(self):
        """
        Чтение файла с результатами забега и его парсинг. Метод возвращает
        список внутри, которого находится словарь с номерами спортсменов и
        временем забега. Если происходит ошибка, то выбрасывается исключение.
        arg: None
        return: List
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
                        raise Exception(
                            'Ошибка! Файл с результатами забега поврежден.')
                    self.check_str(str_1[0], str_1[1], str_1[2])
                    self.check_str(str_2[0], str_2[1], str_2[2])
                    number = str_1[0]
                    competitor = competitors_data[number]
                    time = dt.strptime(str_2[2], '%H:%M:%S,%f') - \
                        dt.strptime(str_1[2], '%H:%M:%S,%f')
                    results_list.append(
                        {'Номер': number,
                         'Участник': f"{competitor['Имя']} "
                                     f"{competitor['Фамилия']}",
                         'Результат': str(time).replace('.', ',')[2:-4]}
                    )
                return results_list
            except IndexError:
                print('Ошибка! Файл с данными спортсменов поврежден.')
            except KeyError:
                print('Ошибка! Спортсмена с таким номером не существует.')

    def calc_results(self):
        """
        Метод сортирует результаты забега по времени. Метод возвращает словарь,
        в котором ключи - места занятые спортсменами в порядке возрастания,
        а значения ключей - данные о спортсменах и время забега.
        arg: None
        return: None
        """
        results_data = self.parse_results_file()
        results_data.sort(key=lambda x: x['Результат'])
        for i, data in enumerate(results_data, start=1):
            self.__results[i] = data

    def show_results(self):
        """
        Вывод данных о спортсменах и времени забега в консоль.
        arg: None
        return: None
        """
        print(f"{'Место':<10}{'Номер':<10}{'Участник':<20}{'Результат':<15}")
        for place, data in self.__results.items():
            print(f"{place:<10}{data['Номер']:<10}{data['Участник']:<20}"
                  f"{data['Результат']:<15}")

    def save_results(self):
        """
        Сохранение данных о спортсменах и времени забега в файл.
        arg: None
        return: None
        """
        with open(self._config.get('Paths', 'output_file'), 'w',
                  encoding='utf-8') as output_file:
            json.dump(self.__results, output_file, ensure_ascii=False,
                      indent=4)
