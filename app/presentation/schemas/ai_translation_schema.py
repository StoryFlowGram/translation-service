from pydantic import BaseModel



class AiTranslationSchema(BaseModel):
    word: str