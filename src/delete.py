import os

from settings import Settings


class DeleteResult(Settings):
    def __init__(self):
        super().__init__()

    def delete_results(self):
        """
        Удаляет созданные файлы.
        arg: None
        return: None
        """
        files = dict(self._config.items('Paths')).values()
        for file in files:
            if os.path.isfile(file):
                os.remove(file)
