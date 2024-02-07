import json
from datetime import datetime as dt

from settings import Settings


class Results(Settings):
    def __init__(self):
        super().__init__()
        self.__results = {}

    @property
    def results(self):
        """
        Геттер, возвращает значение переменной __results.
        arg: None
        return: dict
        """
        return self.__results

    @results.setter
    def results(self, value):
        """
        Сеттер, устанавливает значение переменной __results.
        arg: dict
        return: None
        """
        self.__results = value

    def read_competitors_file(self):
        """
        Чтение файла с данными спортсменов.
        arg: None
        return: dict
        """
        with open(self._config.get('Paths', 'competitors_data_file'), 'r',
                  encoding='utf-8') as competitors_file:
            return json.load(competitors_file)

    def parse_results_file(self):
        """
        Парсинг файла с результатами забега. Для каждой строки выполняются
        следующие действия: чтение двух последовательных строк и разбиение
        их на отдельные элементы, проверка строк на валидность, получение
        номера спортсмена, вычисление времени забега спортсмена. Метод
        возвращает список словарей с данными спортсменов.
        arg: None
        return: list
        """
        results_list = []
        competitors_data = self.read_competitors_file()
        with open(self._config.get('Paths', 'results_file'), 'r',
                  encoding='utf-8-sig') as results_file:
            for line in results_file:
                line_list = line.strip().split(' ')
                number = line_list[0]
                competitor = competitors_data.get(number)
                if competitor:
                    time = dt.strptime(line_list[2], '%H:%M:%S.%f') - (
                        dt.strptime(line_list[1], '%H:%M:%S.%f'))
                    results_list.append(
                        {'Номер': number,
                         'Участник': f"{competitor['Имя']} "
                                     f"{competitor['Фамилия']}",
                         'Результат': str(time)[2:-4]
                         }
                    )
            return results_list

    def get_results(self):
        """
        Сортировка результатов забега по времени. Метод получает данные о
        спортсменах, сортирует их по времени забега в порядке возрастания
        и сохраняет данные в словарь, в котором ключи - места занятые
        спортсменами в порядке возрастания, а значения - данные о спортсменах.
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
