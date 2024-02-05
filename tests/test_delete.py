import configparser
import os

import pytest
from delete import DeleteResult


def test_remove_files():
    settings_file = 'settings.ini'
    config = configparser.ConfigParser()
    config.read(settings_file, encoding='utf-8')

    paths = config['Paths']
    for i, key in enumerate(paths):
        if key:
            file = open(paths.get(key), 'w')
            file.write(f'Test file {i + 1}')
            file.close()

    delete_result = DeleteResult()
    delete_result.delete_results()

    for key in paths:
        assert not os.path.isfile(paths.get(key))


if __name__ == '__main__':
    pytest.main()
