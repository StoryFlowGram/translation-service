from dataclasses import dataclass, field
from typing import List, Optional 



@dataclass(frozen=True)
class CgptDomain:
    word: str
    translation: str
    explanation: str 
    etymology: Optional[str] 