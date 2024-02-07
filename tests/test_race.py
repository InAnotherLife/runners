import os

import pytest
from competitors import Competitors
from race import Race

competitors = {
    "004": {
        "Имя": "Григорий",
        "Фамилия": "Гордеев"
    },
    "003": {
        "Имя": "Дарья",
        "Фамилия": "Матвеева"
    },
    "002": {
        "Имя": "Жанна",
        "Фамилия": "Матвеева"
    },
    "001": {
        "Имя": "Яна",
        "Фамилия": "Горшкова"
    },
    "005": {
        "Имя": "Мария",
        "Фамилия": "Волкова"
    }
}


def test_read_numbers_file(monkeypatch):
    competitors = Competitors()
    competitors.competitors_amount = 5
    competitors.gen_competitors()
    competitors.save_competitors()

    race = Race()
    competitors_numbers = race.read_numbers_file()
    assert isinstance(competitors_numbers, dict)
    assert len(competitors_numbers) == 5


def test_get_times():
    race = Race()
    start_time, finish_time = race.get_times()
    assert isinstance(start_time, str)
    assert isinstance(finish_time, str)
    assert len(start_time) == 15
    assert len(finish_time) == 15
    assert start_time < finish_time


def test_calc_race(monkeypatch):
    def mock_read_numbers_file(self):
        return competitors
    monkeypatch.setattr(Race, 'read_numbers_file', mock_read_numbers_file)

    race = Race()
    race.calc_race()
    assert len(race.results) == 180


def test_save_race(monkeypatch):
    def mock_read_numbers_file(self):
        return competitors
    monkeypatch.setattr(Race, 'read_numbers_file', mock_read_numbers_file)

    race = Race()
    race.calc_race()
    race.save_race()
    file_path = '../src/results.txt'
    assert os.path.isfile(file_path)
    if os.path.isfile(file_path):
        os.remove(file_path)


if __name__ == '__main__':
    pytest.main()
