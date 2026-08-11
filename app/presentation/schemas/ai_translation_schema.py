from pydantic import BaseModel, Field



class AiTranslationSchema(BaseModel):
    word: str = Field(min_length=1, max_length=128)
