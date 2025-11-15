from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class WordTranslationDetailsDTO:
    word: str
    translation: str
    pronunciation: str
    src_lang: str
    dest_lang: str
    additional_translations: List[str]

@dataclass(frozen=True)
class SentenceTranslationDTO:
    sentence: str
    translation: str