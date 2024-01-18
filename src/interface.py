from competitors import Competitors
from delete import DeleteResult
from race import Race
from results import Results
from settings import Settings


class Interface:
    def __init__(self):
        self.__settings = Settings()
        self.__competitors = Competitors()
        self.__race = Race()
        self.__results = Results()
        self.__delete = DeleteResult()
        self.__gen_competitors = False
        self.__gen_race = False

    def show_menu(self):
        print('Выберите пункт меню:')
        print('1. Сгенерировать данные спортсменов')
        print('2. Сгенерировать время забега')
        print('3. Посчитать результаты забега')
        print('4. Сохранить результаты забега в файл')
        print('5. Удалить файлы с результатами расчета')
        print('6. Выйти из программы')
        print()

    def check_menu_item(self):
        if not self.__gen_competitors:
            print('Ошибка! Необходимо сгенерировать данные спортсменов.')
            print()
            return False
        if not self.__gen_competitors:
            print('Ошибка! Необходимо сгенерировать время забега.')
            print()
            return False
        return True

    def start_runners(self):
        print('Меню программы:')
        print()
        while True:
            self.show_menu()
            menu = int(input())
            print('Выбран пункт меню: ', menu)
            print()
            if menu == 1:
                man_amount = int(input('Введите количество спортсменов: '))
                print()
                self.__competitors.competitors_amount = man_amount
                self.__competitors.gen_competitors()
                self.__competitors.save_competitors()
                self.__gen_competitors = True
                self.__gen_race = False
                print('Данные спортсменов сохранены в файл:',
                      self.__settings._config.get(
                          'Paths', 'competitors_data_file'))
                print()
            elif menu == 2:
                self.__race.calc_race()
                self.__race.save_race()
                self.__gen_race = True
                print('Результаты забега сохранены в файл:',
                      self.__settings._config.get('Paths', 'results_file'))
                print()
            elif menu == 3:
                if self.check_menu_item():
                    self.__results.calc_results()
                    self.__results.show_results()
                    print()
            elif menu == 4:
                if self.check_menu_item():
                    print('Результаты расчета сохранены в файл:',
                          self.__settings._config.get('Paths', 'output_file'))
                    print()
                    self.__results.save_results()
            elif menu == 5:
                if self.check_menu_item():
                    print('Результаты расчета успешно удалены.')
                    print()
                    self.__gen_competitors = False
                    self.__gen_race = False
                    self.__delete.delete_results()
            elif menu == 6:
                print('Выход из программы.')
                exit()
            else:
                print('Ошибка! Недопустимый пункт меню.')
                print()