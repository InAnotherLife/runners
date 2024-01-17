import json
import random

from settings import Settings


class CompetitorsData(Settings):
    def __init__(self, competitors_amount):
        super().__init__()
        self.__competitors_amount = competitors_amount
        self.__competitors = self.gen_competitors()

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
        competitors_dict = {}
        men_first_name, men_last_name, women_first_name, women_last_name = \
            self.read_competitors_file()
        competitors_numbers = self.get_numbers()
        men_amount, women_amount = self.get_man_amount()
        for number in competitors_numbers:
            random_first_name = random.choice(men_first_name)
            random_last_name = random.choice(men_last_name)
            competitors_dict[number] = {
                'First name': random_first_name,
                'Last name': random_last_name
            }
        return competitors_dict

    def save_results(self):
        """Сохранение данных о спортсменах и результатов в файл."""
        with open(self._config.get('Paths', 'competitors_file'), 'w',
                  encoding='utf-8') as competitors_file:
            json.dump(self.__competitors, competitors_file, ensure_ascii=False,
                      indent=4)


if __name__ == '__main__':
    data = CompetitorsData(100)
    data.save_results()
