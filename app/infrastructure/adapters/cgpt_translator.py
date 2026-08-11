import logging
from google.genai import Client
from google.genai import types
from pydantic import BaseModel

from app.application.protocols.cgpt_protocols import CgptProtocol
from app.domain.entity.cgpt import CgptDomain
from app.infrastructure.config.config import Setting


settings = Setting()

logger = logging.getLogger(__name__)


class _TranslationSchema(BaseModel):
    translation: str
    explanation: str
    etymology: str


class CgptAdapter(CgptProtocol):
    def __init__(self):
        print(f"--- DEBUG: Gemini Key is: '{settings.gemini_api_key}' ---")
        
        if not settings.gemini_api_key:
            raise ValueError("API ключ Gemini пустой! Проверьте проброс переменных в Docker.")
            
        self.client = Client(api_key=settings.gemini_api_key)

    async def get_translation_and_explanation(self, word: str) -> CgptDomain:
        prompt = (
            f"Дай подробную информацию о слове '{word}' "
            f"СТРОГО с английского на украинский: основной перевод, "
            f"подробное толкование значения и этимологию."
        )

        try:
            response = await self.client.aio.models.generate_content(
                model="gemini-2.5-flash", 
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=_TranslationSchema,
                ),
            )
            
            data: _TranslationSchema = response.parsed

        except Exception as e:
            logger.exception("Gemini translation failed for word=%r. Error: %s", word, e)
            return CgptDomain(
                word=word,
                translation=word,
                explanation="Переклад тимчасово недоступний (Помилка сервісу перекладу).",
                etymology="Етимологію не знайдено.",
            )

        return CgptDomain(
            word=word,
            translation=data.translation,
            explanation=data.explanation,
            etymology=data.etymology,
        )