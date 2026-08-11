from abc import ABC, abstractmethod

from app.domain.entity.cgpt import CgptDomain


class CgptProtocol(ABC):
    @abstractmethod
    async def get_translation_and_explanation(self, word: str) -> "CgptDomain":
        ...