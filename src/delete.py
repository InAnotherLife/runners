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
        paths = dict(self._config.items('Paths')).values()
        for path in paths:
            if os.path.isfile(path):
                os.remove(path)
