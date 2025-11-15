from abc import abstractmethod, ABC


class TranslationProtocol(ABC):
    @abstractmethod
    async def translate_word(self, text: str, src_lang: str, dest_lang: str) -> str:
        pass


    @abstractmethod
    async def translate_sentence(self, text: str, src_lang: str, dest_lang: str) -> str:
        pass


    