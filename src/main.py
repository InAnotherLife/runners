from competitors import Competitors
from delete import DeleteResult
from menu import show_menu
from race import Race
from results import Results
from settings import Settings


def check_menu_item(gen_competitors, gen_race):
    if not gen_competitors:
        print('Ошибка! Необходимо сгенерировать данные спортсменов.')
        print()
        return False
    if not gen_race:
        print('Ошибка! Необходимо сгенерировать время забега.')
        print()
        return False
    return True


if __name__ == '__main__':
    settings = Settings()
    competitors = Competitors()
    race = Race()
    results = Results()
    delete = DeleteResult()
    gen_competitors = False
    gen_race = False
    print('Меню программы:')
    print()
    while True:
        show_menu()
        menu = int(input())
        print('Выбран пункт меню: ', menu)
        print()
        if menu == 1:
            man_amount = int(input('Введите количество спортсменов: '))
            print()
            competitors.competitors_amount = man_amount
            competitors.gen_competitors()
            competitors.save_competitors()
            gen_competitors = True
            gen_race = False
            print('Данные спортсменов сохранены в файл:', settings._config.get(
                'Paths', 'competitors_data_file'))
            print()
        elif menu == 2:
            race.calc_race()
            race.save_race()
            gen_race = True
            print('Результаты забега сохранены в файл:', settings._config.get(
                'Paths', 'results_file'))
            print()
        elif menu == 3:
            if check_menu_item(gen_competitors, gen_race):
                results.calc_results()
                results.show_results()
                print()
        elif menu == 4:
            if check_menu_item(gen_competitors, gen_race):
                print('Результаты расчета сохранены в файл:',
                      settings._config.get('Paths', 'output_file'))
                print()
                results.save_results()
        elif menu == 5:
            if check_menu_item(gen_competitors, gen_race):
                print('Результаты расчета успешно удалены.')
                print()
                gen_competitors = False
                gen_race = False
                delete.delete_results()
        elif menu == 6:
            print('Выход из программы.')
            exit()
        else:
            print('Ошибка! Недопустимый пункт меню.')
            print()
