from calc_results import CompetitorsResults


if __name__ == '__main__':
    res = CompetitorsResults()

    print('Меню программы:')
    while True:
        
        print('"Выбран пункт меню: ', menu)
        if menu == 1:
            res.show_results()
            res.save_results()
            

    
