import json
import random

from settings import Settings


class Competitors(Settings):
    def __init__(self):
        super().__init__()
        self.__competitors_amount = None
        self.__competitors = {}

    @property
    def competitors_amount(self):
        return self.__competitors_amount

    @competitors_amount.setter
    def competitors_amount(self, value):
        if value <= 0:
            raise ValueError(
                f'Количество спортсменов не может быть отрицательным или '
                f'равным нулю!')
        self.__competitors_amount = value

    def read_competitors_file(self):
        with open(self._config.get('Paths', 'competitors_file'), 'r',
                  encoding='utf-8-sig') as competitors_file:
            men_first_name = competitors_file.readline().strip().split(' ')
            men_last_name = competitors_file.readline().strip().split(' ')
            women_first_name = competitors_file.readline().strip().split(' ')
            women_last_name = competitors_file.readline().strip().split(' ')
            return men_first_name, men_last_name, women_first_name, \
                women_last_name

    def get_numbers(self):
        numbers = []
        for i in range(1, self.__competitors_amount + 1):
            numbers.append(str(i).zfill(3))
        random.shuffle(numbers)
        return numbers

    def get_man_amount(self):
        men_amount = random.randint(0, self.__competitors_amount)
        women_amount = self.__competitors_amount - men_amount
        return men_amount, women_amount

    def gen_competitors(self):
        men_first_name, men_last_name, women_first_name, women_last_name = \
            self.read_competitors_file()
        competitors_numbers = self.get_numbers()
        men_amount, women_amount = self.get_man_amount()
        for number in competitors_numbers:
            random_first_name = random.choice(men_first_name)
            random_last_name = random.choice(men_last_name)
            self.__competitors[number] = {
                'First name': random_first_name,
                'Last name': random_last_name
            }

    def show_results(self):
        competitors = json.dumps(
            self.__competitors, indent=4, ensure_ascii=False)
        print(competitors)

    def save_results(self):
        """Сохранение данных о спортсменах и результатов в файл."""
        with open(self._config.get('Paths', 'competitors_data_file'), 'w',
                  encoding='utf-8') as competitors_data_file:
            json.dump(self.__competitors, competitors_data_file,
                      ensure_ascii=False, indent=4)


if __name__ == '__main__':
    competitors = Competitors()
    competitors.competitors_amount = 100
    competitors.gen_competitors()
    competitors.show_results()
    competitors.save_results()
