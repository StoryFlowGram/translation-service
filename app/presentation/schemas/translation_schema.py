from unittest.mock import Base
from pydantic import BaseModel

class TranslationWordSchema(BaseModel):
    text: str
    src_lang: str = "english"
    dest_lang: str = "ukrainian"



class TranslationSentenceSchema(BaseModel):
    text: str
    src_lang: str = "english"
    dest_lang: str = "ukrainian"