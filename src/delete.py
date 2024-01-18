import os

from settings import Settings


class DeleteResult(Settings):
    def __init__(self):
        super().__init__()

    def delete_results(self):
        """
        Удаляет результаты расчета. Метод при возникновении любых исключений
        ничего не делает.
        arg: None
        return: None
        """
        try:
            os.remove(self._config.get('Paths', 'competitors_data_file'))
            os.remove(self._config.get('Paths', 'results_file'))
            os.remove(self._config.get('Paths', 'output_file'))
        except Exception:
            pass
