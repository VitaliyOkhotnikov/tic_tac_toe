class FieldIndexError(IndexError):
    """Выбрасывается, если выбрано значение вне поля."""

    def __init__(
        self,
        # Текст по умолчанию.
        message='Введено значение за границами игрового поля!'
    ):
        super().__init__(message)


class CellOccupiedError(Exception):
    """Выбрасывается, если выбрано занятое поле"""

    def __init__(
        self,
        message='Попытка заменить занятую ячейку'
    ):
        super().__init__(message)
