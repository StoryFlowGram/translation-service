from fastapi import FastAPI

from app.presentation.api.v1.translation_controller import translation_router
from app.presentation.api.v1.cgpt_controller import cgpt_router
from app.infrastructure import di
from app.presentation.api import depends


app = FastAPI()

app.include_router(translation_router)
app.include_router(cgpt_router)

app.dependency_overrides[depends.translation_repo] = di.get_google_translate_adapter
app.dependency_overrides[depends.cgpt_repo] = di.cgpt_adapter