from dataclasses import dataclass



@dataclass
class CgptTranslationDTO:
    word: str
    translation: str
    explanation: str 
    etymology: str