from fastapi import APIRouter, Depends, HTTPException

from app.application.usecase.cgpt_usecase import CgptUsecase
from app.presentation.api.depends import cgpt_repo


cgpt_router = APIRouter(
    prefix="/api/v1/cgpt",
    tags=["CGPT"]
)



@cgpt_router.get("/ai_translation")
async def get_ai_translation(
    word: str,
    protocol = Depends(cgpt_repo)
):
    usecase = CgptUsecase(protocol)
    try:
        result = await usecase.get_translation_and_explanation(word)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

