import logging

from fastapi import APIRouter, Depends, HTTPException

from app.application.usecase.cgpt_usecase import CgptUsecase
from app.presentation.api.depends import cgpt_repo, get_current_user
from app.presentation.schemas.ai_translation_schema import AiTranslationSchema
from app.presentation.security.rate_limit import InMemoryRateLimiter
from app.domain.exception.cgpt_exeption import CgptNotFoundException

cgpt_router = APIRouter(tags=["CGPT"])
logger = logging.getLogger(__name__)
cgpt_rate_limiter = InMemoryRateLimiter(max_requests=20, window_seconds=60)



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
    except CgptNotFoundException as e:
        logger.warning(f"Переклад не знайдено: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e.message if hasattr(e, 'message') else e))
    except HTTPException:
        raise
    except Exception as e:
        # Логуємо непередбачувані системні помилки
        logger.exception("Неочікувана помилка при отриманні перекладу")
        raise HTTPException(status_code=500, detail="Внутрішня помилка сервера")
    

