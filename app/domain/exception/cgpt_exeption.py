from typing import Optional

class CgptException(Exception):
    pass




class CgptNotFoundException(CgptException):
    def __init__(self, text: Optional[str], ):
        if text:
            super().__init__(f"Перевод слова  '{text}' из Русского на английский не найден")
        else:
            super().__init__(f"Неизвестная ошибка ")