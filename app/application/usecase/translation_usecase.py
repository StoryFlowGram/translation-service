from app.domain.entity.translation import WordTranslationDetails, SentenceTranslation
from app.domain.exception.translation_exception import TranslationNotFoundException
from app.application.protocols.translation_protocols import TranslationProtocol
from app.application.dto.translation_dto import WordTranslationDetailsDTO, SentenceTranslationDTO



class GetTranslationUsecase:
    def __init__(self, translation_repository: TranslationProtocol):
        self.translation_repository = translation_repository


    async def get_word_translation(self, text: str, src_lang: str, dest_lang: str) -> WordTranslationDetails:
        result = await self.translation_repository.translate_word(text, src_lang, dest_lang)
        if not result:
            raise TranslationNotFoundException(text, src_lang, dest_lang)
        
        return WordTranslationDetailsDTO(
            word=result.word,
            translation=result.translation,
            pronunciation=result.pronunciation,
            src_lang=result.src_lang,
            dest_lang=result.dest_lang,
            additional_translations=result.additional_translations
        )


    async def get_translate_sentence(self, text: str, src_lang: str, dest_lang: str) -> SentenceTranslation:
        result = await self.translation_repository.translate_sentence(text, src_lang, dest_lang)
        if not result:
            raise TranslationNotFoundException(text, src_lang, dest_lang)
        
        return SentenceTranslationDTO(
            sentence=result.sentence, 
            translation=result.translation
        )