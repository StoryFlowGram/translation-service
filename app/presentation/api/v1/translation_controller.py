from fastapi import APIRouter, HTTPException, Depends

from app.application.usecase.translation_usecase import GetTranslationUsecase
from app.presentation.api.depends import translation_repo



translation_router = APIRouter(
    prefix="/api/v1/translation",
    tags=["Translation"]
)



@translation_router.get("/")
async def get_word_translation(
    text: str, 
    src_lang: str = "english",
    dest_lang: str = "russian",
    protocol = Depends(translation_repo)
):
    try:
        usecase = GetTranslationUsecase(protocol)
        return await usecase.get_word_translation(text, src_lang, dest_lang)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    


@translation_router.get("/sentence")
async def get_sentence_translation(
    text: str, 
    src_lang: str = "english",
    dest_lang: str = "russian",
    protocol = Depends(translation_repo)

):
    try:
        usecase = GetTranslationUsecase(protocol)
        return await usecase.get_translate_sentence(text, src_lang, dest_lang)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    