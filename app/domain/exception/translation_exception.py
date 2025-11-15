from typing import Optional

class TranslationException(Exception):
    pass



class TranslationNotFoundException(TranslationException):
    def __init__(self, text: Optional[str], src_lang: Optional[str], dest_lang: Optional[str]):
        if text:
            super().__init__(f"Перевод слова  '{text}' из '{src_lang}' в '{dest_lang}' не найден")
        else:
            super().__init__(f"Неизвестная ошибка ")
        self.text = text
        self.src_lang = src_lang
        self.dest_lang = dest_lang