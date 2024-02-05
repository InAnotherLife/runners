import configparser
import os

import pytest
from delete import DeleteResult


def test_remove_files():
    settings_file = 'settings.ini'
    config = configparser.ConfigParser()
    config.read(settings_file, encoding='utf-8')

    keys = config['Paths']
    for i, key in enumerate(keys):
        if key:
            file = open(keys.get(key), 'w')
            file.write(f'Test file {i + 1}')
            file.close()

    delete = DeleteResult()
    delete.delete_results()

    for key in keys:
        if key:
            assert not os.path.isfile(keys.get(key))


if __name__ == '__main__':
    pytest.main()
