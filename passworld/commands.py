from enum import Enum


class command(Enum):
    ADD_PASSWORD = "Добавить пароль"
    FIND_PASSWORD = "Найти пароль"
    CHANGE_PASSWORD = "Изменить пароль"

    def __init__(self, text):
        self.text = text
