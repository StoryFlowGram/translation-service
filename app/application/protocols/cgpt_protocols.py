from abc import ABC, abstractmethod


class CgptProtocol(ABC):
    @abstractmethod
    async def get_translation_and_explanation(self, text: str) -> str:
        ...