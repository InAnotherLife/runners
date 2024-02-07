import os

import pytest
from competitors import Competitors
from results import Results

competitors = {
    "004": {
        "Имя": "Василий",
        "Фамилия": "Петров"
    },
    "003": {
        "Имя": "Василий",
        "Фамилия": "Шарапов"
    },
    "005": {
        "Имя": "Лидия",
        "Фамилия": "Костина"
    },
    "002": {
        "Имя": "Валентина",
        "Фамилия": "Щукина"
    },
    "001": {
        "Имя": "Светлана",
        "Фамилия": "Матвеева"
    }
}

results_data = [
    {
        "Номер": "004",
        "Участник": "Василий Петров",
        "Результат": "31:58.77"
    },
    {
        "Номер": "003",
        "Участник": "Василий Шарапов",
        "Результат": "44:40.79"
    },
    {
        "Номер": "005",
        "Участник": "Лидия Костина",
        "Результат": "35:39.38"
    },
    {
        "Номер": "002",
        "Участник": "Валентина Щукина",
        "Результат": "16:37.56"
    },
    {
        "Номер": "001",
        "Участник": "Светлана Матвеева",
        "Результат": "59:03.53"
    }
]

final = {
    "1": {
        "Номер": "002",
        "Участник": "Валентина Щукина",
        "Результат": "16:37.56"
    },
    "2": {
        "Номер": "004",
        "Участник": "Василий Петров",
        "Результат": "31:58.77"
    },
    "3": {
        "Номер": "005",
        "Участник": "Лидия Костина",
        "Результат": "35:39.38"
    },
    "4": {
        "Номер": "003",
        "Участник": "Василий Шарапов",
        "Результат": "44:40.79"
    },
    "5": {
        "Номер": "001",
        "Участник": "Светлана Матвеева",
        "Результат": "59:03.53"
    }
}


def test_read_numbers_file():
    competitors = Competitors()
    competitors.competitors_amount = 5
    competitors.gen_competitors()
    competitors.save_competitors()

    results = Results()
    competitors_data = results.read_competitors_file()
    assert isinstance(competitors_data, dict)
    assert len(competitors_data) == 5

    file_path = 'competitors.json'
    if os.path.isfile(file_path):
        os.remove(file_path)


def test_parse_results_file(monkeypatch):
    def mock_read_competitors_file(self):
        return competitors
    monkeypatch.setattr(Results, 'read_competitors_file',
                        mock_read_competitors_file)

    file_path = 'results.txt'
    with open(file_path, 'w', encoding='utf-8-sig') as file:
        file.write('004 16:58:04.144161 17:30:02.919575\n')
        file.write('003 16:58:04.144161 17:42:44.935140\n')
        file.write('005 16:58:04.144161 17:33:43.529931\n')
        file.write('002 16:58:04.144161 17:14:41.713726\n')
        file.write('001 16:58:04.144161 17:57:07.675733\n')

    results = Results()
    results_data = results.parse_results_file()
    assert len(results_data) == 5
    assert isinstance(results_data, list)
    for i, value in enumerate(results_data):
        result_item = results_data[i]
        assert result_item.get('Номер') == value.get('Номер')
        assert result_item.get('Участник') == value.get('Участник')
        assert result_item.get('Результат') == value.get('Результат')

    if os.path.isfile(file_path):
        os.remove(file_path)


def test_get_results(monkeypatch):
    def mock_parse_results_file(self):
        return results_data
    monkeypatch.setattr(Results, 'parse_results_file', mock_parse_results_file)

    results = Results()
    results.get_results()
    for key, value in final.items():
        item = results.results[int(key)]
        if item:
            assert item.get('Номер') == value.get('Номер')
            assert item.get('Участник') == value.get('Участник')
            assert item.get('Результат') == value.get('Результат')


def test_save_results():
    results = Results()
    results.results = final
    results.save_results()
    file_path = 'final.json'
    assert os.path.isfile(file_path)
    if os.path.isfile(file_path):
        os.remove(file_path)


if __name__ == '__main__':
    pytest.main()
