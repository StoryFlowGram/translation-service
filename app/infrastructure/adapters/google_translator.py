from googletrans import Translator, LANGUAGES
from fastapi import HTTPException 
from typing import Optional, List

from app.application.protocols.translation_protocols import TranslationProtocol


from app.domain.entity.translation import (
    WordTranslationDetails, 
    SentenceTranslation
)


class GoogleTranslateAdapter(TranslationProtocol):
    
    def __init__(self):
        self.translator = Translator()

    def _get_language_code(self, lang_name: str) -> str:
        lang_name = lang_name.lower()
        for code, name in LANGUAGES.items():
            if name.lower() == lang_name:
                return code
        raise HTTPException(status_code=400, detail=f"Unsupported language: {lang_name}")

    async def translate_word(self, word: str, src: str, dest: str) -> Optional[WordTranslationDetails]:
        try:
            src_code = self._get_language_code(src)
            dest_code = self._get_language_code(dest)
            
            raw_result = await self.translator.translate(word, src=src_code, dest=dest_code)
        
            
            flat_translations_list: List[str] = []
            raw_groups = raw_result.extra_data.get('all-translations')
            
            if raw_groups:
                for group_data in raw_groups:
                    translations_list = group_data[1]
                    
                    if translations_list:
                        flat_translations_list.extend(translations_list)
            
            return WordTranslationDetails(
                word=word,
                translation=raw_result.text,
                pronunciation=raw_result.pronunciation,
                src_lang=src,
                dest_lang=dest,
                additional_translations=flat_translations_list 
            )
        
        except Exception as e:
            print(f"Google Translate Error (word: {word}): {e}") 
            return None 

    async def translate_sentence(self, sentence: str, src: str, dest: str) -> Optional[SentenceTranslation]:
        try:
            src_code = self._get_language_code(src)
            dest_code = self._get_language_code(dest)
            
            raw_result = await self.translator.translate(sentence, src=src_code, dest=dest_code)
            
            return SentenceTranslation(
                sentence=sentence,
                translation=raw_result.text
            )
        
        except Exception as e:
            print(f"Google Translate Error (sentence: {sentence}): {e}")
            return None