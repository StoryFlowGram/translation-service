from fastapi import APIRouter, Depends, HTTPException

from app.application.usecase.cgpt_usecase import CgptUsecase
from app.presentation.api.depends import cgpt_repo, get_current_user
from app.presentation.schemas.ai_translation_schema import AiTranslationSchema


cgpt_router = APIRouter(tags=["CGPT"])


#TODO: "Добавить рейт лимиты"
@cgpt_router.post("/ai/explain")
async def get_ai_translation(
    word: AiTranslationSchema,
    protocol = Depends(cgpt_repo),
):
    usecase = CgptUsecase(protocol)
    try:
        result = await usecase.get_translation_and_explanation(word)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

