import logging

from fastapi import APIRouter, Depends, HTTPException

from app.presentation.schemas.translation_schema import TranslationWordSchema, TranslationSentenceSchema

from app.application.usecase.translation_usecase import GetTranslationUsecase
from app.presentation.api.depends import get_current_user, translation_repo
from app.presentation.security.rate_limit import InMemoryRateLimiter


translation_router = APIRouter(
    tags=["Translation"]
)

logger = logging.getLogger(__name__)
translation_rate_limiter = InMemoryRateLimiter(max_requests=120, window_seconds=60)


@translation_router.post("/translate/word")
async def get_word_translation(
    body: TranslationWordSchema,
    protocol = Depends(translation_repo),
    user_id: int = Depends(get_current_user),
):
    try:
        await translation_rate_limiter.check(f"translation:{user_id}")
        usecase = GetTranslationUsecase(protocol)
        return await usecase.get_word_translation(body.text, body.src_lang, body.dest_lang)
    except HTTPException:
        raise
    except Exception:
        logger.exception("Word translation failed")
        raise HTTPException(status_code=400, detail="Failed to translate word")
    


@translation_router.post("/sentence")
async def get_sentence_translation(
    body: TranslationSentenceSchema,
    protocol = Depends(translation_repo),
    user_id: int = Depends(get_current_user),

):
    try:
        await translation_rate_limiter.check(f"translation:{user_id}")
        usecase = GetTranslationUsecase(protocol)
        return await usecase.get_translate_sentence(body.text, body.src_lang, body.dest_lang)
    except HTTPException:
        raise
    except Exception:
        logger.exception("Sentence translation failed")
        raise HTTPException(status_code=400, detail="Failed to translate sentence")
    
    
