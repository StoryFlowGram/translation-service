import logging

from fastapi import APIRouter, Depends, HTTPException

from app.application.usecase.cgpt_usecase import CgptUsecase
from app.presentation.api.depends import cgpt_repo, get_current_user
from app.presentation.schemas.ai_translation_schema import AiTranslationSchema
from app.presentation.security.rate_limit import InMemoryRateLimiter


cgpt_router = APIRouter(tags=["CGPT"])
logger = logging.getLogger(__name__)
cgpt_rate_limiter = InMemoryRateLimiter(max_requests=20, window_seconds=60)


#TODO: "Добавить рейт лимиты"
@cgpt_router.post("/ai/explain")
async def get_ai_translation(
    word: AiTranslationSchema,
    protocol = Depends(cgpt_repo),
    user_id: int = Depends(get_current_user),
):
    usecase = CgptUsecase(protocol)
    try:
        await cgpt_rate_limiter.check(f"cgpt:{user_id}")
        result = await usecase.get_translation_and_explanation(word.word)
        return result
    except HTTPException:
        raise
    except Exception:
        logger.exception("AI translation failed")
        raise HTTPException(status_code=400, detail="Failed to generate AI explanation")
    

