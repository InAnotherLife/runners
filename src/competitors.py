import json
import random

from settings import Settings


class Competitors(Settings):
    def __init__(self):
        super().__init__()
        self.__competitors_amount: int = None
        self.__competitors = {}

    @property
    def competitors_amount(self):
        """
        Геттер, возвращает значение переменной __competitors_amount.
        arg: None
        return: int
        """
        return self.__competitors_amount

    @competitors_amount.setter
    def competitors_amount(self, value):
        """
        Сеттер, устанавливает значение переменной __competitors_amount.
        Метод также проверяет, что значение переменной value не является
        отрицательным или равным нулю.
        arg: int
        return: None
        """
        if value <= 0:
            raise ValueError(
                f"{'Количество спортсменов не может быть отрицательным или '}"
                f"{'равным нулю!'}"
            )
        self.__competitors_amount = value

    def read_competitors_file(self):
        """
        Чтение фамилий и имен спортсменов из файла.
        arg: None
        return: list, list, list, list
        """
        with open(self._config.get('Data', 'competitors_file'), 'r',
                  encoding='utf-8-sig') as competitors_file:
            men_last_name = competitors_file.readline().strip().split(' ')
            men_first_name = competitors_file.readline().strip().split(' ')
            women_last_name = competitors_file.readline().strip().split(' ')
            women_first_name = competitors_file.readline().strip().split(' ')
            return (men_first_name, men_last_name, women_first_name,
                    women_last_name)

    def get_competitors_numbers(self):
        """
        Генерирует номера спортсменов.
        arg: None
        return: list
        """
        numbers = [str(i).zfill(3)
                   for i in range(1, self.__competitors_amount + 1)]
        random.shuffle(numbers)
        return numbers

    def get_men_amount(self):
        """
        Генерирует количество мужчин.
        arg: None
        return: int, int
        """
        return random.randint(0, self.__competitors_amount)

    def gen_competitors(self):
        """
        Генерирует данные о спортсменах: номер спортсмена, фамилию, имя.
        В методе происходит чтение данных из файла с фамилиями и именами
        спортсменов, получение номеров спортсменов, определение количества
        мужчин и женщин. Затем для каждого спортсмена выбираются случайные
        фамилия и имя. Данные добавляются в словарь __competitors под
        соответствующим номером спортсмена.
        arg: None
        return: None
        """
        men_first_name, men_last_name, women_first_name, women_last_name = (
            self.read_competitors_file())
        competitors_numbers = self.get_competitors_numbers()
        men_amount = self.get_men_amount()
        for i, number in enumerate(competitors_numbers):
            if i in range(0, men_amount):
                random_first_name = random.choice(men_first_name)
                random_last_name = random.choice(men_last_name)
            else:
                random_first_name = random.choice(women_first_name)
                random_last_name = random.choice(women_last_name)
            self.__competitors[number] = {
                'Имя': random_first_name,
                'Фамилия': random_last_name
            }

    def show_competitors(self):
        """
        Выводит данные о спортсменах в консоль.
        arg: None
        return: None
        """
        print(json.dumps(self.__competitors, indent=4, ensure_ascii=False))

    def save_competitors(self):
        """
        Сохраняет данные о спортсменах в файл.
        arg: None
        return: None
        """
        with open(self._config.get('Paths', 'competitors_data_file'), 'w',
                  encoding='utf-8') as competitors_data_file:
            json.dump(self.__competitors, competitors_data_file,
                      ensure_ascii=False, indent=4)
