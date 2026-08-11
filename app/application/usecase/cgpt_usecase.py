import logging
from app.application.protocols.cgpt_protocols import CgptProtocol
from app.application.dto.cgpt_dto import CgptTranslationDTO
from app.domain.exception.cgpt_exeption import CgptNotFoundException

logger = logging.getLogger(__name__)

class CgptUsecase:
    def __init__(self, cgpt_repository: CgptProtocol):
        self.cgpt_repository = cgpt_repository

    async def get_translation_and_explanation(self, text: str) -> CgptTranslationDTO:
        logger.info(f"Запит на переклад слова: '{text}'")
        
        result = await self.cgpt_repository.get_translation_and_explanation(text)
        
        logger.info(f"Результат з адаптера: {result}")
        if not result:
            raise CgptNotFoundException(text)
            
        if "Переклад тимчасово недоступний" in result.explanation:
             raise CgptNotFoundException(text)

        return CgptTranslationDTO(
            word=result.word,
            translation=result.translation,
            explanation=result.explanation,
            etymology=result.etymology,
        )