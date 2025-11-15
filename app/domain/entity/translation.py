from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class WordTranslationDetails:
    word: str
    translation: str
    pronunciation: Optional[str]
    src_lang: str
    dest_lang: str
    additional_translations: List[str] = field(default_factory=list)

@dataclass(frozen=True)
class SentenceTranslation:
    sentence: str
    translation: str