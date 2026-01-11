from fastapi import APIRouter, HTTPException, Depends

from app.presentation.schemas.translation_schema import TranslationWordSchema, TranslationSentenceSchema

from app.application.usecase.translation_usecase import GetTranslationUsecase
from app.presentation.api.depends import translation_repo


translation_router = APIRouter(
    tags=["Translation"]
)



@translation_router.post("/translate/word")
async def get_word_translation(
    body: TranslationWordSchema,
    protocol = Depends(translation_repo)
):
    try:
        usecase = GetTranslationUsecase(protocol)
        return await usecase.get_word_translation(body.text, body.src_lang, body.dest_lang)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    


@translation_router.post("/sentence")
async def get_sentence_translation(
    body: TranslationSentenceSchema,
    protocol = Depends(translation_repo)

):
    try:
        usecase = GetTranslationUsecase(protocol)
        return await usecase.get_translate_sentence(body.text, body.src_lang, body.dest_lang)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    