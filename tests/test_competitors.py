import os

import pytest
from competitors import Competitors


def test_competitors_setter_getter():
    competitors = Competitors()
    competitors.competitors_amount = 10
    assert competitors.competitors_amount == 10


def test_read_competitors_file():
    competitors = Competitors()
    men_first_name, men_last_name, women_first_name, women_last_name = (
        competitors.read_competitors_file())
    assert isinstance(men_first_name, list)
    assert isinstance(men_last_name, list)
    assert isinstance(women_first_name, list)
    assert isinstance(women_last_name, list)
    assert len(men_first_name) > 0
    assert len(men_last_name) > 0
    assert len(women_first_name) > 0
    assert len(women_last_name) > 0


def test_get_competitors_numbers():
    competitors = Competitors()
    competitors.competitors_amount = 10
    numbers = competitors.get_competitors_numbers()
    assert isinstance(numbers, list)
    assert len(numbers) == competitors.competitors_amount


def test_get_men_amount():
    competitors = Competitors()
    competitors.competitors_amount = 10
    men_amount = competitors.get_men_amount()
    assert str(men_amount).isdigit()
    assert 0 <= men_amount <= 10


def test_gen_competitors():
    competitors = Competitors()
    competitors.competitors_amount = 10
    competitors.gen_competitors()
    assert len(competitors._Competitors__competitors) == 10


def test_save_competitors():
    competitors = Competitors()
    competitors.competitors_amount = 10
    competitors.gen_competitors()
    competitors.save_competitors()
    file_path = '../src/competitors.json'
    assert os.path.isfile(file_path)
    if os.path.isfile(file_path):
        os.remove(file_path)


if __name__ == '__main__':
    pytest.main()
