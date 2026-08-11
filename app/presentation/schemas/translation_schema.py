from pydantic import BaseModel, Field

class TranslationWordSchema(BaseModel):
    text: str = Field(min_length=1, max_length=128)
    src_lang: str = "english"
    dest_lang: str = "ukrainian"



class TranslationSentenceSchema(BaseModel):
    text: str = Field(min_length=1, max_length=2000)
    src_lang: str = "english"
    dest_lang: str = "ukrainian"
