from g4f import AsyncClient
import json

from app.application.protocols.cgpt_protocols import CgptProtocol
from app.domain.entity.cgpt import CgptDomain


class CgptAdapter(CgptProtocol):
    def __init__(self):
        self.client = AsyncClient()


    async def get_translation_and_explanation(self, word: str):
        prompt = f"""
        Дай подробную информацию о слове '{word}' (с Английского на Украинский).
        Верни ответ ИСКЛЮЧИТЕЛЬНО в формате JSON со следующей структурой:
        {{
          "translation": "основной перевод",
          "explanation": "подробное толкование и значение слова",
          "etymology": "этимология, происхождение слова",
        }}
        """

        try:
            response = await self.client.chat.completions.create(
                model="deepseek-v3",
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as e:
            raise Exception(f"Ошибка обращения к AI {e}")

        raw_content: str = response.choices[0].message.content

        if raw_content.startswith("```json"):
                raw_content = raw_content[7:-3].strip()

        data = json.loads(raw_content)

        return CgptDomain(
            word = data.get("translation"),
            translation = data.get("translation"),
            explanation = data.get("explanation"),
            etymology = data.get("etymology"),
        )